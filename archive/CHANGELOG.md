# บันทึกการเปลี่ยนแปลงของระบบ (Project Changelog)

## [Phase 7] - 2026-10-22 (Scroll & Interactive Polish)

### สรุปการเปลี่ยนแปลง:
- **แถบนำทาง Scrubber และ Stepper เข้าถึงได้สมบูรณ์ (Accessible Slider)**:
  - เพิ่ม `role="slider"`, `tabindex="0"`, `aria-valuemin="0"`, `aria-valuemax="10"`, `aria-valuenow`, `aria-valuetext`
  - รองรับการควบคุมด้วยคีย์บอร์ดเต็มรูปแบบ: ลูกศรซ้าย/ขวา/ขึ้น/ลง, PageUp, PageDown, Home (กลับจุดเริ่มต้น), End (ไปยังบทสรุป)
- **ปรับปรุง Modal เข้าถึงได้ตามมาตรฐาน WAI-ARIA**:
  - เพิ่ม `role="dialog"`, `aria-modal="true"`, `aria-labelledby="mFacTitle"`
  - ปิด Modal ได้ทันทีด้วยปุ่ม `Escape` บนคีย์บอร์ด
- **ปรับปรุง Leaflet GIS Map**:
  - เปิดการแสดงผล Attribution อย่างถูกต้อง (`attributionControl: true`)
  - รองรับการใช้งานสัมผัส 2 นิ้วบนสมาร์ทโฟน (`touchZoom: true`, `dragging: true`)
- **ปรับปรุง TU 2034 Strategy Cockpit**:
  - กำกับป้ายน้ำหนักยุทธศาสตร์ [30%, 25%, 25%, 20%] ชัดเจน
  - ปรับค่าคะแนนดัชนีเริ่มต้นให้ตรงกับสูตรการคำนวณ (93.0)
  - เพิ่มปุ่ม "รีเซ็ตค่ามาตรฐาน" (`resetCockpit()`)
- **รองรับ `prefers-reduced-motion` เต็มรูปแบบ**:
  - ผู้ใช้งานที่ตั้งค่าลดความเคลื่อนไหวในระบบปฏิบัติการ จะเห็นตัวเลขและองค์ประกอบคงที่ทันที โดยไม่ถูกบังคับให้รับชมแอนิเมชัน
- **บันทึกภาพถ่ายหน้าจอ Phase 7**:
  - แคปภาพ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 70 รูปใน `qa/phase7_screens/`

---

## [Phase 6] - 2026-10-22 (Data Visualization & Storytelling Polish)

### สรุปการเปลี่ยนแปลง:
- **เพิ่มส่วน "สรุปผลลัพธ์เชิงประจักษ์ 3 มิติสำคัญ" (`#key-findings`) หลัง Hero Section**:
  - มิติที่ 1: การเปิดกว้างทางการศึกษา (42,850 คน, นักศึกษาหญิง 62.4%)
  - มิติที่ 2: ความเป็นเลิศและเสถียรภาพ (Triple Crown แห่งแรกของไทย, บริหารงบประมาณแผ่นดินและเงินรายได้ 15,350 ล้านบาท)
  - มิติที่ 3: สุขภาวะและความยั่งยืน (Solar 15.0 MWp, อันดับ 1 โลก SDG 16, รพ.ธรรมศาสตร์ 824 เตียง และ รพ.สนาม 308 เตียง ดูแลผู้ป่วย 3,083 ราย)
- **เพิ่มสะพานเชื่อมโยงข้อมูล (Narrative Connector Bridges) ระหว่างหัวข้อ**:
  - วางประโยคสะพานเชื่อมรอยต่อบริบทข้อมูลระหว่างฉาก ช่วยให้การเล่าเรื่องลื่นไหลเป็นหนึ่งเดียว
