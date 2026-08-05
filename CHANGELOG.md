# Changelog

เอกสารนี้บันทึกการเปลี่ยนแปลงของโครงงาน Mini Game Hub ตามลำดับเวลา โดยระบุว่าคุยกับ AI เรื่องอะไร เพิ่มหรือแก้ไขโค้ดส่วนใด และได้ผลลัพธ์อะไร

---

## 19 ก.ค. 2568

| ลำดับ | การเปลี่ยนแปลง | ไฟล์/ส่วนที่เกี่ยวข้อง | ผลลัพธ์ |
|---|---|---|---|
| 1 | ถาม AI เรื่องกติกา Hangman — สอบถามว่าเกมทำงานอย่างไร มีองค์ประกอบอะไรบ้าง และเหมาะกับ mini project แค่ไหน | แนวคิดเกม | เข้าใจกติกา: สุ่มคำ ซ่อนตัวอักษร รับการเดา ตรวจถูก/ผิด นับชีวิต 6 ครั้ง ตัดสินชนะ/แพ้ |
| 2 | วาง pseudocode กับ AI — ออกแบบ logic ทีละขั้นตอน ตั้งแต่สุ่มคำจนถึงเงื่อนไขจบเกม | pseudocode (ยังไม่มีโค้ด) | ได้โครงสร้างที่ชัดเจนก่อนเริ่มเขียนโค้ดจริง |
| 3 | สร้าง `WORDS` dictionary — คุยกับ AI เรื่องการใช้ `dict` จัดหมวดคำศัพท์ และ `list` เก็บคำในแต่ละหมวด | `games/hangman/hangman.py` — ตัวแปร `WORDS` | ได้ `WORDS = {"ANIMALS": [...], "FRUITS": [...], "COUNTRIES": [...]}` พร้อมใช้ |
| 4 | เพิ่มการสุ่มคำด้วย `random.choice()` — ถาม AI วิธีสุ่มหมวดและสุ่มคำจาก `list` | `hangman.py` — ฟังก์ชัน `_new()` | `cat = random.choice(list(WORDS.keys()))` และ `word = random.choice(WORDS[cat])` ทำงานได้ |
| 5 | เพิ่ม `set` เก็บตัวอักษรที่เดา — ถาม AI ว่าทำไม `set` ดีกว่า `list` สำหรับเก็บตัวอักษรที่เดาแล้ว | `hangman.py` — ฟังก์ชัน `_public()` | ใช้ `guessed = set(g["guessed"])` ป้องกันการเดาซ้ำและเปรียบเทียบได้เร็วขึ้น |
| 6 | เพิ่มเงื่อนไขตรวจชนะด้วย `all()` — ถาม AI วิธีตรวจว่าเปิดเผยตัวอักษรครบทุกตัวหรือยัง | `hangman.py` — ฟังก์ชัน `api_guess()` | `all(ch in game["guessed"] for ch in game["word"])` ตรวจชนะได้ถูกต้อง |
| 7 | เพิ่ม input validation — ถาม AI วิธีตรวจว่าผู้เล่นป้อนตัวอักษร 1 ตัวและเป็นตัวอักษรจริง | `hangman.py` — ฟังก์ชัน `api_guess()` | `len(letter) != 1 or not letter.isalpha()` คืน error 400 เมื่อ input ไม่ถูกต้อง |
| 8 | กำหนด `MAX_WRONG = 6` และตรวจเงื่อนไขแพ้ — ถาม AI เรื่องการนับชีวิตและตัดสินแพ้ | `hangman.py` — ตัวแปร `MAX_WRONG` และ `api_guess()` | เมื่อ `wrong_count >= MAX_WRONG` สถานะเปลี่ยนเป็น `"lose"` |

---

## 19 ก.ค. 2568 (ช่วงบ่าย)

