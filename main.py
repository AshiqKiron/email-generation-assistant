"""
Main entry point for the Email Generation Assistant Assessment.
"""
import json
import os
import numpy as np
from src.evaluator import Evaluator
from config import MODEL_A, MODEL_B, OUTPUT_DIR

def main():
    print("Starting Email Generation Assistant Assessment...")
    print(f"Model A: {MODEL_A['model_name']}")
    print(f"Model B: {MODEL_B['model_name']}")
    
    evaluator = Evaluator()
    
    # Run Evaluation for Model A
    results_a = evaluator.run_evaluation("Model_A", evaluator.generator_a)
    evaluator.save_results("Model_A", results_a)
    averages_a = evaluator.calculate_averages(results_a)
    
    # Run Evaluation for Model B
    results_b = evaluator.run_evaluation("Model_B", evaluator.generator_b)
    evaluator.save_results("Model_B", results_b)
    averages_b = evaluator.calculate_averages(results_b)
    
    # Generate Comparison Report
    evaluator.generate_comparison_report(results_a, results_b)
    
    # Print Summary
    print("\n" + "="*50)
    print("EVALUATION SUMMARY")
    print("="*50)
    print(f"\nModel A ({MODEL_A['model_name']}):")
    print(json.dumps(averages_a, indent=2))
    
    print(f"\nModel B ({MODEL_B['model_name']}):")
    print(json.dumps(averages_b, indent=2))
    
    # Save comprehensive report
    comprehensive_report = {
        "model_a_averages": averages_a,
        "model_b_averages": averages_b,
        "model_a_name": MODEL_A['model_name'],
        "model_b_name": MODEL_B['model_name']
    }
    
    with open(os.path.join(OUTPUT_DIR, "comprehensive_report.json"), 'w') as f:
        json.dump(comprehensive_report, f, indent=2)
        
    print("\nAssessment Complete! Check data/results/ for outputs.")

if __name__ == "__main__":
    main()
