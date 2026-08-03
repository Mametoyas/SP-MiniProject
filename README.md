<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=4FC3F7&center=true&vCenter=true&width=600&lines=Mini+Game+Hub;Hangman+with+AI;Script+Programming+Mini+Project" />

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

---

# Mini Game Hub

โปรเจกต์ Mini Project รายวิชา **Script Programming (CP352301)**
เว็บรวมมินิเกมที่พัฒนาด้วย Flask โดยเกมหลักคือ **Hangman** พร้อมระบบ AI สำหรับแนะนำตัวอักษรที่ควรเดา

---

## สารบัญ

- [เกี่ยวกับเกม](#เกี่ยวกับเกม)
- [สมาชิกในกลุ่ม](#สมาชิกในกลุ่ม)
- [เทคโนโลยี](#เทคโนโลยี)
- [เริ่มต้นใช้งาน](#เริ่มต้นใช้งาน)
- [โครงสร้างโปรเจกต์](#โครงสร้างโปรเจกต์)
- [API หลัก](#api-หลัก)
- [AI Pipeline](#ai-pipeline)
- [Kanban Backlog](#kanban-backlog)
- [Group Learning Outcomes](#group-learning-outcomes)
- [Group Grading Rubric](#group-grading-rubric)
- [เอกสารเพิ่มเติม](#เอกสารเพิ่มเติม)

---

## เกี่ยวกับเกม

Hangman มี 3 รูปแบบการเล่น

<table>
  <thead>
    <tr>
      <th width="120px">โหมด</th>
      <th>รายละเอียด</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>Classic</b></td>
      <td>เดาคำศัพท์ทีละตัวอักษร มีโอกาสเดาผิด 6 ครั้ง</td>
    </tr>
    <tr>
      <td align="center"><b>AI Assist</b></td>
      <td>ผู้เล่นเดาเอง โดย AI แนะนำตัวอักษรที่น่าจะถูก 5 อันดับแรก</td>
    </tr>
    <tr>
      <td align="center"><b>VS AI</b></td>
      <td>ผู้เล่นและ AI ผลัดกันเดาคำเดียวกัน ผู้ที่เดาผิดครบ 6 ครั้งก่อนเป็นฝ่ายแพ้</td>
    </tr>
  </tbody>
</table>

คำศัพท์ถูกสุ่มจากหมวดสัตว์ ผลไม้ และประเทศ
ระบบ AI ใช้ Decision Tree ที่ผ่านการเทรนจากคลังคำศัพท์ และมี Logistic Regression กับ Naive Bayes สำหรับเปรียบเทียบผลแบบออฟไลน์

---

## สมาชิกในกลุ่ม

<table>
  <thead>
    <tr>
      <th width="40px">#</th>
      <th>ชื่อ - นามสกุล</th>
      <th width="160px">รหัสนักศึกษา</th>
      <th>สาขาวิชา</th>
    </tr>
  </thead>
  <tbody>
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
  </tbody>
</table>

---

## เทคโนโลยี

<table>
  <thead>
    <tr>
      <th width="160px">ส่วน</th>
      <th>เทคโนโลยี</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Backend</b></td>
      <td>Python, Flask</td>
    </tr>
    <tr>
      <td><b>Frontend</b></td>
      <td>HTML, CSS, JavaScript</td>
    </tr>
    <tr>
      <td><b>Machine Learning</b></td>
      <td>scikit-learn, pandas, joblib</td>
    </tr>
  </tbody>
</table>

---

## เริ่มต้นใช้งาน

**1. Clone และสร้าง virtual environment**

```bash
git clone https://github.com/<your-username>/SP-MiniProject.git
cd SP-MiniProject
python -m venv venv
```

**2. เปิดใช้งาน virtual environment**

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. ติดตั้ง dependency และรันเซิร์ฟเวอร์**

```bash
pip install -r requirements.txt
python app.py
```

จากนั้นเปิด http://localhost:5000 ในเบราว์เซอร์

---

## โครงสร้างโปรเจกต์

```text
📁SP-MiniProject/
 │
 ├── 📁codes/
 │    ├── eval_models.py
 │    ├── generate_words.py
 │    ├── Hangman_AI.ipynb
 │    ├── Hangman.ipynb
 │    ├── make_dataset.py
 │    ├── predict.py
 │    ├── test_ai.ipynb
 │    └── train_models.py
 │
 ├── 📁datasets/
 │    ├── hangman_dataset.csv
 │    ├── model_comparison.csv
 │    └── words.txt
 │
 ├── 📁docs/
 │    ├── GAMEPLAY.md
 │    ├── HANGMAN_AI.md
 │    ├── Mini-Project.md
 │    └── QUICKSTART.md
 │
 ├── 📁games/
 │    ├── __init__.py
 │    └── 📁hangman/
 │        ├── __init__.py
 │        ├── hangman_ai.css
 │        ├── hangman_ai.html
 │        ├── hangman_ai.js
 │        ├── hangman.css
 │        ├── hangman.html
 │        ├── hangman.js
 │        └── hangman.py
 │
 ├── 📁models/
 │    ├── hangman_lr.pkl
 │    ├── hangman_nb.pkl
 │    └── hangman_tree.pkl
 │
 ├── 📁static/
 │    ├── menu.css
 │    └── menu.js
 │
 ├── 📁templates/
 │    └── index.html
 │
 ├── app.py
 ├── CHANGELOG.md
 ├── ChatGPT-history.txt
 ├── LEARNINGLOG.md
 ├── LEARNINGLOG.txt
 ├── Mini_Project.ipynb
 ├── README.md
 ├── requirements.txt
 ├── Teacher prompt.txt
 └── TEST.md

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
    ├── QUICKSTART.md           # คู่มือติดตั้งและรันแบบเร็ว
    ├── HANGMAN_AI.md           # AI pipeline & predict()
    └── GAMEPLAY.md             # วิธีเล่นแต่ละโหมด & API
```

---

## API หลัก

<table>
  <thead>
    <tr>
      <th width="80px">Method</th>
      <th width="220px">Endpoint</th>
      <th>การทำงาน</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><code>POST</code></td>
      <td><code>/api/hangman/new</code></td>
      <td>เริ่มเกมใหม่ โดยระบุโหมดได้</td>
    </tr>
    <tr>
      <td align="center"><code>POST</code></td>
      <td><code>/api/hangman/guess</code></td>
      <td>ส่งตัวอักษรที่ต้องการเดา เช่น <code>{ "letter": "a" }</code></td>
    </tr>
  </tbody>
</table>

> Game state เก็บใน memory — รีเซ็ตเมื่อ restart server

---

## AI Pipeline

```text
datasets/words.txt
    → codes/make_dataset.py
    → codes/train_models.py
    → codes/eval_models.py
    → models/hangman_tree.pkl
```

หากต้องการสร้างและเทรนโมเดลใหม่:

```bash
cd codes
python make_dataset.py
python train_models.py
python eval_models.py
```

---

## Kanban Backlog

ตารางนี้เรียงลำดับการพัฒนาโครงงานตั้งแต่การวางแนวคิดเกม ไปจนถึงการนำ AI และเว็บ UI มาใช้งาน

<table>
  <thead>
    <tr>
      <th width="80px">สถานะ</th>
      <th>งาน</th>
      <th>ผลลัพธ์/ขอบเขต</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>สอบถาม AI เกี่ยวกับหัวข้อเกม Hangman</td>
      <td>ศึกษากติกา องค์ประกอบเกม และวางแนวทางพัฒนาเป็น mini project</td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>วาง pseudocode และออกแบบ logic เกม</td>
      <td>กำหนดการสุ่มคำ การรับตัวอักษร การตรวจคำตอบ จำนวนชีวิต และเงื่อนไขชนะ/แพ้</td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>ทำ draft Hangman แบบไม่มี AI</td>
      <td>พัฒนา Classic mode ให้เล่นได้ด้วย logic Python และคลังคำศัพท์</td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>เพิ่มและจัดระเบียบโมดูล</td>
      <td>แยก game logic, Flask Blueprint, scripts สำหรับ AI และไฟล์ static ตามหน้าที่</td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>สร้าง dataset สำหรับ Hangman</td>
      <td>จำลอง game state จาก <code>words.txt</code> เป็น <code>hangman_dataset.csv</code></td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>ศึกษาและประยุกต์ AI กับเกม</td>
      <td>เทรน/เปรียบเทียบ Decision Tree, Logistic Regression และ Naive Bayes เพื่อแนะนำตัวอักษร</td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>เชื่อม AI เข้ากับรูปแบบการเล่น</td>
      <td>เพิ่ม AI Assist และ VS AI โดยใช้ <code>predict()</code> เพื่อสร้างคำแนะนำ</td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>พัฒนาเว็บ UI และ API</td>
      <td>สร้าง Menu, หน้าเกมทั้ง 3 โหมด, CSS/JavaScript และ API สำหรับเริ่มเกม/เดาตัวอักษร</td>
    </tr>
    <tr>
      <td align="center"><code>Done</code></td>
      <td>จัดทำเอกสารโครงการ</td>
      <td>มี Quick Start, Gameplay, AI pipeline และ README</td>
    </tr>
    <tr>
      <td align="center"><code>To do</code></td>
      <td>เพิ่ม automated tests สำหรับ API และ logic เกม</td>
      <td>ตรวจสอบการเริ่มเกม การเดา และสถานะชนะ/แพ้</td>
    </tr>
    <tr>
      <td align="center"><code>To do</code></td>
      <td>เพิ่มเกมหรือคลังคำศัพท์</td>
      <td>ขยาย Mini Game Hub ในอนาคต</td>
    </tr>
  </tbody>
</table>

---

## Group Learning Outcomes

เมื่อจบโครงงาน กลุ่มสามารถ:

<table>
  <thead>
    <tr>
      <th width="260px">ผลลัพธ์การเรียนรู้</th>
      <th>หลักฐานและตัวอย่างจากโครงงาน</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>วิเคราะห์และออกแบบปัญหา</b></td>
      <td>เปลี่ยนกติกา Hangman เป็นขั้นตอนการทำงานที่ตรวจสอบได้ ได้แก่ สุ่มคำ สร้างช่องว่าง รับตัวอักษร ตรวจคำซ้ำ นับการเดาผิด และตัดสินชนะ/แพ้ โดยกำหนด <code>MAX_WRONG = 6</code> ใน <code>games/hangman/hangman.py</code></td>
    </tr>
    <tr>
      <td><b>เลือกใช้โครงสร้างข้อมูล Python ได้เหมาะสม</b></td>
      <td><code>WORDS</code> เป็น dictionary สำหรับจัดหมวดคำศัพท์ และคำในแต่ละหมวดเป็น list เพื่อสุ่มด้วย <code>random.choice()</code>; ส่วน <code>set</code> ใช้เก็บอักษรไม่ซ้ำ เช่น <code>set(target)</code> ใน <code>codes/make_dataset.py</code> และหาอักษรผิดด้วย <code>guessed - set(word)</code></td>
    </tr>
    <tr>
      <td><b>เขียนโปรแกรมแบบแยกส่วนและนำกลับมาใช้ได้</b></td>
      <td>แยกจุดเริ่มระบบไว้ใน <code>app.py</code>, game/API ไว้ใน <code>games/hangman/hangman.py</code>, การทำนายไว้ใน <code>codes/predict.py</code> และ pipeline AI ไว้ใน <code>codes/</code></td>
    </tr>
    <tr>
      <td><b>ใช้ control flow และ validation ในโปรแกรมจริง</b></td>
      <td>API ตรวจ input ด้วย <code>len(letter) != 1 or not letter.isalpha()</code> ใช้เงื่อนไขกำหนดผลถูก/ผิด และใช้ <code>all(...)</code> ตรวจว่าผู้เล่นเปิดเผยอักษรครบทุกตัว</td>
    </tr>
    <tr>
      <td><b>พัฒนาเว็บแอปพลิเคชันและ API</b></td>
      <td>Flask Blueprint จัด route ของ Hangman; HTML/CSS/JavaScript ใน <code>games/hangman/</code> เรียก API เพื่ออัปเดตเกมจากการโต้ตอบของผู้เล่น</td>
    </tr>
    <tr>
      <td><b>เตรียมข้อมูลและประยุกต์ Machine Learning</b></td>
      <td><code>make_dataset.py</code> จำลองสถานะเกมจาก <code>words.txt</code>; pipeline เทรน/ประเมิน 3 โมเดล และ <code>predict.py</code> ส่งคำแนะนำไปใช้ใน AI Assist กับ VS AI</td>
    </tr>
    <tr>
      <td><b>ทำงานกลุ่มและจัดทำเอกสาร</b></td>
      <td>ใช้ Git ติดตามงาน แบ่งโครงสร้างโฟลเดอร์ตามหน้าที่ และจัดทำคู่มือ/บันทึกการเปลี่ยนแปลง/บันทึกการเรียนรู้แยกกัน</td>
    </tr>
  </tbody>
</table>

---

## Group Grading Rubric

ส่วนนี้เป็นการประเมินเพื่อนร่วมกลุ่มรายบุคคล เพื่อแสดงให้อาจารย์เห็นระดับการมีส่วนร่วมและคุณภาพงานของสมาชิกแต่ละคน ไม่ใช่คะแนนประเมินตัวโครงงาน

### วิธีประเมิน

1. สมาชิกทุกคนให้คะแนนเพื่อนร่วมกลุ่มอีก 3 คน โดยให้คะแนนตามผลงานที่เห็นจริงตลอดโครงงาน
2. ให้คะแนนเต็ม **10 คะแนน** ต่อสมาชิก 1 คน
3. ใช้หลักฐานประกอบ เช่น commit ใน Git, โค้ด/เอกสารที่รับผิดชอบ, การเข้าร่วมประชุม, การสื่อสาร และการช่วยแก้ปัญหา
4. คะแนนเฉลี่ยรายบุคคลคำนวณจากคะแนนที่ได้รับทั้งหมด เพื่อให้เห็นภาพรวมที่เป็นธรรม

### เกณฑ์การให้คะแนน 1–10

<table>
  <thead>
    <tr>
      <th width="120px">ช่วงคะแนน</th>
      <th>ความหมาย</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>9–10</b></td>
      <td>มีส่วนร่วมโดดเด่น รับผิดชอบงานครบหรือเกินขอบเขต ส่งงานมีคุณภาพ ช่วยทีมแก้ปัญหา และสื่อสารอย่างสม่ำเสมอ</td>
    </tr>
    <tr>
      <td align="center"><b>7–8</b></td>
      <td>ทำงานที่ได้รับมอบหมายได้ดี ส่งงานตรงเวลา มีส่วนร่วมกับทีมและแก้ไขงานเมื่อได้รับข้อเสนอแนะ</td>
    </tr>
    <tr>
      <td align="center"><b>5–6</b></td>
      <td>ทำงานได้บางส่วน แต่ต้องติดตามหรือช่วยเหลือเป็นระยะ คุณภาพ/ความต่อเนื่องของงานยังไม่สม่ำเสมอ</td>
    </tr>
    <tr>
      <td align="center"><b>3–4</b></td>
      <td>มีส่วนร่วมค่อนข้างน้อย ส่งงานล่าช้าหรือไม่ครบ และต้องให้สมาชิกคนอื่นรับงานต่อ</td>
    </tr>
    <tr>
      <td align="center"><b>1–2</b></td>
      <td>แทบไม่มีส่วนร่วม ไม่รับผิดชอบงานที่ได้รับมอบหมาย หรือไม่สามารถติดต่อ/ทำงานร่วมกับกลุ่มได้</td>
    </tr>
  </tbody>
</table>

### ตารางให้คะแนนเพื่อนร่วมกลุ่ม

<table>
  <thead>
    <tr>
      <th>ผู้ประเมิน \ ผู้ถูกประเมิน</th>
      <th align="center">นายจักรพรรดิ์ มั่งกูล</th>
      <th align="center">นายเชิดตระกูล แข็งขัน</th>
      <th align="center">นายพงษกร มานาดี</th>
      <th align="center">นางสาวทักษพร มูลมณี</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>นายจักรพรรดิ์ มั่งกูล</td>
      <td align="center">—</td>
      <td align="center">10 / 10</td>
      <td align="center">____ / 10</td>
      <td align="center">____ / 10</td>
    </tr>
    <tr>
      <td>นายเชิดตระกูล แข็งขัน</td>
      <td align="center">____ / 10</td>
      <td align="center">—</td>
      <td align="center">____ / 10</td>
      <td align="center">____ / 10</td>
    </tr>
    <tr>
      <td>นายพงษกร มานาดี</td>
      <td align="center">____ / 10</td>
      <td align="center">____ / 10</td>
      <td align="center">—</td>
      <td align="center">____ / 10</td>
    </tr>
    <tr>
      <td>นางสาวทักษพร มูลมณี</td>
      <td align="center">10 / 10</td>
      <td align="center">10 / 10</td>
      <td align="center">9 / 10</td>
      <td align="center">—</td>
    </tr>
    <tr>
      <td><b>คะแนนเฉลี่ยที่ได้รับ</b></td>
      <td align="center"><b>____ / 10</b></td>
      <td align="center"><b>____ / 10</b></td>
      <td align="center"><b>____ / 10</b></td>
      <td align="center"><b>____ / 10</b></td>
    </tr>
  </tbody>
</table>

> ให้เว้นช่องของผู้ประเมินตนเองเป็น `—` และคำนวณคะแนนเฉลี่ยจากผู้ประเมินอีก 3 คน

---

## เอกสารเพิ่มเติม

<table>
  <thead>
    <tr>
      <th>หัวข้อ</th>
      <th>ไฟล์</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Quick Start — ติดตั้งและรันแบบเร็ว</td>
      <td><a href="docs/QUICKSTART.md">docs/QUICKSTART.md</a></td>
    </tr>
    <tr>
      <td>Hangman AI — pipeline &amp; predict()</td>
      <td><a href="docs/HANGMAN_AI.md">docs/HANGMAN_AI.md</a></td>
    </tr>
    <tr>
      <td>Gameplay — วิธีเล่นแต่ละโหมด &amp; API</td>
      <td><a href="docs/GAMEPLAY.md">docs/GAMEPLAY.md</a></td>
    </tr>
    <tr>
      <td>แผนและผลการทดสอบ</td>
      <td><a href="TEST.md">TEST.md</a></td>
    </tr>
    <tr>
      <td>ประวัติการเปลี่ยนแปลง</td>
      <td><a href="CHANGELOG.md">CHANGELOG.md</a></td>
    </tr>
    <tr>
      <td>บันทึกการเรียนรู้</td>
      <td><a href="LEARNINGLOG.md">LEARNINGLOG.md</a></td>
    </tr>
  </tbody>
</table>
