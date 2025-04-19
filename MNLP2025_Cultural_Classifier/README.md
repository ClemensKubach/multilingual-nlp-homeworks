echo " MNLP2025 Cultural Classifier – Rule-Based Approach

This is a group project for the MNLP 2025 course, aiming to classify cultural items into one of three categories:

- **Cultural Agnostic**
- **Cultural Representative**
- **Cultural Exclusive**

The classification is based on enriched knowledge from **Wikidata** and a custom-built rule-based classifier.

---

## 📁 Project Structure

\`\`\`
MNLP2025_Cultural_Classifier/
├── data/                       # CSV files (original, processed, and enriched)
│   ├── validation_sapienza.csv
│   ├── validation_prepared.csv
│   ├── validation_enriched.csv
│   ├── rule_predictions.csv
│   └── train_sapienza.csv      # Optional, not currently used
├── diagnostics/                # Diagnostic tools for error analysis
│   └── frequent_instance_qids.py
├── scripts/                    # Main pipeline and supporting tools
│   ├── main.py
│   ├── diagnostics.py
│   ├── enrichment_coverage.py
│   ├── inspect_misclassified.py
│   └── diagnostics_analyze_exclusive.py
├── requirements.txt
└── README.md
\`\`\`

---

## 🧩 Workflow Overview

### 1. **Data Preparation**
- Extract QIDs from \`validation_sapienza.csv\`
- Output: \`validation_prepared.csv\`

### 2. **Data Enrichment**
- For each QID, fetch data from Wikidata using the SPARQL API:
  - \`instance_of\`, \`part_of_culture\`, \`heritage_status\`, etc.
- Output: \`validation_enriched.csv\`

### 3. **Rule-Based Classification**
- Uses manually designed logic based on common \`instance_of\` and \`heritage_status\` values.
- The main classifier logic is in \`main.py\`.
- Output: \`rule_predictions.csv\`

### 4. **Evaluation**
- Calculates accuracy, classification report, and confusion matrix.
- Displays label distribution (GT vs Prediction) and highlights imbalance.
- Run diagnostics from \`diagnostics.py\`

---

## 🧪 How to Run the Project

### 🔧 Setup
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### ▶️ Run the Classifier
\`\`\`bash
python scripts/main.py
\`\`\`

### 📊 Run Diagnostics
\`\`\`bash
python scripts/diagnostics.py
\`\`\`

---

## ✅ Results So Far

- Accuracy: ~ **56%**
- Strong precision on **Cultural Agnostic**
- Improving **Cultural Representative** and **Cultural Exclusive** using targeted QID-based rule tuning

---

## 🚧 Next Steps (for team continuation)

- Add more \`instance_of\` and \`part_of_culture\` QIDs to improve underperforming classes
- Explore adding multilingual label support (e.g., using aliases from Wikidata)
- Combine with LM-based approach for hybrid prediction

---

## 🙌 Contributors
- Joshua Edwin, Clemens Kubach(teXt-Men)

Feel free to continue this project and improve the rule-based logic!

---
" > README.md
