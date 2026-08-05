# Project Plan

## AI-Assisted Hangman Game

**Course:** Script Programming

**Project Type:** Mini Project

**Development Period:** Week 1 - Week 5

---

# 1. Project Overview

โครงงานนี้มีวัตถุประสงค์เพื่อพัฒนาเว็บเกม Hangman โดยใช้ภาษา Python และ Framework Flask เป็นส่วน Backend และใช้ HTML, CSS และ JavaScript สำหรับ Frontend

นอกจากการสร้างเกม Hangman แบบปกติ (Classic Mode) แล้ว ยังได้เพิ่ม AI Recommendation เพื่อช่วยแนะนำตัวอักษรที่ควรเดา รวมถึงโหมด VS AI ที่ให้ผู้เล่นแข่งขันกับ AI

โครงงานนี้เป็นการนำองค์ความรู้จากรายวิชา Script Programming มาประยุกต์ใช้กับการพัฒนา Web Application และ Machine Learning เบื้องต้น

---

# 2. Objectives

## Functional Objectives

- พัฒนาเกม Hangman บนเว็บ
- รองรับหลายหมวดคำศัพท์
- รองรับ Classic Mode
- รองรับ AI Assist Mode
- รองรับ VS AI Mode
- พัฒนา REST API สำหรับเกม
- พัฒนา Machine Learning สำหรับแนะนำตัวอักษร

## Learning Objectives

ผู้จัดทำต้องการประยุกต์ใช้ความรู้จากรายวิชา ได้แก่

- Variables
- Data Types
- Operators
- Control Flow
- Loop
- Lists
- Tuples
- Dictionaries
- Sets
- Functions
- Modules
- Flask
- External Libraries

---

# 3. Project Scope

## In Scope

- เกม Hangman
- Web Interface
- REST API
- AI Recommendation
- Machine Learning
- Documentation

## Out of Scope

- Database
- User Login
- Online Multiplayer
- Cloud Deployment
- Deep Learning

---

# 4. Technology Stack

Backend

- Python
- Flask

Frontend

- HTML
- CSS
- JavaScript

Machine Learning

- scikit-learn
- pandas
- joblib

Version Control

- Git
- GitHub

---

# 5. System Architecture

```
User
    │
    ▼
Browser
    │
HTML / CSS / JavaScript
    │
Flask Backend
    │
 ├── Game Logic
 ├── REST API
 ├── AI Predictor
 └── Dataset
```

---

# 6. Development Methodology

โครงงานใช้รูปแบบ Incremental Development โดยแบ่งการพัฒนาออกเป็นหลายส่วน และเพิ่มความสามารถของระบบทีละขั้นตอน

ลำดับการพัฒนา

1. ศึกษาเกม Hangman
2. ออกแบบ Logic
3. พัฒนา Game Engine
4. พัฒนา REST API
5. พัฒนา Frontend
6. สร้าง Dataset
7. Train Machine Learning
8. เชื่อม AI เข้ากับเกม
9. ทดสอบระบบ
10. จัดทำเอกสาร

---

# 7. Weekly Development Plan

## Week 1

### หัวข้อที่เรียน

- Introduction to Python
- Variables
- Data Types
- Operators
- Input / Output

### เป้าหมาย

ศึกษากติกาเกม Hangman และออกแบบโครงสร้างโปรแกรม

### แผนงาน

- ศึกษา Gameplay ของ Hangman
- วิเคราะห์ Requirement
- ออกแบบ pseudocode
- ออกแบบโครงสร้างเกม
- สร้าง WORDS Dictionary
- ทดลองใช้ random.choice()
- ทดลองใช้ set()
- ออกแบบการตรวจชนะด้วย all()
- เพิ่ม Input Validation
- กำหนด MAX_WRONG = 6

### ผลลัพธ์ที่คาดหวัง

- ได้ Game Logic
- ได้ข้อมูลคำศัพท์
- ได้โครงสร้างหลักของเกม

---

## Week 2

### หัวข้อที่เรียน

- if
- elif
- else
- Boolean Expression

### เป้าหมาย

พัฒนา Backend ของเกม

### แผนงาน

- สร้าง Flask Project
- สร้าง Blueprint
- สร้าง API New Game
- สร้าง API Guess
- พัฒนา HTML
- พัฒนา CSS
- พัฒนา JavaScript
- เชื่อม API กับ Frontend
- จัดการ Static Files

