/* ═══════════════════════════════════════════
   hangman_ai.js — AI Assist & VS AI modes
   ═══════════════════════════════════════════ */

const API           = "/api/hangman/ai";
const KEYBOARD_ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];

// parts per board prefix
const PARTS = {
  assist: ["as-head","as-body","as-larm","as-rarm","as-lleg","as-rleg"],
  vsp:    ["vp-head","vp-body","vp-larm","vp-rarm","vp-lleg","vp-rleg"],
  vsa:    ["va-head","va-body","va-larm","va-rarm","va-lleg","va-rleg"],
};

let currentMode = null;

// ── Auto-start from URL param ─────────────────────────────────────────────────

window.addEventListener("DOMContentLoaded", () => {
  const mode = new URLSearchParams(location.search).get("mode");
  if (mode === "assist" || mode === "vs") initGame(mode);
});

// ── Audio ─────────────────────────────────────────────────────────────────────

const AudioCtx = window.AudioContext || window.webkitAudioContext;
let audioCtx;
function getAudio() { if (!audioCtx) audioCtx = new AudioCtx(); return audioCtx; }
function playTone(freq, type, dur, vol = 0.3) {
  try {
    const ctx = getAudio(), osc = ctx.createOscillator(), gain = ctx.createGain();
    osc.connect(gain); gain.connect(ctx.destination);
    osc.type = type; osc.frequency.setValueAtTime(freq, ctx.currentTime);
    gain.gain.setValueAtTime(vol, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
    osc.start(ctx.currentTime); osc.stop(ctx.currentTime + dur);
  } catch(e) {}
}
function sfxCorrect() { playTone(880,"square",0.12); setTimeout(()=>playTone(1100,"square",0.12),100); }
function sfxWrong()   { playTone(150,"sawtooth",0.25); }
function sfxWin()     { [523,659,784,1047].forEach((f,i)=>setTimeout(()=>playTone(f,"square",0.18),i*120)); }
function sfxLose()    { [300,250,200,150].forEach((f,i)=>setTimeout(()=>playTone(f,"sawtooth",0.22),i*130)); }

// ── API ───────────────────────────────────────────────────────────────────────

async function apiPost(path, body = {}) {
  const res = await fetch(API + path, {
    method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify(body),
  });
  return res.json();
}

// ── Shared helpers ────────────────────────────────────────────────────────────

function buildKeyboard(containerId, guessed = []) {
  const kb = document.getElementById(containerId);
  kb.innerHTML = "";
  KEYBOARD_ROWS.forEach(row => {
    const rowDiv = document.createElement("div");
    rowDiv.className = "key-row";
    [...row].forEach(ch => {
      const btn = document.createElement("button");
      btn.className = "key"; btn.id = `${containerId}-key-${ch}`;
      btn.textContent = ch.toUpperCase();
      btn.addEventListener("click", () => handleGuess(ch));
      rowDiv.appendChild(btn);
    });
    kb.appendChild(rowDiv);
  });
  guessed.forEach(ch => {
    const btn = document.getElementById(`${containerId}-key-${ch}`);
    if (btn) btn.disabled = true;
  });
}

function renderWord(containerId, maskedWord) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";
  maskedWord.forEach((ch, idx) => {
    const slot = document.createElement("div"); slot.className = "letter-slot";
    const char = document.createElement("div"); char.className = "letter-char";
    char.id = `${containerId}-slot-${idx}`; char.textContent = ch.toUpperCase();
    if (ch !== "_") char.classList.add("revealed");
    const line = document.createElement("div"); line.className = "letter-line";
    slot.appendChild(char); slot.appendChild(line); container.appendChild(slot);
  });
}

function updateHearts(containerId, wrongCount, maxWrong = 6) {
  const el = document.getElementById(containerId); el.innerHTML = "";
  for (let i = 0; i < maxWrong; i++) {
    const s = document.createElement("span"); s.textContent = "♥";
    if (i >= maxWrong - wrongCount) s.classList.add("lost");
    el.appendChild(s);
  }
}

function updateHangman(parts, wrongCount) {
  parts.forEach((id, i) => {
    const el = document.getElementById(id); if (!el) return;
    i < wrongCount ? el.classList.add("show") : el.classList.remove("show");
  });
}

