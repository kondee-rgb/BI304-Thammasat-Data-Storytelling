# บันทึกการเปลี่ยนแปลงของระบบ (Project Changelog)

## [Flourish Hub & CSV Repository Upgrade] - 2026-10-22 (Live Interactive Chart Preview & 1-Click CSV Downloads for 10 Scenes)

### สรุปการแก้ไขและพัฒนาฟีเจอร์ Flourish Hub ตามคำขอของผู้ใช้:
1. **แก้ปัญหา "กด Flourish แล้วไม่ขึ้นอะไร" (Live Interactive Visual Chart Preview)**:
   - ฝังตัวเอนจินแสดงผลกราฟสด (Live Interactive Canvas Chart Preview) ผ่าน Chart.js ในกล่องพรีวิวของ Flourish Hub Modal สำหรับครบทั้ง 10 ฉาก (Scenes 1 ถึง 10)
   - แต่ละฉากแสดงชาร์ตจริงที่ตรงกับเทมเพลตของ Flourish อย่างสวยงาม มีปฏิสัมพันธ์ (Hover Tooltips, Milestones, Dual Y-Axis, Stacked Bar, Inverted Ranks, Radar Benchmark)
   - เมื่อคลิกเปลี่ยนแท็บฉากใด ชาร์ตจะถูกเรนเดอร์ใหม่ทันทีอย่างราบรื่น ไม่ว่างเปล่าอีกต่อไป
2. **ระบบดาวน์โหลดไฟล์ CSV สำหรับอัปโหลดขึ้น Flourish Studio ด้วยตัวเอง (1-Click CSV Downloads)**:
   - เพิ่มปุ่มดาวน์โหลดไฟล์ CSV หลักของแต่ละฉากแบบเด่นชัด (สีแดงเลือดหมู Thammasat Crimson): `📥 ดาวน์โหลด CSV: [ชื่อไฟล์]`
   - มีปุ่มดาวน์โหลดไฟล์เสริม (Secondary Dataset) สำหรับฉากที่มีข้อมูลหลายมุมมอง (เช่น Bar Chart Race, GIS Coordinates, Triple Crown Business Schools, 4 Centennial Pillars)
   - เพิ่มปุ่มเปิดตรงสู่แม่แบบที่แนะนำบน Flourish Studio (เช่น Line Chart, Marker Map, Hierarchy Treemap, Sankey, Radar, Cards)
   - เพิ่มปุ่มดาวน์โหลดชุดข้อมูล CSV ครบทั้ง 10 ฉากในไฟล์ ZIP เดียว (`thammasat_flourish_all_scenes.zip`) บนแถบ Header ของโมดอล
3. **การ์ดแนะนำวิธีใช้งาน 3 ขั้นตอนง่ายๆ (3-Step Quick Guide)**:
   - แสดงวิธีนำเข้าไฟล์ CSV ใน Flourish Studio แบบเป็นขั้นตอน:
     1. ดาวน์โหลดไฟล์ CSV
     2. เปิดเทมเพลตบน Flourish Studio
     3. กดแท็บ Data > Upload data file
4. **ตารางพรีวิวข้อมูลจริง (Raw Data Table Preview)**:
   - อัปเดตคอลัมน์และข้อมูลตัวอย่างให้ตรงกับไฟล์ `.csv` จริงทุกประการ
5. **การทดสอบความถูกต้อง**:
   - ตรวจสอบผ่าน Puppeteer: เปิดโมดอลได้สมบูรณ์, เรนเดอร์ครบ 10 ฉาก, ลิงก์ดาวน์โหลดถูกต้องทุกไฟล์, JavaScript Console 0 Errors

---

## [Header Navigation Scrollbar Polish] - 2026-10-22 (Native Horizontal Scrollbar at Bottom of Tab Bar)

