import time
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# ===========================================================
# Load Dataset
# ===========================================================

df = pd.read_csv("hangman_dataset.csv", keep_default_na=False)

for c in ["pattern", "guessed", "wrong"]:
    df[c] = df[c].fillna("").astype(str)

feature_columns = ["pattern", "guessed", "wrong", "length", "revealed", "candidate_count"]
label_columns   = ["label1", "label2", "label3", "label4", "label5"]

X = df[feature_columns]
y = df[label_columns]

# ===========================================================
# Train/Test Split
# ===========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===========================================================
# Load & Evaluate
# ===========================================================

MODEL_NAMES = ["tree", "rf", "lr", "nb"]

results = []
best_top1 = 0
best_name = None

for name in MODEL_NAMES:

    path = f"../models/hangman_{name}.pkl"

    try:
        model = joblib.load(path)
    except FileNotFoundError:
        print(f"[skip] {path} not found")
        continue

    print("=" * 60)
    print(name)

    start = time.time()
    pred = model.predict(X_test)          # shape (n, 5)
    predict_time = time.time() - start

    y_true_arr = y_test.values            # shape (n, 5)

    # top-1 accuracy: label1 ตรงกัน
    top1 = accuracy_score(y_true_arr[:, 0], pred[:, 0])

    # top-5 accuracy: ตัวที่ทายมาอยู่ใน label1-5 จริงมั้ย
    top5 = np.mean([
        pred[i, 0] in y_true_arr[i]
        for i in range(len(pred))
    ])

    # per-label metrics (label1 only)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true_arr[:, 0], pred[:, 0],
        average="weighted", zero_division=0
    )

    print(f"Top-1 Accuracy : {top1:.4f}")
    print(f"Top-5 Accuracy : {top5:.4f}")
    print(f"Precision      : {precision:.4f}")
    print(f"Recall         : {recall:.4f}")
    print(f"F1 Score       : {f1:.4f}")
    print(f"Predict Time(s): {predict_time:.2f}")

    results.append({
        "Model"           : name,
        "Top-1 Accuracy"  : top1,
        "Top-5 Accuracy"  : top5,
        "Precision"       : precision,
        "Recall"          : recall,
        "F1 Score"        : f1,
        "Predict Time (s)": predict_time,
    })

    if top1 > best_top1:
        best_top1 = top1
        best_name = name

# ===========================================================
# Save Best Model
# ===========================================================

if best_name:
    best_model = joblib.load(f"../models/hangman_{best_name}.pkl")
    joblib.dump(best_model, "../models/hangman_best.pkl")
    print(f"\nBest Model: {best_name} (top-1={best_top1:.4f}) -> ../models/hangman_best.pkl")

# ===========================================================
# Save Result
# ===========================================================

result_df = pd.DataFrame(results).sort_values(by="Top-1 Accuracy", ascending=False)
result_df.to_csv("../datasets/model_comparison.csv", index=False)

print("\n")
print(result_df)