"""
Custom evaluation metrics for email generation.
"""
import numpy as np

class CustomMetrics:
    @staticmethod
    def fact_recall_integration_score(generated_email: str, key_facts: list) -> float:
        """
        Metric 1: Fact Recall & Integration Score (FRIS)
        Measures how well key facts are included and naturally integrated.
        """
        if not key_facts:
            return 1.0
        
        score = 0.0
        facts_found = 0
        total_facts = len(key_facts)
        
        for fact in key_facts:
            keywords = [word.lower() for word in fact.split() if len(word) > 3]
            if not keywords:
                continue
                
            matches = sum(1 for kw in keywords if kw in generated_email.lower())
            if matches > 0:
                facts_found += 1
        
        recall = facts_found / total_facts if total_facts > 0 else 0
        return round(recall * 100, 2)

    @staticmethod
    def tone_consistency_index(generated_email: str, desired_tone: str) -> float:
        """
        Metric 2: Tone Consistency Index (TCI)
        Evaluates whether the generated email maintains the requested tone.
        """
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
        
        if not tone_category:
            return 50.0 
        
        email_lower = generated_email.lower()
        matches = sum(1 for kw in tone_keywords[tone_category] if kw in email_lower)
        
        max_possible = len(tone_keywords[tone_category])
        score = (matches / max_possible) * 100 if max_possible > 0 else 50
        return round(min(score, 100), 2)

    @staticmethod
    def structural_quality_score(generated_email: str) -> float:
        """
        Metric 3: Structural Quality Score (SQS)
        Assesses formatting, logical flow, and overall clarity.
        """
        score = 0.0
        
        if "subject:" in generated_email.lower():
            score += 30
        
        greetings = ["dear", "hi", "hello", "good morning"]
        if any(g in generated_email.lower() for g in greetings):
            score += 20
        
        closings = ["best regards", "sincerely", "thank you", "best", "cheers"]
        if any(c in generated_email.lower() for c in closings):
            score += 20
        
        if "\n" in generated_email:
            score += 15
        
        if len(generated_email.split()) > 50:
            score += 15
            
        return round(score, 2)
