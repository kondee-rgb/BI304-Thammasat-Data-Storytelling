# 🎓 90 ปี มหาวิทยาลัยธรรมศาสตร์: ขับเคลื่อนปัญญาและนวัตกรรมเพื่อประชาชน (2477 — 2567)
### โครงงานกลุ่มวิชา BI304: Data Visualization and Storytelling | คณะพาณิชยศาสตร์และการบัญชี มหาวิทยาลัยธรรมศาสตร์ (TBS)
**อาจารย์ผู้สอน:** อาจารย์ ดร. นพธนิษฐ์ โชติสาร (Dr. Noptanit Chotisarn)  
**รูปแบบผลงาน:** Interactive Scrollytelling Intelligence Report (High-Performance Vanilla JS, Chart.js 4.4.1, Leaflet 1.9.4 GIS)

---

## 🌐 ช่องทางการเข้าชมผลงาน (Live Deployment)
สามารถเปิดดูและโต้ตอบกับเว็บไซต์ได้โดยตรงบนคอมพิวเตอร์ แท็บเล็ต และสมาร์ตโฟน:  
👉 **[https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/](https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/)**

*(คลังผลงานเวอร์ชันก่อนหน้า: [`v1/index.html`](https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/v1/))*

---

## 🛠️ โครงสร้างเทคโนโลยีและสถาปัตยกรรมระบบ (Architecture)
- **Frontend Core**: Semantic HTML5 (WCAG 2.1 AA Compliant with `<main id="main">`, skip-link, Accessible Fallback Tables), Modular CSS3 (Design Tokens, Responsive Grid & Flexbox, Scrollytelling Animation), Vanilla JavaScript ES6+ (No Heavy Framework Overhead)
- **Data Visualizations**: 
  - [Chart.js 4.4.1](https://www.chartjs.org/) สำหรับชาร์ตข้อมูลทางการเงิน, สัดส่วนประชากร, การโยกย้ายศูนย์กลาง, พลังงานหมุนเวียน และสถิติบริการทางการแพทย์
  - **Horizontal Dot/Lollipop Plot** สำหรับสถิติคัดเลือก TCAS 25 คณะวิชา (แกน 60 — 85 คะแนน) พร้อมจุดคลัสเตอร์สีคมชัด
  - [Leaflet 1.9.4](https://leafletjs.com/) สำหรับ Interactive GIS Map แสดง 4 ศูนย์การศึกษา พร้อมสลับ Basemap ถนน/ดาวเทียม และระบบพิกัด GPS จำลอง
  - **Triple Crown SVG Badges**: ตราสัญลักษณ์ความสำเร็จมาตรฐานสากล AACSB (2012), EQUIS (2012), และ AMBA (2018)
- **Interactive Scrollytelling & UX**:
  - Slim Top Reading Progress Bar: แถบแสดงความคืบหน้าการอ่านด้านบนสุด เชื่อมโยงกับตำแหน่งสกรอลล์
  - Desktop Dot Navigation: สารบัญจุดนำทางแนวตั้งด้านขวาหน้าจอ พร้อม Tooltip อัจฉริยะ
  - Mobile Optimized Drawer: เมนูนำทางแบบสไลด์สะดวกบนสมาร์ตโฟน รองรับทุกขนาดหน้าจอ
  - Scroll-Triggered Animated Counters: แอนิเมชันนับตัวเลขสถิติสำคัญด้วย `IntersectionObserver` พร้อม Easing และระบบจัดรูปแบบหน่วยวัด
  - Accessible Modals: กล่องข้อมูลเจาะลึก 26 คณะวิชา และคลังภาพข้อมูล Flourish 10 ฉาก พร้อมระบบ Focus Trap และ Escape Dismissal

---

## 📊 รายการ 10 หัวข้อเชิงลึกและเทคนิคการเล่าเรื่อง (The 10 Narrative Scenes)

| ฉาก | หัวข้อการนำเสนอ | รูปแบบการแสดงผลข้อมูล (Visualization) | สาระสำคัญและข้อมูลที่ได้รับการยืนยัน |
|:---:|:---|:---|:---|
| **01** | ปฐมบท 2477: ตลาดวิชาเพื่อราษฎร | **Interactive Milestone Stepper (7 ยุค)** | เส้นทางประวัติศาสตร์ 7 ยุคสำคัญ จากสถาปนา มธก. 2477 (ผู้สมัครรุ่นแรก 7,094 คน) สู่การขยายตัว 90 ปี (นักศึกษา 42,850 คน) |
| **02** | การกระจายโอกาสสู่ภูมิภาค 4 ศูนย์ | **Interactive GIS Campus Map (Leaflet)** | แผนที่แสดงที่ตั้งและสถิติ 4 ศูนย์ (ท่าพระจันทร์ 104 ไร่, รังสิต 1,757 ไร่, ลำปาง 364 ไร่, พัทยา 566 ไร่ รวม 2,791 ไร่) |
| **03** | 26 คณะวิชา 4 คลัสเตอร์ & TCAS | **Horizontal Dot/Lollipop Plot with Click-to-Modal** | แผนภูมิคะแนนต่ำสุดรอบ TCAS Admission 25 คณะ (แกน 60 — 85 คะแนน) พร้อมตัวกรอง 4 คลัสเตอร์วิชาการ และ Modal เจาะลึกข้อมูลคณะ |
| **04** | โครงสร้างประชากรและความหลากหลาย | **Demographic Balance Breakdown & Fallback Table** | ดุลยภาพนักศึกษาหญิง 62.4% (26,738 คน) และนักศึกษาชาย 37.6% (16,112 คน) รวม 42,850 คน |
| **05** | สายธารแห่งการโยกย้ายศูนย์กลาง | **Multi-Era Allocation Transition & Fallback Table** | วิวัฒนาการการย้ายศูนย์กลางการศึกษาจากท่าพระจันทร์ 100% (พ.ศ. 2500) สู่ศูนย์รังสิต 73.5% (ปัจจุบัน) |
| **06** | ความมั่นคงทางการคลังและวินัยงบประมาณ | **5-Year Multi-Stream Interactive Line Chart** | เส้นทางงบประมาณ 5 ปี (13,420 สู่ 15,350 ล้านบาท) พร้อมปุ่ม Drilldown 5 แหล่งรายได้ และงบประมาณรวม |
| **07** | ก้าวสู่เวทีโลกและมาตรฐานสากล | **Triple Crown SVG Badges & Benchmark Matrix** | บันทึกประวัติศาสตร์ TBS สถาบันบริหารธุรกิจแห่งแรกในไทยที่คว้า Triple Crown (2018) และจุฬาฯ CBS (2020) พร้อมตารางเลื่อนแนวนอนแบบ Sticky Column |
| **08** | มหาวิทยาลัยสีเขียวและความยั่งยืน | **Sustainability Impact Visualizer & Fallback Table** | อุทยานเรียนรู้ป๋วย 100 ปี (สวนหลังคา 22,000 ตร.ม.), ความจุกักเก็บน้ำฝน TURF 3.1 ล้านแกลลอน, โซลาร์เซลล์ 15 MW, SDG 11 (98.4 คะแนน) และอันดับ 1 โลก SDG 16 |
| **09** | รพ.ธรรมศาสตร์: ที่พึ่งแห่งประชาชน | **Dual-Mode Capacity & Patient Volume** | สถิติผู้ป่วยนอก 1.48 ล้านคน/ปี, เตียงตติยภูมิเปิดบริการจริง 750 เตียง (มติ ครม. ขยายสู่ 1,000 เตียง) และ รพ.สนาม 308 — 470 เตียง (ผู้ป่วยสะสมกว่า 3,200 ราย) |
| **10** | วิสัยทัศน์ TU 2034: ก้าวสู่ 100 ปี | **TU 2034 Centennial Strategy Cockpit** | สไลเดอร์จำลองดัชนีความพร้อม 4 เสาหลัก (Innovation Hub, Future Skills, 88 Sandbox, Net-Zero Campus 2030) ค่าเริ่มต้นคำนวณจริง 92.0 |

---

## 📋 เอกสารและการตรวจสอบความถูกต้อง (Verification & QA Package)
- **`qa/FINAL_REPORT.md`**: รายงานสรุปผลการดำเนินงานและผลการทดสอบการเข้าถึง (A11y Axe Audit 0 Violations)
- **`qa/DATA_VERIFICATION.md`**: บันทึกการสอบทานข้อเท็จจริง 22 รายการ เทียบกับแหล่งข้อมูลทางการระดับ A/B พร้อม Deep Links
- **`qa/UNVERIFIED.md`**: บันทึกตัวเลขที่ยกเลิกการใช้งาน (Reverted Baseline Numbers) ตามมาตรการ Checklist 6
- **`qa/screenshots/`**: ภาพบันทึกหน้าจอความละเอียดสูงทั้งบนหน้าจอ Desktop (1440px) และ Mobile (390px)
- **`BI304_Thammasat_Data_Storytelling.ipynb`**: สมุดโค้ด Python สำหรับวิเคราะห์และประมวลผลข้อมูลบน Google Colab
- **`flourish_data/`**: ชุดข้อมูล CSV ที่เชื่อมโยงกับฉากจำลอง 10 ฉาก และไฟล์ `thammasat_flourish_all_scenes.zip`
