# This script is used to analyze where the rule-based classifier is making mistakes,
# especially on cultural exclusive items. looks at the most common instance_of and
# part_of_culture QIDs in those misclassified examples.

import pandas as pd
import ast
from collections import Counter

df = pd.read_csv("rule_predictions.csv")
df_enriched = pd.read_csv("data/validation_enriched.csv")
df_val = pd.read_csv("data/validation_prepared.csv")

# Merge and align
df_all = df_enriched.merge(df_val[["qid", "label"]], on="qid")
df_all = df_all.merge(df[["qid", "rule_prediction"]], on="qid")

# Filter misclassified predictions
misclassified = df_all[df_all["label"].str.title() != df_all["rule_prediction"].str.title()]

# Extract instance_of terms
misclassified["instance_of"] = misclassified["instance_of"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
instance_qids = [qid.lower() for sublist in misclassified["instance_of"] for qid in sublist]

# Count frequency
freq = Counter(instance_qids)
top_qids = freq.most_common(20)

print(" Top 20 instance_of QIDs in misclassified examples:")
for qid, count in top_qids:
    print(f"{qid}: {count}")
