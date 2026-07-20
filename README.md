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
    <td>&lt;ชื่อ นามสกุล&gt;</td>
    <td align="center">&lt;รหัสนักศึกษา&gt;</td>
    <td>&lt;สาขาวิชา&gt;</td>
  </tr>
  <tr>
    <td align="center">4</td>
    <td>&lt;นางสาวทักษพร มูลมณี&gt;</td>
    <td align="center">&lt;653380198-5&gt;</td>
    <td>Computer Science (CS)</td>
  </tr>
</table>

---

## Project Structure

```text
SP - MiniProject/
├── app.py                  # Flask backend (API + routing)
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # หน้า Menu หลัก
├── static/
│   ├── menu.css            # สไตล์หน้า Menu
│   └── menu.js             # Boot screen animation
└── games/
    ├── hangman/            # เกม Hangman
    │   ├── hangman.html
    │   ├── hangman.css
    │   └── hangman.js

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

## หมายเหตุ

> Game state เก็บใน memory — รีเซ็ตเมื่อ restart server  
> แต่ละเกมมี CSS แยกกันอิสระ ทีมสามารถแก้สไตล์ได้โดยไม่กระทบกัน
