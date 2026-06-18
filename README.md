# AI Engineer Candidate Assessment: Email Generation Assistant

## 📋 Project Overview
This project implements a robust **Email Generation Assistant** prototype designed to generate professional emails based on specific user inputs. The system takes three distinct inputs—**Intent**, **Key Facts**, and **Tone**—and produces a well-structured, professional email using Large Language Models (LLMs). 

Beyond generation, this project features a comprehensive **Evaluation Pipeline** that uses custom-defined metrics to measure performance and compares two different LLM strategies to determine the optimal approach for production use.

---

## 🧠 Prompting Strategy
To maximize output quality and reliability, this assistant utilizes an **Advanced Prompt Engineering** framework combining three key techniques:

1.  **Role-Playing:** The model is assigned the persona of an "Expert Professional Email Writer" with 15+ years of corporate communication experience. This primes the model to adopt a professional tone and structure.
2.  **Few-Shot Learning:** The prompt includes two high-quality example emails (one formal, one casual) to demonstrate the expected format, subject line style, and fact integration.
3.  **Internal Self-Check:** The model is instructed to silently verify fact coverage, tone match, and structure before returning only the final email.

---

## 📏 Custom Metrics Definitions
Three custom metrics were defined and implemented to evaluate the quality of the generated emails:

### 1. Fact Recall & Integration Score (FRIS)
*   **Focus:** Accuracy and Completeness.
*   **Logic:** Measures the percentage of required "Key Facts" that are present in the generated email. It uses keyword matching to ensure that critical information (dates, names, figures) is not omitted.

### 2. Tone Consistency Index (TCI)
*   **Focus:** Style Adherence.
*   **Logic:** Evaluates whether the generated email maintains the requested tone (e.g., "Urgent," "Casual," "Formal"). It checks for the presence of tone-specific vocabulary (e.g., "ASAP" for urgent, "Cheers" for casual) throughout the body.

### 3. Structural Quality Score (SQS)
*   **Focus:** Formatting and Professionalism.
*   **Logic:** A rule-based metric that checks for essential email components:
    *   Presence of a Subject Line.
    *   Proper Greeting and Closing.
    *   Paragraph breaks for readability.
    *   Minimum word count to ensure conciseness without being too brief.

---

## 🛠️ Setup Instructions

### Prerequisites
*   Python 3.8 or higher
*   A free [Groq API Key](https://console.groq.com/)

### Installation
1.  Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd email-generation-assistant
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration
This project uses environment variables for security. 
*   **For Local Use:** Create a `.env` file in the root directory and add:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```
*   **For GitHub Actions:** Add `GROQ_API_KEY` to your repository's **Settings > Secrets and Variables > Actions**.

---

## ▶️ How to Run

You can run the assessment locally or via GitHub Actions.

### Local Execution
```bash
python main.py
```

### GitHub Actions
Push code to the `main` branch or manually trigger the workflow from the **Actions** tab. The workflow will automatically:
1.  Install dependencies.
2.  Run the evaluation against both models.
3.  Upload the results as an artifact.

---

## 📂 Output Files
After running the assessment, the following files are generated in the `data/results/` directory:
Final report is available at data/final_report.pdf.

| File Name | Description |
| :--- | :--- |
| `model_a_results.json` | Raw generated emails and scores for Model A (Llama 3.3). |
| `model_b_results.json` | Raw generated emails and scores for Model B (Mixtral 8x7b). |
| `comparison_report.csv` | A side-by-side comparison of scores for all 10 scenarios. |
| `comprehensive_report.json` | Summary of average scores for both models. |

---

## ⚖️ Model Comparison Explanation
The assessment compares two distinct models available on the Groq platform:

*   **Model A: `llama-3.3-70b-versatile`**
    *   A state-of-the-art open-weight model known for high reasoning capabilities and nuanced language understanding. Model A uses Llama 3.3 70B through Groq.
*   **Model B: `mixtral-8x7b-32768`**
    *   A sparse mixture-of-experts model known for speed and efficiency, though sometimes less nuanced than larger dense models. Model B uses Mixtral 8x7B through Groq.
    *   Both models use the same 10 scenarios and same 3 metrics.

**Analysis Goal:**
The comparative analysis (found in the Final Report) determines which model better balances **Fact Recall**, **Tone Accuracy**, and **Structural Integrity**. The results help identify the most cost-effective and reliable model for production deployment.