- **ปุ่มเปิด-ปิด "ดูตารางข้อมูล" (Accessible Data Table Toggles)**:
  - เพิ่มในหัวข้อ 03 (TCAS Cutoffs) และหัวข้อ 06 (5-Year Budget Streams)
  - รองรับ Screen Reader ด้วย `aria-expanded` และ HTML5 semantic table
- **แก้ไขสเกลแผนภูมิแท่ง TCAS ตามหลัก Edward Tufte**:
  - ปรับสเกลแกนเริ่มต้นจาก 0 (min: 0, max: 100) ขจัดปัญหา Truncated Baseline ไม่บิดเบือนมิติของแท่งข้อมูล
- **จัดทำเอกสาร Tufte / LATCH Framework Audit**:
  - บันทึกการตรวจสอบ Data-Ink Ratio และการจัดหมวดหมู่ข้อมูลใน `qa/DATA_VISUALIZATION_AUDIT.md`
- **บันทึกภาพถ่ายหน้าจอ Phase 6**:
  - แคปภาพ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 70 รูปใน `qa/phase6_screens/`

---

## [Phase 5] - 2026-10-22 (Images & Media Optimization)

### สรุปการเปลี่ยนแปลง:
- **แปลงไฟล์ภาพทั้งหมดสู่ฟอร์แมต WebP คุณภาพสูง ควบคุมขนาดไฟล์ <= 200KB**:
  - `Track2.webp` (ลดจาก 725 KB เหลือ 168 KB)
  - `tha_prachan_dome_editorial.webp` (ลดจาก 841 KB เหลือ 122 KB)
  - `tu_student_walking.webp` (ลดจาก 538 KB เหลือ 37 KB พร้อมช่องความโปร่งใส Alpha คมชัดสมบูรณ์)
  - `pillar_1_innovation_hub.webp` (ลดจาก 874 KB เหลือ 152 KB)
  - `pillar_2_future_skills.webp` (ลดจาก 921 KB เหลือ 167 KB)
  - `pillar_3_88sandbox.webp` (ลดจาก 904 KB เหลือ 157 KB)
  - `pillar_4_netzero_campus.webp` (ลดจาก 996 KB เหลือ 193 KB)
  - *รวมประหยัดแบนด์วิดท์ภาพได้กว่า 85% ยกระดับความเร็ว LCP และการโหลดบนมือถือ*
- **ขจัด External Image Hotlinks 100%**:
  - สร้างไฟล์เวกเตอร์ SVG โลคัล `assets/colab_icon.svg` สำหรับปุ่มเปิด Google Colab ทั้งหมด ป้องกันปัญหา Third-party Tracking และ Network Failures
- **เพิ่มมิติเงาสัมผัสพื้นแนวนอน (Horizontal Ground Contact Shadow)**:
  - อัปเกรด `.tu-student-ground-shadow` ใต้เท้าตัวละครนักศึกษา (Pioneer / Scholar) ให้ทอดยาวสมจริงบนพื้นผิวถนน ไม่ลอย
- **กำหนด Attributes ทางเทคนิคครบถ้วน**:
  - กำหนด `width`, `height`, `loading="lazy"`, `decoding="async"`
  - เพิ่มคำอธิบายภาพ `alt` ภาษาไทยอย่างละเอียด ระบุชัดเจนว่าเป็นภาพประกอบเชิงสร้างสรรค์/ทัศนียภาพจำลอง (AI-Assisted Illustration)
- **บันทึกภาพถ่ายหน้าจอ Phase 5**:
  - แคปภาพ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 65 รูปใน `qa/phase5_screens/`

---

## [Phase 4] - 2026-10-22 (Color & Identity Polish)