function updateWrong(containerId, wrongArr) {
  document.getElementById(containerId).textContent =
    wrongArr.length ? wrongArr.map(c => c.toUpperCase()).join("  ") : "—";
}

function disableKey(kbId, ch, cls) {
  const btn = document.getElementById(`${kbId}-key-${ch}`);
  if (btn) { btn.disabled = true; if (cls) btn.classList.add(cls); }
}

// ── Init game ─────────────────────────────────────────────────────────────────

async function initGame(mode) {
  currentMode = mode;
  document.getElementById("mode-select").classList.add("hidden");
  document.getElementById("game-screen").classList.remove("hidden");
  document.getElementById("message-overlay").classList.remove("show");

  const state = await apiPost("/new", { mode });

  if (mode === "assist") {
    document.getElementById("layout-assist").classList.remove("hidden");
    document.getElementById("layout-vs").classList.add("hidden");
    renderAssist(state);
  } else {
    document.getElementById("layout-vs").classList.remove("hidden");
    document.getElementById("layout-assist").classList.add("hidden");
    renderVS(state);
  }
}

// ── ASSIST ────────────────────────────────────────────────────────────────────

function renderAssist(state) {
  const p = state.player;
  document.getElementById("assist-category").textContent =
    `CATEGORY: ${p.category} / ${p.category_th}`;
  renderWord("assist-word", p.masked_word);
  updateHearts("assist-hearts", p.wrong_count);
  updateHangman(PARTS.assist, p.wrong_count);
  updateWrong("assist-wrong", p.wrong);
  updateHints(state.hints || []);
  buildKeyboard("assist-keyboard", p.guessed);
}

function updateHints(hints) {
  document.getElementById("assist-hints").textContent =
    hints.length ? hints.map(c => c.toUpperCase()).join("  |  ") : "—";
}

// ── VS ────────────────────────────────────────────────────────────────────────

function renderVS(state) {
  const p = state.player, a = state.ai;

  document.getElementById("vs-p-category").textContent =
    `${p.category} / ${p.category_th}`;
  document.getElementById("vs-a-category").textContent =
    `${a.category} / ${a.category_th}`;

  renderWord("vs-p-word", p.masked_word);
  renderWord("vs-a-word", a.masked_word);
  updateHearts("vs-p-hearts", p.wrong_count);
  updateHearts("vs-a-hearts", a.wrong_count);
  updateHangman(PARTS.vsp, p.wrong_count);
  updateHangman(PARTS.vsa, a.wrong_count);
  updateWrong("vs-p-wrong", p.wrong);
  updateWrong("vs-a-wrong", a.wrong);
  updateTurnUI(state.turn);
  buildKeyboard("vs-p-keyboard", p.guessed);
  updateAIGuessedDisplay(a.guessed);
}

function updateAIGuessedDisplay(guessed) {
  document.getElementById("vs-a-guessed-display").textContent =
    guessed.length ? guessed.map(c => c.toUpperCase()).join("  ") : "—";
}

function updateTurnUI(turn) {
  document.getElementById("vs-turn-label").textContent =
    turn === "player" ? "YOUR TURN — เดาคำของ AI" : "AI TURN...";
  document.getElementById("vs-player-side").classList.toggle("inactive", turn !== "player");
  document.getElementById("vs-ai-side").classList.toggle("inactive", turn === "player");
}

// ── Handle guess ──────────────────────────────────────────────────────────────

let guessing = false;

async function handleGuess(ch) {
  if (guessing) return;
  const kbId = currentMode === "assist" ? "assist-keyboard" : "vs-p-keyboard";
  const btn  = document.getElementById(`${kbId}-key-${ch}`);
  if (!btn || btn.disabled) return;
  guessing = true;
  btn.disabled = true;

  const state = await apiPost("/guess", { letter: ch });
  if (state.error) return;

  if (currentMode === "assist") {
    handleAssistResult(state, ch, btn);
    guessing = false;
  } else {
    handleVSResult(state, ch, btn);
  }
}

