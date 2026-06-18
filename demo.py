"""
Interactive CLI Demo for the Email Generation Assistant.
"""
from src.email_generator import EmailGenerator
from config import MODEL_A

def main():
    print("--- Email Generation Assistant Demo ---")
    print(f"Using Model: {MODEL_A['model_name']}")
    
    intent = input("\nEnter Intent (e.g., Follow up after meeting): ")
    facts_input = input("Enter Key Facts (separated by semicolons): ")
    tone = input("Enter Tone (e.g., Professional, Casual, Urgent): ")
    
    key_facts = [f.strip() for f in facts_input.split(';') if f.strip()]
    
    if not intent or not key_facts or not tone:
        print("Error: All fields are required.")
        return

    generator = EmailGenerator(MODEL_A)
    print("\nGenerating email...\n")
    
    email = generator.generate_email(intent, key_facts, tone)
    print("-" * 40)
    print(email)
    print("-" * 40)

if __name__ == "__main__":
    main()