### สรุปการเปลี่ยนแปลง:
- **ย้าย Design Tokens สู่มาตรฐาน `--tu-*`**:
  - เปลี่ยนชื่อ Token เป็น `--tu-navy`, `--tu-crimson`, `--tu-gold`, `--tu-teal`, `--tu-sky-blue`, `--tu-offwhite`, `--tu-text`, `--tu-muted`, `--tu-shadow-*`, `--tu-radius-*`
  - คงค่า Backwards-compatibility aliases สำหรับ `--bidwells-*` เพื่อป้องกันผลกระทบย้อนหลัง
  - ปรับใช้ Token ใหม่ใน `assets/css/style.css`, `index.html`, และ `assets/js/app.js`
- **ตรวจสอบสีอัตลักษณ์ทางการของธรรมศาสตร์**:
  - แดงชาด (Thammasat Crimson): `#c51944`
  - เหลืองทอง (Thammasat Gold): `#ffc72c`
  - กรมท่าเข้ม (Thammasat Deep Navy): `#0b163b`
- **การเกลี่ยรอยต่อพื้นหลังระหว่าง Section (Smooth Gradient Transitions)**:
  - แก้ไขปัญหาฉากหลังตัดกันฉับพลันระหว่างสีขาวและสีกรมท่าเข้ม ตามคำขอของผู้ใช้ (User Request 8 ข้อ 4)
  - เพิ่มเส้นแบ่ง Accent Divider และการเกลี่ยสีแบบ Multi-stop Gradient ในทุกจุดเชื่อมต่อ:
    - Topic 02: `linear-gradient(180deg, var(--tu-navy) 0%, #08112b 120px, #08112b 100%)`
    - Topic 03: `linear-gradient(180deg, #f1f5f9 0%, #ffffff 140px, #ffffff 100%)` พร้อมขอบทอง
    - Topic 05: `linear-gradient(180deg, #070e24 0%, var(--tu-navy) 100px, var(--tu-navy) 100%)` พร้อมขอบแดงชาด
    - Topic 06: `linear-gradient(180deg, #07262a 0%, var(--tu-teal-dark) 100px, var(--tu-teal-dark) 100%)`
    - Topic 07: `linear-gradient(180deg, #061924 0%, #0b1426 100px, #0b1426 100%)`
    - Topic 08: `linear-gradient(180deg, #0b1426 0%, #0d2822 80px, #061517 100%)`
    - Topic 09: `linear-gradient(180deg, #f1f5f9 0%, #ffffff 140px, #ffffff 100%)` พร้อมขอบเขียวมรกต
    - Finish: `linear-gradient(180deg, #070e24 0%, #0f172a 50px, var(--tu-offwhite) 160px, var(--tu-offwhite) 100%)`
- **ตรวจสอบการเข้าถึงตามมาตรฐาน WCAG 2.1 AA**:
  - ปรับสีตัวอักษร Muted Text บนพื้นหลังสว่างเป็น `#475569` (Slate 600, Contrast Ratio 5.9:1 ผ่านเกณฑ์ AA 4.5:1)
  - กำหนดให้สีเหลืองทองใช้บนพื้นหลังเข้มเท่านั้นเพื่อคงความคมชัดสูงสุด
- **บันทึกภาพถ่ายหน้าจอ Phase 4**:
  - แคปภาพ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 65 รูปใน `qa/phase4_screens/`

---

## [Phase 3] - 2026-10-22 (Typography & Language Polish)

### สรุปการเปลี่ยนแปลง:
- **ปรับสถาปัตยกรรม Font Stack ให้สมบูรณ์แบบสำหรับภาษาไทยและตัวเลข**:
  - กำหนด `--font-heading`: `'Prompt', 'Plus Jakarta Sans', sans-serif` สำหรับ Headings, ตัวเลขสถิติ, KPIs, Eyebrows
  - กำหนด `--font-body`: `'Sarabun', 'Plus Jakarta Sans', sans-serif` สำหรับเนื้อหา, คำอธิบาย, เชิงอรรถ
  - กำหนด Body `line-height: 1.75` เพื่อป้องกันวรรณยุกต์ภาษาไทยชนกัน และเพิ่มความสบายตาในการอ่าน
  - บังคับ `text-wrap: balance` บน H1, H2, H3, Eyebrow และการ์ดสรุป เพื่อลดปัญหาคำโดดท้ายบรรทัด
