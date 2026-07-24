/* ═══════════════════════════════════════════
   hangman.js — UI layer (talks to Flask API)
   ═══════════════════════════════════════════ */

// ── Constants ────────────────────────────────────────────────────────────────

const PARTS         = ["p-head","p-body","p-larm","p-rarm","p-lleg","p-rleg"];
const KEYBOARD_ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
const API           = "/api/hangman";

// ── Audio (Web Audio API — 8-bit tones) ──────────────────────────────────────

const AudioCtx = window.AudioContext || window.webkitAudioContext;
let audioCtx;

function getAudio() {
  if (!audioCtx) audioCtx = new AudioCtx();
  return audioCtx;
}

function playTone(freq, type, duration, vol = 0.3) {
  try {
    const ctx  = getAudio();
    const osc  = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.type = type;
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    gain.gain.setValueAtTime(vol, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
    osc.start(ctx.currentTime);
    osc.stop(ctx.currentTime + duration);
  } catch (e) { /* silently ignore */ }
}

function sfxCorrect() {
  playTone(880,  "square",   0.12);
  setTimeout(() => playTone(1100, "square", 0.12), 100);
}
function sfxWrong()   { playTone(150, "sawtooth", 0.25); }
function sfxWin()     { [523,659,784,1047].forEach((f,i) => setTimeout(() => playTone(f,"square",0.18),   i*120)); }
function sfxLose()    { [300,250,200,150] .forEach((f,i) => setTimeout(() => playTone(f,"sawtooth",0.22), i*130)); }

// ── API helpers ───────────────────────────────────────────────────────────────

async function apiPost(path, body = {}) {
  const res = await fetch(API + path, {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify(body),
  });
  return res.json();
}

async function apiGet(path) {
  const res = await fetch(API + path);
  return res.json();
}

// ── DOM builders ─────────────────────────────────────────────────────────────

function buildKeyboard(guessed = []) {
  const kb = document.getElementById("keyboard");
  kb.innerHTML = "";

  KEYBOARD_ROWS.forEach(row => {
    const rowDiv = document.createElement("div");
    rowDiv.className = "key-row";

    [...row].forEach(ch => {
      const btn = document.createElement("button");
      btn.className   = "key";
      btn.id          = `key-${ch}`;
      btn.textContent = ch.toUpperCase();
      btn.addEventListener("click", () => handleGuess(ch));
      rowDiv.appendChild(btn);
    });

    kb.appendChild(rowDiv);
  });

  // Restore disabled state for already-guessed letters
  guessed.forEach(ch => {
    const btn = document.getElementById(`key-${ch}`);
    if (btn) btn.disabled = true;
  });
}

function renderWord(maskedWord, guessed) {
  const guessedSet = new Set(guessed);
  const container  = document.getElementById("word-display");
  container.innerHTML = "";

  maskedWord.forEach((ch, idx) => {
    const slot = document.createElement("div");
    slot.className = "letter-slot";

    const char = document.createElement("div");
    char.className   = "letter-char";
    char.id          = `slot-${idx}`;
    char.textContent = ch.toUpperCase();
    if (ch !== "_") char.classList.add("revealed");

    const line = document.createElement("div");
    line.className = "letter-line";

    slot.appendChild(char);
    slot.appendChild(line);
    container.appendChild(slot);
  });
}

// ── Updaters ─────────────────────────────────────────────────────────────────

function updateHearts(wrongCount, maxWrong) {
  const el = document.getElementById("hearts");
  el.innerHTML = "";
  for (let i = 0; i < maxWrong; i++) {
    const s = document.createElement("span");
    s.textContent = "♥";
    if (i >= maxWrong - wrongCount) s.classList.add("lost");
    el.appendChild(s);
  }
}

function updateWrongDisplay(wrong) {
  document.getElementById("wrong-display").textContent =
    wrong.length ? wrong.map(c => c.toUpperCase()).join("  ") : "—";
}

function updateHangman(wrongCount) {
  PARTS.forEach((id, i) => {
    const el = document.getElementById(id);
    if (!el) return;
    i < wrongCount ? el.classList.add("show") : el.classList.remove("show");
  });
}

// ── Render full state from API response ──────────────────────────────────────

function renderState(state) {
  document.getElementById("category-label").textContent =
    `CATEGORY: ${state.category} / ${state.category_th}`;

  renderWord(state.masked_word, state.guessed);
  updateHearts(state.wrong_count, state.max_wrong);
  updateHangman(state.wrong_count);
  updateWrongDisplay(state.wrong);
}

// ── Handle a guess ────────────────────────────────────────────────────────────

async function handleGuess(ch) {
  const btn = document.getElementById(`key-${ch}`);
  if (!btn || btn.disabled) return;
  btn.disabled = true;

  const state = await apiPost("/guess", { letter: ch });

  // Animate the pressed key
  if (state.result === "correct") {
    sfxCorrect();
    btn?.classList.add("correct");
    // Stagger-reveal newly uncovered slots
    state.masked_word.forEach((letter, i) => {
      if (letter === ch) {
        setTimeout(() => {
          const slot = document.getElementById(`slot-${i}`);
          if (slot) {
            slot.textContent = ch.toUpperCase();
            slot.classList.add("revealed");
          }
        }, 60);
      }
    });
  } else if (state.result === "wrong") {
    sfxWrong();
    btn?.classList.add("wrong");
  }

  updateHearts(state.wrong_count, state.max_wrong);
  updateHangman(state.wrong_count);
  updateWrongDisplay(state.wrong);

  if (state.status === "win")  setTimeout(() => endGame(state, true),  400);
  if (state.status === "lose") setTimeout(() => endGame(state, false), 400);
}

// ── End game ──────────────────────────────────────────────────────────────────

function endGame(state, win) {
  win ? sfxWin() : sfxLose();

  if (!win) {
    // Reveal all letters
    state.masked_word.forEach((_, i) =>
      document.getElementById(`slot-${i}`)?.classList.add("revealed")
    );
    // Show the answer
    renderWord(state.answer.split(""), state.answer.split(""));
  }

  const overlay = document.getElementById("message-overlay");
  const titleEl = document.getElementById("message-title");
  const wordEl  = document.getElementById("message-word");

  titleEl.className   = win ? "win" : "lose";
  titleEl.textContent = win ? "YOU WIN! 🎉" : "GAME OVER 💀";
  wordEl.innerHTML    = `คำตอบคือ / The word was:<br>"${state.answer.toUpperCase()}"`;

  overlay.classList.add("show");
}

// ── Start / Restart ───────────────────────────────────────────────────────────

async function startGame() {
  document.getElementById("message-overlay").classList.remove("show");
  PARTS.forEach(id => document.getElementById(id)?.classList.remove("show"));

  const state = await apiPost("/new");
  renderState(state);
  buildKeyboard(state.guessed);
}

// ── Event listeners ───────────────────────────────────────────────────────────

document.addEventListener("keydown", e => {
  const ch = e.key.toLowerCase();
  if (/^[a-z]$/.test(ch)) handleGuess(ch);
});

document.getElementById("play-again-btn").addEventListener("click", startGame);
document.getElementById("change-mode-btn").addEventListener("click", () => { location.href = "/"; });

// ── Init ──────────────────────────────────────────────────────────────────────

startGame();
