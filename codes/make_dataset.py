import random
import string
import pandas as pd
from collections import Counter
from itertools import combinations
from tqdm import tqdm

# ============================================
# Load Dictionary
# ============================================

with open("../datasets/words.txt", encoding="utf8") as f:
    words = [
        w.strip().lower()
        for w in f
        if w.strip().isalpha()
    ]

print(f"Loaded {len(words):,} words")

# ============================================
# Group by Length
# ============================================

words_by_length = {}

for w in words:
    words_by_length.setdefault(len(w), []).append(w)

alphabet = string.ascii_lowercase
alphabet_set = set(alphabet)

dataset = []

# ============================================
# Generate Dataset
# ============================================

for target in tqdm(words):

    letters = sorted(set(target))

    same_length_words = words_by_length[len(target)]

    for r in range(len(letters) + 1):

        for comb in combinations(letters, r):

            guessed = set(comb)

            # -----------------------------
            # Random Wrong Letters
            # -----------------------------

            possible_wrong = list(alphabet_set - set(target))

            wrong_size = random.randint(
                0,
                min(5, len(possible_wrong))
            )

            wrong = set(
                random.sample(
                    possible_wrong,
                    wrong_size
                )
            )

            # -----------------------------
            # Pattern
            # -----------------------------

            pattern = "".join(
                c if c in guessed else "_"
                for c in target
            )

            # -----------------------------
            # Candidate Search
            # -----------------------------

            candidates = []

            for w in same_length_words:

                if any(c in w for c in wrong):
                    continue

                ok = True

                for p, ch in zip(pattern, w):

                    if p == "_":

                        if ch in guessed:
                            ok = False
                            break

                    else:

                        if p != ch:
                            ok = False
                            break

                if ok:
                    candidates.append(w)

            candidate_count = len(candidates)

            if candidate_count == 0:
                continue

            # -----------------------------
            # Letter Frequency
            # -----------------------------

            freq = Counter()

            for w in candidates:

                for c in set(w):

                    if c not in guessed and c not in wrong:
                        freq[c] += 1

            if not freq:
                continue

            TOP_K = 5

            # เรียงตามความถี่
            top_letters = [c for c, _ in freq.most_common(TOP_K)]

            # ถ้ามีน้อยกว่า TOP_K
            while len(top_letters) < TOP_K:
                top_letters.append("")

            row = {

                "word": target,

                "pattern": pattern,

                "guessed": "".join(sorted(guessed)),

                "wrong": "".join(sorted(wrong)),

                "length": len(target),

                "revealed": len(guessed),

                "candidate_count": candidate_count,

                "label1": top_letters[0],
                "label2": top_letters[1],
                "label3": top_letters[2],
                "label4": top_letters[3],
                "label5": top_letters[4]

            }

            dataset.append(row)


# ============================================
# Save
# ============================================

df = pd.DataFrame(dataset)

df.drop_duplicates(inplace=True)

df.to_csv(
    "../datasets/hangman_dataset.csv",
    index=False
)

print(df.head())

print()

print("Dataset Size :", len(df))

print()

print(df.sample(5))