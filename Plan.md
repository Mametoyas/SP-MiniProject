# Project Plan
## Script Programming Mini Project
### AI-Assisted Hangman Game

---

# 1. Project Objective

พัฒนาเว็บเกม Hangman ด้วยภาษา Python และ Flask พร้อมเพิ่มระบบ AI
เพื่อช่วยแนะนำตัวอักษรที่ควรเดา และเปรียบเทียบประสิทธิภาพของโมเดล Machine Learning

---

# 2. Project Scope

ระบบประกอบด้วย

- หน้าเว็บไซต์ (Frontend)
- ระบบเกม Hangman
- ระบบ AI Recommendation
- ระบบจัดการคำศัพท์
- ระบบเปรียบเทียบโมเดล Machine Learning

---

# 3. Development Plan

| Week | Task | Status |
|------|------|--------|
| Week 1 | ศึกษาความต้องการและออกแบบระบบ | ✅ |
| Week 1 | ออกแบบโครงสร้างโปรเจกต์ | ✅ |
| Week 2 | พัฒนาเกม Hangman | ✅ |
| Week 2 | ออกแบบหน้าตาเว็บไซต์ | ✅ |
| Week 3 | สร้าง Dataset สำหรับ AI | ✅ |
| Week 3 | Train Machine Learning Models | ✅ |
| Week 4 | เชื่อม AI กับเกม | ✅ |
| Week 4 | ทดสอบระบบ | ✅ |
| Week 5 | แก้ไข Bug และปรับปรุง UI | ✅ |
| Week 5 | จัดทำเอกสารและนำเสนอ | ✅ |

---

# 4. System Architecture

```
User
   │
   ▼
Frontend (HTML/CSS/JS)
   │
Flask Backend
   │
   ├── Hangman Engine
   ├── Word Dataset
   ├── AI Predictor
   └── Machine Learning Model
```

---

# 5. Technology Stack

Backend
- Python
- Flask

Frontend
- HTML
- CSS
- JavaScript

Machine Learning
- Scikit-learn
- Pandas
- Joblib

---

# 6. Risk Management

| Risk | Solution |
|------|----------|
| AI Accuracy ต่ำ | ทดลองหลายโมเดล |
| Dataset ไม่เพียงพอ | เพิ่มจำนวนคำศัพท์ |
| Bug ระหว่างเชื่อมระบบ | แยกทดสอบแต่ละ Module |
| UI ใช้งานยาก | ปรับปรุงตามผลการทดสอบ |

---

# 7. Expected Result

- ผู้ใช้สามารถเล่น Hangman ผ่านเว็บไซต์ได้
- AI สามารถแนะนำตัวอักษรที่ควรเดาได้
- ระบบสามารถเปรียบเทียบ Machine Learning ได้
- ผู้ใช้สามารถเล่นได้ทั้ง Classic และ AI Mode