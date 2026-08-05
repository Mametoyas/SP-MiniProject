# Work Tracking

## AI-Assisted Hangman Game

**Course:** Script Programming  
**Project Type:** Mini Project  
**Development Period:** 2 Weeks

---

# 1. Project Team

| ID  |Member   | Responsibility |
|-----|---------|----------------|
| 663380518-4 | นายจักรพรรดิ์ มั่งกูล    | Coder (โค้ด) |
| 663380305-1 | นายเชิดตระกูล แข็งขัน  | Coder (โค้ด) |
| 663380282-7 | นายพงษกร มานาดี    | Debugger (แก้บั๊ก) |
| 653380198-5 | นางสาวทักษพร มูลมณี | Planner (วางแผน) |

---

# 2. Working Process

การดำเนินโครงงานแบ่งออกเป็น 2 ระยะ ได้แก่ การพัฒนาเกม Hangman ให้สามารถใช้งานได้ และการเพิ่มระบบ AI พร้อมทดสอบและจัดทำเอกสาร โดยใช้ GitHub ในการติดตามความคืบหน้าและบันทึกการเปลี่ยนแปลงของโครงงาน

---

# Week 1 : Hangman Core Development

## เป้าหมาย

พัฒนาเกม Hangman ให้สามารถเล่นผ่านเว็บได้ พร้อมวางโครงสร้างของระบบ

## งานที่ดำเนินการ

| Task | Status |
|------|--------|
| ศึกษากติกาเกม Hangman | ✅ |
| วิเคราะห์ Requirement | ✅ |
| ออกแบบ Pseudocode | ✅ |
| สร้างคลังคำศัพท์ (WORDS) | ✅ |
| พัฒนา Game Logic | ✅ |
| ตรวจสอบการเดาซ้ำและการชนะ/แพ้ | ✅ |
| สร้าง API สำหรับ New Game และ Guess | ✅ |
| พัฒนา Frontend (HTML/CSS/JavaScript) | ✅ |
| เชื่อม Frontend กับ Backend | ✅ |
| ปรับโครงสร้างโปรเจกต์และ README | ✅ |

### Meeting Summary

- สรุปโครงสร้างของระบบ
- แบ่งหน้าที่สมาชิก
- ทดสอบการทำงานของเกม Hangman
- แก้ไขข้อผิดพลาดของระบบ

### ปัญหาที่พบ

- การตรวจสอบการเดาซ้ำ
- การจัดการ Route และ Static Files

### วิธีแก้ไข

- ใช้ `set()` เก็บตัวอักษรที่เดา
- ปรับโครงสร้าง Route และ Static Files

---

# Week 2 : AI Integration & Project Completion

## เป้าหมาย

เพิ่มระบบ AI Recommendation พร้อมทดสอบและจัดทำเอกสารโครงงาน

## งานที่ดำเนินการ

| Task | Status |
|------|--------|
| สร้าง Dataset | ✅ |
| พัฒนา make_dataset.py | ✅ |
| Train Machine Learning Models | ✅ |
| เปรียบเทียบผลโมเดล | ✅ |
| พัฒนา predict.py | ✅ |
| เพิ่ม AI Assist Mode | ✅ |
| เพิ่ม VS AI Mode | ✅ |
| พัฒนา AI API | ✅ |
| ปรับปรุง UI และแก้ไข Bug | ✅ |
| จัดทำ Documentation | ✅ |
| จัดทำ TEST.md | ✅ |
| จัดทำ LEARNINGLOG.md | ✅ |
| จัดทำ CHANGELOG.md | ✅ |

### Meeting Summary

- ทดสอบ AI Recommendation
- ทดสอบระบบทั้งหมด
- ตรวจสอบความถูกต้องของเอกสาร
- เตรียมโครงงานสำหรับนำเสนอ

### ปัญหาที่พบ

- AI แนะนำตัวอักษรซ้ำ
- UI ไม่อัปเดตบางสถานะ
- ผู้เล่นสามารถกดปุ่มหลังเกมจบ

### วิธีแก้ไข

- เพิ่ม Fallback Logic
- ปรับปรุง JavaScript
- ปิดการใช้งานปุ่มเมื่อเกมสิ้นสุด

---

# 3. GitHub Progress

| Week | Progress |
|------|----------|
| Week 1 | พัฒนาเกม Hangman และ Web Interface |
| Week 2 | เพิ่ม AI, ทดสอบระบบ และจัดทำเอกสาร |

---

# 4. AI Usage Summary

| Activity | Purpose |
|----------|---------|
| อธิบายกติกา Hangman | ออกแบบเกม |
| ออกแบบ Pseudocode | วาง Logic |
| อธิบายโครงสร้างข้อมูล | พัฒนา Game Logic |
| อธิบาย Machine Learning | สร้างและเลือกโมเดล |
| ช่วยตรวจสอบ Bug | ปรับปรุงระบบ |
| ช่วยจัดทำ Documentation | สรุปและอธิบายโครงงาน |

---

# 5. Issue Tracking

| Issue | Solution | Status |
|------|----------|--------|
| Input Validation | เพิ่มการตรวจสอบข้อมูล | ✅ |
| Duplicate Guess | ใช้ Set | ✅ |
| Static File Error | ปรับ Route | ✅ |
| AI Prediction | เพิ่ม Fallback | ✅ |
| UI Bug | ปรับ JavaScript | ✅ |

---

# 6. Testing Progress

| Module | Status |
|---------|--------|
| Hangman Game | ✅ |
| REST API | ✅ |
| AI Assist | ✅ |
| VS AI | ✅ |
| Machine Learning | ✅ |
| Documentation | ✅ |

---

# 7. Final Project Status

**Project Completion : 100%**

- ✅ Hangman Game
- ✅ Web Interface
- ✅ REST API
- ✅ Machine Learning
- ✅ AI Assist
- ✅ VS AI
- ✅ Testing
- ✅ Documentation
- ✅ GitHub Repository