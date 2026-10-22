# บันทึกการเปลี่ยนแปลงของระบบ (Project Changelog)

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
