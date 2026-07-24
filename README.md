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
├── app.py                      # Flask backend (API + routing)
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # หน้า Menu หลัก
├── static/
│   ├── menu.css
│   └── menu.js
├── games/
│   └── hangman/                # เกม Hangman (frontend)
│       ├── hangman.html
│       ├── hangman.css
│       └── hangman.js
├── models/                     # โมเดล AI ที่เทรนแล้ว
│   ├── hangman_best.pkl        # โมเดลที่ดีที่สุด (ใช้งานจริง)
│   ├── hangman_tree.pkl
│   ├── hangman_rf.pkl
│   ├── hangman_lr.pkl
│   └── hangman_nb.pkl
├── datasets/
│   └── model_comparison.csv    # ผลเปรียบเทียบโมเดล
└── codes/                      # สคริปต์ AI
    ├── words.txt               # คลังคำศัพท์ (animal / country / fruit)
    ├── make_dataset.py         # สร้าง dataset จาก words.txt
    ├── train_models.py         # เทรนโมเดลทั้ง 4 แบบ
    ├── eval_models.py          # ประเมินและเลือกโมเดลที่ดีที่สุด
    ├── predict.py              # ฟังก์ชัน predict ใช้งานจริง
    └── test_ai.ipynb           # Notebook ทดสอบ AI
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

เกม Hangman ในโปรเจกต์นี้มี AI ช่วยแนะนำตัวอักษรที่ควรเดา โดยใช้ Machine Learning เทรนจากคลังคำศัพท์กว่า 1,000 คำ

### AI Pipeline

```
words.txt  →  make_dataset.py  →  train_models.py  →  eval_models.py  →  hangman_best.pkl
```

| ขั้นตอน | ไฟล์ | คำอธิบาย |
|---------|------|----------|
| 1 | `make_dataset.py` | สร้าง dataset จาก words.txt โดย simulate ทุก state ของเกม |
| 2 | `train_models.py` | เทรน 4 โมเดล (Decision Tree, Random Forest, Logistic Regression, Naive Bayes) |
| 3 | `eval_models.py` | โหลดโมเดลที่เทรนแล้ว วัด top-1 / top-5 accuracy แล้วเลือกตัวที่ดีที่สุด |

### วิธีเทรนโมเดล

รันตามลำดับใน `codes/`

```bash
cd codes

# 1. สร้าง dataset
python make_dataset.py

# 2. เทรนโมเดลทั้ง 4 แบบ → บันทึกใน models/
python train_models.py

# 3. ประเมินและบันทึก best model → models/hangman_best.pkl
python eval_models.py
```

### วิธีใช้งาน AI ใน Code

```python
from predict import predict

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

### ทดสอบ AI

เปิด `codes/test_ai.ipynb` ใน Jupyter แล้วรันทีละ cell

---

## เกมที่มี

### Hangman — Game Boy Edition

> สไตล์ Game Boy สีเขียวพิกเซล

**วิธีเล่น:**
- กด **PLAY** ที่หน้า Menu เพื่อเข้าเกม
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

### Hangman AI — 3 Modes (`games/Hangman_AI.ipynb`)

เกม Hangman บน Jupyter Notebook ที่ใช้ AI จาก `hangman_best.pkl` มี 3 โหมด

**Mode 1 — AI Assist**
- ผู้เล่นเดาตัวอักษรเอง
- ก่อนทุก turn AI จะแสดง top-5 ตัวอักษรที่แนะนำ
- ผู้เล่นตัดสินใจเองว่าจะเดาตามหรือไม่
- เหมาะสำหรับผู้เล่นที่ต้องการคำใบ้

**Mode 2 — AI Opponent**
- AI เล่นคนเดียวทั้งหมด ผู้เล่นแค่กด Enter ดูทีละ step
- สามารถกำหนดคำเองได้ หรือปล่อยให้สุ่มอัตโนมัติ
- เหมาะสำหรับทดสอบว่า AI เก่งแค่ไหน

**Mode 3 — VS AI**
- ผู้เล่นตั้งคำให้ AI เดา และ AI สุ่มคำให้ผู้เล่นเดา (คนละคำ)
- สลับ turn กันไปเรื่อยๆ — ผู้เล่น 1 turn → AI 1 turn
- ใครผิดครบ 6 ครั้งก่อน = แพ้

| โหมด | ผู้เล่น | AI | เป้าหมาย |
|------|---------|-----|----------|
| AI Assist | เดาเอง | แนะนำ top-5 | ผู้เล่นชนะเกม |
| AI Opponent | ดู | เล่นคนเดียว | ทดสอบความแม่นของ AI |
| VS AI | เดาคำของ AI | เดาคำของผู้เล่น | ใครผิดครบ 6 ก่อน = แพ้ |

---

## หมายเหตุ

> Game state เก็บใน memory — รีเซ็ตเมื่อ restart server  
> แต่ละเกมมี CSS แยกกันอิสระ ทีมสามารถแก้สไตล์ได้โดยไม่กระทบกัน
