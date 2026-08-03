# Learning Log — AI Chat History

## Prompt 1 — AI Ethics, Explainable AI and Responsible AI

**Prompt ของอาจารย์**

> As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind.

**ChatGPT**
For a Python novice, present the AI part honestly and simply:

- The project uses AI to suggest likely letters in Hangman; it does not “understand” words like a person.
- The model learns patterns from example game states in the dataset, such as the current word pattern, letters guessed, wrong guesses, and word length.
- Three models were compared: Decision Tree, Logistic Regression, and Naive Bayes. The plan says the Decision Tree performed best, so it was selected.

Explainable AI (XAI):

- A Decision Tree is a good beginner-friendly choice because its decision process can be inspected as a series of conditions.
- We can explain its input clearly: `pattern`, `guessed`, `wrong`, `length`, `revealed`, and `candidate_count`.
- The system returns the top 5 suggested letters, not only one answer. This lets the player see alternatives and keeps the player in control.
- Important limitation: a suggestion is a prediction, not a guarantee. The model can be wrong.

Responsible AI:

- AI is used as an assistant in “AI Assist” mode, not as a replacement for the player’s decision.
- The game should show that recommendations come from a trained model and may be inaccurate.
- The training data should contain appropriate words and avoid offensive, sensitive, or copyrighted word lists.
- Test the model across all categories—animals, fruits, and countries—to check that it does not work well only for one category.
- If the AI repeats a letter or returns an unusable prediction, use a fallback alphabet rule. This is a practical safety measure and should be mentioned in the changelog.

A simple presentation line:

> Our AI is a helper, not an authority. It recommends possible letters based on game-state data, explains its inputs through an interpretable Decision Tree model, and keeps the final choice with the player.


## Prompt 2 — Conceive a Python Mini Project

**Prompt ของอาจารย์**

> As a Python beginner, help me to conceive mini projects in Python fundamentals to expand my knowledge and to encounter real-world use cases. Include learning outcomes, traits assessment, and topic.

**ChatGPT**
As a Python beginner, help me explain our project, **Co-op Hangman with AI**, through Python fundamentals and real-world skills.

The project is a cooperative word-guessing game where players work together to guess a hidden word. AI can suggest likely letters, but players make the final decisions.

Explain how we use:

- `list` to store words in each category
- `dictionary` to organize categories such as animals, fruits, and countries
- `set` to save guessed letters without duplicates
- `random.choice()` to select a word randomly
- loops and conditions to control turns, validate guesses, and determine win/loss states
- functions to separate tasks, such as starting a game, processing a guess, checking a win, and generating AI suggestions
- Flask and API routes to connect the game interface with Python logic
- file handling and datasets to prepare data for the AI model
- a Decision Tree model to suggest the top five possible letters

For responsible and explainable AI, explain that the AI is a helper rather than a decision-maker. It uses visible game-state inputs—such as the word pattern, guessed letters, incorrect letters, and word length—to make suggestions. A Decision Tree is relatively easy to inspect and explain. The game should clearly state that suggestions may be wrong, avoid repeated or invalid guesses through validation and fallback logic, and let players choose whether to follow the AI’s recommendation.


## Prompt 3 — Why Kanban, WIP and Changelog from the Beginning?

**Prompt ของอาจารย์**

> Why introduce Kanban, WIP, and Changelog since the beginning of Python programming is a good idea for students to use GenAI to grasp teacher materials and make progress rapidly in learning Python along with `learning_log.ipynb` for prompt and response logging?

**ChatGPT**
Introducing Kanban, WIP limits, changelogs, and a `learning_log.ipynb` from the beginning is a good idea because students learn Python as a practical development process—not just as isolated syntax.

- Kanban makes work visible: students can track tasks from “To Do” to “Doing” to “Done,” such as learning dictionaries, implementing input validation, or testing a function.
- WIP (Work in Progress) limits prevent beginners from starting too many features at once. They finish one small Python concept before moving on, which reduces confusion and encourages steady progress.
- A changelog records what changed, why it changed, and what was learned. This helps students explain their code during presentations and makes improvement visible over time.
- `learning_log.ipynb` can document prompts given to generative AI, AI responses, the student’s own understanding, code experiments, errors, corrections, and references.

When using generative AI, students should treat it as a learning assistant—not as an answer generator. They should verify each suggestion by running it, explaining it in their own words, and recording whether it worked. The log should also disclose which parts were AI-assisted and avoid putting private data, credentials, or copyrighted course materials into external AI tools.

For the Co-op Hangman with AI project, this creates a clear learning trail:

```text
Kanban task
→ learn a Python concept
→ ask AI for an explanation/example
→ test and modify the code
→ record prompt, response, result, and reflection in learning_log.ipynb
→ document the completed change in CHANGELOG.md
```

This builds Python fundamentals alongside responsible AI use, documentation habits, teamwork, and the ability to explain how the project evolved.

## Prompt 4 — Adjust Kanban Backlogs to the Mini-Project Outline

**Prompt ของอาจารย์**

> Adjust Kanban backlogs according to this outline of the mini project.

**ChatGPT**

## Kanban backlog — Co-op Hangman with AI

Use small, testable cards. Keep WIP limited to 2 cards per person.

