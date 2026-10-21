# 📜 บันทึกประวัติการปรับปรุงและการเปลี่ยนแปลงโครงงาน (Project Changelog & Archive)

เอกสารฉบับนี้ใช้สำหรับบันทึกประวัติการพัฒนาและการเปลี่ยนแปลงของโครงงาน BI304: 90 ปี มหาวิทยาลัยธรรมศาสตร์ ในทุกช่วงเวลา โดยในหน้าเว็บหลักจะไม่มีการแสดงตัวเลขหรือคำว่า Version เพื่อความสะอาด สวยงาม และเป็นมืออาชีพตามมาตรฐานสากล

---

## 🕒 ลำดับประวัติการปรับปรุง (Chronological Change Log)

### 2. [ฉบับพัฒนาตามแบบฉบับ Bidwells & BMW Group Report] (ฉบับปัจจุบัน)
* **ไฟล์หลัก:** `index.html` และ `scrollytelling/index.html`
* **ภาพรวม:** ปรับโฉมเป็น Dark Luxury Editorial Scrollytelling ตามมาตรฐานรายงานวิจัยของ Bidwells (*Driving Innovation at Speed*) และ BMW Group Report 2024
* **รายการพัฒนาสำคัญ:**
  1. นำคำว่า Version และตัวเลขระบุเวอร์ชันออกจากหน้าเว็บทั้งหมด เพื่อความสะอาด สวยงามระดับ Editorial
  2. จัดวางส่วนหัวเว็บ Fullscreen 100vh ผสานภาพกราฟิกสถาปัตยกรรมตึกโดม ท่าพระจันทร์ ริมแม่น้ำเจ้าพระยาย่านแสงทองอัสดง (`assets/tha_prachan_dome_editorial.jpg`)
  3. ติดตั้งแนวรางเส้นทางประวัติศาสตร์ (Timeline Road Rail) ด้านข้าง พร้อมตัวละครนักศึกษาธรรมศาสตร์ (`assets/tu_student_walking.png`) ก้าวเดินตามการ Scroll พร้อมหมุดปี พ.ศ.
  4. ปรับปรุง 10 กราฟิกและการแสดงผลข้อมูล:
     - กราฟ 1: Straight Line Chart with Milestones เน้นย้ำระบบปิด พ.ศ. 2495 และศูนย์รังสิต พ.ศ. 2529
     - กราฟ 2: Pretty Maps CartoDB Dark Matter พร้อมเรดาร์เรืองแสงและเส้นทางเชื่อมต่อ
     - กราฟ 3: Faculty Treemap พร้อมระบบคลิกดูคะแนนสอบเข้า TCAS รอบ 3, อัตราแข่งขัน, การได้งานทำ และเงินเดือน
     - กราฟ 4: มิติประชากร หญิง 62.4% พลังขับเคลื่อนแห่งอนาคต
     - กราฟ 5: การกระจายตัวและการย้ายศูนย์การศึกษา 4 ยุค (แทนกราฟสายธารเดิมที่ซับซ้อน)
     - กราฟ 6: แนวโน้มงบประมาณ 5 ปี (2563-2567) พร้อมคลิกเจาะลึก 5 แหล่งรายได้ของแต่ละปี
     - กราฟ 7: เปรียบเทียบ 4 เสาหลัก Business Schools ไทย (TBS vs CBS vs Sasin vs CMMU)
     - กราฟ 8: เรดาร์ SDG 11 เมืองยั่งยืน Top 10 โลก (TU Solar 23.6 MW & สวนป๋วย 100 ปี)
     - กราฟ 9: โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ Dual-Axis และรำลึก รพ.สนาม 308 เตียง
     - กราฟ 10: TU 2034 Strategic Flight Cockpit Simulator ปรับสไลเดอร์คำนวณอันดับโลกแบบเรียลไทม์
  5. ใช้ไลบรารีฟรี 100% (Plotly, Leaflet, CartoDB, Google Fonts, FontAwesome)

---

