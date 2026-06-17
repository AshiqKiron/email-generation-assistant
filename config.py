"""
Configuration settings for the Email Generation Assistant.
"""
import os

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please set it in GitHub Secrets or your local environment.")

# Model Configuration
MODEL_A = {
    "provider": "groq",
    "model_name": "llama-3.3-70b-versatile", # Updated to latest stable model
    "api_key": GROQ_API_KEY,
    "temperature": 0.2,
    "max_tokens": 1000
}

MODEL_B = {
    "provider": "groq",
    "model_name": "mixtral-8x7b-32768",
    "api_key": GROQ_API_KEY,
    "temperature": 0.2,
    "max_tokens": 1000
}

# Evaluation Configuration
NUM_TEST_SCENARIOS = 10
OUTPUT_DIR = "data/results"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)