### สรุปการปรับปรุงแถบนำทางส่วนหัวตามคำขอของผู้ใช้:
1. **เอาปุ่มลูกศรออกทั้งหมด (Remove Arrow Buttons Completely)**:
   - ลบปุ่มลูกศร `#navScrollPrev` และ `#navScrollNext` ออกจากโครงสร้าง HTML, CSS และ JavaScript
2. **เปลี่ยนเป็นแท็บสกรอลล์แนวนอนด้านล่าง (Horizontal Scrollbar under Nav Tabs)**:
   - ปรับสไตล์ของแถบเมนู `.header-nav` ให้มี Scrollbar แนวนอนสีแดงชาด (Thammasat Crimson) ชัดเจนด้านล่างแท็บเมนู
   - ทำงานเหมือนแท็บสกรอลล์ด้านข้างของเว็บไซต์ทั่วไป (คลิกเมาส์ค้างแล้วลาก Thumb แนวนอนได้ทันที)
   - รองรับ WebKit Custom Scrollbar (`height: 6px;`) บน Chrome/Edge/Safari และ `scrollbar-width: thin;` บน Firefox
3. **ระบบเลื่อนอัจฉริยะ (Smart Scrolling)**:
   - **Mouse Wheel**: ชี้เมาส์ไปที่แถบเมนูแล้วหมุนลูกกลิ้งเมาส์ (Vertical Scroll) เพื่อเลื่อนซ้าย-ขวาได้อย่างนุ่มนวล
   - **Click & Drag (Grab to Scroll)**: คลิกเมาส์ค้างแล้วลากเนื้อหาแถบเมนูได้อิสระ
   - **Auto-Scroll Active Tab**: เมื่อเลื่อนหน้าเว็บลงมาถึงหัวข้อใด หัวข้อนั้นจะเลื่อนเข้ามาอยู่กึ่งกลางสายตา พร้อมตัวสกรอลล์ด้านล่างเลื่อนตามให้อัตโนมัติ ครบทั้ง 10 หัวข้อ
4. **การทดสอบความเข้ากันได้**:
   - ผ่านการทดสอบ Puppeteer บนความละเอียด 1366x768 และมือถือ 390px (0 Errors) ไม่พบล้นจอ

---

## [Motion Polish] - 2026-10-22 (Bidwells-Style Editorial Scroll Reveal Motions)

### สรุปการปรับปรุงระบบการเคลื่อนไหวตามสไตล์ Bidwells Research Report:
1. **วิเคราะห์โมชั่นจากคลิปวิดีโอ Bidwells (`Driving innovation at speed _ UK Motorsport Cluster`)**:
   - การเลื่อนของกราฟและองค์ประกอบเนื้อหาใช้การสไลด์นุ่มนวลตามทิศทางเลย์เอาต์ (Slide Up, Slide Left จากขวา, Slide Right จากซ้าย และ Scale Zoom เล็กน้อย)
   - ใช้เส้นโค้งความเร่งแบบพรีเมียม (Decelerated Luxury Easing): `cubic-bezier(0.16, 1, 0.3, 1)` ระยะเวลา 0.85s - 0.95s พร้อม `will-change: transform, opacity`
   - กำหนดจังหวะการเลื่อนแบบต่อเนื่อง (Staggered Entrance): `.tu-stagger-1` ถึง `.tu-stagger-4` (หน่วงเวลาทีละ 0.12s) เพื่อให้การ์ดสถิติไม่กระแทกเข้ามาพร้อมกันหมดในคราวเดียว
2. **การทำงานประสานกันระหว่าง Chart Drawing Animation และ Scroll Intersection**:
   - เชื่อมต่อ `IntersectionObserver` ในฟังก์ชัน `initBidwellsScrollMotions()`: เมื่อเลื่อนหน้าจอมาถึงการ์ดกราฟ (Threshold 0.15) ตัวกราฟิกการ์ดจะค่อยๆ สไลด์เข้ามา
   - สั่ง `chart.reset()` และ `chart.update()` แบบไดนามิกผ่าน `Chart.getChart(canvas)` ทำให้แท่งกราฟ เส้นโค้ง และเรดาร์ค่อยๆ ยืด/วาดขึ้นพร้อมกับที่การ์ดสไลด์เข้ามาในมุมมอง (ครอบคลุมทั้ง 6 ชาร์ตสำคัญ: TCAS, Demographics, Campus Shift, 5-Year Budget, Green Energy และ Hospital Capacity)
   - เชื่อมต่อกับตัวเลขนับขึ้น (`stat-counter`) ให้นับขึ้นพร้อมกันอย่างสมบูรณ์แบบ
