evaluation_queries = [
    # =====================================================
    # VACATION / LEAVE (Direct, Paraphrased, Vague)
    # =====================================================
    {
        "query": "How much vacation time do employees get?",
        "expected_document": "Vacation and Sick Leave.md"
    },
    {
        "query": "Can I take leave after having a baby?",
        "expected_document": "New Parent Leave.md"
    },
    {
        "query": "What holidays does the company observe?",
        "expected_document": "Holiday List.md"
    },
    {
        "query": "How many days of PTO do I earn per month?",
        "expected_document": "Vacation and Sick Leave.md"
    },
    {
        "query": "I'm not feeling well today, how does sick leave work?",
        "expected_document": "Vacation and Sick Leave.md"
    },
    {
        "query": "Is Thanksgiving a day off at Clef?",
        "expected_document": "Holiday List.md"
    },
    {
        "query": "My partner and I are adopting a child — what leave am I entitled to?",
        "expected_document": "New Parent Leave.md"
    },
    {
        "query": "Do fathers get parental leave too or just mothers?",
        "expected_document": "New Parent Leave.md"
    },
    {
        "query": "What happens if a holiday falls on a weekend?",
        "expected_document": "Holiday List.md"
    },
    {
        "query": "I need some time away, what are my options?",
        "expected_document": "Vacation and Sick Leave.md"
    },

    # =====================================================
    # SABBATICAL (Direct, Specific Numbers, Paraphrased)
    # =====================================================
    {
        "query": "How long do I have to work before I'm eligible for a sabbatical?",
        "expected_document": "Sabbatical.md"
    },
    {
        "query": "What is the duration of the sabbatical at Clef?",
        "expected_document": "Sabbatical.md"
    },
    {
        "query": "Can I use my sabbatical to start a side business?",
        "expected_document": "Sabbatical.md"
    },
    {
        "query": "Do I still accrue vacation days while on sabbatical?",
        "expected_document": "Sabbatical.md"
    },
    {
        "query": "I've been here 5 years, what's the deal with the long break?",
        "expected_document": "Sabbatical.md"
    },

    # =====================================================
    # CONTINUING EDUCATION (Direct, Specific Numbers, Employee Terminology)
    # =====================================================
    {
        "query": "What is the annual learning budget for employees?",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "Can I use company money to attend a conference?",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "Does Clef pay for online courses and books?",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "How much does Clef reimburse for speaking at events?",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "Is there a mentorship program at Clef?",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "I joined in June, is my learning budget still $4,000?",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "How many hours per week can I spend on learning projects?",
        "expected_document": "Continuing Education.md"
    },
    {
        "query": "Does the learning budget roll over to the next year?",
        "expected_document": "Continuing Education.md"
    },

    # =====================================================
    # HEALTHCARE & INSURANCE (Direct, Paraphrased, Vague)
    # =====================================================
    {
        "query": "What health insurance does Clef offer?",
        "expected_document": "Healthcare and Disability Insurance.md"
    },
    {
        "query": "Does the company cover dental and vision?",
        "expected_document": "Healthcare and Disability Insurance.md"
    },
    {
        "query": "What percentage of health insurance does Clef pay for dependents?",
        "expected_document": "Healthcare and Disability Insurance.md"
    },
    {
        "query": "I already have insurance through my spouse, can I opt out?",
        "expected_document": "Healthcare and Disability Insurance.md"
    },
    {
        "query": "When does my health coverage start after joining?",
        "expected_document": "Healthcare and Disability Insurance.md"
    },
    {
        "query": "Is there life insurance or disability coverage?",
        "expected_document": "Healthcare and Disability Insurance.md"
    },

    # =====================================================
    # SALARY & EQUITY (Direct, Specific Numbers, Employee Terminology)
    # =====================================================
    {
        "query": "How is salary determined at Clef?",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "What's the salary for a technical employee with more than 5 years experience?",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "How many stock options do new employees receive?",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "What is the equity vesting schedule?",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "Can I trade $5k of salary for more equity?",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "Why doesn't Clef negotiate salaries individually?",
        "expected_document": "Salary and Equity Compensation.md"
    },
    {
        "query": "How much do the founders make?",
        "expected_document": "Salary and Equity Compensation.md"
    },

    # =====================================================
    # REFERRAL BONUSES (Direct, Specific Numbers, Paraphrased)
    # =====================================================
    {
        "query": "How much is the referral bonus?",
        "expected_document": "Referral Bonuses.md"
    },
    {
        "query": "If I refer someone who gets hired, when do I get paid?",
        "expected_document": "Referral Bonuses.md"
    },
    {
        "query": "What's the process for referring a friend to work at Clef?",
        "expected_document": "Referral Bonuses.md"
    },
    {
        "query": "Are founders eligible for the referral bonus?",
        "expected_document": "Referral Bonuses.md"
    },
    {
        "query": "How long does a referred candidate have to be hired within?",
        "expected_document": "Referral Bonuses.md"
    },

    # =====================================================
    # OTHER PROTECTED ABSENCES (Direct, Vague, Related Policies)
    # =====================================================
    {
        "query": "How many days of bereavement leave can I take?",
        "expected_document": "Other Protected Absences.md"
    },
    {
        "query": "I got called for jury duty, am I still paid?",
        "expected_document": "Other Protected Absences.md"
    },
    {
        "query": "My mother-in-law passed away, can I take time off?",
        "expected_document": "Other Protected Absences.md"
    },
    {
        "query": "What is pregnancy disability leave and how long is it?",
        "expected_document": "Other Protected Absences.md"
    },
    {
        "query": "I have a family emergency, what should I do?",
        "expected_document": "Other Protected Absences.md"
    },

    # =====================================================
    # WORKING REMOTELY (Direct, Paraphrased, Employee Terminology)
    # =====================================================
    {
        "query": "What's Clef's policy on working from home?",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "Can I work remotely for a whole week?",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "Do I need my manager's approval to work remotely for an extended period?",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "Does Clef pay for coworking spaces?",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "What happens if I'm not performing well while working remotely?",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "How far in advance do I need to notify the team about extended remote work?",
        "expected_document": "Working Remotely.md"
    },
    {
        "query": "I want to work from my partner's place in another city for a few days — what do I need to do?",
        "expected_document": "Working Remotely.md"
    },

    # =====================================================
    # EMPLOYEE PRIVACY (Direct, Paraphrased, Vague)
    # =====================================================
    {
        "query": "Can the company read my emails?",
        "expected_document": "Employee Privacy.md"
    },
    {
        "query": "Does Clef monitor internet usage?",
        "expected_document": "Employee Privacy.md"
    },
    {
        "query": "Can my manager search my desk or laptop?",
        "expected_document": "Employee Privacy.md"
    },
    {
        "query": "Is it okay to send personal emails from my work account?",
        "expected_document": "Employee Privacy.md"
    },
    {
        "query": "What should I do if I think my computer has a virus?",
        "expected_document": "Employee Privacy.md"
    },
    {
        "query": "Can I share my work email password with a coworker?",
        "expected_document": "Employee Privacy.md"
    },

    # =====================================================
    # CODE OF CONDUCT (Direct, Paraphrased, Vague)
    # =====================================================
    {
        "query": "What behavior is not tolerated in Clef community spaces?",
        "expected_document": "Code of Conduct in the Community.md"
    },
    {
        "query": "Someone is being rude in the Clef Slack channel — what should I do?",
        "expected_document": "Code of Conduct in the Community.md"
    },
    {
        "query": "Does the code of conduct apply to Twitter and Facebook?",
        "expected_document": "Code of Conduct in the Community.md"
    },
    {
        "query": "Who do I contact about harassment in a Clef community?",
        "expected_document": "Code of Conduct in the Community.md"
    },

    # =====================================================
    # COMPLAINT POLICY (Direct, Vague, Related Policies)
    # =====================================================
    {
        "query": "How do I file a workplace complaint at Clef?",
        "expected_document": "Complaint Policy.md"
    },
    {
        "query": "Will I face retaliation for reporting a problem?",
        "expected_document": "Complaint Policy.md"
    },
    {
        "query": "What happens after I submit a complaint?",
        "expected_document": "Complaint Policy.md"
    },
    {
        "query": "What if my complaint is about one of the founders?",
        "expected_document": "Complaint Policy.md"
    },

    # =====================================================
    # DRUG & ALCOHOL POLICY (Direct, Vague)
    # =====================================================
    {
        "query": "Is alcohol allowed in the office?",
        "expected_document": "Drug and Alcohol Policy.md"
    },
    {
        "query": "What is Clef's policy on recreational drug use?",
        "expected_document": "Drug and Alcohol Policy.md"
    },
    {
        "query": "Can we have beer at a company celebration?",
        "expected_document": "Drug and Alcohol Policy.md"
    },

    # =====================================================
    # AT-WILL EMPLOYMENT (Direct, Paraphrased)
    # =====================================================
    {
        "query": "Can Clef fire me without a reason?",
        "expected_document": "At-Will Employment.md"
    },
    {
        "query": "What does at-will employment mean at Clef?",
        "expected_document": "At-Will Employment.md"
    },
    {
        "query": "Who can change my at-will employment status?",
        "expected_document": "At-Will Employment.md"
    },

    # =====================================================
    # EQUAL OPPORTUNITY EMPLOYMENT (Direct, Related Policies)
    # =====================================================
    {
        "query": "Does Clef discriminate based on gender or race?",
        "expected_document": "Equal Opportunity Employment.md"
    },
    {
        "query": "What is Clef's stance on diversity in hiring?",
        "expected_document": "Equal Opportunity Employment.md"
    },

    # =====================================================
    # CLEF VALUES (Direct, Paraphrased, Vague)
    # =====================================================
    {
        "query": "What are Clef's core values?",
        "expected_document": "Clef Values.md"
    },
    {
        "query": "What does 'be better today than yesterday' mean?",
        "expected_document": "Clef Values.md"
    },
    {
        "query": "How does Clef think about inclusion?",
        "expected_document": "Clef Values.md"
    },
    {
        "query": "Why does Clef emphasize trust?",
        "expected_document": "Clef Values.md"
    },

    # =====================================================
    # MISSION STATEMENT (Direct, Vague)
    # =====================================================
    {
        "query": "What is Clef's mission?",
        "expected_document": "Mission Statement.md"
    },
    {
        "query": "What problem is Clef trying to solve?",
        "expected_document": "Mission Statement.md"
    },

    # =====================================================
    # ONBOARDING / WELCOME (Direct, Employee Terminology, Vague)
    # =====================================================
    {
        "query": "What should I expect on my first day at Clef?",
        "expected_document": "Welcome to Clef.md"
    },
    {
        "query": "What are the typical working hours at Clef?",
        "expected_document": "Welcome to Clef.md"
    },
    {
        "query": "How does Clef celebrate a new employee's first day?",
        "expected_document": "Welcome to Clef.md"
    },
    {
        "query": "I just got hired, where do I start?",
        "expected_document": "Welcome to Clef.md"
    },
    {
        "query": "What is the goal for my first day at work?",
        "expected_document": "Welcome to Clef.md"
    },

    # =====================================================
    # HANDBOOK INTRODUCTION (Direct)
    # =====================================================
    {
        "query": "Who is the CEO of Clef?",
        "expected_document": "Handbook Introduction.md"
    },
    {
        "query": "What is the purpose of the employee handbook?",
        "expected_document": "Handbook Introduction.md"
    },

    # =====================================================
    # ONE ON ONES (Direct, Paraphrased, Employee Terminology)
    # =====================================================
    {
        "query": "How often are one-on-one meetings held?",
        "expected_document": "One on Ones.md"
    },
    {
        "query": "Who sets the agenda for 1:1 meetings?",
        "expected_document": "One on Ones.md"
    },
    {
        "query": "What's the minimum duration of a one on one?",
        "expected_document": "One on Ones.md"
    },

    # =====================================================
    # OBJECTIVES AND KEY RESULTS (Direct, Specific Numbers, Employee Terminology)
    # =====================================================
    {
        "query": "How are OKRs scored at Clef?",
        "expected_document": "Objectives and Key Results.md"
    },
    {
        "query": "How often do we set OKRs?",
        "expected_document": "Objectives and Key Results.md"
    },
    {
        "query": "Are OKRs used for performance reviews?",
        "expected_document": "Objectives and Key Results.md"
    },
    {
        "query": "What is a good OKR score?",
        "expected_document": "Objectives and Key Results.md"
    },

    # =====================================================
    # COMMUNICATION & TRANSPARENCY (Direct, Paraphrased)
    # =====================================================
    {
        "query": "What happens on Fridays in terms of team updates?",
        "expected_document": "Communication and Transparency.md"
    },
    {
        "query": "How should I use Slack when working remotely?",
        "expected_document": "Communication and Transparency.md"
    },
    {
        "query": "Should conversations happen in public or private Slack channels?",
        "expected_document": "Communication and Transparency.md"
    },

    # =====================================================
    # DIRECT REPORTS (Direct)
    # =====================================================
    {
        "query": "Who do employees report to at Clef?",
        "expected_document": "Direct Reports.md"
    },

    # =====================================================
    # PRODUCT MANIFESTO (Direct, Paraphrased, Vague)
    # =====================================================
    {
        "query": "What is Clef's core product value?",
        "expected_document": "Product Manifesto.md"
    },
    {
        "query": "Why do people love using Clef over other login solutions?",
        "expected_document": "Product Manifesto.md"
    },

    # =====================================================
    # OPERATIONS: BUDGETING, HACK WEEKS, SHARING FILES, EFFECTIVE MEETINGS
    # =====================================================
    {
        "query": "How is company spending organized at Clef?",
        "expected_document": "Budgeting.md"
    },
    {
        "query": "What are the budget categories at Clef?",
        "expected_document": "Budgeting.md"
    },
    {
        "query": "What is a hack week and when does it happen?",
        "expected_document": "Hack Weeks.md"
    },
    {
        "query": "Can I work on personal projects during hack week?",
        "expected_document": "Hack Weeks.md"
    },
    {
        "query": "How should files and projects be organized at Clef?",
        "expected_document": "Sharing Files.md"
    },
    {
        "query": "What are the base directories every Clef employee should have?",
        "expected_document": "Sharing Files.md"
    },
    {
        "query": "What are the meeting time requirements at Clef?",
        "expected_document": "Effective Meetings.md"
    },
    {
        "query": "Do meetings need to have a video call option?",
        "expected_document": "Effective Meetings.md"
    },

    # =====================================================
    # POLICY CHANGES (Direct, Paraphrased)
    # =====================================================
    {
        "query": "How are policy changes proposed and adopted at Clef?",
        "expected_document": "Policy Changes.md"
    },
    {
        "query": "What tools does Clef use for policy discussions?",
        "expected_document": "Policy Changes.md"
    },

    # =====================================================
    # README / HANDBOOK OVERVIEW
    # =====================================================
    # {
    #     "query": "Why did Clef open source their employee handbook?",
    #     "expected_document": "README.md"
    # },

    # =====================================================
    # CROSS-DOCUMENT / SEMANTICALLY SIMILAR DOCUMENT QUERIES
    # These are tricky — two docs could plausibly match
    # =====================================================
    {
        "query": "What kind of time off can I get after becoming a new parent?",
        "expected_document": "New Parent Leave.md"
    },
    {
        "query": "How does taking parental leave affect my sabbatical eligibility?",
        "expected_document": "New Parent Leave.md"
    },
    {
        "query": "What's the difference between sick leave and vacation?",
        "expected_document": "Vacation and Sick Leave.md"
    },
    {
        "query": "If something bad happens at work who should I talk to — my manager or HR?",
        "expected_document": "Complaint Policy.md"
    },
    {
        "query": "Does the code of conduct apply inside the office or only online?",
        "expected_document": "Code of Conduct in the Community.md"
    },
]
