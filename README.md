# 🎓 90 ปี มหาวิทยาลัยธรรมศาสตร์: จากตลาดวิชาเพื่อราษฎร สู่นวัตกรรมความยั่งยืนระดับโลก
### โครงงานวิชา BI304: Data Visualization and Storytelling | Thammasat Business School (TBS)
**อาจารย์ผู้สอน:** ดร. นพธนิศร์ โชติสาร (Dr. Noptanit Chotisarn)  
**กำหนดการนำเสนอ:** วันที่ 30 ตุลาคม (ห้องละ 6 กลุ่ม | กลุ่มละ 10+ คน)

---

## 🌐 ลิงก์สำหรับเข้าชมและตรวจงานออนไลน์ (Live Deployment)
ไม่ต้องรันโค้ดหรือติดตั้งโปรแกรมใดๆ สามารถคลิกดูผลงาน Scrollytelling และ Flourish Story ได้ทันทีบนทุกอุปกรณ์:  
👉 **[https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/](https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/)**

---

## 📋 สรุปรายการสิ่งที่ต้องส่งตามเกณฑ์วิชา BI304 (Submission Deliverables Checklist)

| ลำดับ | สิ่งที่ต้องส่ง | รูปแบบไฟล์ / ลิงก์ | รายละเอียด |
|:---:|:---|:---|:---|
| **1** | **Storyboard (ฉบับสมบูรณ์)** | `Storyboard_Thammasat_BI304.pdf` | โครงร่างเรื่องราว 5 หน้า ตามแบบจำลอง Minard (1812 Napoleonic Campaign) ครบ 10 ฉาก พร้อม LATCH Model, Edward Tufte Rationale, และตารางจัดสรรบทบาทสมาชิกกลุ่ม 10+ คน |
| **2** | **Data Scrollytelling Web App** | `index.html` + Live URL | เว็บแอปพลิเคชันเล่าเรื่องด้วยข้อมูล รองรับ 2 โหมด: <br>1. **Scrollytelling Mode** (เลื่อนอ่านพร้อมภาพเปลี่ยนตามจังหวะ)<br>2. **Flourish Story Mode** (สไลด์นำเสนอ 10 สไลด์ พร้อมปุ่มควบคุมและเล่นอัตโนมัติ) |
| **3** | **Google Colab Notebook** | `BI304_Thammasat_Data_Storytelling.ipynb` | โน้ตบุ๊ก Python ตามที่อาจารย์สอนในคลาส รัน Plotly, Folium (แผนที่ CartoDB), และ Streamlit Web App ผ่าน LocalTunnel |
| **4** | **Flourish Studio Datasets** | โฟลเดอร์ `flourish_data/*.csv` | ชุดข้อมูล 6 ไฟล์ CSV จัดรูปแบบพร้อมอัปโหลดเข้าแม่แบบ Flourish Studio (Bar chart race, Treemap, Map, Radar, Grouped bar) |
| **5** | **ไฟล์แพ็กเกจส่งงาน (ZIP)** | `BI304_Thammasat_Group_Submission.zip` | รวมไฟล์ทั้งหมดสำหรับการส่งงานบนระบบ LMS ของคณะ (Moodle / Google Classroom) |

---

## 📊 รายการ 10 Data Visualizations ที่ร้อยเรียงในเรื่องราว

