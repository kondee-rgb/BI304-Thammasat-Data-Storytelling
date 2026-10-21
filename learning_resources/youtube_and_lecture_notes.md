# บันทึกเนื้อหาการเรียนรู้: YouTube Folium & BI304 Class Lecture Summary

## 1. วิดีโอสอน: "Start Creating Web Maps With Python Folium" (YouTube: X8CoVymMOLw)
- **จุดมุ่งหมาย:** เข้าใจหลักการทำงานของ Folium ซึ่งเป็น Python Wrapper ของไลบรารี Leaflet.js
- **เทคนิคสำคัญ:**
  1. การสร้าง Map Object: `m = folium.Map(location=[lat, lng], zoom_start=x, tiles='...')`
  2. การเลือกใช้ Tilesets: OpenStreetMap, Stamen, หรือ CartoDB เพื่อให้แผนที่มีสไตล์มินิมอล รองรับการแสดงผลเลเยอร์ข้อมูล
  3. การเพิ่ม Marker และ Popup: 
     ```python
     folium.Marker(
         location=[lat, lng],
         popup="HTML formatted info",
         icon=folium.Icon(color='red', icon='info-sign')
     ).add_to(m)
     ```
  4. การเพิ่ม LayerControl และ MiniMap เพื่อให้ผู้ใช้สามารถสำรวจแผนที่ได้สะดวก
  5. การส่งออกเป็นไฟล์เดี่ยวแบบ `.html` เพื่อนำไปฝัง (Embed) บนหน้าเว็บไซต์หรือ Scrollytelling

---

## 2. วิดีโอบันทึกการสอนในห้องเรียน: `Online-20261016_101910-Meeting Recording.mp4`
- **ช่วงต้น (0-20 นาที): ภาพรวมของ Data Visualization Tools**
  - แยกความแตกต่างระหว่าง Data Exploration (วิเคราะห์ค้นหาคำตอบใน Python) กับ Data Storytelling (เล่าให้ผู้บริหาร/บุคคลทั่วไปเข้าใจและตัดสินใจได้)
  - Edward Tufte's Rules: Maximize Data-Ink Ratio, ห้ามใส่เส้นกริดลายตา, ห้ามต่อเส้นในกราฟแท่งแบบไม่มีความหมาย, หลีกเลี่ยง 3D Scatter Plot
  - กฎ LATCH: 5 วิธีในการจัดระเบียบข้อมูล

- **ช่วงกลาง (20-40 นาที): การเขียนโค้ดและ Geospatial Analysis**
  - อาจารย์สาธิตการใช้ **Google Colab** ควบคู่กับ **Gemini AI** เพื่อร่างโค้ดวิเคราะห์ข้อมูล
  - จัดการข้อมูลพิกัด (Coordinates, Lat/Lng) เพื่อเตรียมเข้าสู่ Kepler.gl และ Folium
  - แก้ไขปัญหา OpenStreetMap 403 Access Blocked ใน Colab ด้วยการสลับไปใช้ CartoDB Positron หรือ Leaflet standalone

- **ช่วงปลาย (40-55 นาที): การสร้าง Dashboard & Storyboard**
  - การเขียน Streamlit dashboard: สร้าง dropdown, filter, วาดกราฟเส้น Plotly พร้อมใส่เส้น benchmark (`fig.add_hline(y=100, line_dash='dash')`)
  - โครงสร้าง Storyboard: จำลองตัวอย่าง Napoleonic 1812 Campaign แบ่งเป็น 6 ฉาก แต่ละฉากมีชื่อฉาก, Visual description, และ Caption ดำเนินเรื่องที่กระชับ ตรงประเด็น
  - มอบหมายงานกลุ่ม: นำเสนอวันที่ 30 ต.ค. สรุปเป็น Storyboard (PDF) และ Scrollytelling (Web) มี 10 Visualizations ร้อยเรียงเรื่องราวธรรมศาสตร์