### ผลลัพธ์ที่คาดหวัง

- เกมสามารถเล่นผ่านเว็บได้
- Frontend ติดต่อ Backend ได้

---

## Week 3

### หัวข้อที่เรียน

- Loop
- for
- while
- break
- continue

### เป้าหมาย

ปรับโครงสร้างโปรเจกต์ให้รองรับหลายเกม

### แผนงาน

- Refactor Project
- แยกโฟลเดอร์ Hangman
- ปรับ README
- สร้าง words.txt
- เตรียม Dataset

### ผลลัพธ์ที่คาดหวัง

- โครงสร้างโปรเจกต์เป็นระเบียบ
- รองรับการเพิ่มเกมใหม่

---

## Week 4

### หัวข้อที่เรียน

- Lists
- Tuples

### เป้าหมาย

สร้าง Machine Learning Dataset

### แผนงาน

- สร้าง make_dataset.py
- สร้าง hangman_dataset.csv
- Train Decision Tree
- Train Logistic Regression
- Train Naive Bayes
- เปรียบเทียบ Accuracy

### ผลลัพธ์ที่คาดหวัง

- ได้โมเดล Machine Learning
- เลือกโมเดลที่ดีที่สุด

---

## Week 5

### หัวข้อที่เรียน

- Dictionary
- Set
- Functions
- Modules

### เป้าหมาย

เชื่อม AI เข้ากับเกม

### แผนงาน

- พัฒนา predict.py
- โหลดโมเดล .pkl
- พัฒนา AI Assist
- พัฒนา VS AI
- สร้าง AI API
- พัฒนา AI Interface
- แก้ไข Bug
- จัดทำ Documentation
- จัดทำ Test Case
- จัดทำ Learning Log

### ผลลัพธ์ที่คาดหวัง

- ระบบ AI ทำงานได้
- เกมสมบูรณ์พร้อมส่ง

---

# 8. Mapping with Course Contents

| Course Topic | Applied in Project |
|--------------|-------------------|
| Variables | lives, score, word |
| Data Types | String, Integer, Boolean |
| List | WORDS |
| Dictionary | WORDS Categories |
| Set | guessed letters |
| Conditional | ตรวจคำตอบ |
| Loop | Game Loop |
| Function | api_guess(), predict() |
| Module | hangman.py, predict.py |
| Flask | REST API |
| Pandas | Dataset |
| Scikit-learn | Machine Learning |

---

# 9. Risk Assessment

| Risk | Impact | Solution |
|------|--------|----------|
| Dataset มีน้อย | AI Accuracy ต่ำ | เพิ่มจำนวนคำศัพท์ |
| Route Error | ระบบใช้งานไม่ได้ | แยก Blueprint |
| Input ผิดรูปแบบ | โปรแกรม Error | Input Validation |
| UI Bug | ผู้ใช้ใช้งานยาก | User Testing |
| AI ทายผิด | ประสิทธิภาพลดลง | เปรียบเทียบหลายโมเดล |

---

# 10. Testing Plan

ทดสอบ

- เริ่มเกมใหม่
- เดาถูก
- เดาผิด
- เดาซ้ำ
- Input ไม่ถูกต้อง
- ชนะ
- แพ้
- AI Assist
- VS AI
- REST API

---

# 11. Expected Deliverables

- Source Code
- GitHub Repository
- README.md
- Plan.md
- WorkTracking.md
- CHANGELOG.md
- TEST.md
- LEARNINGLOG.md
- AI Documentation
- Trained Machine Learning Model

---

# 12. Expected Outcomes

เมื่อสิ้นสุดโครงงาน ผู้จัดทำคาดว่าจะสามารถพัฒนาเกม Hangman ที่ทำงานผ่านเว็บได้อย่างสมบูรณ์ พร้อมระบบ AI Recommendation ที่ช่วยแนะนำตัวอักษรสำหรับผู้เล่น อีกทั้งยังสามารถประยุกต์ใช้ความรู้จากรายวิชา Script Programming ทั้งในด้านการเขียนโปรแกรม การจัดการโครงสร้างโปรเจกต์ การใช้ Flask และการนำ Machine Learning มาใช้ในงานจริงได้