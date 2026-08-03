# Learning Log — AI Chat History

## Prompt 1 — AI Ethics, Explainable AI and Responsible AI

**Prompt ของอาจารย์**

> As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind.

**คำตอบที่นำมาใช้กับโครงงาน**

สำหรับเกม Hangman กลุ่มเลือกใช้ Machine Learning แบบขนาดเล็กและข้อมูลคำศัพท์ภายในโปรเจกต์ แทนการพึ่งพา LLM หรือบริการภายนอก เพราะอธิบายกระบวนการทำงาน ตรวจสอบข้อมูล และรันซ้ำได้ง่ายกว่า เหมาะกับผู้เริ่มต้นที่ต้องการเข้าใจว่า AI สร้างคำแนะนำอย่างไร

- **AI ethics:** ใช้ `datasets/words.txt` ซึ่งเป็นคลังคำศัพท์สำหรับเกม หลีกเลี่ยงข้อมูลส่วนบุคคล ไม่มีการบันทึกชื่อหรือพฤติกรรมของผู้เล่น และใช้ AI เพื่อช่วยเล่นเกม ไม่ใช่ตัดสินคุณค่าหรือความสามารถของบุคคล
- **Explainable AI:** AI รับข้อมูล 3 ส่วน ได้แก่ pattern ของคำ เช่น `_a__a_`, อักษรที่เดาถูก และอักษรที่เดาผิด จากนั้นกรอง candidate words ที่เข้ากัน นับ/ประเมินตัวอักษรที่ยังเป็นไปได้ แล้วคืนคำแนะนำสูงสุด 5 ตัวอักษร ผู้เล่นยังเป็นผู้ตัดสินใจเลือกคำตอบเองใน AI Assist mode
- **Responsible AI:** คำแนะนำของโมเดลไม่ควรถูกนำเสนอเป็นคำตอบที่ถูกต้องแน่นอน ระบบจึงแสดงเป็น hint และไม่เปิดเผยคำตอบระหว่างเกม นอกจากนี้ `predict()` ตัดอักษรที่เดาแล้วออกด้วย `used = guessed | wrong` เพื่อลดคำแนะนำซ้ำและช่วยให้ผู้ใช้เข้าใจข้อจำกัดของ AI

**หลักฐานในโครงงาน**

| ส่วน | การนำไปใช้ |
|---|---|
| `datasets/words.txt` | แหล่งคำศัพท์ที่ใช้สร้างข้อมูลและเล่นเกม โดยไม่มีข้อมูลส่วนบุคคล |
| `codes/make_dataset.py` | สร้างสถานะเกมจากคำศัพท์อย่างตรวจสอบได้ เช่น pattern, guessed, wrong และ candidate count |
| `codes/predict.py` | แปลงสถานะเกมเป็นคำแนะนำ พร้อมตัดตัวอักษรที่ใช้แล้ว |
| AI Assist | แสดงคำแนะนำให้ผู้เล่น แต่ผู้เล่นเป็นผู้เลือกอักษรที่จะเดา |

## Prompt 2 — Conceive a Python Mini Project

**Prompt ของอาจารย์**

> As a Python beginner, help me to conceive mini projects in Python fundamentals to expand my knowledge and to encounter real-world use cases. Include learning outcomes, traits assessment, and topic.

**คำตอบที่นำมาใช้กับโครงงาน**

กลุ่มเลือกหัวข้อ **Mini Game Hub: Hangman with AI Assistance** เพราะเริ่มต้นจากเกม console ที่มี logic ไม่ซับซ้อน และค่อย ๆ ต่อขยายเป็นเว็บแอปและ AI ได้ ช่วยให้เรียนรู้พื้นฐาน Python ผ่านปัญหาจริงขนาดเล็กแทนการเรียนแนวคิดแยกส่วน

| องค์ประกอบ | การออกแบบสำหรับโครงงาน |
|---|---|
| หัวข้อ | เกม Hangman 3 โหมด: Classic, AI Assist และ VS AI |
| พื้นฐาน Python | ตัวแปร, `str`, `int`, `list`, `set`, `dict`, loop, condition, function, import และ file I/O |
| โจทย์ปัญหา | รับคำเดา ตรวจคำซ้ำ แสดงช่องว่าง นับโอกาสผิด และระบุผลชนะ/แพ้ |
| การประยุกต์ใช้ | สร้าง REST API ด้วย Flask และให้ JavaScript เรียก API เพื่ออัปเดตหน้าเกม |
| การต่อยอด | สร้าง dataset จากคลังคำศัพท์ เทรนโมเดล และนำคำแนะนำ AI กลับมาใช้ในเกม |
| Traits ที่ประเมิน | การวิเคราะห์ปัญหา, การแบ่งงาน, ความรับผิดชอบ, การสื่อสาร, การตรวจสอบข้อผิดพลาด และการใช้ AI อย่างมีวิจารณญาณ |

