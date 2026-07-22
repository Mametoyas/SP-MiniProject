import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.multioutput import MultiOutputClassifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# ============================================
# Load Dataset
# ============================================

df = pd.read_csv("hangman_dataset.csv",keep_default_na=False)

print(df.isna().sum())
text_cols = [
    "pattern",
    "guessed",
    "wrong"
]

for c in text_cols:
    df[c] = df[c].fillna("").astype(str)

# ============================================
# Features
# ============================================

feature_columns = [
    "pattern",
    "guessed",
    "wrong",
    "length",
    "revealed",
    "candidate_count"
]

X = df[feature_columns]

y = df[
    [
        "label1",
        "label2",
        "label3",
        "label4",
        "label5"
    ]
]

# ============================================
# Feature Engineering
# ============================================

numeric_features = [
    "length",
    "revealed",
    "candidate_count"
]

preprocessor = ColumnTransformer(
    transformers=[

        (
            "pattern",
            CountVectorizer(
                analyzer="char",
                ngram_range=(1,2)
            ),
            "pattern"
        ),

        (
            "guessed",
            CountVectorizer(
                analyzer="char"
            ),
            "guessed"
        ),

        (
            "wrong",
            CountVectorizer(
                analyzer="char"
            ),
            "wrong"
        ),

        (
            "numeric",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ]),
            numeric_features
        )

    ]
)

# Naive Bayes ใช้ scaler ไม่ได้
nb_preprocessor = ColumnTransformer(
    transformers=[

        (
            "pattern",
            CountVectorizer(
                analyzer="char",
                ngram_range=(1,2)
            ),
            "pattern"
        ),

        (
            "guessed",
            CountVectorizer(analyzer="char"),
            "guessed"
        ),

        (
            "wrong",
            CountVectorizer(analyzer="char"),
            "wrong"
        ),

        (
            "candidate_count",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median"))
            ]),
            ["candidate_count"]
        )

    ]
)

models = {

    "tree": Pipeline([
        ("features", preprocessor),
        ("classifier", MultiOutputClassifier(
            DecisionTreeClassifier(max_depth=50, random_state=42)
        ))
    ]),

    "rf": Pipeline([
        ("features", preprocessor),
        ("classifier", MultiOutputClassifier(
            RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
        ))
    ]),

    "lr": Pipeline([
        ("features", preprocessor),
        ("classifier", MultiOutputClassifier(
            LogisticRegression(max_iter=50, n_jobs=-1)
        ))
    ]),

    "nb": Pipeline([
        ("features", nb_preprocessor),
        ("classifier", MultiOutputClassifier(
            MultinomialNB()
        ))
    ]),

}

for name, model in models.items():
    model.fit(X, y)
    joblib.dump(model, f"../models/hangman_{name}.pkl")
    print(f"✓ {name} saved -> ../models/hangman_{name}.pkl")