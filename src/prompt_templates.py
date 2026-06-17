"""
Advanced prompt templates using Role-Playing, Few-Shot Learning, and Chain-of-Thought.
"""

ROLE_PLAYING_TEMPLATE = """
You are an expert professional email writer with 15+ years of experience in corporate communications. 
You specialize in crafting clear, concise, and impactful emails that achieve their intended purpose 
while maintaining appropriate tone and professionalism.
"""

FEW_SHOT_EXAMPLES = """
Here are two examples of excellent professional emails:

EXAMPLE 1:
Intent: Follow up after meeting
Key Facts: 
- Met with Sarah Johnson yesterday at 2 PM
- Discussed Q3 marketing strategy
- Need her feedback on budget proposal by Friday
Tone: Professional but friendly

Subject: Following Up on Our Q3 Marketing Discussion

Hi Sarah,

It was great meeting with you yesterday afternoon to discuss our Q3 marketing strategy. I really appreciated your insights on the target audience segmentation.

As we discussed, I've prepared the initial budget proposal. Could you please review it and share your feedback by this Friday? This will help us stay on track for our early July launch timeline.

Looking forward to hearing from you!

Best regards,
[Your Name]

---

EXAMPLE 2:
Intent: Request for proposal details
Key Facts:
- Received RFP #2024-089 last week
- Deadline is March 15th
- Need clarification on technical requirements section 4.2
Tone: Formal and urgent

Subject: Urgent: Clarification Needed for RFP #2024-089 - Section 4.2

Dear Procurement Team,

I am writing regarding RFP #2024-089. We are actively preparing our response for the March 15th deadline.

However, we require clarification on Section 4.2 (Technical Requirements). The current language leaves room for interpretation. Could you please provide additional details by end of day tomorrow?

Thank you for your prompt attention to this matter.

Sincerely,
[Your Name]
"""

CHAIN_OF_THOUGHT_GUIDANCE = """
Before writing the email, think through these steps:
1. Analyze the Intent - What is the primary goal?
2. Review Key Facts - How can they be woven in naturally?
3. Consider the Tone - What words match this tone?
4. Plan the Structure - Subject line, greeting, body, closing
5. Write and Refine - Draft the email ensuring all facts are included.
"""

def build_complete_prompt(intent: str, key_facts: list, tone: str) -> str:
    facts_formatted = "\n".join([f"- {fact}" for fact in key_facts])
    
    prompt = f"""
{ROLE_PLAYING_TEMPLATE}

{FEW_SHOT_EXAMPLES}

{CHAIN_OF_THOUGHT_GUIDANCE}

---

YOUR TASK:

Generate a professional email based on the following inputs:

**Intent:** {intent}

**Key Facts:**
{facts_formatted}

**Tone:** {tone}

**Requirements:**
1. Create a compelling subject line
2. Include ALL key facts naturally in the body
3. Maintain the specified tone throughout
4. Use proper email format
5. Keep it concise (150-300 words)

Generate the email now:
"""
    return prompt


def build_simple_prompt(intent: str, key_facts: list, tone: str) -> str:
    facts_formatted = "\n".join([f"- {fact}" for fact in key_facts])
    
    prompt = f"""
Write a professional email with the following specifications:

Intent: {intent}
Key Facts:
{facts_formatted}
Tone: {tone}

Make sure to include all key facts and maintain the specified tone.
"""
    return prompt
