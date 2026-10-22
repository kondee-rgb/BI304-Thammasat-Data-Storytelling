# คำเตือน: ห้ามรันสคริปต์ในโฟลเดอร์นี้ (Do NOT Run Legacy Build Scripts)

ไฟล์ในโฟลเดอร์นี้ (`build_full_story.py`, `build_v2_bidwells.py`, `build_v2_html.py`) เป็นสคริปต์ในอดีต (Legacy) ที่สร้างไฟล์ `index.html` แบบ Monolithic String ก้อนเดียว และมีการเขียนทับตัวเอง 

**ข้อห้ามสำคัญ**:
- **ห้ามรันสคริปต์ในโฟลเดอร์นี้เด็ดขาด** เพราะจะทำให้ไฟล์ `index.html`, CSS, JS และ Data ที่แยกโครงสร้างและพัฒนาแล้วถูกเขียนทับด้วยเวอร์ชันเก่า
- โครงสร้างปัจจุบันของโปรเจกต์ถูกแยกเป็นโมดูลาร์เรียบร้อยแล้ว:
  - `index.html` (Semantic HTML)
  - `assets/css/style.css` (Stylesheets & Tokens)
  - `assets/js/app.js` (JavaScript Logic & Interactive Visualizations)
  - `data/data.json` (Single Source of Truth)