ตัวอย่างการเลือกใช้โครงสร้างข้อมูลตามหน้าที่จริง:

```python
# dictionary จัดหมวดคำศัพท์ และ list เก็บคำในแต่ละหมวดเพื่อสุ่มคำ
WORDS = {"ANIMALS": ["elephant", "giraffe"], "FRUITS": ["mango", "coconut"]}

# set ใช้เก็บตัวอักษรไม่ซ้ำ และรองรับการหาผลต่าง/ผลรวมของชุดข้อมูล
letters_in_word = set("elephant")
wrong_letters = guessed_letters - letters_in_word
used_letters = guessed_letters | wrong_letters
```

แนวคิดนี้ถูกใช้จริงใน `games/hangman/hangman.py`, `codes/make_dataset.py` และ `codes/predict.py` โดย list เหมาะกับการสุ่ม/เก็บลำดับ ส่วน set เหมาะกับการตัดข้อมูลซ้ำและตรวจ membership อย่างชัดเจน

## Prompt 3 — Why Kanban, WIP and Changelog from the Beginning?

**Prompt ของอาจารย์**

> Why introduce Kanban, WIP, and Changelog since the beginning of Python programming is a good idea for students to use GenAI to grasp teacher materials and make progress rapidly in learning Python along with `learning_log.ipynb` for prompt and response logging?

**คำตอบที่นำมาใช้กับโครงงาน**

การเริ่มใช้ Kanban, WIP limit, Changelog และ Learning Log ตั้งแต่ช่วงต้น ช่วยให้กลุ่มเปลี่ยนการเรียนด้วย GenAI ให้เป็นกระบวนการที่ตรวจสอบได้ ไม่ใช่เพียงรับคำตอบหรือคัดลอกโค้ดจาก AI

| เครื่องมือ | วิธีใช้ในโครงงาน | ประโยชน์ต่อการเรียนรู้ |
|---|---|---|
| Kanban Backlog | แตกงานเป็นการศึกษากติกาเกม, draft Classic mode, แยกโมดูล, สร้าง dataset, เทรนโมเดล, ทำ UI และจัดทำเอกสาร | เห็นลำดับก่อน–หลังและงานคงค้างอย่างชัดเจน |
| WIP (Work in Progress) | ทำงานหลักทีละเรื่อง เช่น ทำ game logic ให้เล่นได้ก่อนเริ่มสร้าง dataset และเทรนโมเดล | ลดการทำหลายส่วนพร้อมกันจนตรวจสอบข้อผิดพลาดไม่ได้ และทำให้ milestone ทดสอบได้จริง |
| Changelog | บันทึกสิ่งที่เปลี่ยน พร้อมไฟล์และผลลัพธ์ใน `CHANGELOG.md` | ทำให้ย้อนดูการพัฒนาและตรวจหลักฐานการทำงานได้ |
| Learning Log | บันทึก prompt ของอาจารย์ คำตอบที่นำมาใช้ และเหตุผลในการปรับใช้กับโครงงาน | ฝึกตั้งคำถามกับ AI, ตรวจสอบคำตอบ และอธิบายการตัดสินใจของตนเองได้ |

หลักการสำคัญคือ **GenAI เป็นผู้ช่วยเสนอแนวทาง ไม่ใช่ผู้ตัดสินคำตอบสุดท้าย** ทุกข้อเสนอถูกตรวจเทียบกับข้อกำหนดเกม โค้ดที่มีอยู่ และผลการทดลองก่อนนำมาใช้

## Prompt 4 — Adjust Kanban Backlogs to the Mini-Project Outline

**Prompt ของอาจารย์**

> Adjust Kanban backlogs according to this outline of the mini project.

**คำตอบที่นำมาใช้กับโครงงาน**

กลุ่มปรับ Kanban ให้แต่ละงานส่งมอบผลลัพธ์ที่ตรวจสอบได้ และเรียงจากพื้นฐาน Python ไปยังเว็บและ AI ดังนี้

