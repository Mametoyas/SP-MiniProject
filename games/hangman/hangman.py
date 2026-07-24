import random
import sys
from pathlib import Path
from flask import Blueprint, jsonify, request, send_from_directory

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "codes"))
from predict import predict

hangman_bp = Blueprint("hangman", __name__)

WORDS = {
    "ANIMALS":   ["elephant","giraffe","penguin","dolphin","cheetah",
                  "kangaroo","crocodile","butterfly","octopus","flamingo"],
    "FRUITS":    ["strawberry","pineapple","watermelon","blueberry","mango",
                  "avocado","raspberry","pomegranate","apricot","coconut"],
    "COUNTRIES": ["thailand","australia","brazil","canada","germany",
                  "japan","mexico","norway","portugal","sweden"],
}
CATEGORY_TH = {"ANIMALS": "สัตว์", "FRUITS": "ผลไม้", "COUNTRIES": "ประเทศ"}
MAX_WRONG   = 6
game: dict  = {}
ai_game: dict = {}

def _new() -> dict:
    cat  = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[cat])
    return {"word": word, "category": cat, "category_th": CATEGORY_TH[cat],
            "guessed": [], "wrong_count": 0, "status": "playing"}

def _public(g: dict) -> dict:
    guessed = set(g["guessed"])
    return {
        "category":    g["category"],
        "category_th": g["category_th"],
        "masked_word": [ch if ch in guessed else "_" for ch in g["word"]],
        "word_length": len(g["word"]),
        "guessed":     g["guessed"],
        "wrong":       [ch for ch in g["guessed"] if ch not in g["word"]],
        "wrong_count": g["wrong_count"],
        "max_wrong":   MAX_WRONG,
        "status":      g["status"],
        "answer":      g["word"] if g["status"] != "playing" else None,
    }

@hangman_bp.route("/hangman")
def page():
    return send_from_directory("games/hangman", "hangman.html")

@hangman_bp.route("/hangman-ai")
def page_ai():
    return send_from_directory("games/hangman", "hangman_ai.html")

# ── AI Game helpers ───────────────────────────────────────────────────────────

def _ai_public(g: dict) -> dict:
    mode = g["mode"]
    out  = {"mode": mode, "status": g["status"]}

    # player board (always present)
    p_guessed = set(g["p_guessed"])
    p_word    = g["p_word"]
    out["player"] = {
        "masked_word": [c if c in p_guessed else "_" for c in p_word],
        "guessed":     g["p_guessed"],
        "wrong":       [c for c in g["p_guessed"] if c not in p_word],
        "wrong_count": g["p_wrong"],
        "category":    g["p_category"],
        "category_th": g["p_category_th"],
        "word_length": len(p_word),
    }
    if g["status"] != "playing":
        out["player"]["answer"] = p_word

    # hints for player
    if mode == "assist":
        pattern  = "".join(c if c in p_guessed else "_" for c in p_word)
        wrong_s  = p_guessed - set(p_word)
        out["hints"] = predict(pattern, p_guessed & set(p_word), wrong_s)[:2]

    # AI board (VS AI only)
    if mode == "vs":
        a_guessed = set(g["a_guessed"])
        a_word    = g["a_word"]
        out["ai"] = {
            "masked_word": [c if c in a_guessed else "_" for c in a_word],
            "guessed":     g["a_guessed"],
            "wrong":       [c for c in g["a_guessed"] if c not in a_word],
            "wrong_count": g["a_wrong"],
            "category":    g["a_category"],
            "category_th": g["a_category_th"],
            "word_length": len(a_word),
        }
        if g["status"] != "playing":
            out["ai"]["answer"] = a_word
        out["turn"] = g["turn"]

    return out

def _check_win(word, guessed_list):
    return all(c in guessed_list for c in word)

# ── AI endpoints ──────────────────────────────────────────────────────────────

@hangman_bp.route("/api/hangman/ai/new", methods=["POST"])
def api_ai_new():
    data = request.get_json(silent=True) or {}
    mode = data.get("mode", "assist")  # "assist" | "vs"

    p_cat  = random.choice(list(WORDS.keys()))
    p_word = random.choice(WORDS[p_cat])

    g = {
        "mode":        mode,
        "status":      "playing",
        "p_word":      p_word,
        "p_category":  p_cat,
        "p_category_th": CATEGORY_TH[p_cat],
        "p_guessed":   [],
        "p_wrong":     0,
    }

    if mode == "vs":
        a_cat  = p_cat
        a_word = p_word
        g.update({
            "a_word":      a_word,
            "a_category":  a_cat,
            "a_category_th": CATEGORY_TH[a_cat],
            "a_guessed":   [],
            "a_wrong":     0,
            "turn":        "player",
        })

    ai_game.clear()
    ai_game.update(g)
    return jsonify(_ai_public(ai_game))

