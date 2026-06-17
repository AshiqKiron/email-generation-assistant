"""
Evaluation pipeline for comparing models.
"""
import json
import csv
import os
import numpy as np # Added this import
from tqdm import tqdm
from src.email_generator import EmailGenerator
from src.test_scenarios import TEST_SCENARIOS
from src.metrics import CustomMetrics
from config import OUTPUT_DIR, MODEL_A, MODEL_B

class Evaluator:
    def __init__(self):
        self.metrics = CustomMetrics()
        self.generator_a = EmailGenerator(MODEL_A)
        self.generator_b = EmailGenerator(MODEL_B)

    def evaluate_scenario(self, scenario: dict, generator: EmailGenerator) -> dict:
        intent = scenario["intent"]
        key_facts = scenario["key_facts"]
        tone = scenario["tone"]
        reference = scenario["reference_email"]
        
        generated_email = generator.generate_email(intent, key_facts, tone)
        
        fris = self.metrics.fact_recall_integration_score(generated_email, key_facts)
        tci = self.metrics.tone_consistency_index(generated_email, tone)
        sqs = self.metrics.structural_quality_score(generated_email)
        
        return {
            "scenario_id": scenario["id"],
            "intent": intent,
            "generated_email": generated_email,
            "reference_email": reference,
            "metrics": {
                "Fact_Recall_Integration_Score": fris,
                "Tone_Consistency_Index": tci,
                "Structural_Quality_Score": sqs
            }
        }

    def run_evaluation(self, model_name: str, generator: EmailGenerator) -> list:
        results = []
        print(f"\nEvaluating {model_name}...")
        
        for scenario in tqdm(TEST_SCENARIOS):
            result = self.evaluate_scenario(scenario, generator)
            results.append(result)
            
        return results

    def save_results(self, model_name: str, results: list):
        filename = os.path.join(OUTPUT_DIR, f"{model_name.replace(' ', '_').lower()}_results.json")
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {filename}")

    def generate_comparison_report(self, results_a: list, results_b: list):
        filename = os.path.join(OUTPUT_DIR, "comparison_report.csv")
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Scenario ID", "Intent", "Model_A_Fact_Score", "Model_B_Fact_Score", 
                           "Model_A_Tone_Score", "Model_B_Tone_Score", 
                           "Model_A_Structure_Score", "Model_B_Structure_Score"])
            
            for res_a, res_b in zip(results_a, results_b):
                writer.writerow([
                    res_a["scenario_id"],
                    res_a["intent"],
                    res_a["metrics"]["Fact_Recall_Integration_Score"],
                    res_b["metrics"]["Fact_Recall_Integration_Score"],
                    res_a["metrics"]["Tone_Consistency_Index"],
                    res_b["metrics"]["Tone_Consistency_Index"],
                    res_a["metrics"]["Structural_Quality_Score"],
                    res_b["metrics"]["Structural_Quality_Score"]
                ])
        
        print(f"Comparison report saved to {filename}")

    def calculate_averages(self, results: list) -> dict:
        avg_fris = np.mean([r["metrics"]["Fact_Recall_Integration_Score"] for r in results])
        avg_tci = np.mean([r["metrics"]["Tone_Consistency_Index"] for r in results])
        avg_sqs = np.mean([r["metrics"]["Structural_Quality_Score"] for r in results])
        
        return {
            "Average_Fact_Recall_Integration_Score": round(avg_fris, 2),
            "Average_Tone_Consistency_Index": round(avg_tci, 2),
            "Average_Structural_Quality_Score": round(avg_sqs, 2),
            "Overall_Average": round((avg_fris + avg_tci + avg_sqs) / 3, 2)
        }