- **ออกแบบ Responsive Fluid Typography ด้วย `clamp()`**:
  - `.section-headline`: `clamp(1.85rem, 3.8vw, 2.75rem)` สวยงามลงตัวทุกขนาดจอ (360px ถึง 1440px)
  - `.section-lead`: `clamp(1rem, 1.2vw, 1.12rem)` พร้อมจำกัดความยาวบรรทัดสูงสุดที่ `72ch` ตามหลัก Editorial Design
- **ปรับ H2 ทั้ง 10 หัวข้อเป็น Insight Statements พร้อมตัวเลขจริง (ตัด Marketing Fluff)**:
  - หัวข้อ 01: "ปฐมบท 2477: ตลาดวิชาเพื่อราษฎร สู่ 4.2 หมื่นคน"
  - หัวข้อ 02: "การกระจายโอกาสสู่ภูมิภาค: 4 ศูนย์การศึกษา 2,791 ไร่ ทั่วประเทศ"
  - หัวข้อ 03: "26 คณะวิชา 4 คลัสเตอร์: ความหลากหลายทางปัญญาและสถิติคัดเลือก TCAS 2566"
  - หัวข้อ 04: "โครงสร้างประชากร: นักศึกษาหญิง 62.4% สะท้อนมิติใหม่แห่งโอกาสทางการศึกษา"
  - หัวข้อ 05: "การเปลี่ยนผ่านทางกายภาพ: การโยกย้ายศูนย์กลาง 73.5% สู่รังสิต"
  - หัวข้อ 06: "เสถียรภาพทางการเงิน: บริหารงบประมาณแผ่นดินและเงินรายได้ 12,987 ล้านบาท"
  - หัวข้อ 07: "ความเป็นเลิศระดับสากล: Triple Crown 3 สถาบัน และยุทธศาสตร์ QS Asia Top 70"
  - หัวข้อ 08: "แคมปัสยั่งยืนแห่งอนาคต: พลังงานสะอาด 15.0 MWp และอันดับ 1 ของโลก SDG 16"
  - หัวข้อ 09: "สุขภาวะเพื่อประชาชน: รพ.ธรรมศาสตร์ 824 เตียง และบทบาท รพ.สนาม 308 เตียง ยามวิกฤต"
  - หัวข้อ 10: "TU 2034 สู่ศตวรรษที่ 2: 4 เสาหลักยุทธศาสตร์และการจำลองดัชนีความพร้อม"
- **การตัดคำภาษาไทยใน Chart.js Tooltips (`formatThaiTooltipText`)**:
  - ตั้งค่า Chart.defaults ใช้แบบอักษร `Prompt` และ `Sarabun`
  - เพิ่มฟังก์ชันตัดบรรทัดอัจฉริยะด้วย `Intl.Segmenter('th', { granularity: 'word' })` ป้องกันการตัดคำขาดกลางคำ
- **บันทึกภาพถ่ายหน้าจอ Phase 3**:
  - แคปภาพ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 65 รูปใน `qa/phase3_screens/`

---

## [Phase 2] - 2026-10-22 (Data & Sources)

### สรุปการเปลี่ยนแปลง:
- **สร้าง `data/data.json`**:
  - แหล่งข้อมูลศูนย์กลาง (Single Source of Truth) สำหรับสถิติทุกด้านในวาระ 90 ปี
  - กำกับ Metadata ระดับความน่าเชื่อถือ (Level A/B), URL แหล่งอ้างอิงทางการ, และวันที่สำรวจข้อมูล (as_of)
