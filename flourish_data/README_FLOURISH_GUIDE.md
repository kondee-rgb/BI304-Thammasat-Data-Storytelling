# คู่มือการใช้งาน Flourish (flourish.studio) สำหรับโปรเจกต์ BI304
**หัวข้อ: 90 ปี ธรรมศาสตร์: จากตลาดวิชาสู่นวัตกรรมความยั่งยืนระดับโลก**
**ชุดข้อมูลครบถ้วน 10 ฉาก (Scenes 1 - 10) ตรงตาม Storyboard 1:1**

---

## 🌟 1. วิธีสร้าง Flourish Story ครบ 10 ฉาก
Flourish เป็นเครื่องมือ Data Storytelling ระดับโลก (No-Code / High-Interactivity) ใช้งานฟรี 100% ไม่เสียค่าบริการ และไม่ต้องกรอกบัตรเครดิต

### ขั้นตอนการสร้างแต่ละ Visualisation ใน Flourish:
1. เข้าเว็บไซต์ [https://flourish.studio](https://flourish.studio)
2. คลิก **"+ New visualisation"**
3. เลือกเทมเพลตที่ตรงกับฉากนั้นๆ (ดูตารางข้อ 2)
4. คลิกแท็บ **"Data"** ด้านบน -> กดปุ่ม **"Upload data"** แล้วเลือกไฟล์ CSV ของฉากนั้นๆ
5. แมปคอลัมน์ (Column bindings) ตามที่ระบุในตารางด้านล่าง
6. คลิกแท็บ **"Preview"** เพื่อปรับแต่งสี (Colors: เหลืองมธ. `#F7C800` แดงมธ. `#D13438`) และใส่หัวข้อ (Header/Title)
7. ทำครบทั้ง 10 ฉาก (หรือเลือกฉากเด่นๆ ที่ต้องการนำเสนอ)

### ขั้นตอนการร้อยเรียงเป็น 10-Scene Flourish Story:
1. ที่หน้าหลัก Flourish คลิก **"+ New story"**
2. เลือก Visualisation ที่ทำไว้ทีละฉากใส่ลงใน Slide (สไลด์ที่ 1 ถึง 10)
3. ใส่ **Caption / Headline** เล่าเรื่องตามบทพากย์ใน Storyboard
4. ปรับ Transition (การเลื่อนเปลี่ยนฉากแบบ Smooth Animation)
5. กดปุ่ม **"Export & publish"** มุมขวาบน -> เลือก **"Publish to make public and get link"**
6. คัดลอกลิงก์ Story ส่งให้อาจารย์ หรือนำรหัส Embed Code มาใส่ในเว็บไซต์ Scrollytelling ได้ทันที!

---

## 📊 2. ตารางแมปไฟล์ CSV ทั้ง 10 ฉาก กับ Flourish Template

| ฉากที่ | ชื่อไฟล์ CSV | เทมเพลต Flourish ที่ต้องเลือก | Column Bindings ใน Flourish Data Tab |
| :---: | :--- | :--- | :--- |
| **1** | `01_flourish_scene1_student_growth.csv` | **Line chart** หรือ **Bar chart race** | **X / Labels:** Year_BE<br>**Values:** Total_Students, Law_and_Politics, Business_and_Econ |
| **2** | `02_flourish_scene2_campus_locations.csv` | **Marker map** | **Latitude:** Latitude<br>**Longitude:** Longitude<br>**Size:** Area_Rai หรือ Students_Count<br>**Name / Label:** Campus_Name_TH |
| **3** | `03_flourish_scene3_faculty_hierarchy.csv` | **Treemap** หรือ **Hierarchy (Sunburst)** | **Level 1 (Parent):** Cluster_Name<br>**Level 2 (Child):** Faculty_Name_TH<br>**Value / Size:** Student_Count |
| **4** | `04_flourish_scene4_gender_diversity.csv` | **Bar chart (Grouped / Stacked)** | **Labels:** Discipline_Group<br>**Values:** Female_Percentage, Male_Percentage |
| **5** | `05_flourish_scene5_migration_flow_sankey.csv` | **Sankey diagram** | **Step 1 (Source):** Source_Node<br>**Step 2 (Target):** Target_Node<br>**Value:** Student_Flow_Value |
| **6** | `06_flourish_scene6_budget_waterfall.csv` | **Bar chart (Waterfall / Column)** | **Labels:** Revenue_Source<br>**Values:** Amount_Million_THB |
| **7** | `07_flourish_scene7_rankings_trend.csv` | **Line chart** หรือ **Slope chart** | **X / Time:** Year_AD<br>**Lines:** QS_World_Rank, QS_Asia_Rank, TBS_Subject_Rank |
| **8** | `08_flourish_scene8_sdg_radar.csv` | **Radar chart** | **Categories:** SDG_Goal<br>**Values:** Thammasat_Score, Global_Benchmark |
| **9** | `09_flourish_scene9_hospital_growth.csv` | **Line chart** หรือ **Bar & Line (Dual axis)** | **X:** Year_BE<br>**Bar Value:** Outpatient_Visits<br>**Line Value:** Hospital_Beds |
| **10** | `10_flourish_scene10_strategic_gauges.csv` | **Cards** หรือ **Gauge / Progress** | **Metric Name:** KPI_Name<br>**Current:** Current_Value<br>**Target:** Target_Value |

---

## 🔒 3. การันตีเรื่องความเป็นส่วนตัว (Privacy) และฟรีตลอดชีพ
1. **ฟรี 100% ตลอดไป:** Flourish มี Public Tier ที่ฟรีตลอดชีพ ไม่ต้องใส่บัตรเครดิต สามารถ Publish Story และรับลิงก์ได้ไม่จำกัด
2. **ความปลอดภัยของข้อมูลส่วนตัว:**
   - ชุดข้อมูลทั้งหมดในโฟลเดอร์นี้เป็นข้อมูลสถิติมหาวิทยาลัย ไม่ใช่ข้อมูลส่วนตัวของนักศึกษา
   - ลิงก์ที่แชร์ให้อาจารย์เป็น Public Presentation Link ซึ่งแสดงเฉพาะตัวกราฟและสไลด์นำเสนอเท่านั้น ผู้ชมคนอื่นหรืออาจารย์**ไม่สามารถ**เข้าถึงบัญชีส่วนตัว Google, รหัสผ่าน หรือไดรฟ์ส่วนตัวของผู้ทำได้ 100%
