# Clef Employee Handbook — Retrieval-Augmented Generation (RAG)

A Retrieval-Augmented Generation (RAG) system that enables users to ask questions about the Clef Employee Handbook and receive relevant, context-aware answers using semantic search, vector retrieval, and a Large Language Model (LLM).

## Overview

I built this project to make employee handbook information easier to access through a conversational interface. Instead of manually searching through multiple documents, users can ask questions in natural language and retrieve relevant information from the handbook.

The system uses structure-aware document processing, semantic embeddings, FAISS-based vector search, and cross-encoder reranking to improve retrieval relevance before generating answers.

## Features

* **Structure-Aware Chunking:** Preserves document headings and section hierarchy to maintain contextual relationships.
* **Semantic Embeddings:** Converts handbook content into vector representations for semantic similarity search.
* **FAISS Vector Search:** Enables efficient retrieval of relevant document chunks.
* **Cross-Encoder Reranking:** Reorders retrieved results based on query-document relevance.
* **RAG-Based Answer Generation:** Uses retrieved handbook content as context for generating answers.
* **FastAPI Backend:** Provides an API for handling user queries and processing the RAG pipeline.
* **Conversational Interface:** Allows users to interact with handbook information through a chat interface.
* **Retrieval Evaluation:** Evaluates retrieval performance using Top-1 accuracy and Top-3/Top-5 recall.

## Architecture

```text
Employee Handbook Documents
          |
          v
 Document Processing
          |
          v
 Structure-Aware Chunking
          |
          v
  Text Embeddings
          |
          v
    FAISS Index
          |
          v
      User Query
          |
          v
   Query Embedding
          |
          v
 Semantic Retrieval
          |
          v
 Cross-Encoder Reranking
          |
          v
 Relevant Context
          |
          v
    LLM Generation
          |
          v
   Generated Answer
          |
          v
   Chat Interface
```

## Tech Stack

| Component               | Technology                |
| ----------------------- | ------------------------- |
| Programming Language    | Python                    |
| Embeddings & Reranking  | Sentence Transformers     |
| Vector Database / Index | FAISS                     |
| LLM                     | Gemma 3 1B                |
| API Framework           | FastAPI                   |
| Data Processing         | Pandas, NumPy             |
| ML Utilities            | Scikit-learn              |
| Model Runtime           | Hugging Face Transformers |

## Retrieval Pipeline

### 1. Document Processing

I processed the employee handbook documents and extracted their content while preserving the original document structure and section hierarchy.

### 2. Structure-Aware Chunking

I divided the documents into manageable chunks while retaining relevant headings and section information. This helps preserve context during retrieval.

### 3. Embedding Generation

I generated semantic embeddings for the document chunks using Sentence Transformers and stored the resulting vectors for similarity-based retrieval.

### 4. FAISS Indexing

I indexed the embeddings using FAISS to efficiently retrieve relevant handbook sections for incoming queries.

### 5. Cross-Encoder Reranking

I used a cross-encoder to rerank the retrieved candidates based on their relevance to the user's query, improving the ordering of the final context.

### 6. Answer Generation

The retrieved chunks are passed to the Gemma 3 1B model as contextual information. The model uses this context to generate a response to the user's question.

### 7. API and Chat Interface

I integrated the RAG pipeline with a FastAPI backend that accepts user queries, retrieves relevant context, and returns generated answers to the chat interface.

## Evaluation

I evaluated the retrieval pipeline using an independent benchmark of **157 queries**, consisting of 116 short queries and 41 long queries.

The evaluation focuses on retrieval relevance and the ability to identify the correct handbook content.

### Short Queries

| Metric         | Semantic Retrieval |    Semantic + Reranking |
| -------------- | -----------------: | ----------------------: |
| Top-1 Accuracy |             78.45% |                  83.62% |
| Improvement    |                  — | +5.17 percentage points |

### Long Queries

| Metric         | Semantic Retrieval |    Semantic + Reranking |
| -------------- | -----------------: | ----------------------: |
| Top-1 Accuracy |             87.80% |                  90.24% |
| Improvement    |                  — | +2.44 percentage points |

### Additional Retrieval Results

The hybrid retrieval approach achieved **100% Top-3 and Top-5 recall on the long-query benchmark**, indicating that the relevant content was retrieved within the top results for those evaluated queries.

> Note: These metrics measure retrieval performance on the evaluation dataset, not the factual accuracy of every generated answer.

## Project Structure

```text
Clef-Employee-Handbook-RAG/
│
├── data/
│   └── employee_handbook/
│       └── Handbook documents
│
├── notebooks/
│   ├── document_processing.ipynb
│   ├── embedding_generation.ipynb
│   ├── retrieval_evaluation.ipynb
│   └── rag_pipeline.ipynb
│
├── embeddings/
│   └── embedding_metadata.json
│
├── vector_store/
│   └── FAISS index files
│
├── app/
│   └── FastAPI application
│
├── requirements.txt
└── README.md
```

*The directory structure above is a suggested layout. Adjust it to match the actual files in your repository.*

## Getting Started

### Prerequisites

* Python 3.10 or later
* pip
* Jupyter Notebook (for running the notebooks)
* Sufficient RAM and storage for the embedding model and LLM

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Clef-Employee-Handbook-RAG
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If a requirements file is not yet available, install the core packages:

```bash
pip install sentence-transformers faiss-cpu transformers accelerate bitsandbytes pandas==2.2.2 numpy==2.0.2 tqdm scikit-learn fastapi uvicorn
```

### 4. Prepare the Documents

Place the employee handbook documents in the appropriate data directory and run the document-processing and embedding-generation notebooks.

Ensure that the FAISS index and corresponding metadata are generated before running the query pipeline.

### 5. Run the Application

Once the FastAPI application is configured, start the server:

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

*Update the application module path if your FastAPI entry point is located elsewhere.*

## Example Usage

A user can ask questions such as:

```text
What is the onboarding process for new employees?

What documents are required when joining Clef?

What are the company's leave policies?
```

The system retrieves relevant handbook sections and uses them as context to generate an answer.

## Future Improvements

* Add source citations and document references to generated answers.
* Improve retrieval using additional hybrid search strategies.
* Evaluate answer quality using faithfulness and context-relevance metrics.
* Add conversation history for multi-turn interactions.
* Optimize inference latency and memory usage.
* Expand the document collection and evaluation dataset.

## Learning Outcomes

Through this project, I gained practical experience in:

* Building an end-to-end Retrieval-Augmented Generation pipeline.
* Processing structured documents for semantic retrieval.
* Implementing vector search with FAISS.
* Improving retrieval quality using cross-encoder reranking.
* Evaluating retrieval systems using quantitative metrics.
* Integrating an LLM pipeline with FastAPI and a conversational interface.

## Author

**Anshul Gupta**

B.Tech in Information Technology
Indian Institute of Information Technology Vadodara

---

If you find this project interesting, feel free to explore the repository and its implementation.