### 1. [ฉบับคลาสสิก Flourish Story & Scrollytelling] (ฉบับดั้งเดิม)
* **ไฟล์เก็บถาวร:** `v1/index.html` และ `archive/classic_edition/index.html`
* **ภาพรวม:** หน้าเว็บแสดงผลแบบ 2 โหมด (Scrollytelling + Flourish Story Mode 10 สไลด์พร้อมตัวเล่นอัตโนมัติ) 
* **สถานะ:** บันทึกเก็บรักษาไว้ในโฟลเดอร์แยกต่างหากอย่างสมบูรณ์เพื่อใช้อ้างอิงย้อนหลัง

---

## Change Snapshot: 20261022_013500
- **แกนหลักของการปรับปรุง:** ปรับเปลี่ยนโมเดลการนำเสนอตามข้อสั่งการของผู้ใช้งาน โดยนำภาพจำลองรถแข่ง Formula 1 ของจริง (`car-white.png`, `car-pink.png`, `car-blue.png`) และสนามแข่งรถมาเป็นยานพาหนะหลักในการ Scrollytelling แทนตัวละครนักศึกษา และจัดวางองค์ประกอบทุกส่วนให้ตรงกับวิดีโอบันทึกหน้าจอของเว็บไซต์ Bidwells (*Driving Innovation at Speed: UK Motorsport Cluster*)
- **รายการพัฒนาและองค์ประกอบทางสายตาที่เทียบเท่า 100%:**
  1. **จุดสตาร์ทและสนามแข่งแนวตั้งตรงกลางจอ (Starting Grid Track):**
     - ผิวสนามแอสฟัลต์สีเนวี่เข้ม พร้อมเส้นชะลอความเร็ว/ขอบทางลายตารางหมากรุก (Checkered Curb) ทางฝั่งซ้ายตรงตามวิดีโอ
     - ช่องปล่อยตัว Grid Box ลายเส้นวงเล็บสีขาว `[ POLE POSITION ]` และ `[ GRID 02 ]`
     - รถแข่ง F1 สีขาว (`car-white.png`) ประจำตำแหน่ง Pole Position และรถแข่ง F1 สีแดง/ชมพูธรรมศาสตร์ (`car-pink.png`) ประจำตำแหน่งกริดที่ 2
     - ระบบขับเคลื่อนเมื่อผู้ใช้เลื่อนหน้าจอ รถแข่งจะเร่งสปีดทะยานไปข้างหน้าพร้อมสายลมความเร็ว (Speed Trails `car-trials.svg`)
  2. **High-Key Statement Section & 3 Winning Stat Cards (เฟรม 008s - 016s):**
     - ภาพอาคารโดมริมแม่น้ำเจ้าพระยาพร้อมการ์ดคำพูดเหลื่อมซ้อน: *"Thanks to everyone back at the university — ขอขอบคุณประชาคมธรรมศาสตร์ทุกคน..."*
     - หัวข้อเน้นคำด้วยไฮไลท์สีเหลือง: `For most, that foundation lies within มหาวิทยาลัยธรรมศาสตร์...`
     - ลายน้ำตัวเลขยักษ์ `90` แบบ Outline ด้านหลัง
     - การ์ดสถิติ 3 มิติขอบหนา 2px พร้อมบล็อกสีสดด้านล่าง (Sky Blue: ท่าพระจันทร์ 90 ปี, Crimson: ศูนย์รังสิต 26 คณะ, Emerald: Green Circuit Top 5 โลก SDG 11)
  3. **แผนที่ Cluster Matrix ดอทแมทริกซ์ 4 วิทยาเขตยุทธศาสตร์ (เฟรม 017s - 024s):**
     - การ์ดเลือกศูนย์การศึกษาทรงแคปซูลด้านซ้าย พร้อมแถบสีแดงบอกสถานะ
     - แผนที่เครือข่ายดอทแมทริกซ์ พร้อมเส้นวิถีวงโคจร (Orbital Trajectory Curves) และวงแหวนพัลส์เป้าหมาย (Pulsing Target Rings)
     - กราฟแท่งแสดงการกระจายตัวของนักศึกษา 4 ยุคสมัย (2500 - 2567)
     - เส้นแกนหมุดหมายประวัติศาสตร์การปฏิรูประบบปิด (2496–2503) พร้อมการ์ดไฮไลท์ 7,094 คน
  4. **Cost Cap & Budget Analysis บนพื้นสีเขียวทีล (เฟรม 025s - 035s):**
     - การ์ดขาวลอยตัวขอบมนสไตล์ Cost Cap วิเคราะห์งบประมาณ 5 ปี (2563-2567) พร้อมปุ่มเจาะลึก 5 แหล่งรายได้อย่างละเอียด
     - การ์ดประชากรศาสตร์: *"มิติประชากร: หญิง 62.4% พลังขับเคลื่อนแห่งอนาคต"* พร้อมแท่งสัดส่วนเปรียบเทียบ
     - ตาราง 26 คณะวิชา พร้อมป๊อปอัปโมดอลเจาะลึกเกณฑ์คะแนน TCAS รอบ 3 และเส้นทางอาชีพ
  5. **ทางโค้งสนามแข่งตัวเอส (Curved Track Frame 037s - 040s):**
     - ใช้ภาพสนามแข่งรถแอสฟัลต์ของจริง `assets/Track2.jpg` เป็นฉากหลัง
     - รถแข่ง F1 เลี้ยวตามแนวโค้ง พร้อมตารางเปรียบเทียบมาตรฐานการศึกษาบริหารธุรกิจระดับโลก (TBS Triple Crown vs CBS, Sasin, CMMU, NIDA)
  6. **วงจรสถิติ Silverstone Innovation Circuit (เฟรม 041s - 050s):**
     - เส้นทางสนามแข่งรถซิลเวอร์สโตนพร้อมหมุดเรืองแสง 1 ถึง 4 สลับข้อมูลแบบเรียลไทม์ (รพ.ธรรมศาสตร์ 810 เตียง, อาคารป๋วย 100 ปี, SDG 11 Top 5 โลก, ยุทธศาสตร์ TU 2034)
     - ค็อกพิทจำลองยุทธศาสตร์ TU 2034 Cockpit พร้อมสไลเดอร์ 4 มิติ
  7. **เส้นชัยธงตารางหมากรุก (Checkered Finish Line Frame 051s - 054s):**
     - แบนเนอร์ธงตารางหมากรุก `assets/finish.svg` วางพาดเต็มหน้าจอ
     - รถแข่ง F1 สองคันวิ่งทะยานข้ามเส้นชัยเคียงข้างกันพร้อมสายความเร็ว
     - ฟอร์มดาวน์โหลดรายงานวิจัยฉบับเต็ม พร้อมแอนิเมชัน Confetti เฉลิมฉลอง
  8. **Bottom Floating Scrubber Capsule:**
     - แคปซูลควบคุมการเลื่อนหน้าจอด้านล่าง พร้อมหมุดบอกช่วงเนื้อหาและปุ่มดาวน์โหลดรายงาน
  9. **กฎการไม่แสดงเลขเวอร์ชัน:** ไม่มีตัวเลขหรือข้อความ Version ใดๆ ปรากฏบนหน้าเว็บหลัก โดยใช้ชื่อปุ่ม *"คลังบันทึกประวัติ (Classic Archive)"* แทน
- Archived previous iteration before applying full Bidwells scrollytelling template matching user video recording.
- Requirements incorporated:
  1. Full Bidwells visual architecture (crisp white header, bottom floating scrubber pill with interactive timeline & download button).
  2. Student walking character on central campus milestone avenue (replacing F1 car).
  3. Straight Line Chart with Event Milestones (closed system reform & 4 campuses).
  4. Pretty Dotted Matrix Map for 4 strategic campuses (matching Bidwells / BMW Group report).
  5. 26 Faculties structure with interactive TCAS admission scores and detail modal.
  6. Demographic headline exact text: "มิติประชากร: หญิง 62.4% พลังขับเคลื่อนแห่งอนาคต".
  7. Clear multi-era campus distribution chart (replacing streamgraph).
  8. 5-year budget comparison (2563-2567) with interactive drill-down.
  9. Comprehensive Business School benchmarking (TBS vs CBS, Sasin, CMMU, NIDA).
  10. SDG 11, Hospital, TU 2034 cockpits.
  11. Absolute removal of explicit version numbers from UI.