3. **การเพิ่มประสิทธิภาพการแสดงผลบนโทรศัพท์มือถือ (Mobile Responsive Containment)**:
   - สลับแอนิเมชันจากการสไลด์ซ้าย-ขวาเป็นการสไลด์ขึ้นแนวดิ่งบนจอเล็ก (`max-width: 768px`) เพื่อป้องกันอาการหน้าจอกว้างเกินหรือเกิด Horizontal Scrollbar
   - แก้ไขโครงสร้าง Offscreen Navigation Drawer และองค์ประกอบล้นจอ ทำให้บนหน้าจอ iPhone (375px, 390px, 414px) มี `overflow: false` 100%
   - รองรับ `prefers-reduced-motion` เพื่อการเข้าถึงที่เป็นมิตรต่อผู้ใช้งานทุกคน
4. **ผลการทดสอบ Lighthouse & Automation**:
   - Desktop Performance: **89 คะแนน**
   - Desktop Accessibility: **86 คะแนน**
   - Best Practices: **100 คะแนนเต็ม**
   - SEO: **100 คะแนนเต็ม**
   - ไม่พบข้อผิดพลาดใน JavaScript Console (`0 errors`)

---

## [Quick Fix] - 2026-10-22 (User Feedback: Remove Methodology & Fix Dome Image Path)

### สรุปการแก้ไขตามคำขอของผู้ใช้:
1. **เอาส่วน "ระเบียบวิธีและข้อจำกัดของข้อมูล" (`#methodology`) ออกตามที่ผู้ใช้ระบุในภาพที่ 1**:
   - ลบส่วน `#methodology` ออกจาก `index.html` เพื่อให้ดีไซน์หน้าเว็บสะอาด สบายตา และเชื่อมต่อไปยังการ์ดบทสรุป 9 ทศวรรษได้อย่างลงตัว
   - อัปเดตรายการ sections ใน `assets/js/app.js` ให้ข้ามไปยัง `#finish` ทันที
2. **แก้ไขรูปภาพตึกโดม ท่าพระจันทร์ ไม่แสดงผล (`.editorial-photo-frame`) ในหัวข้อ 01 ตามภาพที่ 2**:
   - แก้ไข Relative Path ใน `assets/css/style.css` จาก `url('assets/...')` เป็น `url('../...')` ให้สอดคล้องกับตำแหน่งไฟล์ CSS
   - เพิ่มแท็ก `<img src="assets/tha_prachan_dome_editorial.webp" ...>` ภายใน `.editorial-photo-frame` พร้อม `onerror` fallback ทำให้ภาพแสดงผลคมชัด 100%

---

## [Phase 9] - 2026-10-22 (QA, Performance & Release Gate Verification)

### สรุปการเปลี่ยนแปลง:
- **เพิ่มประสิทธิภาพการโหลดและ SEO สู่ระดับ 100 เต็ม (Perfect SEO 100)**:
  - เพิ่ม Primary Meta Tags (Title, Description, Keywords, Author, Theme-Color)
  - เพิ่ม Open Graph Tags สำหรับการแชร์บน Social Media (`og:title`, `og:description`, `og:image`, `og:locale`)
  - สร้างไฟล์ไอคอน Favicon เวกเตอร์ `assets/tu_favicon.svg` (ยอดตึกโดมสีทอง-แดงชาด)
  - กำหนด `defer` บนสคริปต์ภายนอกทั้งหมด (Chart.js, Leaflet, Confetti) ช่วยปลดล็อกการประมวลผล HTML