- **ปรับปรุงตัวเลขสถิติที่ผ่านการ Fact-Check ใน `index.html` และ `assets/js/app.js`**:
  - ข้อความคำกล่าว ศ.ดร.ปรีดี พนมยงค์ ฉบับสมบูรณ์ถูกต้องตามบันทึกพิธีสถาปนา 2477
  - สรุปพื้นที่ 4 ศูนย์การศึกษาครบถ้วน 2,791 ไร่ (ท่าพระจันทร์ 104, รังสิต 1,757, ลำปาง 364, พัทยา 566 ไร่)
  - สัดส่วนเพศนักศึกษา: หญิง 26,738 คน (62.4%), ชาย 16,112 คน (37.6%), รวม 42,850 คน
  - กำลังผลิต Solar Rooftop: 15.0 MWp ครอบคลุม 44 อาคาร (ร่วมกับ กฟผ. และ Solartron)
  - อันดับความยั่งยืน THE Impact Rankings: SDG 11 ได้ 84.1 คะแนน (อันดับ 38 ของโลก), SDG 16 คว้าอันดับ 1 ของโลก
  - โรงพยาบาลสนามธรรมศาสตร์: 308 เตียง ณ อาคาร DLUXX รองรับผู้ป่วยสะสมกว่า 3,083 ราย
- **เพิ่มแถบการอ้างอิงแหล่งที่มา (`.section-source-citation`) ใต้หัวข้อทั้ง 10 หัวข้อ**:
  - ระบุชื่อหน่วยงาน/องค์กรทางการ พร้อมลิงก์ที่สามารถคลิกตรวจสอบได้ทันที
  - รองรับทั้ง Dark Theme และ Light Theme ด้วย Contrast ที่อ่านง่ายชัดเจน
- **เพิ่มส่วน "ระเบียบวิธีและข้อจำกัดของข้อมูล" (`#methodology`)**:
  - ชี้แจงรอบเวลาและฐานข้อมูลอ้างอิง (ปีการศึกษา 2566 และปีงบประมาณ 2567)
  - ระบุข้อกำหนดแบบจำลองเชิงสาธิต (Simulated Model Notice) สำหรับ TU 2034 Strategy Cockpit
  - ชี้แจงขอบเขตประชากรและเกณฑ์การจัดอันดับสากล
- **สร้างและตรวจสอบชุดข้อมูล Flourish 10 ชุด**:
  - อัปเดต `generate_flourish_datasets.py` ให้ดึงข้อมูลตรงจาก `data/data.json`
  - สร้างไฟล์ CSV 10 ชุดใน `flourish_data/`
- **ระบบตรวจสอบความสมบูรณ์ของข้อมูล (`qa/check_data.py`)**:
  - ตรวจสอบความถูกต้องทางคณิตศาสตร์ 100% ระหว่าง `data.json`, `index.html` และชุดข้อมูล CSV ทุกไฟล์
- **บันทึกภาพถ่ายหน้าจอ Phase 2**:
  - แคปภาพ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 65 รูปใน `qa/phase2_screens/`

---

## [Phase 1] - 2026-10-22 (Repo Restructuring & Cleanliness)

### สรุปการเปลี่ยนแปลง:
- **แยกสถาปัตยกรรม Monolithic String ใน `index.html`**:
  - `index.html` (Semantic HTML5 ลดลงจาก 5,901 บรรทัดเหลือ 1,329 บรรทัด)
  - `assets/css/style.css` (สไตล์ทั้งหมด 3,023 บรรทัด)
  - `assets/js/app.js` (ตรรกะและการแสดงผลกราฟทั้งหมด 1,546 บรรทัด)
  - `data/data.json` (แหล่งข้อมูลศูนย์กลางพร้อม `source_id` และ `as_of`)
- **การจัดการไฟล์ Legacy Build**:
  - ย้าย `build_full_story.py`, `build_v2_bidwells.py`, `build_v2_html.py` ไปไว้ใน `archive/legacy_build/`
  - สร้าง `archive/legacy_build/README.md` กำชับข้อห้ามรันสคริปต์
