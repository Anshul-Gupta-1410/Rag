
import json
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder

from .config import (
    SEMANTIC_TOP_K,
    FINAL_TOP_K,
    EMBEDDING_MODEL_NAME,
    RERANKER_MODEL_NAME,
)


class RAGRetriever:
    """
    Reusable Phase 6.5 retrieval pipeline.

    Pipeline:
        Query
          ↓
        BGE embedding
          ↓
        FAISS semantic retrieval
          ↓
        Top-10 candidates
          ↓
        Cross-Encoder reranking
          ↓
        Top-5 final chunks
    """

    def __init__(
        self,
        chunks_path,
        index_path,
        semantic_top_k=SEMANTIC_TOP_K,
        final_top_k=FINAL_TOP_K,
        embedding_model_name=EMBEDDING_MODEL_NAME,
        reranker_model_name=RERANKER_MODEL_NAME,
    ):

        self.chunks_path = Path(chunks_path)
        self.index_path = Path(index_path)

        self.semantic_top_k = semantic_top_k
        self.final_top_k = final_top_k

        # ----------------------------------------------------
        # Load chunks
        # ----------------------------------------------------

        if not self.chunks_path.exists():
            raise FileNotFoundError(
                f"Chunks file not found: {self.chunks_path}"
            )

        self.chunks = []

        with open(self.chunks_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if line:
                    self.chunks.append(json.loads(line))

        # ----------------------------------------------------
        # Load FAISS index
        # ----------------------------------------------------

        if not self.index_path.exists():
            raise FileNotFoundError(
                f"FAISS index not found: {self.index_path}"
            )

        self.index = faiss.read_index(str(self.index_path))

        if self.index.ntotal != len(self.chunks):
            raise ValueError(
                "FAISS/chunk mismatch: "
                f"{self.index.ntotal} vectors vs "
                f"{len(self.chunks)} chunks."
            )

        # ----------------------------------------------------
        # Load embedding model
        # ----------------------------------------------------

        self.embedding_model = SentenceTransformer(
            embedding_model_name
        )

        embedding_dim = (
            self.embedding_model
            .get_sentence_embedding_dimension()
        )

        if embedding_dim != self.index.d:
            raise ValueError(
                "Embedding dimension mismatch: "
                f"model={embedding_dim}, "
                f"FAISS={self.index.d}"
            )

        # ----------------------------------------------------
        # Load cross-encoder
        # ----------------------------------------------------

        self.reranker = CrossEncoder(
            reranker_model_name
        )

    # ========================================================
    # Internal helper
    # ========================================================

    @staticmethod
    def _extract_text(chunk):
        """
        Extract the text field while keeping compatibility
        with common chunk JSON structures.
        """

        if isinstance(chunk, str):
            return chunk

        for key in [
            "text",
            "chunk_text",
            "content",
            "page_content",
        ]:
            if key in chunk:
                return str(chunk[key])

        raise KeyError(
            "Could not find chunk text field. "
            f"Available keys: {list(chunk.keys())}"
        )

    # ========================================================
    # Retrieve
    # ========================================================

    def retrieve(self, query):
        """
        Run complete semantic + reranker retrieval.

        Returns a list of dictionaries sorted by final
        cross-encoder score.
        """

        if not isinstance(query, str) or not query.strip():
            raise ValueError("Query must be a non-empty string.")

        query = query.strip()

        # ----------------------------------------------------
        # 1. Query embedding
        # ----------------------------------------------------

        query_embedding = self.embedding_model.encode(
            [query],
            normalize_embeddings=True,
            convert_to_numpy=True,
        ).astype("float32")

        # ----------------------------------------------------
        # 2. FAISS semantic retrieval
        # ----------------------------------------------------

        semantic_k = min(
            self.semantic_top_k,
            self.index.ntotal
        )

        distances, indices = self.index.search(
            query_embedding,
            semantic_k
        )

        candidate_indices = indices[0]
        candidate_distances = distances[0]

        candidates = []

        for rank, (idx, distance) in enumerate(
            zip(candidate_indices, candidate_distances),
            start=1
        ):

            idx = int(idx)

            if idx < 0 or idx >= len(self.chunks):
                continue

            chunk = self.chunks[idx]

            candidates.append({
                "chunk_index": idx,
                "semantic_rank": rank,
                "semantic_score": float(distance),
                "text": self._extract_text(chunk),
                "chunk": chunk,
            })

        if not candidates:
            return []

        # ----------------------------------------------------
        # 3. Cross-encoder reranking
        # ----------------------------------------------------

        pairs = [
            (query, candidate["text"])
            for candidate in candidates
        ]

        reranker_scores = self.reranker.predict(
            pairs,
            show_progress_bar=False
        )

        for candidate, score in zip(
            candidates,
            reranker_scores
        ):
            candidate["reranker_score"] = float(score)

        # ----------------------------------------------------
        # 4. Sort by cross-encoder score
        # ----------------------------------------------------

        candidates.sort(
            key=lambda x: x["reranker_score"],
            reverse=True
        )

        # ----------------------------------------------------
        # 5. Assign final rank
        # ----------------------------------------------------

        final_results = candidates[
            :min(self.final_top_k, len(candidates))
        ]

        for rank, result in enumerate(
            final_results,
            start=1
        ):
            result["final_rank"] = rank

        return final_results

    # ========================================================
    # Context helper
    # ========================================================

    def build_context(self, results):
        """
        Convert retrieved chunks into an ordered context
        string suitable for an LLM prompt.
        """

        context_parts = []

        for result in results:

            context_parts.append(
                f"[Chunk {result['final_rank']}]\n"
                f"{result['text']}"
            )

        return "\n\n".join(context_parts)