@hangman_bp.route("/api/hangman/ai/guess", methods=["POST"])
def api_ai_guess():
    if not ai_game:
        return jsonify({"error": "no game"}), 400
    if ai_game["status"] != "playing":
        return jsonify({**_ai_public(ai_game), "result": "game_over"})

    data   = request.get_json(silent=True) or {}
    letter = str(data.get("letter", "")).strip().lower()
    if len(letter) != 1 or not letter.isalpha():
        return jsonify({"error": "invalid"}), 400

    mode = ai_game["mode"]

    # ── Assist: player guesses p_word ────────────────────────────────────────
    if mode == "assist":
        if letter in ai_game["p_guessed"]:
            return jsonify({**_ai_public(ai_game), "result": "already_guessed"})
        ai_game["p_guessed"].append(letter)
        if letter in ai_game["p_word"]:
            result = "correct"
            if _check_win(ai_game["p_word"], ai_game["p_guessed"]):
                ai_game["status"] = "win"
        else:
            result = "wrong"
            ai_game["p_wrong"] += 1
            if ai_game["p_wrong"] >= MAX_WRONG:
                ai_game["status"] = "lose"
        return jsonify({**_ai_public(ai_game), "result": result})

    # ── VS: player guesses p_word, then AI guesses a_word ────────────────────
    if mode == "vs":
        if ai_game["turn"] != "player":
            return jsonify({"error": "not your turn"}), 400
        if letter in ai_game["p_guessed"]:
            return jsonify({**_ai_public(ai_game), "result": "already_guessed"})

        ai_game["p_guessed"].append(letter)
        if letter in ai_game["p_word"]:
            p_result = "correct"
            if _check_win(ai_game["p_word"], ai_game["p_guessed"]):
                ai_game["status"] = "player_win"
                return jsonify({**_ai_public(ai_game), "result": p_result, "ai_result": None})
        else:
            p_result = "wrong"
            ai_game["p_wrong"] += 1
            if ai_game["p_wrong"] >= MAX_WRONG:
                ai_game["status"] = "player_lose"
                return jsonify({**_ai_public(ai_game), "result": p_result, "ai_result": None})

        # AI's turn
        ai_game["turn"] = "ai"
        a_word    = ai_game["a_word"]
        a_guessed = set(ai_game["a_guessed"])
        pattern   = "".join(c if c in a_guessed else "_" for c in a_word)
        wrong_s   = a_guessed - set(a_word)
        suggestions = predict(pattern, a_guessed & set(a_word), wrong_s)
        ai_letter   = suggestions[0]

        ai_game["a_guessed"].append(ai_letter)
        if ai_letter in a_word:
            ai_result = "correct"
            if _check_win(a_word, ai_game["a_guessed"]):
                ai_game["status"] = "ai_win"
                ai_game["turn"]   = "player"
                return jsonify({**_ai_public(ai_game), "result": p_result, "ai_result": ai_result, "ai_letter": ai_letter})
        else:
            ai_result = "wrong"
            ai_game["a_wrong"] += 1
            if ai_game["a_wrong"] >= MAX_WRONG:
                ai_game["status"] = "ai_lose"
                ai_game["turn"]   = "player"
                return jsonify({**_ai_public(ai_game), "result": p_result, "ai_result": ai_result, "ai_letter": ai_letter})

        ai_game["turn"] = "player"
        return jsonify({**_ai_public(ai_game), "result": p_result, "ai_result": ai_result, "ai_letter": ai_letter})

@hangman_bp.route("/api/hangman/new", methods=["POST"])
def api_new():
    game.update(_new())
    return jsonify(_public(game))

@hangman_bp.route("/api/hangman/guess", methods=["POST"])
def api_guess():
    if not game:
        game.update(_new())
    data   = request.get_json(silent=True) or {}
    letter = str(data.get("letter", "")).strip().lower()
    if len(letter) != 1 or not letter.isalpha():
        return jsonify({"error": "invalid"}), 400
    if game["status"] != "playing":
        return jsonify({**_public(game), "result": "game_over"})
    if letter in game["guessed"]:
        return jsonify({**_public(game), "result": "already_guessed"})
    game["guessed"].append(letter)
    if letter in game["word"]:
        result = "correct"
        if all(ch in game["guessed"] for ch in game["word"]):
            game["status"] = "win"
    else:
        result = "wrong"
        game["wrong_count"] += 1
        if game["wrong_count"] >= MAX_WRONG:
            game["status"] = "lose"
    return jsonify({**_public(game), "result": result})