1. **ฉากที่ 1 (Time & Magnitude):** วิวัฒนาการยอดนักศึกษา พ.ศ. 2477 - 2567 (90 ปี ตลาดวิชาสู่สากล 42,650 คน) — *Plotly Spline Area Chart*
2. **ฉากที่ 2 (Location):** เครือข่าย 4 ศูนย์การศึกษาทั่วประเทศไทย (ท่าพระจันทร์, รังสิต, ลำปาง, พัทยา EEC) — *Leaflet Geospatial (Esri Light Gray Canvas)*
3. **ฉากที่ 3 (Hierarchy & Category):** โครงสร้าง 19 คณะ ใน 4 คลัสเตอร์วิชาการ — *Plotly Hierarchical Treemap*
4. **ฉากที่ 4 (Category):** มิติประชากรและความเท่าเทียมทางเพศ (หญิง 62.4% vs ชาย 37.6%) — *Plotly Grouped Bar & 50% Benchmark*
5. **ฉากที่ 5 (Location & Movement):** สายธารการโยกย้ายศูนย์การศึกษาจากท่าพระจันทร์สู่รังสิต — *Plotly Sankey Flow Diagram*
6. **ฉากที่ 6 (Hierarchy & Finance):** โครงสร้างงบประมาณและแหล่งรายได้รวม 11,500 ล้านบาท — *Plotly Financial Waterfall Chart*
7. **ฉากที่ 7 (Time & Magnitude):** เส้นทางทะยานสู่อันดับโลก QS World & Asia Rankings (Top 70 เอเชีย & Top 125 โลก) — *Plotly Inverted Benchmark Chart*
8. **ฉากที่ 8 (Category & Sustainability):** สมรรถนะเป้าหมายการพัฒนาที่ยั่งยืน UN SDGs (Top 10 ของโลกใน SDG 11) — *Plotly Polar / Radar Chart*
9. **ฉากที่ 9 (Time & Impact):** สถิติบริการทางการแพทย์ รพ.ธรรมศาสตร์เฉลิมพระเกียรติ (1.46 ล้านครั้ง/ปี) — *Plotly Dual-Axis Combination*
10. **ฉากที่ 10 (Time & Vision):** วิสัยทัศน์ TU 2034 สู่หลักชัย 100 ปี (TU Net-Zero 2030 & 88 Sandbox) — *Plotly Strategic Gauge KPI Dashboard*

---

## 🛠️ โครงสร้างไฟล์ในโฟลเดอร์โครงงาน (Directory Structure)

```text
d:\BI304\
│
├── index.html                                 # เว็บแอปพลิเคชัน Scrollytelling & Flourish Story
├── Storyboard_Thammasat_BI304.pdf             # เอกสาร Storyboard ฉบับเต็ม 5 หน้า (PDF)
├── BI304_Thammasat_Data_Storytelling.ipynb    # Google Colab Notebook พร้อมโค้ดทั้งหมด
├── START_HERE.bat                             # ดับเบิลคลิกเปิดเว็บทันที (Local Server)
├── RUN_WEB.bat                                # รันเว็บเซิร์ฟเวอร์แบบพกพา
├── README.md                                  # เอกสารสรุปโครงงานและคู่มือส่งงาน
│
├── flourish_data/                             # ชุดข้อมูล 6 ชุดสำหรับ Flourish Studio
│   ├── 01_flourish_bar_chart_race_faculties.csv
│   ├── 02_flourish_campuses_map.csv
│   ├── 03_flourish_hierarchy_clusters.csv
│   ├── 04_flourish_demographics_gender.csv
│   ├── 05_flourish_rankings_time_series.csv
│   ├── 06_flourish_sdg_scores.csv
│   └── README_FLOURISH_GUIDE.md
│
└── learning_resources/                        # โค้ดตัวอย่างและบันทึกการเรียนรู้
    ├── streamlit_scrolly_app.py
    ├── folium_map_tutorial.py
    ├── thammasat_campuses_map.html
    └── thammasat_story_dataset.json
```

---

## 🚀 วิธีการเปิดใช้งานในเครื่อง (Local Execution)
1. **เปิดผ่านเบราว์เซอร์โดยตรง:** ดับเบิลคลิกไฟล์ `index.html` หรือรัน `START_HERE.bat`
2. **เปิดบน Google Colab:** อัปโหลดไฟล์ `BI304_Thammasat_Data_Storytelling.ipynb` เข้าสู่ Google Drive แล้วคลิก "Open with Google Colaboratory"
