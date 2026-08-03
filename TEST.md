# Model Evaluation Results

เอกสารนี้สรุปผลการประเมินโมเดลสำหรับ Hangman AI โดยอ้างอิงข้อมูลจาก `datasets/model_comparison.csv`

## Evaluation Metrics

| Metric | ความหมาย |
|---|---|
| Top-1 Accuracy | สัดส่วนที่อักษรแนะนำอันดับ 1 ตรงกับคำตอบที่คาดหวัง |
| Top-5 Accuracy | สัดส่วนที่คำตอบที่คาดหวังปรากฏอยู่ในคำแนะนำ 5 อันดับแรก |
| Precision | ความถูกต้องของอักษรที่โมเดลทำนาย |
| Recall | ความสามารถในการพบอักษรที่ควรแนะนำ |
| F1 Score | ค่าเฉลี่ยสมดุลระหว่าง Precision และ Recall |
| Predict Time | เวลาที่ใช้ทำนายผล หน่วยเป็นวินาที |

## Results

| Model | Top-1 Accuracy | Top-5 Accuracy | Precision | Recall | F1 Score | Predict Time (s) |
|---|---:|---:|---:|---:|---:|---:|
| Random Forest | 0.9992 | 0.9995 | 0.9992 | 0.9992 | 0.9991 | 0.4756 |
| Decision Tree | 0.9915 | 0.9942 | 0.9916 | 0.9915 | 0.9915 | 0.2048 |
| Logistic Regression | 0.4918 | 0.6131 | 0.4861 | 0.4918 | 0.4726 | 0.1759 |
| Naive Bayes | 0.4077 | 0.5886 | 0.4472 | 0.4077 | 0.4146 | 0.1724 |

## Conclusion

- Random Forest ให้ค่า Top-1 Accuracy สูงสุด แต่ใช้เวลาทำนายมากที่สุด
- **Random Forest ไม่ได้อัปโหลดไว้บน GitHub** เนื่องจากไฟล์โมเดลที่ serialize แล้วมีขนาดใหญ่เกินกว่าที่ repository นี้รองรับ จึงไม่มีไฟล์ `hangman_rf.pkl` ในโฟลเดอร์ `models/`
- หากต้องการใช้งาน Random Forest ต้องเทรนโมเดลใหม่ตั้งแต่ต้น โดยใช้ `datasets/hangman_dataset.csv` ร่วมกับสคริปต์เทรนใน `codes/` แล้วบันทึกโมเดลไว้ในเครื่องหรือพื้นที่จัดเก็บที่รองรับไฟล์ขนาดใหญ่
- Decision Tree มีความแม่นยำสูงและใช้เวลาทำนายต่ำกว่า Random Forest จึงถูกเลือกใช้ในระบบปัจจุบันผ่าน `models/hangman_tree.pkl`
- Logistic Regression และ Naive Bayes ใช้เป็นโมเดลสำหรับเปรียบเทียบผลการทดลอง

← [กลับหน้าโครงการ](README.md)
