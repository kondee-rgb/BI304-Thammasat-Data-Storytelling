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

## Change Snapshot: 20261022_003737
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
