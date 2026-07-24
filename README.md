<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=4FC3F7&center=true&vCenter=true&width=500&lines=Welcome+to+OUR+GitHub!;Script+Programming+Mini+Project;College+of+Computing" />

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

</div>

---

# Mini Game Hub

Repository นี้จัดทำขึ้นเพื่อใช้สำหรับ **Mini Project** ในรายวิชาเท่านั้น

**รายวิชา:** Script Programming &nbsp;---&nbsp; CP352301

---

## Student Information

<table>
  <tr>
    <th>#</th>
    <th>ชื่อ - นามสกุล</th>
    <th>รหัสนักศึกษา</th>
    <th>สาขาวิชา</th>
  </tr>
  <tr>
    <td align="center">1</td>
    <td>นายจักรพรรดิ์ มั่งกูล</td>
    <td align="center">663380518-4</td>
    <td>Artificial Intelligence (AI)</td>
  </tr>
  <tr>
    <td align="center">2</td>
    <td>นายเชิดตระกูล แข็งขัน</td>
    <td align="center">663380305-1</td>
    <td>Artificial Intelligence (AI)</td>
  </tr>
  <tr>
    <td align="center">3</td>
    <td>นายพงษกร มานาดี</td>
    <td align="center">663380282-7</td>
    <td>Artificial Intelligence (AI)</td>
  </tr>
  <tr>
    <td align="center">4</td>
    <td>นางสาวทักษพร มูลมณี</td>
    <td align="center">653380198-5</td>
    <td>Computer Science (CS)</td>
  </tr>
</table>

---

## Project Structure

```text
SP-MiniProject/
├── app.py                      # Flask entry point (routing + blueprints)
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # หน้า Menu หลัก
├── static/
│   ├── menu.css
│   └── menu.js
├── games/
│   └── hangman/                # เกม Hangman (frontend + blueprint)
│       ├── hangman.py          # Flask blueprint (API)
│       ├── hangman.html        # Classic mode UI
│       ├── hangman.css
│       ├── hangman.js
│       ├── hangman_ai.html     # AI Assist / VS AI mode UI
│       ├── hangman_ai.css
│       └── hangman_ai.js
├── models/
│   ├── hangman_tree.pkl        # Decision Tree (ใช้งานจริง)
│   ├── hangman_lr.pkl          # Logistic Regression (offline)
│   └── hangman_nb.pkl          # Naive Bayes (offline)
├── datasets/
│   ├── words.txt               # คลังคำศัพท์ (animal / country / fruit)
│   ├── hangman_dataset.csv     # Dataset ที่สร้างจาก words.txt
│   └── model_comparison.csv   # ผลเปรียบเทียบโมเดล
└── codes/                      # Offline AI pipeline scripts
    ├── predict.py              # ฟังก์ชัน predict (ใช้งานจริง)
    ├── make_dataset.py         # สร้าง dataset จาก words.txt
    ├── train_models.py         # เทรนโมเดลทั้ง 3 แบบ
    ├── eval_models.py          # ประเมินและเปรียบเทียบโมเดล
    ├── generate_words.py       # สร้าง/จัดการ words.txt
    ├── Hangman_AI.ipynb        # Notebook ทดสอบ AI pipeline
    ├── Hangman.ipynb           # Notebook ทดสอบเกม Hangman
    └── test_ai.ipynb           # Notebook ทดสอบ predict()
```

---

## วิธีติดตั้งและรัน

**1. ติดตั้ง dependencies**

```bash
pip install -r requirements.txt
```

**2. รัน Flask server**

```bash
python app.py
```

**3. เปิดเบราว์เซอร์**

```
http://localhost:5000
```

---

## Hangman AI

เกม Hangman ในโปรเจกต์นี้มี AI ช่วยแนะนำตัวอักษรที่ควรเดา โดยใช้ Decision Tree เทรนจากคลังคำศัพท์กว่า 1,000 คำ

### AI Pipeline (Offline)

```
words.txt  →  make_dataset.py  →  train_models.py  →  eval_models.py  →  hangman_tree.pkl
```

