# Work Tracking

## AI-Assisted Hangman Game

**Course:** Script Programming  
**Project Type:** Mini Project  
**Development Period:** Week 1 - Week 5

---

# 1. Project Team

| Member | Responsibility |
|---------|----------------|
| Member A | Project Management, Flask Backend |
| Member B | Frontend Development (HTML/CSS/JavaScript) |
| Member C | Machine Learning & Dataset |
| Member D | Testing, Documentation & GitHub |

---

# 2. Working Process

ทีมใช้การพัฒนาแบบ Incremental Development โดยแบ่งการทำงานเป็นหลายช่วงตามบทเรียนในรายวิชา Script Programming และเพิ่มความสามารถของระบบทีละส่วน

การติดตามงานแบ่งออกเป็น

- วางแผนก่อนเริ่มพัฒนา
- ประชุมสรุปงานประจำสัปดาห์
- พัฒนาและ Commit ลง GitHub
- ทดสอบระบบ
- แก้ไขปัญหา
- จัดทำเอกสารประกอบ

---

# Week 1

## หัวข้อที่เรียน

- Python Basics
- Variables
- Data Types
- Operators
- Input / Output

## เป้าหมาย

ศึกษากติกาเกม Hangman และออกแบบ Logic ของระบบ

## งานที่ดำเนินการ

| Task | Member | Status |
|------|--------|--------|
| ศึกษากติกาเกม Hangman | A | ✅ |
| วิเคราะห์ Requirement | A | ✅ |
| ออกแบบ Pseudocode | A, B | ✅ |
| สร้าง WORDS Dictionary | B | ✅ |
| ทดลองใช้ random.choice() | B | ✅ |
| ทดลองใช้ set() | C | ✅ |
| เพิ่ม all() ตรวจชนะ | A | ✅ |
| เพิ่ม Input Validation | C | ✅ |
| กำหนด MAX_WRONG | A | ✅ |

### Meeting Summary

**วันที่:** 19 กรกฎาคม

หัวข้อ

- เลือกหัวข้อโครงงาน
- วิเคราะห์เกม Hangman
- แบ่งหน้าที่สมาชิก

มติ

- ใช้ Flask
- ใช้ GitHub
- เตรียมรองรับ AI ในอนาคต

### ปัญหาที่พบ

- ยังไม่เข้าใจ Logic การตรวจชนะ
- ยังไม่แน่ใจว่าจะเก็บข้อมูลตัวอักษรแบบใด

### วิธีแก้ไข

- ศึกษาเอกสาร Python
- ใช้ AI อธิบายการใช้ set() และ all()

---

# Week 2

## หัวข้อที่เรียน

- Conditionals
- if
- elif
- else

## เป้าหมาย

พัฒนา Backend และเชื่อม Frontend

## งานที่ดำเนินการ

| Task | Member | Status |
|------|--------|--------|
| สร้าง Flask Project | A | ✅ |
| สร้าง Blueprint | A | ✅ |
| API New Game | A | ✅ |
| API Guess | A | ✅ |
| HTML Menu | B | ✅ |
| Hangman UI | B | ✅ |
| CSS | B | ✅ |
| JavaScript | B | ✅ |
| Static Route | C | ✅ |

### Meeting Summary

หัวข้อ

- Review Backend
- ทดสอบ API

ผลการประชุม

Backend สามารถเชื่อมกับ Frontend ได้สำเร็จ

### ปัญหาที่พบ

- Route ไม่ถูกต้อง
- Static File โหลดไม่ได้

### วิธีแก้ไข

- แยก Blueprint
- ใช้ send_from_directory()

---

# Week 3

## หัวข้อที่เรียน

- Loop
- for
- while

## เป้าหมาย

ปรับโครงสร้างโปรเจกต์และเตรียม Dataset

## งานที่ดำเนินการ

| Task | Member | Status |
|------|--------|--------|
| Refactor Project | A | ✅ |
| ย้าย Hangman | A | ✅ |
| ปรับ README | D | ✅ |
| สร้าง words.txt | C | ✅ |
| เตรียม Dataset | C | ✅ |

### Meeting Summary

หัวข้อ

- Review Folder Structure
- ตรวจสอบ Dataset

ผลการประชุม

ปรับโครงสร้างให้รองรับหลายเกม

### ปัญหาที่พบ

- โฟลเดอร์เริ่มซับซ้อน
- Dataset ยังมีคำศัพท์น้อย

### วิธีแก้ไข

- แยกโฟลเดอร์ตามเกม
- เพิ่มหมวดคำศัพท์

---

# Week 4

## หัวข้อที่เรียน

- Lists
- Tuples

## เป้าหมาย

สร้าง Machine Learning Pipeline

## งานที่ดำเนินการ

| Task | Member | Status |
|------|--------|--------|
| make_dataset.py | C | ✅ |
| สร้าง Dataset | C | ✅ |
| Train Decision Tree | C | ✅ |
| Train Logistic Regression | C | ✅ |
| Train Naive Bayes | C | ✅ |
| เปรียบเทียบผลโมเดล | C | ✅ |

### Meeting Summary

หัวข้อ

- วิเคราะห์ผล Machine Learning

ผลการประชุม

เลือกใช้ Decision Tree

### ปัญหาที่พบ

- Accuracy ของแต่ละโมเดลแตกต่างกัน
- Feature ยังไม่เพียงพอ

