# 🎓 90 ปี มหาวิทยาลัยธรรมศาสตร์: จากตลาดวิชาสู่มหาวิทยาลัยวิจัยระดับโลกเพื่อประชาชน
### โครงงานกลุ่มวิชา BI304: Data Visualization and Storytelling | คณะพาณิชยศาสตร์และการบัญชี มหาวิทยาลัยธรรมศาสตร์ (TBS)
**อาจารย์ผู้สอน:** อาจารย์ ดร. นพธนิษฐ์ โชติสาร (Dr. Noptanit Chotisarn)  
**รูปแบบผลงาน:** Interactive Scrollytelling Intelligence Report & Flourish Story (รองรับทั้ง Version 2 Luxury Editorial และ Version 1 Classic)

---

## 🌐 ลิงก์สำหรับเข้าชมและตรวจงานออนไลน์ (Live Deployment)
ไม่ต้องติดตั้งโปรแกรม สามารถคลิกดูผลงาน Scrollytelling แบบเรียลไทม์ได้บนคอมพิวเตอร์ แท็บเล็ต และสมาร์ตโฟน:  
👉 **[https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/](https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/)**

- **Version 2 (Luxury Editorial):** หน้าหลัก ออกแบบสไตล์ **Bidwells (Driving Innovation at Speed)** และ **BMW Group Report 2024** พร้อมภาพพื้นหลังตึกโดมท่าพระจันทร์เสมือนจริง และนักศึกษาธรรมศาสตร์เดินก้าวไปข้างหน้าตาม Scroll Progress
- **Version 1 (Classic Scrollytelling):** สามารถสลับไปดู Version 1 ได้ตลอดเวลาผ่านปุ่มสลับเวอร์ชันที่แถบเมนูด้านบน หรือเข้าชมได้ที่ [`v1/index.html`](https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/v1/)

---

## 🚀 ฟีเจอร์เด่นของ Version 2 (ตามข้อเสนอแนะและการพัฒนาขั้นสูง)

1. **สไตล์และโทนสีหรูหราแบบ Bidwells / BMW Group Report:**
   - ธีม Dark Luxury Slate (`#0B0F17`) สบายตา ผสานกระจกใส Glassmorphism (`backdrop-filter: blur(16px)`)
   - สีประจำมหาวิทยาลัยธรรมศาสตร์: แดงเลือดหมูสง่างาม (`#DC2626`) และเหลืองทองอำพัน (`#F59E0B`)
   - ใช้ไลบรารีฟรี 100% (Plotly.js, Leaflet.js, CartoDB Dark Matter, Google Fonts Prompt/Sarabun, FontAwesome 6)
2. **ภาพกราฟิกเสมือนจริงตึกโดมท่าพระจันทร์ริมแม่น้ำเจ้าพระยา (Editorial Backdrop):**
   - ภาพความละเอียดสูงของสถาปัตยกรรมตึกโดมยามแสงอาทิตย์อัสดง พร้อมเลเยอร์ Vignette สร้างมิติเชิงลึก
3. **นักศึกษาธรรมศาสตร์เดินก้าวไปข้างหน้าตาม Timeline (Walking Student Scrollytelling HUD):**
   - แถบความคืบหน้าด้านล่างมีตัวละครนักศึกษาธรรมศาสตร์เดินก้าวไปข้างหน้าเรื่อยๆ ตามการเลื่อนอ่านเรื่องราว 90 ปี จาก พ.ศ. 2477 สู่ 2567 และวิสัยทัศน์ 2034
4. **ปุ่มสลับเวอร์ชัน Version Switcher Pill:**
   - สลับระหว่าง **Version 2 (Editorial)** และ **Version 1 (Classic)** ได้อย่างไร้รอยต่อ

---

## 📊 รายการปรับปรุงทั้ง 10 กราฟ / ฉากใน Version 2

