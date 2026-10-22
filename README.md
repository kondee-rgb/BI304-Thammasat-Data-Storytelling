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
โปรเจกต์นี้ได้รับการพัฒนาให้เป็น **Modular Clean Architecture** สำหรับการเผยแพร่ผ่าน GitHub Pages โดยตรงโดยไม่ต้องพึ่งพา Build Process:
- **`index.html`**: Semantic HTML5 โครงสร้างเนื้อหา 10 หัวข้อ พร้อมโครงข่ายการนำทาง Accessible Scrubber และ Navigation Drawer
- **`assets/css/style.css`**: ดีไซน์และชุดตัวแปร Design Tokens (`--tu-*`), Typography ที่รองรับภาษาไทยสมบูรณ์, Smooth Transitions และ WCAG AA Color Contrast
- **`assets/js/app.js`**: ตรรกะการโต้ตอบทั้งหมด, การควบคุม Scroll ด้วย `IntersectionObserver`, การเรนเดอร์กราฟิก และการทำงานของโมเดล Interactive
- **`data/data.json`**: คลังข้อมูลศูนย์กลาง (Single Source of Truth) ที่ผ่านการตรวจสอบข้อเท็จจริง (Fact-Check) พร้อมระบุ `source_id` และ `as_of` กำกับทุกชุดข้อมูล
- **ไลบรารีภายนอกที่ใช้จริง**:
  - **Chart.js 4.4.1**: สำหรับการเรนเดอร์แผนภูมิ Interactive (Line Chart, Horizontal Bar Chart, Doughnut Chart)
  - **Leaflet 1.9.4**: แผนที่ดาวเทียมและแผนที่ถนนความละเอียดสูงผ่าน Esri World Imagery & Esri World Street Map Tiles

---

## 📊 รายการ 10 หัวข้อเชิงลึกและเทคนิคการเล่าเรื่อง (The 10 Narrative Scenes)

| ฉาก | หัวข้อการนำเสนอ | รูปแบบการแสดงผลข้อมูล (Visualization) | สาระสำคัญและข้อมูลที่ได้รับการยืนยัน |
|:---:|:---|:---|:---|
| **01** | ปฐมบท 2477: ตลาดวิชาเพื่อราษฎร | **Interactive Milestone Stepper (7 ยุค)** | เส้นทางประวัติศาสตร์ 7 ยุคสำคัญ จากสถาปนา มธก. 2477 (ผู้สมัครรุ่นแรก 7,094 คน) สู่การขยายตัว 90 ปี |
| **02** | การกระจายโอกาสสู่ภูมิภาค 4 ศูนย์ | **Interactive GIS Campus Map (Leaflet)** | แผนที่แสดงที่ตั้งและสถิติ 4 ศูนย์ (ท่าพระจันทร์ 104 ไร่, รังสิต 1,757 ไร่, ลำปาง 364 ไร่, พัทยา 566 ไร่ รวม 2,791 ไร่) |
| **03** | 26 คณะวิชา 4 คลัสเตอร์ & TCAS | **Horizontal Bar Chart with Click-to-Modal** | แผนภูมิคะแนนต่ำสุดรอบ TCAS Admission 26 คณะ พร้อมตัวกรอง 4 คลัสเตอร์วิชาการ และ Modal เจาะลึกข้อมูลคณะ |
| **04** | โครงสร้างประชากรและความหลากหลาย | **Demographic Balance Breakdown** | ดุลยภาพนักศึกษาหญิง 62.4% (26,738 คน) และนักศึกษาชาย 37.6% (16,112 คน) รวม 42,850 คน |
| **05** | สายธารแห่งการโยกย้ายศูนย์กลาง | **Multi-Era Allocation Transition** | วิวัฒนาการการย้ายศูนย์กลางการศึกษาจากท่าพระจันทร์ 100% (พ.ศ. 2500) สู่ศูนย์รังสิต 73.5% (ปัจจุบัน) |
| **06** | ความมั่นคงทางการคลังและวินัยงบประมาณ | **5-Year Multi-Stream Interactive Line Chart** | เส้นทางงบประมาณ 5 ปี (13,420 สู่ 15,350 ล้านบาท) พร้อมปุ่ม Drilldown 5 แหล่งรายได้ และงบประมาณรวม |
| **07** | ก้าวสู่เวทีโลกและมาตรฐานสากล | **Business School Benchmark Matrix** | บันทึกประวัติศาสตร์ TBS สถาบันบริหารธุรกิจแห่งแรกในไทยที่คว้า Triple Crown (2018) และจุฬาฯ CBS (2023) |
| **08** | มหาวิทยาลัยสีเขียวและความยั่งยืน | **Sustainability Impact Visualizer** | อุทยานเรียนรู้ป๋วย 100 ปี (สวนหลังคา 22,000 ตร.ม.), โซลาร์เซลล์ 15 MWp, และลดก๊าซเรือนกระจก 25,500 ตัน/ปี |
| **09** | รพ.ธรรมศาสตร์: ที่พึ่งแห่งประชาชน | **Dual-Mode Capacity & Patient Volume** | สถิติผู้ป่วยนอก 1.48 ล้านคน/ปี, ขีดความสามารถเตียงตติยภูมิ 1,400 เตียง และ รพ.สนาม 308 เตียง (ผู้ป่วยสะสม 3,083 ราย) |
| **10** | วิสัยทัศน์ TU 2034: ก้าวสู่ 100 ปี | **TU 2034 Centennial Strategy Cockpit** | สไลเดอร์จำลองดัชนีความพร้อม 4 เสาหลัก (Innovation Hub, Future Skills, 88 Sandbox, Net-Zero Campus 2030) |

---

## 📋 เอกสารและการตรวจสอบความถูกต้อง (Verification & QA Package)
- **`AUDIT.md`**: รายงานการตรวจสอบระบบและจุดขัดแย้งของข้อมูล
- **`qa/DATA_VERIFICATION.md`**: บันทึกการสอบทานข้อเท็จจริง 22 รายการ เทียบกับแหล่งข้อมูลทางการระดับ A/B
- **`qa/FEATURE_PARITY.md`**: ตารางตรวจสอบความเท่าเทียมของฟังก์ชันและการโต้ตอบ (Zero-Regression Matrix)
- **`qa/baseline_lighthouse.json`**: ผลการทดสอบประสิทธิภาพการโหลด (Lighthouse) ก่อนเริ่มการปรับปรุง
- **`BI304_Thammasat_Data_Storytelling.ipynb`**: สมุดโค้ด Python สำหรับวิเคราะห์และประมวลผลข้อมูล
- **`flourish_data/`**: ชุดข้อมูล CSV ที่เชื่อมโยงกับฉากจำลอง 10 ฉาก
