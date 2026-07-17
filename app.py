# ═══════════════════════════════════════════
#  app.py — Game Hub Flask Backend
# ═══════════════════════════════════════════

from flask import Flask, render_template, send_from_directory
from games.hangman.hangman import hangman_bp

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")
app.register_blueprint(hangman_bp)

# ── Static files per game ─────────────────────────────────────────────────────

@app.route("/games/<game>/<path:filename>")
def game_static(game, filename):
    return send_from_directory(f"games/{game}", filename)

# ── Menu ──────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)