| Priority | Backlog card | Done when |
|---|---|---|
| P0 | Define game rules and three modes: Classic, AI Assist, VS AI | Rules are written and agreed by the team |
| P0 | Create word categories with a dictionary | `WORDS` has Animals, Fruits, Countries and each has sample words |
| P0 | Randomly choose a category and word | `random.choice()` selects a valid word |
| P0 | Store guessed letters in a set | Duplicate guesses do not change the game state |
| P0 | Build core guess-validation function | Reject blank, multi-character, non-letter, and repeated guesses |
| P0 | Implement win/loss conditions | Correctly detects all letters revealed or maximum wrong guesses reached |
| P0 | Display game state | Shows hidden-word pattern, guessed letters, wrong letters, and remaining attempts |
| P1 | Create Flask app and Hangman Blueprint | App starts and Hangman routes are separated from `app.py` |
| P1 | Add `POST /api/hangman/new` | Returns a new safe game state |
| P1 | Add `POST /api/hangman/guess` | Receives a guess, validates it, and returns updated state |
| P1 | Connect frontend with `fetch()` | Player can start and play through the browser |
| P1 | Implement co-op interaction | Players can share the same game state and take turns or contribute guesses |
| P1 | Prepare AI dataset | Dataset contains game-state features: pattern, guessed, wrong, length, revealed, candidate count |
| P1 | Train and compare models | Decision Tree, Logistic Regression, and Naive Bayes are evaluated and results recorded |
| P1 | Implement AI letter suggestions | `predict()` returns five valid, unguessed suggestions |
| P1 | Add AI safety fallback | If prediction is invalid/repeated, choose from remaining alphabet letters |
| P1 | Add responsible-AI explanation | UI/documentation says AI is a suggestion, may be wrong, and player chooses |
| P2 | Test core Python functions | Tests cover valid/invalid/repeated guesses and win/loss cases |
| P2 | Test all word categories and AI modes | No category or mode breaks during normal play |
| P2 | Update `CHANGELOG.md` | Every completed feature/fix has date, description, and author |
| P2 | Maintain `learning_log.ipynb` | Prompts, AI responses, verification, code changes, and reflections are recorded |
| P2 | Prepare demo and backup | Happy path works; screenshots/GIF are available if the live demo fails |
| P2 | Prepare presentation artifacts | Slides, repository/QR link, changelog, learning log, and demo are ready |

Suggested board columns:

```text
Backlog → Ready → Doing (max 2/person) → Review/Test → Done
```

Example first sprint:

```text
Ready:
- Dictionary word categories
- Random word selection
- Guessed-letter set
- Guess validation

Doing:
- Core game-state function
- Win/loss conditions

Done:
- Project rules and modes
```

This order ensures the team learns Python fundamentals first, then Flask integration, then AI, testing, documentation, and presentation.

## Prompt 5 — Execute the Kanban Backlog

**Prompt ของอาจารย์**

> Execute the Kanban backlog.

**คำตอบที่นำมาใช้กับโครงงาน**

กลุ่มดำเนินงานตาม Kanban โดยยึดหลัก “ทำให้ส่วนพื้นฐานใช้งานได้ก่อน แล้วจึงเพิ่ม AI” ผลลัพธ์ที่ได้มีดังนี้

| งานที่ดำเนินการ | วิธีดำเนินการ | ผลลัพธ์จริง |
|---|---|---|
| Game logic | สร้าง dictionary state ของเกม เก็บคำศัพท์ ตัวอักษรที่เดา จำนวนผิด และสถานะ | Classic Hangman รับ `POST /api/hangman/new` และ `POST /api/hangman/guess` ได้ |
| Data pipeline | จำลอง combinations ของตัวอักษรในคำ สร้าง pattern และค้น candidate words | ได้ `datasets/hangman_dataset.csv` จาก `codes/make_dataset.py` |
| Model pipeline | เทรน/เปรียบเทียบโมเดลด้วย scikit-learn และบันทึกผล | มี `hangman_tree.pkl`, `hangman_lr.pkl`, `hangman_nb.pkl` และ `model_comparison.csv` |
| AI integration | โหลดโมเดลด้วย joblib สร้าง features จาก state เกม และตัดตัวอักษรซ้ำก่อนคืนคำแนะนำ | `codes/predict.py` ถูกเรียกจาก API ของ AI Assist และ VS AI |
| Web application | สร้าง Flask routes และเชื่อมหน้า HTML/CSS/JavaScript เข้ากับ API | เล่นได้ผ่าน `http://localhost:5000` |
| Documentation | แยกคู่มือใช้งาน ประวัติการเปลี่ยนแปลง และ learning log | มี `docs/`, `CHANGELOG.md`, `README.md` และไฟล์นี้ |

### สิ่งที่เรียนรู้จากการลงมือทำ

1. ต้องกำหนด input/output ของแต่ละโมดูลก่อนเขียนโค้ด เช่น `predict()` รับ `pattern`, `guessed`, `wrong` และส่งกลับ list ของตัวอักษร
2. การใช้ `set` ช่วยลดการตรวจอักษรซ้ำและทำให้การหาความแตกต่างระหว่างตัวอักษรที่เดากับคำตอบชัดเจน
3. การแยก UI, API และ AI pipeline ช่วยให้แก้ปัญหาเฉพาะส่วนได้ง่ายกว่าเขียนทุกอย่างไว้ในไฟล์เดียว
4. ข้อเสนอจาก GenAI ต้องนำมาตรวจด้วย code review, การทดลองรัน และการเปรียบเทียบกับเป้าหมายของโครงงานเสมอ
5. งานที่ยังต้องทำต่อคือ automated tests และการย้าย game state จาก memory ไปยัง storage หากต้องการรองรับผู้เล่นหลายคนหรือรีสตาร์ตเซิร์ฟเวอร์

← [กลับหน้าโครงการ](README.md)