| ลำดับ | Kanban item | ผลลัพธ์ที่ตรวจสอบได้ | สถานะ |
|:---:|---|---|:---:|
| 1 | ศึกษาหัวข้อ Hangman และกำหนดกติกา | pseudocode สำหรับสุ่มคำ รับคำเดา ชีวิต 6 ครั้ง และเงื่อนไขชนะ/แพ้ | Done |
| 2 | สร้าง draft เกมแบบไม่มี AI | Classic mode เล่นได้ด้วยคำศัพท์และ game state ใน Python | Done |
| 3 | แยกโมดูลและสร้าง API | `app.py`, Flask Blueprint และ routes ของ Hangman แยกจาก UI | Done |
| 4 | ออกแบบข้อมูลสำหรับ AI | `words.txt` และ `hangman_dataset.csv` มี pattern, guessed, wrong และ candidate count | Done |
| 5 | เทรนและประเมินโมเดล | มี Decision Tree, Logistic Regression, Naive Bayes และผลเปรียบเทียบ | Done |
| 6 | เชื่อมโมเดลเข้ากับเกม | `predict(pattern, guessed, wrong)` ส่งคำแนะนำให้ AI Assist/VS AI | Done |
| 7 | พัฒนาเว็บ UI | มี Menu, Classic, AI Assist, VS AI พร้อม CSS และ JavaScript แยกตามหน้าที่ | Done |
| 8 | ทดสอบและปรับปรุง | ตรวจ flow การเริ่มเกม การเดา และเอกสาร; automated tests เป็นงานต่อยอด | In progress |

Kanban ฉบับสรุปสำหรับติดตามงานอยู่ใน [README.md](README.md#kanban-backlog) ส่วน Changelog บันทึกเหตุการณ์ที่เกิดขึ้นแล้วใน [CHANGELOG.md](CHANGELOG.md)

## Prompt 5 — Execute the Kanban Backlog

**Prompt ของอาจารย์**

> Execute the Kanban backlog.

**คำตอบที่นำมาใช้กับโครงงาน**

กลุ่มดำเนินงานตาม Kanban โดยยึดหลัก “ทำให้ส่วนพื้นฐานใช้งานได้ก่อน แล้วจึงเพิ่ม AI” ผลลัพธ์ที่ได้มีดังนี้

| งานที่ดำเนินการ | วิธีดำเนินการ | ผลลัพธ์จริง |
|---|---|---|
| Game logic | สร้าง dictionary state ของเกม เก็บคำศัพท์ ตัวอักษรที่เดา จำนวนผิด และสถานะ | Classic Hangman รับ `POST /api/hangman/new` และ `POST /api/hangman/guess` ได้ |
| Data pipeline | จำลอง combinations ของตัวอักษรในคำ สร้าง pattern และค้น candidate words | ได้ `datasets/hangman_dataset.csv` จาก `codes/make_dataset.py` |
| Model pipeline | เทรน/เปรียบเทียบโมเดลด้วย scikit-learn และบันทึกผล | มี `hangman_tree.pkl`, `hangman_lr.pkl`, `hangman_nb.pkl` และ `model_comparison.csv` |
| AI integration | โหลดโมเดลด้วย joblib สร้าง features จาก state เกม และตัดตัวอักษรซ้ำก่อนคืนคำแนะนำ | `codes/predict.py` ถูกเรียกจาก API ของ AI Assist และ VS AI |
| Web application | สร้าง Flask routes และเชื่อมหน้า HTML/CSS/JavaScript เข้ากับ API | เล่นได้ผ่าน `http://localhost:5000` |
| Documentation | แยกคู่มือใช้งาน ประวัติการเปลี่ยนแปลง และ learning log | มี `docs/`, `CHANGELOG.md`, `README.md` และไฟล์นี้ |

### สิ่งที่เรียนรู้จากการลงมือทำ

1. ต้องกำหนด input/output ของแต่ละโมดูลก่อนเขียนโค้ด เช่น `predict()` รับ `pattern`, `guessed`, `wrong` และส่งกลับ list ของตัวอักษร
2. การใช้ `set` ช่วยลดการตรวจอักษรซ้ำและทำให้การหาความแตกต่างระหว่างตัวอักษรที่เดากับคำตอบชัดเจน
3. การแยก UI, API และ AI pipeline ช่วยให้แก้ปัญหาเฉพาะส่วนได้ง่ายกว่าเขียนทุกอย่างไว้ในไฟล์เดียว
4. ข้อเสนอจาก GenAI ต้องนำมาตรวจด้วย code review, การทดลองรัน และการเปรียบเทียบกับเป้าหมายของโครงงานเสมอ
5. งานที่ยังต้องทำต่อคือ automated tests และการย้าย game state จาก memory ไปยัง storage หากต้องการรองรับผู้เล่นหลายคนหรือรีสตาร์ตเซิร์ฟเวอร์

← [กลับหน้าโครงการ](README.md)
