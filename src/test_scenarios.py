"""
Test scenarios for evaluating the Email Generation Assistant.
"""

TEST_SCENARIOS = [
    {
        "id": 1,
        "intent": "Follow up after job interview",
        "key_facts": [
            "Interviewed for Senior Developer position on Monday",
            "Spoke with hiring manager Jennifer Lee",
            "Excited about the company's AI initiatives",
            "Available to start in 3 weeks"
        ],
        "tone": "Professional and enthusiastic",
        "reference_email": """Subject: Thank You - Senior Developer Interview

Dear Jennifer,

Thank you so much for taking the time to meet with me on Monday to discuss the Senior Developer position. I truly enjoyed our conversation and learning more about your team's exciting work in AI initiatives.

I'm particularly excited about the opportunity to contribute to your machine learning projects. As mentioned during our conversation, I'm available to start within three weeks.

I look forward to hearing about next steps in the process.

Best regards,
[Candidate Name]"""
    },
    {
        "id": 2,
        "intent": "Request deadline extension for project",
        "key_facts": [
            "Current deadline is March 20th",
            "Need 5 additional days due to unexpected data quality issues",
            "New proposed deadline: March 25th",
            "Will deliver partial results by original deadline"
        ],
        "tone": "Professional and apologetic",
        "reference_email": """Subject: Request for Deadline Extension - Project Alpha

Dear [Manager Name],

I'm writing to request a brief extension for the Project Alpha deliverable currently due on March 20th. During our final data validation phase, we discovered some unexpected data quality issues.

To ensure high quality, I'm requesting a five-day extension to March 25th. I apologize for any inconvenience. I will still deliver partial results by the original March 20th deadline.

Thank you for your understanding.

Best regards,
[Your Name]"""
    },
    {
        "id": 3,
        "intent": "Decline meeting invitation politely",
        "key_facts": [
            "Invited to quarterly planning meeting on April 5th",
            "Have scheduling conflict with client presentation",
            "Would like to receive meeting notes afterward",
            "Happy to provide input via email beforehand"
        ],
        "tone": "Polite and professional",
        "reference_email": """Subject: Re: Quarterly Planning Meeting - April 5th

Hi [Organizer Name],

Thank you for inviting me to the quarterly planning meeting on April 5th. Unfortunately, I have a scheduling conflict with a client presentation.

Would it be possible to share the meeting notes with me afterward? Additionally, I'm happy to provide any input via email before the meeting.

Apologies for not being able to attend.

Best regards,
[Your Name]"""
    },
    {
        "id": 4,
        "intent": "Introduce new team member to clients",
        "key_facts": [
            "New account manager: Michael Chen",
            "Starting date: Next Monday",
            "10 years experience in financial services",
            "Will be primary contact going forward"
        ],
        "tone": "Warm and professional",
        "reference_email": """Subject: Introducing Your New Account Manager

Dear Valued Client,

I'm pleased to introduce Michael Chen, who will be joining our team as your new account manager starting next Monday. Michael brings over 10 years of experience in financial services.

Moving forward, Michael will be your primary point of contact. He's already been briefed on your account history.

We're confident that Michael will provide you with excellent service.

Warm regards,
[Your Name]"""
    },
    {
        "id": 5,
        "intent": "Report bug in production system",
        "key_facts": [
            "Bug found in payment processing module",
            "Affects approximately 15% of transactions",
            "Error code: PAY-4521",
            "Temporary workaround: manual verification"
        ],
        "tone": "Urgent and factual",
        "reference_email": """Subject: URGENT: Production Bug in Payment Processing Module

Hi Team,

I'm reporting a critical bug in our payment processing module. The issue affects approximately 15% of transactions.

Details:
- Error Code: PAY-4521
- Impact: ~15% of transactions failing
- Temporary workaround: Manual verification process implemented

The engineering team is investigating. Please prioritize this issue.

Regards,
[Your Name]"""
    },
    {
        "id": 6,
        "intent": "Request budget approval for software license",
        "key_facts": [
            "Need enterprise license for design tool",
            "Cost: $2,400 annually",
            "Will benefit 8 team members",
            "ROI: 20% productivity increase estimated"
        ],
        "tone": "Persuasive and professional",
        "reference_email": """Subject: Budget Approval Request: Enterprise Design Tool License

Dear [Manager Name],

I'm requesting approval for an enterprise license for our design tool ($2,400 annually). This will benefit all 8 members of our design team.

We estimate a 20% productivity increase, saving approximately 40 hours per month. The cost breaks down to just $300 per team member.

Thank you for considering this request.

Best regards,
[Your Name]"""
    },
    {
        "id": 7,
        "intent": "Apologize for delayed response to client",
        "key_facts": [
            "Client emailed 5 days ago",
            "Delay due to internal system migration",
            "Issue is now resolved",
            "Attached requested report"
        ],
        "tone": "Apologetic and reassuring",
        "reference_email": """Subject: Apologies for the Delay - Report Attached

Dear [Client Name],

Please accept my sincere apologies for the delay in responding to your email from 5 days ago. We experienced an unexpected internal system migration that slowed our response times.

The issue is now resolved, and I have attached the requested report. Thank you for your patience.

Best regards,
[Your Name]"""
    },
    {
        "id": 8,
        "intent": "Invite colleague to lunch for networking",
        "key_facts": [
            "Colleague: David from Marketing",
            "Purpose: Discuss cross-department collaboration",
            "Suggested time: Next Tuesday at 12:30 PM",
            "Location: Cafe downstairs"
        ],
        "tone": "Casual and friendly",
        "reference_email": """Subject: Lunch next Tuesday?

Hi David,

Hope you're having a good week!

I'd love to grab lunch next Tuesday at 12:30 PM at the cafe downstairs to chat about potential cross-department collaboration ideas. No agenda, just a casual chat.

Let me know if that works for you!

Best,
[Your Name]"""
    },
    {
        "id": 9,
        "intent": "Confirm attendance at conference",
        "key_facts": [
            "Conference: TechSummit 2024",
            "Date: October 10-12",
            "Will attend workshop on 'AI Ethics'",
            "Need hotel recommendation nearby"
        ],
        "tone": "Professional and inquisitive",
        "reference_email": """Subject: Confirmation: TechSummit 2024 Attendance

Dear Organizers,

I am writing to confirm my attendance at TechSummit 2024 (October 10-12). I have registered for the 'AI Ethics' workshop.

Could you please recommend any hotels nearby the venue?

Looking forward to the event.

Best regards,
[Your Name]"""
    },
    {
        "id": 10,
        "intent": "Resignation letter",
        "key_facts": [
            "Last day: November 30th",
            "Grateful for opportunities",
            "Will help with transition",
            "Reason: Pursuing further education"
        ],
        "tone": "Formal and grateful",
        "reference_email": """Subject: Resignation - [Your Name]

Dear [Manager Name],

Please accept this letter as formal notification that I am resigning from my position. My last day will be November 30th.

I am grateful for the opportunities I have had here. I am leaving to pursue further education. I will do everything possible to wrap up my duties and train other team members during this transition.

Thank you for your guidance.

Sincerely,
[Your Name]"""
    }
]