| ลำดับ | การเปลี่ยนแปลง | ไฟล์/ส่วนที่เกี่ยวข้อง | ผลลัพธ์ |
|---|---|---|---|
| 9 | สร้าง Flask app และ Blueprint — ถาม AI วิธีแยก route ของเกมออกจาก `app.py` หลัก | `app.py`, `games/hangman/__init__.py` | `hangman_bp = Blueprint("hangman", __name__)` ลงทะเบียนใน `app.py` สำเร็จ |
| 10 | เพิ่ม `POST /api/hangman/new` — ถาม AI วิธีสร้าง API endpoint สำหรับเริ่มเกมใหม่ | `hangman.py` — ฟังก์ชัน `api_new()` | เรียก `_new()` และคืน game state ที่ปลอดภัยด้วย `_public()` |
| 11 | เพิ่ม `POST /api/hangman/guess` — ถาม AI วิธีรับ JSON body และส่งผลลัพธ์กลับ | `hangman.py` — ฟังก์ชัน `api_guess()` | รับ `{"letter": "a"}` ตรวจสอบ ประมวลผล และคืน state พร้อม `result` |
| 12 | สร้างหน้า Menu และ Classic Mode UI — ถาม AI เรื่องโครงสร้าง HTML/CSS/JS สำหรับหน้าเกม | `templates/index.html`, `games/hangman/hangman.html`, `hangman.css`, `hangman.js` | หน้าเมนูและหน้าเกม Classic เชื่อมกับ API ด้วย `fetch()` ได้ |
| 13 | เพิ่ม route สำหรับ static files ของแต่ละเกม — ถาม AI วิธีให้ Flask serve ไฟล์จากโฟลเดอร์เกม | `app.py` — ฟังก์ชัน `game_static()` | `send_from_directory(f"games/{game}", filename)` ให้ browser โหลด CSS/JS ของเกมได้ |

---

## 21 ก.ค. 2568

| ลำดับ | การเปลี่ยนแปลง | ไฟล์/ส่วนที่เกี่ยวข้อง | ผลลัพธ์ |
|---|---|---|---|
| 14 | ย้าย Hangman ไปโครงสร้างโฟลเดอร์เฉพาะเกม — ถาม AI วิธีจัดโครงสร้างโปรเจกต์ให้รองรับหลายเกม | `games/hangman/` ทั้งโฟลเดอร์ | แยก logic, UI และ static ของ Hangman ออกจากส่วนอื่น ไม่ปะปนกัน |
| 15 | ปรับข้อมูลสมาชิกและ README — อัปเดตชื่อ รหัสนักศึกษา และโครงสร้างโปรเจกต์ | `README.md` | README สะท้อนโครงสร้างโฟลเดอร์ปัจจุบันและข้อมูลทีมที่ถูกต้อง |

---

## 23 ก.ค. 2568

| ลำดับ | การเปลี่ยนแปลง | ไฟล์/ส่วนที่เกี่ยวข้อง | ผลลัพธ์ |
|---|---|---|---|
| 16 | สร้างคลังคำศัพท์ `words.txt` — ถาม AI เรื่องการเลือกคำศัพท์ที่เหมาะสมสำหรับเกม Hangman | `datasets/words.txt` | ได้คำศัพท์หมวดสัตว์ ผลไม้ และประเทศ สำหรับใช้เทรนโมเดล |
| 17 | เขียน `make_dataset.py` — ถาม AI วิธีจำลอง game state จากคำศัพท์เพื่อสร้าง training data | `codes/make_dataset.py`, `datasets/hangman_dataset.csv` | ได้ dataset ที่มี feature: `pattern`, `guessed`, `wrong`, `length`, `revealed`, `candidate_count` |
| 18 | เขียน `train_models.py` — ถาม AI วิธีเทรนและบันทึก Decision Tree, Logistic Regression และ Naive Bayes | `codes/train_models.py`, `models/` | ได้ไฟล์ `hangman_tree.pkl`, `hangman_lr.pkl`, `hangman_nb.pkl` |
| 19 | เขียน `eval_models.py` — ถาม AI วิธีเปรียบเทียบผลโมเดลและบันทึกผล | `codes/eval_models.py`, `datasets/model_comparison.csv` | Decision Tree ให้ผลดีที่สุด → เลือกใช้ใน production |

---

## 24 ก.ค. 2568

