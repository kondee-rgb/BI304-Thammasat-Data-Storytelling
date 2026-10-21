# คู่มือการใช้งาน Flourish (flourish.studio) สำหรับโปรเจกต์ BI304
**หัวข้อ: 90 ปี ธรรมศาสตร์: จากตลาดวิชาสู่นวัตกรรมความยั่งยืนระดับโลก**

---

## 🌟 1. วิธีสร้าง Flourish Story (ตามที่อาจารย์แนะนำในวิชา BI304)
Flourish เป็นเครื่องมือ Data Storytelling ระดับโลก (No-Code / High-Interactivity) ที่แปลงข้อมูลตารางเป็นเรื่องเล่าเคลื่อนไหวได้อัตโนมัติ

### ขั้นตอนการทำ Story ใน Flourish:
1. เข้าเว็บไซต์ [https://flourish.studio](https://flourish.studio) (ล็อกอินด้วย Google Account หรือ TBS Email)
2. คลิก **"+ New visualisation"**
3. เลือกเทมเพลตที่ต้องการตามแต่ละฉาก:
   - **ฉากที่ 1 & การเติบโตของคณะ:** เลือกเทมเพลต **"Bar chart race"** -> อัปโหลดไฟล์ `01_flourish_bar_chart_race_faculties.csv`
   - **ฉากที่ 2 แผนที่ 4 ศูนย์:** เลือกเทมเพลต **"Marker map"** หรือ **"Projection map"** -> อัปโหลดไฟล์ `02_flourish_campuses_map.csv`
   - **ฉากที่ 3 โครงสร้าง 19 คณะ:** เลือกเทมเพลต **"Treemap"** หรือ **"Hierarchy"** -> อัปโหลดไฟล์ `03_flourish_hierarchy_clusters.csv`
   - **ฉากที่ 4 ประชากรและความเท่าเทียม:** เลือกเทมเพลต **"Bar chart (grouped/stacked)"** -> อัปโหลดไฟล์ `04_flourish_demographics_gender.csv`
   - **ฉากที่ 7 อันดับโลก QS Rankings:** เลือกเทมเพลต **"Line chart"** -> อัปโหลดไฟล์ `05_flourish_rankings_time_series.csv`
   - **ฉากที่ 8 สมรรถนะความยั่งยืน SDGs:** เลือกเทมเพลต **"Radar chart"** -> อัปโหลดไฟล์ `06_flourish_sdg_scores.csv`
4. เมื่อสร้างแต่ละ Visualisation เสร็จ ให้กดปุ่ม **"Create a story"** (มุมขวาบน)
5. ใน Story Editor:
   - กด **"+ New slide"** เพื่อเพิ่มฉากที่ 1 ถึง 10
   - แต่ละสไลด์ให้ใส่ข้อความ **Caption / Headline** ตาม Storyboard ของเรา
   - ตั้งค่าการเคลื่อนไหว (Animation duration) และลูกศรเลื่อนสไลด์
6. กด **"Export & publish"** -> จะได้ลิงก์ Embed หรือ HTML เพื่อนำมาเปิดนำเสนอได้ทันที!

---

## 📊 2. ชุดไฟล์ CSV ในโฟลเดอร์นี้
| ชื่อไฟล์ | เทมเพลต Flourish ที่แนะนำ | ข้อมูลที่แสดง |
| :--- | :--- | :--- |
| `01_flourish_bar_chart_race_faculties.csv` | **Bar chart race** | การเติบโตของจำนวนนักศึกษาแต่ละคณะตั้งแต่ พ.ศ. 2477 - 2569 |
| `02_flourish_campuses_map.csv` | **Marker map** | พิกัด ละติจูด ลองจิจูด ขนาดไร่ และจำนวนนักศึกษา 4 ศูนย์ มธ. |
| `03_flourish_hierarchy_clusters.csv` | **Treemap / Sunburst** | สัดส่วน 19 คณะใน 4 คลัสเตอร์วิชาการ |
| `04_flourish_demographics_gender.csv` | **Grouped / Stacked Bar** | ความหลากหลายทางเพศ ชาย vs หญิง (62%) รายกลุ่มสาขา |
| `05_flourish_rankings_time_series.csv` | **Line chart** | อันดับโลก QS Asia และสาขา Business & Management |
| `06_flourish_sdg_scores.csv` | **Radar chart** | คะแนนสมรรถนะความยั่งยืน UN SDGs เทียบค่าเฉลี่ยโลก |
