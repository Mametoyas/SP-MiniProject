# Mini Game Hub

เว็บรวมเกมมินิ สไตล์ retro pixel art สร้างด้วย Python Flask + HTML/CSS/JS

---

## โครงสร้างโปรเจกต์

```
MiniProject/
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
    ├── number_guess/       # เกม Number Guess
    │   ├── number_guess.html
    │   ├── number_guess.css
    │   └── number_guess.js
    └── word_scramble/      # เกม Word Scramble
        ├── word_scramble.html
        ├── word_scramble.css
        └── word_scramble.js
```

---

## วิธีติดตั้งและรัน

### 1. ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

### 2. รัน Flask server

```bash
python app.py
```

### 3. เปิดเบราว์เซอร์

```
http://localhost:5000
```

---

## 🕹️ เกมที่มี

### ☠️ Hangman — Game Boy Edition
> สไตล์ Game Boy สีเขียวพิกเซล

**วิธีเล่น:**
- กด **PLAY** ที่หน้า Menu เพื่อเข้าเกม
- เดาตัวอักษรทีละตัวโดยกดปุ่มบน keyboard บนหน้าจอ
- มีชีวิต **6 ครั้ง** — เดาผิดแต่ละครั้งจะวาดร่างคนแขวนคอเพิ่มขึ้น
- เดาถูกทุกตัวก่อนหมดชีวิต = **ชนะ!**

**หมวดคำ:** สัตว์ / ผลไม้ / ประเทศ (สุ่มอัตโนมัติ)

**API:**
| Method | Endpoint | คำอธิบาย |
|--------|----------|-----------|
| POST | `/api/hangman/new` | เริ่มเกมใหม่ |
| POST | `/api/hangman/guess` | ส่งตัวอักษรที่เดา `{ "letter": "a" }` |

---

### 🔢 Number Guess *(Coming Soon)*
> ทายตัวเลขที่ซ่อนอยู่ระหว่าง 1–100

**วิธีเล่น:**
- กดตัวเลขบน numpad แล้วกด **GUESS**
- ระบบจะบอกว่าตัวเลขที่ทายสูงหรือต่ำกว่าคำตอบ
- มีโอกาสทาย **10 ครั้ง**

**API:**
| Method | Endpoint | คำอธิบาย |
|--------|----------|-----------|
| POST | `/api/number-guess/new` | เริ่มเกมใหม่ |
| POST | `/api/number-guess/guess` | ส่งตัวเลข `{ "number": 42 }` |

---

### 🔤 Word Scramble *(Coming Soon)*
> เรียงตัวอักษรที่สับเปลี่ยนให้เป็นคำที่ถูกต้อง

**วิธีเล่น:**
- ดูคำที่ถูกสับตัวอักษร แล้วพิมพ์คำที่ถูกต้องลงในช่อง
- มีเวลา **30 วินาที** ต่อรอบ
- กด **HINT** เพื่อเปิดเผยตัวอักษรแรก (เสียเวลา 5 วินาที)

**API:**
| Method | Endpoint | คำอธิบาย |
|--------|----------|-----------|
| POST | `/api/word-scramble/new` | เริ่มเกมใหม่ |
| POST | `/api/word-scramble/guess` | ส่งคำตอบ `{ "word": "elephant" }` |
| POST | `/api/word-scramble/hint` | ขอ hint |
| POST | `/api/word-scramble/timeout` | แจ้งหมดเวลา |

---

## 🛠️ Tech Stack

| ส่วน | เทคโนโลยี |
|------|-----------|
| Backend | Python 3, Flask |
| Frontend | HTML5, CSS3, Vanilla JS |
| Font | Press Start 2P (Google Fonts) |
| State | In-memory dict (server-side) |

---

## 📝 หมายเหตุ

- Game state เก็บใน memory — รีเซ็ตเมื่อ restart server
- แต่ละเกมมี CSS แยกกันอิสระ ทีมสามารถแก้สไตล์ได้โดยไม่กระทบกัน
