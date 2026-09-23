evaluation_queries_long = [
    # =====================================================
    # VACATION / LEAVE — Long-form queries
    # =====================================================
    {
        "query": "I've been working at Clef for about six months now and I'm wondering how many vacation days I've accumulated so far and whether unused sick days carry over to the next year",
        "expected_document": "Vacation and Sick Leave.md"
    },
    {
        "query": "My spouse and I are expecting a baby in a few months and I want to understand the full maternity and paternity leave policy including how it interacts with California state disability programs",
        "expected_document": "New Parent Leave.md"
    },
    {
        "query": "I recently adopted a child and I'm trying to figure out within what timeframe I need to take my new parent leave and whether I need to give any advance notice to my team",
        "expected_document": "New Parent Leave.md"
    },
    {
        "query": "I have a chronic illness that sometimes makes it hard to come into the office regularly — is there any policy around flexible work arrangements or disability support for someone in my situation",
        "expected_document": "Vacation and Sick Leave.md"
    },
    {
        "query": "If I take the full twelve weeks of new parent leave does that time count toward my five year requirement for becoming eligible for a sabbatical or does it pause the clock",
        "expected_document": "New Parent Leave.md"
    },

    # =====================================================
    # SABBATICAL — Long-form queries
    # =====================================================
    {
        "query": "I've been at Clef for almost five years and I'm interested in taking a sabbatical to volunteer at a nonprofit — do I need to present something to the team when I return and how far in advance should I notify everyone",
        "expected_document": "Sabbatical.md"
    },
    {
        "query": "I'm worried that if I take a three month sabbatical I might lose my accrued sick days — can you explain whether paid time off continues to accumulate during the sabbatical period or if it freezes",
        "expected_document": "Sabbatical.md"
    },

    # =====================================================
    # CONTINUING EDUCATION — Long-form queries
    # =====================================================
    {
        "query": "I want to attend a machine learning conference in Europe next quarter — would the flight and hotel costs come out of my learning budget or is there a separate travel budget for professional development events",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "I've been invited to speak at a cybersecurity conference and I'm wondering how much Clef will cover for travel expenses and whether this comes from the same pool as the annual learning budget or a different one",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "I started working at Clef in July of this year and I want to know if my learning budget is the full four thousand dollars or if it is reduced since I joined after the midpoint of the calendar year",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "Can I use a portion of my work hours during the week to study for a certification that is related to my role at Clef and if so is there a limit on how many hours I can dedicate to that",
        "expected_document": "Continuing Education.md"
    },

    # =====================================================
    # HEALTHCARE & INSURANCE — Long-form queries
    # =====================================================
    {
        "query": "My wife already has health insurance through her employer and I don't need Clef's medical plan — is there any financial incentive or allowance if I choose to waive my medical coverage through TriNet",
        "expected_document": "Healthcare and Disability Insurance.md"
    },
    {
        "query": "I'm starting at Clef next month and I want to add my two kids to my health insurance plan — what percentage of the dependent coverage does the company contribute and when does the coverage actually begin",
        "expected_document": "Healthcare and Disability Insurance.md"
    },

    # =====================================================
    # SALARY & EQUITY — Long-form queries
    # =====================================================
    {
        "query": "I'm a software engineer with seven years of experience and I'd like to understand what my starting salary would be at Clef and whether there is room for individual negotiation beyond the standard rubric",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "I noticed the equity vesting schedule at Clef is six years instead of the typical four — can you explain the reasoning behind that and how many stock options a new employee typically receives",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "If I choose to take the five thousand dollar salary reduction in exchange for additional equity how many extra stock options would I receive and what total percentage of the company would that represent",
        "expected_document": "Salary and Equity Compensation.md"
    },

    # =====================================================
    # REFERRAL BONUSES — Long-form queries
    # =====================================================
    {
        "query": "I referred a friend to Clef about four months ago and she just got an offer — do I qualify for the referral bonus and when exactly would I expect to receive the payment after she starts",
        "expected_document": "Referral Bonuses.md"
    },
    {
        "query": "Two people on the team both claim they referred the same candidate independently — how does the company determine who gets the five thousand dollar referral bonus in a situation like this",
        "expected_document": "Referral Bonuses.md"
    },

    # =====================================================
    # WORKING REMOTELY — Long-form queries
    # =====================================================
    {
        "query": "I'm planning to work from my parents house in another state for about ten days next month — do I need to get my manager's approval beforehand and how much advance notice should I give the rest of the team",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "I've been working remotely a couple days a week but my manager says my productivity has dropped — can they revoke my remote work privileges entirely and what process has to happen before that decision is made",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "When I'm working from home I know I should be available on Slack but I'm unclear about the exact expectations — is there a specific set of hours where I need to be reachable for meetings and collaboration",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "I want to work from a coffee shop while traveling but I'm concerned about the internet connection requirements — what are the specific prerequisites Clef expects me to have in place before working from somewhere irregular",
        "expected_document": "Working Remotely.md"
    },

    # =====================================================
    # EMPLOYEE PRIVACY — Long-form queries
    # =====================================================
    {
        "query": "I sometimes send personal emails from my Clef email address and I want to know if the company has the ability to read those messages even if I mark them as private or personal in the subject line",
        "expected_document": "Employee Privacy.md"
    },
    {
        "query": "I keep a personal journal on my work laptop and I want to know if management has the right to access files stored on company devices or if my personal data on company property is protected",
        "expected_document": "Employee Privacy.md"
    },

    # =====================================================
    # CODE OF CONDUCT — Long-form queries
    # =====================================================
    {
        "query": "A community member made an offensive joke in the Clef Slack channel and someone complained about it — what does the code of conduct say about jokes and what are the consequences for the person who made the comment",
        "expected_document": "Code of Conduct in the Community.md"
    },
    {
        "query": "I witnessed someone being harassed at a Clef-hosted event last week and I want to report it — who exactly should I contact and does it matter if the harassment was not directed at me personally",
        "expected_document": "Code of Conduct in the Community.md"
    },

    # =====================================================
    # COMPLAINT POLICY — Long-form queries
    # =====================================================
    {
        "query": "I want to file a complaint about something that happened at work but I'm afraid my manager might treat me differently afterward — does Clef have a policy against retaliation for employees who report issues",
        "expected_document": "Complaint Policy.md"
    },
    {
        "query": "If my complaint involves one of the founders of the company how is the investigation handled differently and is there a possibility that an outside investigator would be brought in to ensure impartiality",
        "expected_document": "Complaint Policy.md"
    },

    # =====================================================
    # OKRs — Long-form queries
    # =====================================================
    {
        "query": "I'm new to the OKR system and I don't understand how scoring works at the end of the quarter — if I score a perfect ten on all my key results does that mean I set my goals too low or is that considered ideal",
        "expected_document": "Objectives and Key Results.md"
    },
    {
        "query": "I want to set a key result that involves delivering a project by a certain date — how should I structure the scoring so that points are deducted fairly if the project ends up being delivered late",
        "expected_document": "Objectives and Key Results.md"
    },

    # =====================================================
    # ONE ON ONES — Long-form queries
    # =====================================================
    {
        "query": "I have a problem with a coworker and I want to bring it up during my one on one meeting — will my manager step in to address it directly or do they need my permission before talking to that person about it",
        "expected_document": "One on Ones.md"
    },
    {
        "query": "My one on one meetings with my manager feel more like status updates than meaningful conversations — what does Clef recommend regarding the agenda and tone of these meetings to make them more productive",
        "expected_document": "One on Ones.md"
    },

    # =====================================================
    # COMMUNICATION & TRANSPARENCY — Long-form queries
    # =====================================================
    {
        "query": "When I set my Slack status to Do Not Disturb and the indicator shows green what does that signal to my teammates — should they expect a response immediately or should they wait until my focus time is over",
        "expected_document": "Communication and Transparency.md"
    },
    {
        "query": "I've noticed that a lot of important decisions are being discussed in private Slack channels and I feel out of the loop — what is Clef's official guideline on using public versus private channels for team conversations",
        "expected_document": "Communication and Transparency.md"
    },

    # =====================================================
    # OPERATIONS — Long-form queries
    # =====================================================
    {
        "query": "I have an idea for a hack week project that would require three other people to help me build it — how do I pitch this project to the team and are there any restrictions on what we can work on during that week",
        "expected_document": "Hack Weeks.md"
    },
    {
        "query": "When a project is completed and no longer active how should I archive the project folder and what naming convention does Clef use so that old projects are easy to find later on",
        "expected_document": "Sharing Files.md"
    },
    {
        "query": "I need to schedule a meeting with a remote colleague but they are in a different time zone — what are the core hours during which all Clef employees are expected to be available for face to face meetings",
        "expected_document": "Effective Meetings.md"
    },

    # =====================================================
    # POLICY CHANGES — Long-form queries
    # =====================================================
    {
        "query": "I disagree with a recent policy change that was merged into the handbook and I want to voice my concerns — what is the proper channel for giving feedback and will there be a team discussion about it before it takes effect",
        "expected_document": "Policy Changes.md"
    },
    {
        "query": "I heard that employees need to sign an acknowledgement every time the handbook is updated — how often do these updates get adopted and is there a formal review process before changes become official policy",
        "expected_document": "Policy Changes.md"
    },

    # =====================================================
    # CROSS-DOCUMENT / TRICKY — Long-form queries
    # =====================================================
    {
        "query": "I'm pregnant and dealing with severe morning sickness that makes it hard to come to work every day — can I take intermittent pregnancy disability leave while still keeping my job and benefits at Clef",
        "expected_document": "Other Protected Absences.md"
    },
    {
        "query": "I want to understand how Clef avoids salary bias during the hiring process — is there a standard pay scale for all roles or does compensation depend on individual negotiation skills and previous salary history",
        "expected_document": "Salary and Equity Compensation.md"
    },
]