| ขั้นตอน | ไฟล์ | คำอธิบาย |
|---------|------|----------|
| 1 | `make_dataset.py` | สร้าง dataset จาก words.txt โดย simulate ทุก state ของเกม |
| 2 | `train_models.py` | เทรน 3 โมเดล (Decision Tree, Logistic Regression, Naive Bayes) |
| 3 | `eval_models.py` | วัด top-1 / top-5 accuracy และเปรียบเทียบโมเดล |

### วิธีเทรนโมเดล (ถ้าต้องการ retrain)

```bash
cd codes

python make_dataset.py
python train_models.py
python eval_models.py
```

### วิธีใช้งาน AI ใน Code

```python
from codes.predict import predict

# predict(pattern, guessed, wrong) → list of 5 suggested letters
suggestions = predict(
    pattern = "e_e_h__t",
    guessed = {"e", "h", "t"},
    wrong   = {"a", "i"}
)

print(suggestions)  # ['l', 'p', 'n', 'r', 's']
```

| Parameter | Type | คำอธิบาย |
|-----------|------|----------|
| `pattern` | `str` | pattern ปัจจุบัน เช่น `"e_e_h__t"` (`_` = ยังไม่รู้) |
| `guessed` | `set` | ตัวอักษรที่เดาถูกแล้ว |
| `wrong` | `set` | ตัวอักษรที่เดาผิดแล้ว |
| return | `list[str]` | top-5 ตัวอักษรที่แนะนำ |

---

## เกมที่มี

### Hangman — Classic Mode

> สไตล์ Game Boy สีเขียวพิกเซล

**วิธีเล่น:**
- กด **HANGMAN** ที่หน้า Menu เพื่อเข้าเกม
- เดาตัวอักษรทีละตัวโดยกดปุ่มบน keyboard บนหน้าจอ
- มีชีวิต **6 ครั้ง** — เดาผิดแต่ละครั้งจะวาดร่างคนแขวนคอเพิ่มขึ้น
- เดาถูกทุกตัวก่อนหมดชีวิต = **ชนะ!**

**หมวดคำ:** สัตว์ / ผลไม้ / ประเทศ (สุ่มอัตโนมัติ)

**API:**

| Method | Endpoint | คำอธิบาย |
|:------:|----------|-----------|
| `POST` | `/api/hangman/new` | เริ่มเกมใหม่ |
| `POST` | `/api/hangman/guess` | ส่งตัวอักษรที่เดา `{ "letter": "a" }` |

---

### Hangman — AI Assist Mode

- ผู้เล่นเดาตัวอักษรเอง
- AI แสดง top-5 ตัวอักษรที่แนะนำก่อนทุก turn
- ผู้เล่นตัดสินใจเองว่าจะเดาตามหรือไม่

**เข้าเกม:** กด **AI ASSIST** ที่หน้า Menu

**API:**

| Method | Endpoint | คำอธิบาย |
|:------:|----------|-----------|
| `POST` | `/api/hangman/new` | เริ่มเกมใหม่ (mode=assist) |
| `POST` | `/api/hangman/guess` | ส่งตัวอักษรที่เดา — response มี `suggestions` |

---

### Hangman — VS AI Mode

- ผู้เล่นและ AI ได้คำเดียวกัน สลับ turn กัน
- ผู้เล่น 1 turn → AI 1 turn ไปเรื่อยๆ
- ใครผิดครบ 6 ครั้งก่อน = **แพ้**

**เข้าเกม:** กด **VS AI** ที่หน้า Menu

**API:**

| Method | Endpoint | คำอธิบาย |
|:------:|----------|-----------|
| `POST` | `/api/hangman/new` | เริ่มเกมใหม่ (mode=vs) |
| `POST` | `/api/hangman/guess` | ส่งตัวอักษร — response มีผล turn ของ AI ด้วย |

| สถานะ | ความหมาย |
|-------|----------|
| `player_win` | ผู้เล่นเดาถูกทุกตัว |
| `player_lose` | ผู้เล่นผิดครบ 6 ครั้ง |
| `ai_win` | AI เดาถูกทุกตัว |
| `ai_lose` | AI ผิดครบ 6 ครั้ง |

---

## หมายเหตุ

> Game state เก็บใน memory — รีเซ็ตเมื่อ restart server  
> แต่ละโหมดมี CSS แยกกันอิสระ แก้สไตล์ได้โดยไม่กระทบกัน
