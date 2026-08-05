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

- Variables, Data Types, Operators
- Control Flow, Loop
- Lists, Tuples, Dictionaries, Sets
- Functions, Modules
- Flask, External Libraries

---

# 3. Project Scope

## In Scope

- เกม Hangman (Classic, AI Assist, VS AI)
- Web Interface
- REST API
- AI Recommendation ด้วย Decision Tree
- Documentation

---

# 4. Technology Stack

| ส่วน | เทคโนโลยี |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | scikit-learn, pandas, joblib |
| Version Control | Git, GitHub |

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

1. เลือกหัวข้อและศึกษาเกม Hangman
2. ออกแบบ Logic และวาง pseudocode
3. ทำ draft Classic Mode
4. พัฒนา Flask Backend และ REST API
5. พัฒนา Frontend และเชื่อม API
6. Refactor โครงสร้างโปรเจกต์
7. สร้าง Dataset และเทรนโมเดล AI
8. เชื่อม AI เข้ากับเกม (AI Assist, VS AI)
9. ทดสอบและแก้ไข Bug
10. จัดทำเอกสาร

---

# 7. Weekly Development Plan

| สัปดาห์ | วันที่ | เป้าหมาย | แผนงาน |
|---|---|---|---|
| Week 1 | 19 ก.ค. 2568 (เช้า) | ศึกษาและออกแบบเกม | เลือกหัวข้อ Hangman, ถาม AI เรื่องกติกา, วาง pseudocode, ออกแบบ logic เกม, ทำ draft Classic Mode ด้วย Python fundamentals |
| Week 1 | 19 ก.ค. 2568 (บ่าย) | พัฒนา Flask Backend และ Classic Mode UI | สร้าง Flask app และ Blueprint, เพิ่ม API `/new` และ `/guess`, สร้างหน้า Menu และ Classic Mode UI, เชื่อม Frontend กับ API |
| Week 1 | 21 ก.ค. 2568 | Refactor โครงสร้างโปรเจกต์ | ย้าย Hangman ไปโฟลเดอร์เฉพาะเกม, ปรับ README แ1ละข้อมูลสมาชิก |
| Week 2 | 23 ก.ค. 2568 | สร้าง Dataset และเทรนโมเดล AI | สร้างคลังคำศัพท์, เขียน make_dataset.py, เทรน Decision Tree / Logistic Regression / Naive Bayes, เปรียบเทียบและเลือกโมเดล |
| Week 2 | 24 ก.ค. 2568 | เชื่อม AI เข้ากับเกม และจัดทำเอกสาร | เขียน predict.py, เพิ่ม AI Assist และ VS AI mode, สร้าง AI API และ UI, แก้ไข Bug, จัดทำ docs, TEST.md, LEARNINGLOG.md |

---

# 8. Mapping with Course Contents

| Course Topic | Applied in Project |
|---|---|
| Variables | `word`, `wrong_count`, `MAX_WRONG` |
| Data Types | String, Integer, Boolean, List, Dict, Set |
| List | คำศัพท์ในแต่ละหมวด |
| Dictionary | `WORDS` จัดหมวดคำศัพท์ |
| Set | `guessed` เก็บตัวอักษรที่เดาแล้ว |
| Conditional | ตรวจคำตอบถูก/ผิด ชนะ/แพ้ |
| Loop | Game loop, วนตรวจ pattern |
| Function | `_new()`, `api_guess()`, `predict()` |
| Module | `hangman.py`, `predict.py`, `random`, `joblib` |
| Flask | REST API, Blueprint, `send_from_directory()` |
| pandas | สร้างและจัดการ Dataset |
| scikit-learn | เทรนและใช้งานโมเดล ML |

---

# 9. Risk Assessment

| Risk | Impact | Solution |
|---|---|---|
| Dataset มีน้อย | AI Accuracy ต่ำ | เพิ่มจำนวนคำศัพท์ |
| Route Error | ระบบใช้งานไม่ได้ | แยก Blueprint |
| Input ผิดรูปแบบ | โปรแกรม Error | Input Validation |
| UI Bug | ผู้ใช้ใช้งานยาก | User Testing |
| AI ทายผิดหรือซ้ำ | ประสิทธิภาพลดลง | เปรียบเทียบหลายโมเดล + fallback logic |

---

# 10. Testing Plan

| กรณีทดสอบ | ผลที่คาดหวัง |
|---|---|
| เริ่มเกมใหม่ | คืน game state พร้อม masked word |
| เดาถูก | ตัวอักษรปรากฏในคำ |
| เดาผิด | `wrong_count` เพิ่มขึ้น 1 |
| เดาซ้ำ | คืน `already_guessed` ไม่เปลี่ยน state |
| Input ไม่ถูกต้อง | คืน error 400 |
| ชนะ | `status = "win"` เมื่อเปิดครบทุกตัว |
| แพ้ | `status = "lose"` เมื่อ `wrong_count >= 6` |
| AI Assist | คืน hints top-5 ตัวอักษร |
| VS AI | AI เดาสลับกับผู้เล่น ตรวจสถานะทั้งสองฝ่าย |

---

# 11. Expected Deliverables

- Source Code (GitHub Repository)
- README.md
- Plan.md
- CHANGELOG.md
- TEST.md
- LEARNINGLOG.md
- docs/ (QUICKSTART, GAMEPLAY, HANGMAN_AI)
- Trained Machine Learning Model (.pkl)

---

# 12. Expected Outcomes

เมื่อสิ้นสุดโครงงาน ผู้จัดทำคาดว่าจะสามารถพัฒนาเกม Hangman ที่ทำงานผ่านเว็บได้อย่างสมบูรณ์ พร้อมระบบ AI Recommendation ที่ช่วยแนะนำตัวอักษรสำหรับผู้เล่น อีกทั้งยังสามารถประยุกต์ใช้ความรู้จากรายวิชา Script Programming ทั้งในด้านการเขียนโปรแกรม การจัดการโครงสร้างโปรเจกต์ การใช้ Flask และการนำ Machine Learning มาใช้ในงานจริงได้

← [กลับหน้าโครงการ](README.md)
