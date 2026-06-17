"""
LLM Integration layer using Groq API.
"""
import time
from groq import Groq
from src.prompt_templates import build_complete_prompt, build_simple_prompt

class EmailGenerator:
    def __init__(self, model_config: dict):
        self.model_config = model_config
        self.client = Groq(api_key=model_config["api_key"])
        self.model_name = model_config["model_name"]

    def generate_email(self, intent: str, key_facts: list, tone: str, use_advanced_prompt: bool = True) -> str:
        if use_advanced_prompt:
            prompt = build_complete_prompt(intent, key_facts, tone)
        else:
            prompt = build_simple_prompt(intent, key_facts, tone)

        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional email assistant. Output only the email content."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model_name,
                temperature=self.model_config["temperature"],
                max_tokens=self.model_config["max_tokens"],
            )
            
            return completion.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"Error generating email with {self.model_name}: {e}")
            if "rate_limit" in str(e).lower():
                print("Rate limit hit. Waiting 10 seconds...")
                time.sleep(10)
                return self.generate_email(intent, key_facts, tone, use_advanced_prompt)
            return f"ERROR: Could not generate email. {str(e)}"

    def get_model_name(self) -> str:
        return self.model_name
