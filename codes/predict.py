import string
import joblib
import pandas as pd

# ============================================
# Load Model & Words
# ============================================

model = joblib.load("../models/hangman_best.pkl")

with open("../datasets/words.txt", encoding="utf8") as f:
    words = [w.strip().lower() for w in f if w.strip().isalpha()]

words_by_length = {}
for w in words:
    words_by_length.setdefault(len(w), []).append(w)

# ============================================
# Candidate Count Helper
# ============================================

def count_candidates(pattern: str, guessed: set, wrong: set) -> int:
    same = words_by_length.get(len(pattern), [])
    count = 0
    for w in same:
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
            count += 1
    return count

# ============================================
# Predict
# ============================================

def predict(pattern: str, guessed: set, wrong: set) -> list[str]:
    """
    Returns top-5 suggested letters for the current Hangman state.

    Args:
        pattern : current pattern e.g. "e_e_h__t"
        guessed : set of correctly guessed letters e.g. {'e', 'h', 't'}
        wrong   : set of wrong guessed letters e.g. {'a', 'i'}

    Returns:
        list of up to 5 suggested letters, excluding already guessed/wrong
    """
    candidate_count = count_candidates(pattern, guessed, wrong)

    X = pd.DataFrame([{
        "pattern"        : pattern,
        "guessed"        : "".join(sorted(guessed)),
        "wrong"          : "".join(sorted(wrong)),
        "length"         : len(pattern),
        "revealed"       : sum(1 for c in pattern if c != "_"),
        "candidate_count": candidate_count,
    }])

    pred = model.predict(X)[0]   # ['e', 'l', 'p', 'h', 'a']

    used = guessed | wrong
    suggestions = [c for c in pred if c and c not in used]

    # fallback: fill with frequency-based letters if model gives < 5
    if len(suggestions) < 5:
        alphabet = string.ascii_lowercase
        for c in alphabet:
            if c not in used and c not in suggestions:
                suggestions.append(c)
            if len(suggestions) == 5:
                break

    return suggestions[:5]


# ============================================
# Demo
# ============================================

if __name__ == "__main__":
    examples = [
        ("_______",  set(),          set()),
        ("e_e_h__t", {"e","h","t"},  {"a","i"}),
        ("_iger",    {"i",'g',"r","e"},          {"n","a"}),
        ("p_th__",   {"p","t","h"},  {"a","i"}),
    ]

    for pattern, guessed, wrong in examples:
        result = predict(pattern, guessed, wrong)
        print(f"pattern : {pattern}")
        print(f"guessed : {sorted(guessed)}")
        print(f"wrong   : {sorted(wrong)}")
        print(f"suggest : {result}")
        print()