- **ผลการทดสอบประสิทธิภาพ Google Lighthouse**:
  - **Desktop Performance**: ทะยานแตะ **90 คะแนน (สีเขียว)** จากเดิม 78 (+12 จุด)
  - **Desktop Accessibility**: แตะ **86 คะแนน** จากเดิม 81 (+5 จุด)
  - **Desktop SEO**: แตะ **100 คะแนนเต็ม** จากเดิม 91 (+9 จุด)
  - **Mobile SEO**: แตะ **100 คะแนนเต็ม** จากเดิม 91 (+9 จุด)
  - **Best Practices**: คงที่ในระดับสูงที่ **96 คะแนน** ทั้ง Mobile และ Desktop
- **ตรวจสอบการทำงานและความเข้ากันได้ (Feature Parity & Release Gate)**:
  - ผ่านการทดสอบฟังก์ชัน JavaScript ทั้ง 32 ฟังก์ชัน ครบ 100%
  - ผ่านการทดสอบความถูกต้องของข้อมูล `qa/check_data.py` (0 Errors, 0 Warnings)
  - จัดทำรายงานสรุปฉบับสมบูรณ์ใน `qa/FINAL_REPORT.md`
- **บันทึกภาพถ่ายหน้าจอและพร้อมสำหรับการส่งมอบ**:
  - เก็บโค้ดทั้งหมดบน Branch `polish-v2` อย่างปลอดภัย พร้อมให้ผู้ใช้ตรวจทานก่อน Merge เข้าสู่ `main`

---

## [Phase 8] - 2026-10-22 (Hero Theme - Approach A Implementation)

### สรุปการเปลี่ยนแปลง:
- **ปรับธีม Hero Section สู่จิตวิญญาณแห่งธรรมศาสตร์ (Approach A: River of Wisdom & Centennial Timeline Arc)**:
  - ยกเลิกอุปมาการแข่งขันความเร็ว (Racing Curb / Checkered Asphalt)
  - เปลี่ยนผ่านสู่สายธารแห่งกาลเวลาและปัญญา (Chao Phraya River & Centennial Timeline Arc 2477 — 2577)
  - เส้นแนวแกนกลางปรับเป็นลำธารสะท้อนแสงสีทองอร่ามและขอบสีแดงชาดอันสง่างาม
  - หมุดหมายทางประวัติศาสตร์ปรับเป็น: 2477 (ปฐมบทตลาดวิชา มธก.), 2567 (วาระ 90 ปีแห่งเกียรติภูมิ)
- **ปรับปรุงหัวข้อหลัก (Headings & Mission Statement)**:
  - H1 ภาษาอังกฤษ: `Shaping Future Through Wisdom`
  - ชื่อเรื่องภาษาไทย: `90 ปี ธรรมศาสตร์: พลังแห่งปัญญา สู่ศตวรรษแห่งความยั่งยืน`
  - แท็กหมวดหมู่: `รายงานวิจัยและยุทธศาสตร์ข้อมูลวาระ 90 ปี • 2477 — 2567`
  - ปุ่มนำทาง: `เริ่มต้นสำรวจรายงาน` เชื่อมต่อไปยัง Executive Summary 3 มิติสำคัญ
- **เพิ่มประสิทธิภาพ LCP (Largest Contentful Paint)**:
  - เพิ่มแท็ก `<link rel="preload" as="image" href="assets/tu_student_walking.webp" type="image/webp" fetchpriority="high">` ใน `<head>`
  - กำหนด `fetchpriority="high"` บนรูปภาพนักศึกษาใน Hero Section เพื่อการเรนเดอร์ที่รวดเร็วทันใจ
- **บันทึกภาพถ่ายหน้าจอ Phase 8**:
  - แคปภาพ 5 Breakpoints (360px, 390px, 768px, 1024px, 1440px) ครบ 70 รูปใน `qa/phase8_screens/`

---

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