| ฉาก | หัวข้อการนำเสนอ | ชนิดของ Visual ใน Version 2 | ฟังก์ชันและการปรับปรุงตามโจทย์ |
|:---:|:---|:---|:---|
| **1** | วิวัฒนาการ 9 ทศวรรษ & การปรับสู่ระบบปิด | **Straight Line Chart with Discrete Milestones** | แสดงเส้นตรงพร้อมหมุดหมายประวัติศาสตร์ เจาะลึกการก่อตั้ง 2477 (7,094 คน), จุดเปลี่ยนสำคัญสู่ **"ระบบปิด (Closed System)"** พ.ศ. 2495 (4,200 คน) และการขยายสู่ศูนย์รังสิต 2529 |
| **2** | ยุทธศาสตร์ 4 ศูนย์การศึกษา | **Pretty Maps Architectural Edition** | แผนที่ภูมิศาสตร์มืดแนวสถาปัตยกรรม (Leaflet + CartoDB Dark Matter) พร้อมวงคลื่นสัญญาณเรดาร์ (Beacon Pulses) และเส้นเชื่อมต่อการเดินทางระหว่าง 4 แคมปัส พร้อมการ์ดข้อมูลและ FlyTo อัตโนมัติ |
| **3** | โครงสร้าง 26 คณะ & คะแนน TCAS | **Hierarchical Treemap with Click-to-Modal** | แบ่ง 4 คลัสเตอร์วิชาการ **เมื่อคลิกที่คณะจะเปิดหน้าต่าง Modal แสดงคะแนนสอบเข้า TCAS รอบ 3 Admission, อัตราการแข่งขัน, อัตราการได้งานทำ, เงินเดือนเฉลี่ย และการรับรองสากล** |
| **4** | **มิติประชากร: หญิง 62.4% พลังขับเคลื่อนแห่งอนาคต** | **Stacked Demographic Distribution** | ปรับชื่อตรงตามที่ต้องการ เปรียบเทียบสัดส่วนหญิง 62.4% (26,620 คน) vs ชาย 37.6% (16,030 คน) พร้อมเทียบเกณฑ์เฉลี่ยโลก OECD (54%) |
| **5** | การกระจายตัวและการย้ายศูนย์การศึกษา | **Intuitive Multi-Era Allocation Matrix** | **ปรับแทนกราฟสายธารเดิมที่ดูยาก** เป็นกราฟแท่งเปรียบเทียบสัดส่วน 4 ยุคสำคัญ (ยุคท่าพระจันทร์ 100% สู่ยุครังสิต 78.5%) ดูง่าย ชัดเจน และเห็นภาพทันที |
| **6** | แนวโน้มงบประมาณ 5 ปี (2563 - 2567) | **5-Year Comparative Bar + Click Drilldown** | กราฟเปรียบเทียบงบ 5 ปี (11,280 สู่ 13,745 ลบ.) **เมื่อกดเข้าไปที่แท่งของปีใด จะแสดงรายละเอียดโครงสร้าง 5 แหล่งรายได้ของปีนั้นๆ ทันที** |
| **7** | ความเป็นเลิศทางธุรกิจ: เปรียบเทียบ Business Schools | **Multi-Dimension Radar Benchmark** | **เปรียบเทียบอย่างเข้มข้นระหว่าง TBS (มธ.), CBS (จุฬาฯ), Sasin (ศศินทร์ จุฬาฯ) และ CMMU (ม.มหิดล)** ทั้งด้าน Triple Crown, QS Ranking, Internationalization, และแชมป์กรณีศึกษาโลก |
| **8** | SDG 11 เมืองและชุมชนยั่งยืน (Top 10 โลก) | **Enhanced Sustainability Polar Radar** | เรดาร์ 6 มิติเมืองยั่งยืน โชว์ TU Solar Rooftop 23.6 MW (อันดับ 1 เอเชีย) สวนป๋วย 100 ปี (22,000 ตร.ม.) และรถโดยสาร EV 100% |
| **9** | โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ | **Enhanced Dual-Axis & Centers of Excellence** | สถิติ OPD 1.45 ล้านครั้ง และ IPD 35,200 ราย พร้อมสลับดู 5 ศูนย์ความเป็นเลิศเฉพาะทาง และรำลึกโรงพยาบาลสนามธรรมศาสตร์ 308 เตียง |
| **10** | TU 2034 Strategic Flight Cockpit | **Interactive Strategic Flight Simulator** | สไลเดอร์จำลองการจัดสรรงบประมาณวิจัย AI และกรีนแคมปัส พร้อมเข็มไมล์คำนวณคาดการณ์อันดับโลก QS และความพร้อมบัณฑิตแบบเรียลไทม์ |

---

## 📋 รายการสิ่งที่ต้องส่งครบถ้วน (Deliverables Package)

1. **เว็บ Scrollytelling เวอร์ชัน 2 และ 1:**
   - Version 2 (หน้าหลัก): [`index.html`](file:///d:/BI304/index.html)
   - Version 1 (คลาสสิก): [`v1/index.html`](file:///d:/BI304/v1/index.html)
2. **เอกสาร Storyboard PDF ฉบับสมบูรณ์:**
   - [`story board.pdf`](file:///d:/BI304/story%20board.pdf) (ตั้งชื่อไฟล์ `story board.pdf` ตามที่ระบุ)
3. **Google Colab Notebook:**
   - [`BI304_Thammasat_Data_Storytelling.ipynb`](file:///d:/BI304/BI304_Thammasat_Data_Storytelling.ipynb)
4. **ชุดข้อมูล Flourish 10 ไฟล์ CSV:**
   - โฟลเดอร์ [`flourish_data/`](file:///d:/BI304/flourish_data/) พร้อมคลิกดาวน์โหลดได้จากปุ่มบนหัวเว็บ
5. **ไฟล์แพ็กเกจส่งงาน (ZIP):**
   - `BI304_Thammasat_Group_Submission.zip` (รวมไฟล์ Version 1, Version 2, รูปภาพ assets, storyboard, และ datasets)