### วิธีแก้ไข

- เพิ่ม candidate_count
- เพิ่ม revealed
- ปรับ Feature Engineering

---

# Week 5

## หัวข้อที่เรียน

- Dictionary
- Set
- Functions
- Modules

## เป้าหมาย

เชื่อม AI เข้ากับเกมและจัดทำเอกสาร

## งานที่ดำเนินการ

| Task | Member | Status |
|------|--------|--------|
| predict.py | C | ✅ |
| AI Assist | A | ✅ |
| VS AI | A | ✅ |
| AI API | A | ✅ |
| AI Frontend | B | ✅ |
| Bug Fix | A, B | ✅ |
| Documentation | D | ✅ |
| TEST.md | D | ✅ |
| LEARNINGLOG.md | D | ✅ |
| requirements.txt | D | ✅ |

### Meeting Summary

หัวข้อ

- Integration Test
- User Testing
- Final Review

ผลการประชุม

ระบบทำงานครบทุกฟังก์ชัน

### ปัญหาที่พบ

- AI แนะนำตัวอักษรซ้ำ
- ปุ่มกดค้าง
- สถานะเกมไม่อัปเดต

### วิธีแก้ไข

- เพิ่ม fallback ใน predict()
- Disable Button หลังเกมจบ
- ปรับปรุง JavaScript State

---

# 3. GitHub Progress

| Week | Commit Summary |
|------|----------------|
| Week 1 | Initial Project Setup |
| Week 2 | Implement Hangman Backend |
| Week 3 | Refactor Project Structure |
| Week 4 | Add Machine Learning Models |
| Week 5 | Integrate AI and Complete Documentation |

---

# 4. AI Usage Summary

| Activity | Purpose |
|----------|---------|
| อธิบายกติกา Hangman | วิเคราะห์ Requirement |
| ออกแบบ Pseudocode | วาง Logic |
| อธิบาย random.choice() | สุ่มคำศัพท์ |
| อธิบาย set() | ป้องกันการเดาซ้ำ |
| อธิบาย all() | ตรวจสอบการชนะ |
| อธิบาย Flask Blueprint | แยก Route |
| อธิบาย REST API | สร้าง Endpoint |
| อธิบาย Machine Learning | Train Model |
| อธิบาย Joblib | โหลดโมเดล |
| อธิบาย Testing | สร้าง Test Case |

---

# 5. Issue Tracking

| Issue | Cause | Solution | Status |
|------|-------|----------|--------|
| Route Error | Blueprint | แก้ URL Mapping | ✅ |
| Static File Error | Path ไม่ถูกต้อง | send_from_directory() | ✅ |
| Input Validation | รับข้อมูลผิด | ตรวจสอบ isalpha() | ✅ |
| Duplicate Guess | ใช้ List | เปลี่ยนเป็น Set | ✅ |
| AI Prediction ซ้ำ | Model Output | เพิ่ม Fallback | ✅ |
| UI ไม่อัปเดต | JavaScript State | Refactor Logic | ✅ |

---

# 6. Testing Progress

| Module | Status |
|---------|--------|
| New Game | ✅ |
| Guess Letter | ✅ |
| Win Condition | ✅ |
| Lose Condition | ✅ |
| Input Validation | ✅ |
| AI Assist | ✅ |
| VS AI | ✅ |
| REST API | ✅ |
| Dataset Generation | ✅ |
| Model Prediction | ✅ |

---

# 7. Final Project Status

| Module | Progress |
|---------|----------|
| Backend | 100% |
| Frontend | 100% |
| Game Logic | 100% |
| Machine Learning | 100% |
| API | 100% |
| Testing | 100% |
| Documentation | 100% |

---

# 8. Lessons Learned

ตลอดการพัฒนาโครงงาน สมาชิกในทีมได้นำความรู้จากรายวิชา Script Programming มาประยุกต์ใช้จริง ตั้งแต่การออกแบบโครงสร้างโปรแกรม การใช้ตัวแปร การควบคุมการทำงานด้วยเงื่อนไขและลูป การจัดเก็บข้อมูลด้วย List, Dictionary และ Set การแบ่งโปรแกรมออกเป็น Function และ Module ตลอดจนการใช้ Flask เพื่อพัฒนา Web Application และการนำ Machine Learning มาประยุกต์ใช้ในการแนะนำตัวอักษรภายในเกม

การใช้ GitHub และ CHANGELOG ทำให้สามารถติดตามความคืบหน้าของโครงการได้อย่างเป็นระบบ ขณะที่การใช้ AI เป็นผู้ช่วยในการอธิบายแนวคิด การตรวจสอบโค้ด และเสนอแนวทางแก้ไขปัญหา ช่วยให้ทีมสามารถพัฒนาโครงงานได้อย่างมีประสิทธิภาพ โดยสมาชิกทุกคนยังคงเป็นผู้วิเคราะห์ ตัดสินใจ และทดสอบระบบด้วยตนเองก่อนนำไปใช้งานจริง

---

# 9. Overall Progress

**Project Completion : 100%**

- ✅ Game Engine
- ✅ Flask Backend
- ✅ REST API
- ✅ Frontend
- ✅ Machine Learning
- ✅ AI Assist
- ✅ VS AI
- ✅ Testing
- ✅ Documentation
- ✅ GitHub Repository