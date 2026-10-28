# BI304 — Scroll Story Enhancement (Local)

ชุดนี้เพิ่มชั้นการเล่าเรื่องด้วยการเลื่อน (scrollytelling) ลงในโปรเจกต์ BI304 เดิม โดยคงส่วนกราฟ แผนที่ ตาราง และเครื่องมือโต้ตอบเดิมไว้

## สิ่งที่เพิ่ม

- เพิ่มฉากเล่าเรื่องในหัวข้อ `topic-01` ถึง `topic-10` รวม 34 ช่วงข้อมูล
- แผง Visualization แบบ sticky เปลี่ยน metric, annotation และรูปแบบการแสดงข้อมูลตามช่วงที่อ่าน
- รูปคน 100 รูปสำหรับสัดส่วนหญิง–ชายในหัวข้อความหลากหลาย รวมทั้งกลุ่มนานาชาติ/สถาบันบูรณาการ
- กราฟแถบสัดส่วน 4 ศูนย์ที่อัปเดตตามยุค และแก้ค่าปี 2545 ให้ตรงตารางในหน้าเว็บเดิม (ท่าพระจันทร์ 26%, รังสิต 70%, ลำปาง 2.5%, พัทยา 1.5%)
- ปรับ Contrast ของข้อความรองที่ระบุไว้ และลดความสูงของแผง sticky บนมือถือเพื่อไม่ให้บดบังเนื้อหา
- รองรับการเลือก step ด้วยคลิก, Enter และ Space; เคารพ `prefers-reduced-motion`

## วิธีเปิดในเครื่อง

1. แตก ZIP ลงในโฟลเดอร์ใหม่
2. เปิดโฟลเดอร์ในเครื่อง Windows แล้วดับเบิลคลิก `RUN_WEB.bat`
3. เปิด URL Local ที่สคริปต์แจ้ง (โดยทั่วไปคือ `http://localhost:8080`) แล้วลองเลื่อนดูทุกหัวข้อ

## ไฟล์ที่เพิ่ม/แก้

- `index.html` — โหลด `scroll-story.css` และ `scroll-story.js`
- `assets/css/scroll-story.css` — styling, contrast overrides, responsive layout และ motion
- `assets/js/scroll-story.js` — data scenes และ logic ผูกกับ scroll

## ผลตรวจสอบ

- `node --check assets/js/scroll-story.js` — ผ่าน
- `python qa/check_data.py` — ผ่าน: 0 errors และ 0 warnings
- Browser harness สำหรับโมดูลที่เพิ่ม: สร้าง 10 โมดูล/34 steps, activation ของทุก step ผ่าน, มี 100 person icons ในฉากสัดส่วน, ไม่มี page errors ใน harness และไม่มี horizontal overflow ที่ viewport กว้าง 360–1440 px

หมายเหตุ: Browser harness ทดสอบ layout/logic ของโมดูลใหม่ใน HTML fixture และไม่ได้แทนการทดสอบ end-to-end ของแผนที่ Leaflet, กราฟ Chart.js และทรัพยากรภายนอกทั้งหมดในเซิร์ฟเวอร์ Local จริง ควรเปิดผ่าน `RUN_WEB.bat` แล้วทดลองทุก interaction ก่อนอนุญาตเผยแพร่

## ก่อนเผยแพร่

ตรวจสอบแหล่งข้อมูลและวันที่อ้างอิงสำหรับ metric ทุกหัวข้อ โดยเฉพาะอันดับมหาวิทยาลัย/โรงเรียนธุรกิจและตัวชี้วัดด้านความยั่งยืน อย่าใช้การ์ดเรื่องเล่าที่เพิ่มขึ้นแทนการเปิดอ่านกราฟ/ตารางต้นฉบับและแหล่งอ้างอิงด้านล่าง
