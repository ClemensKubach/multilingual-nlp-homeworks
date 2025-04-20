import pandas as pd
import ast
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


# 1. Load Data

print(" Loading data...")
df_val = pd.read_csv("data/validation_prepared.csv")
df_enriched = pd.read_csv("data/validation_enriched.csv")

df_val["qid"] = df_val["qid"].astype(str)
df_enriched["qid"] = df_enriched["qid"].astype(str)

# Parse stringified list columns
list_columns = [
    "country_of_origin", "country", "located_in",
    "part_of_culture", "instance_of", "heritage_status"
]
for col in list_columns:
    df_enriched[col] = df_enriched[col].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

# Merge labels into enriched dataset
df_merged = df_enriched.merge(df_val[["qid", "label"]], on="qid")
print(" Successfully merged enriched and labeled datasets.")


# 2. Refined Rule-Based Classifier

def refined_rule_based_classifier(row):
    instance_of = [x.lower() for x in row["instance_of"]]
    culture = [x.lower() for x in row["part_of_culture"]]
    heritage = [x.lower() for x in row["heritage_status"]]

    # Updated Cultural Exclusive QIDs
    exclusive_qids = {
        "q12126757", "q12127133",  # UNESCO, Intangible Heritage
        "q847017", "q2221906",     # cultural identity, mythology
        "q12819564", "q740752",    # folk music, cultural region
        "q215380", "q12973014"     # ethnic group, indigenous community
    }

    if heritage or any(qid in exclusive_qids for qid in heritage + culture + instance_of):
        return "Cultural Exclusive"

    # Cultural Representative QIDs (already in use + genre-related)
    representative_qids = {
        "q5", "q11424", "q18127", "q20860083", "q4830453", "q6881511", "q7777573",
        "q55488", "q1339195", "q123705", "q40050", "q2221906", "q13418847", "q375336"
    }

    if any(inst in representative_qids for inst in instance_of):
        return "Cultural Representative"

    return "Cultural Agnostic"

# Apply classifier
df_merged["rule_prediction"] = df_merged.apply(refined_rule_based_classifier, axis=1)
df_merged["label"] = df_merged["label"].str.title()
df_merged["rule_prediction"] = df_merged["rule_prediction"].str.title()

# Save predictions
df_merged[["qid", "label", "rule_prediction"]].to_csv("rule_predictions.csv", index=False)
print(" Predictions saved to 'rule_predictions.csv'.")


# 3. Evaluation

accuracy = accuracy_score(df_merged["label"], df_merged["rule_prediction"])
print(f"\n Accuracy: {round(accuracy, 2)}")

print("\n Classification Report:")
print(classification_report(df_merged["label"], df_merged["rule_prediction"]))

# Confusion Matrix
labels_order = ["Cultural Agnostic", "Cultural Representative", "Cultural Exclusive"]
cm = confusion_matrix(df_merged["label"], df_merged["rule_prediction"], labels=labels_order)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels_order, yticklabels=labels_order)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix – Rule-Based Classifier")
plt.tight_layout()
plt.show()







