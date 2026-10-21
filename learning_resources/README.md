# BI304: แหล่งเรียนรู้และคู่มือการทำ Data Scrollytelling
**วิชา BI304: การเสริมพลังแก่ข้อมูลผ่านการเล่าเรื่องและการแสดงภาพ (Empowering Data Through Storytelling and Visualization)**  
*คณะพาณิชยศาสตร์และการบัญชี มหาวิทยาลัยธรรมศาสตร์ (Thammasat Business School - TBS)*  
*อาจารย์ผู้สอน: อ.ดร. นภธนิตย์ โชติสาร (Noptanit Chotisarn)*

---

## 📌 1. โครงสร้างการส่งงาน (Group Assignment Overview)
- **วันนำเสนอ:** วันที่ 30 ของแต่ละห้องเรียน
- **รูปแบบกลุ่ม:** ห้องละ 6 กลุ่ม (สมาชิก 10+ คนต่อกลุ่ม)
- **ชิ้นงานหลักที่ต้องส่ง:**
  1. **Storyboard (PDF):** โครงเรื่องและสคริปต์ 10 Visualizations ตามหลัก Data Storytelling (ส่งและนำเสนอก่อนขึ้นเว็บ)
  2. **Data Scrollytelling (Web Application):** เว็บไซต์เล่าเรื่องราวแบบ Scrollytelling ที่มี 10 Visualizations โต้ตอบได้จริง (Interactive)
- **หัวข้อหลัก:** **เรื่องราวของมหาวิทยาลัยธรรมศาสตร์ผ่านข้อมูล (Thammasat University: A Data-Driven Journey)**

---

## 🎥 2. บันทึกการเรียนรู้และลิงก์วิดีโอ (Video & Lecture Hub)
1. **คลิปแนะนำการสร้าง Interactive Web Map ด้วย Python Folium / Leaflet:**
   - URL: [https://www.youtube.com/watch?v=X8CoVymMOLw](https://www.youtube.com/watch?v=X8CoVymMOLw)
   - สาระสำคัญ: การติดตั้ง folium, การสร้างแผนที่อินเทอร์แอคทีฟ, การระบุพิกัด (Coordinates), การใส่ Markers & Popups, และการเลือกใช้ Map Tiles (OpenStreetMap, CartoDB Positron)
2. **วิดีโอบันทึกการสอนในห้องเรียน (โฟลเดอร์ BI304):**
   - ไฟล์: `Online-20261016_101910-Meeting Recording.mp4`
   - อาจารย์สอนหัวข้อ:
     - การประยุกต์ใช้ **Gemini AI ใน Google Colab** ช่วยเขียนโค้ดและวิเคราะห์ข้อมูล
     - การทำ **Geospatial Visualization** (Folium, Kepler.gl, GeoJSON, Arc Layer, 3D Hexbin)
     - การสร้าง **Interactive Dashboard** ด้วย **Plotly** และ **Streamlit** (`st.plotly_chart`, `px.line`, `px.scatter`)
     - การนำเสนอชาร์ตแบบ **Edward Tufte** (Clean Design, Data-Ink Ratio, ห้าม 3D Scatter, ห้ามต่อเส้นมั่ว)
     - ตัวอย่าง **Storyboard** 6 ฉาก (Minard Napoleonic Russia Campaign 1812) สู่การร้อยเรียงเรื่องราว

---

## 📊 3. กฎและกรอบแนวคิดที่ต้องนำมาใช้ (Core Frameworks)

### A. กรอบการจัดระเบียบข้อมูล LATCH (Richard Saul Wurman)
ข้อมูลทุกชนิดในโลกจัดกลุ่มได้ 5 วิธี:
1. **L - Location (สถานที่):** พิกัด 4 ศูนย์การศึกษา (ท่าพระจันทร์, รังสิต, ลำปาง, พัทยา)
2. **A - Alphabet (ตัวอักษร):** การจัดหมวดหมู่คณะ/หน่วยงาน ก-ฮ หรือ A-Z
3. **T - Time (เวลา/ลำดับ):** เส้นทางประวัติศาสตร์ 90+ ปี จาก พ.ศ. 2477 ถึงปัจจุบัน และมุ่งสู่ศตวรรษที่ 1 ในปี 2577 (TU2034)
4. **C - Category (หมวดหมู่):** กลุ่มสาขาวิชา (สังคมศาสตร์-มนุษยศาสตร์, วิทยาศาสตร์และเทคโนโลยี, วิทยาศาสตร์สุขภาพ, นานาชาติ)
5. **H - Hierarchy (ลำดับขั้น/ขนาด):** ขนาดงบประมาณ, จำนวนนักศึกษาในแต่ละคณะ, อันดับมหาวิทยาลัยโลก (Rankings)

### B. กฎการออกแบบภาพข้อมูลของ Edward Tufte (Tufte's Rules)
1. **Show Data:** แสดงข้อมูลที่แท้จริงอย่างโปร่งใส มีตัวเลขและบริบทกำกับ
2. **Use Labels Wisely:** ใส่ Label ชัดเจนที่จุดข้อมูล (Direct Labeling) ลดการพึ่งพา Legend ที่ต้องกวาดสายตาไปมา
3. **Avoid Chartjunk:** ตัดของตกแต่งที่ไม่จำเป็น เส้นตารางที่หนาเกินไป แสงเงา 3D ที่บิดเบือนสเกล
4. **Maximize Data-Ink Ratio:** เพิ่มสัดส่วนหมึกที่ใช้แทนข้อมูลให้มากที่สุดเมื่อเทียบกับหมึกทั้งหมด
5. **Avoid Lie Factor:** สเกลแกน Y ต้องเริ่มต้นที่ 0 สำหรับ Bar Chart และไม่บิดเบือนอัตราส่วนความเปลี่ยนแปลง

---

## 🛠️ 4. แนะนำเครื่องมือ Data Visualization Tools ที่เรียน
| หมวดหมู่ | เครื่องมือ | จุดเด่น | การนำไปใช้ในโปรเจกต์นี้ |
| :--- | :--- | :--- | :--- |
| **Python Libraries** | `Plotly`, `Matplotlib`, `Seaborn` | กราฟิกสถิติ สวยงาม โต้ตอบได้ ซูม/Hover ได้ | ฉาก Time-series, Treemap, Scatter, Waterfall |
| **Geospatial Tools** | `Folium`, `Leaflet.js`, `Kepler.gl` | แผนที่พิกัด ปักหมุด ขอบเขตพื้นที่ และการไหล (Arc) | ฉากแผนที่ 4 ศูนย์ และเส้นทางการย้ายศูนย์รังสิต |
| **Web Dashboard** | `Streamlit`, `Dash` | พัฒนา Web Dashboard ด้วย Python ได้อย่างรวดเร็ว | การสร้างแดชบอร์ดต้นแบบ |
| **Storytelling & Low-Code** | `Flourish`, `Datawrapper`, `RAWGraphs` | สตอรี่เทลลิ่ง แอนิเมชันกราฟิก Sankey/Alluvial | การออกแบบโครงเรื่องและกราฟิกการไหล |

---

## 📁 5. ไฟล์ในโฟลเดอร์นี้
- `folium_map_tutorial.py` : ตัวอย่างโค้ดสร้างแผนที่ 4 ศูนย์ มธ. ด้วย Folium
- `thammasat_campuses_map.html` : ไฟล์แผนที่ HTML ที่เรนเดอร์สำเร็จ
- `youtube_and_lecture_notes.md` : สรุปเนื้อหาการบรรยายและเทคนิคการเขียนโค้ดอย่างละเอียด
