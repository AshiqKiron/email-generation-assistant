"""
Custom evaluation metrics for email generation.
"""
import numpy as np
import os
from groq import Groq

class CustomMetrics:
    def __init__(self):
        # Initialize Groq client for the Judge metric
        self.judge_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.judge_model = "llama-3.3-70b-versatile"

    @staticmethod
    def fact_recall_integration_score(generated_email: str, key_facts: list) -> float:
        """Metric 1: Fact Recall & Integration Score (FRIS)"""
        if not key_facts: return 1.0
        facts_found = 0
        total_facts = len(key_facts)
        for fact in key_facts:
            keywords = [word.lower() for word in fact.split() if len(word) > 3]
            if not keywords: continue
            matches = sum(1 for kw in keywords if kw in generated_email.lower())
            if matches > 0: facts_found += 1
        recall = facts_found / total_facts if total_facts > 0 else 0
        return round(recall * 100, 2)

    @staticmethod
    def tone_consistency_index(generated_email: str, desired_tone: str) -> float:
        """Metric 2: Tone Consistency Index (TCI)"""
        tone_keywords = {
            "formal": ["dear", "sincerely", "regards", "please", "kindly"],
            "casual": ["hi", "hey", "thanks", "cheers", "best"],
            "urgent": ["urgent", "immediately", "asap", "critical", "right away"],
            "apologetic": ["apologize", "sorry", "regret", "inconvenience", "pardon"],
            "enthusiastic": ["excited", "great", "wonderful", "looking forward", "thrilled"],
            "professional": ["professional", "efficient", "effective", "quality", "standard"]
        }
        tone_category = None
        for category, keywords in tone_keywords.items():
            if category in desired_tone.lower():
                tone_category = category
                break
        if not tone_category: return 50.0 
        email_lower = generated_email.lower()
        matches = sum(1 for kw in tone_keywords[tone_category] if kw in email_lower)
        max_possible = len(tone_keywords[tone_category])
        score = (matches / max_possible) * 100 if max_possible > 0 else 50
        return round(min(score, 100), 2)

    @staticmethod
    def structural_quality_score(generated_email: str) -> float:
        """Metric 3: Structural Quality Score (SQS)"""
        score = 0.0
        if "subject:" in generated_email.lower(): score += 30
        greetings = ["dear", "hi", "hello", "good morning"]
        if any(g in generated_email.lower() for g in greetings): score += 20
        closings = ["best regards", "sincerely", "thank you", "best", "cheers"]
        if any(c in generated_email.lower() for c in closings): score += 20
        if "\n" in generated_email: score += 15
        if len(generated_email.split()) > 50: score += 15
        return round(score, 2)

    def llm_judge_score(self, generated_email: str, intent: str, key_facts: list, tone: str) -> float:
        """
        Metric 4: LLM-as-a-Judge Business Email Quality Score.
        Evaluates semantic quality, fact preservation, and professionalism.
        """
        facts_str = "\n".join([f"- {f}" for f in key_facts])
        
        prompt = f"""
You are an expert business communication judge. Evaluate the following email based on:
1. Fact Preservation: Are all key facts included?
2. Tone Match: Does it match the requested tone?
3. Professional Clarity: Is it clear and concise?
4. No Hallucinations: Are there any invented details?
5. Ready-to-Send: Is it professional enough to send immediately?

Intent: {intent}
Key Facts:
{facts_str}
Tone: {tone}

Generated Email:
{generated_email}

Provide a score from 1 to 5 (1=Poor, 5=Excellent). Return ONLY the number.
"""
        try:
            completion = self.judge_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.judge_model,
                temperature=0,
                max_tokens=10
            )
            raw_score = completion.choices[0].message.content.strip()
            # Extract just the number if the model adds text
            score = float(''.join(filter(str.isdigit, raw_score)))
            return round((score / 5) * 100, 2)
        except Exception as e:
            print(f"Judge Error: {e}")
            return 0.0
