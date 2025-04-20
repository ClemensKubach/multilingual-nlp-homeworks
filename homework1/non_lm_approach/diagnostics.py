import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Load predictions (title-cased labels)
df = pd.read_csv("data/rule_predictions.csv")

# Normalize label casing (just in case)
df["label"] = df["label"].str.title()
df["rule_prediction"] = df["rule_prediction"].str.title()

# Label order for consistent display
labels_order = ["Cultural Agnostic", "Cultural Representative", "Cultural Exclusive"]

# 1. Ground Truth Class Distribution
print(" Ground Truth Label Distribution:")
gt_counts = df["label"].value_counts().reindex(labels_order, fill_value=0)
print(gt_counts)

print("\n Ground Truth Label Distribution (percentages):")
gt_percent = df["label"].value_counts(normalize=True).reindex(labels_order, fill_value=0) * 100
print(gt_percent.round(2))

# 2. Predicted Class Distribution
print("\n Predicted Label Distribution:")
pred_counts = df["rule_prediction"].value_counts().reindex(labels_order, fill_value=0)
print(pred_counts)

# 3. Baseline Accuracy
most_frequent_class = df["label"].value_counts().idxmax()
baseline_accuracy = (df["label"] == most_frequent_class).mean()
print(f"\n Baseline Accuracy (if model predicted only '{most_frequent_class}'): {baseline_accuracy:.2f}")

# 4. Confusion Matrix
cm = confusion_matrix(df["label"], df["rule_prediction"], labels=labels_order)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=labels_order, yticklabels=labels_order)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix – Rule-Based Classifier")
plt.tight_layout()
plt.show()

# 5. Histogram: GT vs Predicted
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
gt_counts.plot(kind="bar", color="skyblue")
plt.title("Ground Truth Label Distribution")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
pred_counts.plot(kind="bar", color="salmon")
plt.title("Predicted Label Distribution")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

