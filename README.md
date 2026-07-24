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
├── codes/                      # Offline AI pipeline scripts
│   ├── predict.py              # ฟังก์ชัน predict (ใช้งานจริง)
│   ├── make_dataset.py
│   ├── train_models.py
│   ├── eval_models.py
│   ├── generate_words.py
│   ├── Hangman_AI.ipynb
│   ├── Hangman.ipynb
│   └── test_ai.ipynb
└── docs/
    ├── HANGMAN_AI.md           # AI pipeline & predict()
    └── GAMEPLAY.md             # วิธีเล่นแต่ละโหมด & API
```

---

## วิธีติดตั้งและรัน

**1. สร้าง Virtual Environment**

```bash
python -m venv venv
```

**2. Activate Virtual Environment**

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

> ถ้า activate สำเร็จ จะเห็น `(venv)` นำหน้า prompt

**3. ติดตั้ง dependencies**

```bash
pip install -r requirements.txt
```

**4. รัน Flask server**

```bash
python app.py
```

**5. เปิดเบราว์เซอร์**

```
http://localhost:5000
```

> ออกจาก env เมื่อเลิกใช้งานด้วย `deactivate`

---

## เอกสารเพิ่มเติม

| หัวข้อ | ไฟล์ |
|--------|------|
| Quick Start — ติดตั้งและรันแบบเร็ว | [docs/QUICKSTART.md](docs/QUICKSTART.md) |
| Hangman AI — pipeline & predict() | [docs/HANGMAN_AI.md](docs/HANGMAN_AI.md) |
| Gameplay — วิธีเล่นแต่ละโหมด & API | [docs/GAMEPLAY.md](docs/GAMEPLAY.md) |

---

## หมายเหตุ

> Game state เก็บใน memory — รีเซ็ตเมื่อ restart server  
> แต่ละโหมดมี CSS แยกกันอิสระ แก้สไตล์ได้โดยไม่กระทบกัน
