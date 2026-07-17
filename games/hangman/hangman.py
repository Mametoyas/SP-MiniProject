import random
from flask import Blueprint, jsonify, request, send_from_directory

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