- **การทำความสะอาด Assets ที่ไม่ใช้งาน**:
  - ย้ายไฟล์ขยะ 18 ไฟล์ (รูปรถยนต์, แผนที่ UK motorsport, ภาพคัดลอกซ้ำ รวม 3.67 MB) ไปไว้ใน `archive/unused_assets/`
  - เหลืองานภาพจริงเพียง 8 ไฟล์หลักใน `assets/`
- **การปรับปรุงการแคช**:
  - ลบแท็ก `<meta http-equiv="Cache-Control|Pragma|Expires">` ที่บังคับ no-cache/no-store
- **การปรับปรุงเอกสาร**:
  - ปรับปรุง `README.md` ใหม่ทั้งหมด ให้สะท้อนเทคโนโลยีจริง (Chart.js 4.4.1, Leaflet 1.9.4) และข้อมูลที่ยืนยันแล้ว
- **การตรวจสอบความถอยหลัง (Regression Check)**:
  - แคปภาพเปรียบเทียบ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 60 รูปใน `qa/phase1_screens/` เทียบกับ `qa/baseline_screens/` แสดงผลตรงกัน 100%

---

## [Phase 0.5] - 2026-10-22 (Data Verification & Fact-Check Protocol)

### สรุปการเปลี่ยนแปลง:
- ตรวจสอบข้อเท็จจริง 22 รายการผ่านแหล่งข้อมูลทางการ (ระดับ A/B)
- บันทึกใน `qa/DATA_VERIFICATION.md`
- ค้นพบข้อเท็จจริงสำคัญ:
  - ขนาดเตียง รพ.สนาม แท้จริงคือ 308 เตียง (DLUXX) โดยมีผู้ป่วยสะสม 3,083 ราย
  - โครงการ Solar Rooftop ของ มธ. มีขนาด 15 MWp บน 44 อาคาร (กฟผ./Solartron)
  - อันดับ QS Asia 2025 คืออันดับที่ 128 ในเอเชีย (อันดับ 4 ของไทย) ส่วน Top 70 คือเป้าหมายยุทธศาสตร์
  - คะแนน THE Impact Rankings SDG 11 คือ 84.1 คะแนน (อันดับ 38 ของโลก) และคว้าอันดับ 1 ของโลกใน SDG 16
  - สรุปตัวเลขนักศึกษาหญิง 26,738 คน (62.4%) และชาย 16,112 คน (37.6%) รวมเป็น 42,850 คน (100.0%)

---

## [Phase 0] - 2026-10-22 (Comprehensive System Audit)

### สรุปการเปลี่ยนแปลง:
- จัดทำเอกสาร `AUDIT.md` ระบุจุดขัดแย้งของข้อมูล (ISS-01 ถึง ISS-13)
- ตรวจสอบรายการข้ออ้างที่ต้องมีแหล่งยืนยัน
- บันทึกไฟล์ Assets ที่ตกค้างและปัญหาด้านการเข้าถึง (A11y/Scroll)

---

## [Phase -1] - 2026-10-22 (Baseline Recording)

### สรุปการเปลี่ยนแปลง:
- สร้าง Git Tag `v1-baseline` บนคอมมิตเดิมของ `main`
- สร้าง Branch `polish-v2`
- รัน Lighthouse Mobile (Performance: 44, Accessibility: 79, Best Practices: 96, SEO: 91)
- รัน Lighthouse Desktop (Performance: 78, Accessibility: 81, Best Practices: 96, SEO: 91)
- บันทึกผลใน `qa/baseline_lighthouse.json`
- สร้าง `qa/FEATURE_PARITY.md` สแกน Event Listener 63 จุด, 32 JS Functions, และ Modal 8 รายการ
- แคปภาพ Baseline 60 รูป ครอบคลุม 12 ฉากที่ 5 Breakpoints