function handleAssistResult(state, ch, btn) {
  const p = state.player;
  if (state.result === "correct") {
    sfxCorrect(); btn.classList.add("correct");
    p.masked_word.forEach((letter, i) => {
      if (letter === ch) {
        const slot = document.getElementById(`assist-word-slot-${i}`);
        if (slot) { slot.textContent = ch.toUpperCase(); slot.classList.add("revealed"); }
      }
    });
  } else if (state.result === "wrong") {
    sfxWrong(); btn.classList.add("wrong");
  }
  updateHearts("assist-hearts", p.wrong_count);
  updateHangman(PARTS.assist, p.wrong_count);
  updateWrong("assist-wrong", p.wrong);
  updateHints(state.hints || []);

  if (state.status === "win")  setTimeout(() => endGame(state, "win"),  400);
  if (state.status === "lose") setTimeout(() => endGame(state, "lose"), 400);
}

function handleVSResult(state, ch, btn) {
  const p = state.player;

  const endMap = {
    player_win:  "win",
    player_lose: "lose",
    ai_win:      "ai_win",
    ai_lose:     "ai_lose",
  };

  // player result
  if (state.result === "correct") {
    sfxCorrect(); btn.classList.add("correct");
    renderWord("vs-p-word", p.masked_word);
  } else if (state.result === "wrong") {
    sfxWrong(); btn.classList.add("wrong");
  }
  updateHearts("vs-p-hearts", p.wrong_count);
  updateHangman(PARTS.vsp, p.wrong_count);
  updateWrong("vs-p-wrong", p.wrong);

  // no AI turn (player win/lose)
  if (!state.ai_letter) {
    guessing = false;
    if (endMap[state.status]) setTimeout(() => endGame(state, endMap[state.status]), 400);
    return;
  }

  // AI turn
  updateTurnUI("ai");
  const aiLetter = state.ai_letter;
  const a = state.ai;
  setTimeout(() => {
    if (state.ai_result === "correct") {
      sfxCorrect();
      renderWord("vs-a-word", a.masked_word);
    } else {
      sfxWrong();
    }
    updateHearts("vs-a-hearts", a.wrong_count);
    updateHangman(PARTS.vsa, a.wrong_count);
    updateWrong("vs-a-wrong", a.wrong);
    updateAIGuessedDisplay(a.guessed);

    if (endMap[state.status]) {
      setTimeout(() => endGame(state, endMap[state.status]), 400);
    } else {
      updateTurnUI("player");
    }
    guessing = false;
  }, 800);
}

// ── End game ──────────────────────────────────────────────────────────────────

function endGame(state, result) {
  const titleEl = document.getElementById("message-title");
  const wordEl  = document.getElementById("message-word");

  const msgs = {
    win:      ["YOU WIN! 🎉", "win"],
    lose:     ["GAME OVER 💀", "lose"],
    ai_win:   ["AI WINS 🤖", "lose"],
    ai_lose:  ["YOU WIN! 🎉 AI แพ้", "win"],
  };
  const [title, cls] = msgs[result] || ["GAME OVER", "lose"];
  result === "win" || result === "ai_lose" ? sfxWin() : sfxLose();

  titleEl.textContent = title;
  titleEl.className   = cls;

  if (currentMode === "assist") {
    const answer = state.player.answer || "";
    wordEl.innerHTML = `The word is: <b>${answer.toUpperCase()}</b>`;
    if (result === "lose") renderWord("assist-word", answer.split(""));
  } else {
    const pa = state.player.answer || "";
    wordEl.innerHTML = `The word is: <b>${pa.toUpperCase()}</b>`;
    if (result === "lose" || result === "ai_win") renderWord("vs-p-word", pa.split(""));
    if (result === "ai_lose") renderWord("vs-a-word", (state.ai?.answer || "").split(""));
  }

  document.getElementById("message-overlay").classList.add("show");
}

// ── Keyboard event ────────────────────────────────────────────────────────────

document.addEventListener("keydown", e => {
  const ch = e.key.toLowerCase();
  if (/^[a-z]$/.test(ch) && currentMode) handleGuess(ch);
});

// ── Buttons ───────────────────────────────────────────────────────────────────

document.getElementById("play-again-btn").addEventListener("click", () => {
  document.getElementById("message-overlay").classList.remove("show");
  // reset hangman parts
  Object.values(PARTS).flat().forEach(id => document.getElementById(id)?.classList.remove("show"));
  initGame(currentMode);
});

document.getElementById("change-mode-btn").addEventListener("click", () => {
  location.href = "/";
});