| ลำดับ | การเปลี่ยนแปลง | ไฟล์/ส่วนที่เกี่ยวข้อง | ผลลัพธ์ |
|---|---|---|---|
| 20 | เขียน `predict.py` — ถาม AI วิธีโหลด `.pkl` และสร้างฟังก์ชัน `predict()` ที่รับ game state แล้วคืน top-5 ตัวอักษร | `codes/predict.py` | `predict(pattern, guessed, wrong)` คืน list ตัวอักษรสูงสุด 5 ตัว |
| 21 | เพิ่ม fallback logic ใน `predict()` — ถาม AI กรณีที่โมเดลคืนตัวอักษรซ้ำหรือไม่ครบ 5 ตัว ควรทำอย่างไร | `codes/predict.py` — ส่วน fallback | เติมตัวอักษรที่ยังไม่ถูกใช้จาก `string.ascii_lowercase` จนครบ 5 ตัว |
| 22 | เพิ่ม `count_candidates()` ใน `predict.py` — ถาม AI วิธีนับคำศัพท์ที่เป็นไปได้จาก pattern ปัจจุบัน | `codes/predict.py` — ฟังก์ชัน `count_candidates()` | ใช้เป็น feature `candidate_count` ให้โมเดลตัดสินใจได้แม่นขึ้น |
| 23 | เพิ่ม AI Assist mode — ถาม AI วิธีเชื่อม `predict()` เข้ากับ game loop ให้แสดงคำแนะนำก่อนผู้เล่นเดา | `hangman.py` — `_ai_public()` ส่วน `mode == "assist"` | `out["hints"] = predict(pattern, guessed, wrong)[:2]` ส่งคำแนะนำไปยัง frontend |
| 24 | เพิ่ม VS AI mode — ถาม AI วิธีให้ผู้เล่นและ AI ผลัดกันเดาคำเดียวกัน และตรวจสถานะชนะ/แพ้ของแต่ละฝ่าย | `hangman.py` — `api_ai_guess()` ส่วน `mode == "vs"` | ผู้เล่นเดา `p_word` และ AI เดา `a_word` สลับกัน ตรวจ `player_win`, `player_lose`, `ai_win`, `ai_lose` |
| 25 | เพิ่ม `POST /api/hangman/ai/new` และ `POST /api/hangman/ai/guess` — ถาม AI วิธีแยก endpoint ของ AI mode ออกจาก Classic | `hangman.py` — `api_ai_new()`, `api_ai_guess()` | AI mode มี endpoint แยกต่างหาก ไม่กระทบ Classic mode |
| 26 | สร้าง UI สำหรับ AI Assist และ VS AI — ถาม AI วิธีแสดงคำแนะนำและสถานะของทั้งสองฝ่ายบนหน้าจอ | `games/hangman/hangman_ai.html`, `hangman_ai.css`, `hangman_ai.js` | หน้าจอแสดง hint, board ของผู้เล่น และ board ของ AI แยกกันชัดเจน |
| 27 | แก้ไข UI bugs และปรับ UX ที่เพื่อนแจ้งเข้ามาโดยถาม AI เรื่องปัญหาที่พบระหว่างทดสอบ ได้แก่ ปุ่มค้าง สถานะไม่อัปเดต และมีการใช้คีย์บอร์ดด้วยกันกับ AI | HTML/CSS/JS ทุกไฟล์ | การใช้งานลื่นขึ้น ปุ่มถูก disable หลังเกมจบ และแสดงคำตอบเมื่อแพ้ |
| 28 | เพิ่ม `requirements.txt` | `requirements.txt` | ระบุ `flask`, `scikit-learn`, `pandas`, `joblib` พร้อม version |
| 29 | จัดทำเอกสาร `docs/` — ถาม AI วิธีเขียน Quick Start, Gameplay guide และ AI pipeline อธิบาย | `docs/QUICKSTART.md`, `docs/GAMEPLAY.md`, `docs/HANGMAN_AI.md` | มีคู่มือติดตั้ง วิธีเล่นแต่ละโหมด และคำอธิบาย AI pipeline ครบถ้วน |
| 30 | เขียน `TEST.md` — ถาม AI วิธีวางแผนทดสอบ API และ game logic | `TEST.md` | มีกรณีทดสอบ: เริ่มเกมใหม่, เดาถูก, เดาผิด, เดาซ้ำ, input ไม่ถูกต้อง, ชนะ, แพ้ |
| 31 | เขียน `LEARNINGLOG.md` — บันทึกสิ่งที่เรียนรู้ตลอดโครงงาน รวมถึงการใช้ AI อย่างรับผิดชอบ | `LEARNINGLOG.md` | บันทึก prompt, response, การทดลอง และข้อสังเกตของทีมตลอดโครงงาน |

---

← [กลับหน้าโครงการ](README.md)
