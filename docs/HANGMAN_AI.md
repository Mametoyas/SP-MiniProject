# Hangman AI

← [กลับหน้าหลัก](../README.md)

เกม Hangman ในโปรเจกต์นี้มี AI ช่วยแนะนำตัวอักษรที่ควรเดา โดยใช้ Decision Tree เทรนจากคลังคำศัพท์กว่า 1,000 คำ

---

## AI Pipeline (Offline)

```
words.txt  →  make_dataset.py  →  train_models.py  →  eval_models.py  →  hangman_tree.pkl
```

| ขั้นตอน | ไฟล์ | คำอธิบาย |
|---------|------|----------|
| 1 | `make_dataset.py` | สร้าง dataset จาก words.txt โดย simulate ทุก state ของเกม |
| 2 | `train_models.py` | เทรน 3 โมเดล (Decision Tree, Logistic Regression, Naive Bayes) |
| 3 | `eval_models.py` | วัด top-1 / top-5 accuracy และเปรียบเทียบโมเดล |

### วิธีเทรนโมเดล (ถ้าต้องการ retrain)

```bash
cd codes

python make_dataset.py
python train_models.py
python eval_models.py
```

---

## วิธีใช้งาน AI ใน Code

```python
from codes.predict import predict

# predict(pattern, guessed, wrong) → list of 5 suggested letters
suggestions = predict(
    pattern = "e_e_h__t",
    guessed = {"e", "h", "t"},
    wrong   = {"a", "i"}
)

print(suggestions)  # ['l', 'p', 'n', 'r', 's']
```

| Parameter | Type | คำอธิบาย |
|-----------|------|----------|
| `pattern` | `str` | pattern ปัจจุบัน เช่น `"e_e_h__t"` (`_` = ยังไม่รู้) |
| `guessed` | `set` | ตัวอักษรที่เดาถูกแล้ว |
| `wrong` | `set` | ตัวอักษรที่เดาผิดแล้ว |
| return | `list[str]` | top-5 ตัวอักษรที่แนะนำ |
