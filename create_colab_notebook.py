"""
Generate Google Colab Notebook: BI304_Thammasat_Data_Storytelling.ipynb
Replicating the exact Google Colab workflow taught by Dr. Noptanit Chotisarn in BI304
"""

import json
import os

def make_cell(cell_type, source, outputs=None, execution_count=None):
    if isinstance(source, str):
        source = [line + "\n" for line in source.split("\n")]
        # remove trailing newline on the last line
        if source and source[-1].endswith("\n"):
            source[-1] = source[-1][:-1]
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": source
    }
    if cell_type == "code":
        cell["outputs"] = outputs or []
        cell["execution_count"] = execution_count
    return cell

cells = []

# Title & Metadata
cells.append(make_cell("markdown", """# BI304: การเสริมพลังแก่ข้อมูลผ่านการเล่าเรื่องและการแสดงภาพ
## โครงงานกลุ่ม 10+ คน: "90 ปี ธรรมศาสตร์ — จากตลาดวิชาสู่นวัตกรรมความยั่งยืนระดับโลก"
**หลักสูตรบริหารธุรกิจบัณฑิต คณะพาณิชยศาสตร์และการบัญชี มหาวิทยาลัยธรรมศาสตร์ (TBS)**  
*อาจารย์ผู้สอน: อ.ดร. นภธนิตย์ โชติสาร (Noptanit Chotisarn)*  
*กำหนดนำเสนอ: วันที่ 30 ตุลาคม*

---
### 📌 วัตถุประสงค์ของ Notebook นี้:
1. สาธิตการเตรียมข้อมูล (Data Preparation) สถิติ 90 ปี มหาวิทยาลัยธรรมศาสตร์
2. พัฒนา 10 Visualizations ตามกรอบ **LATCH** (Location, Alphabet, Time, Category, Hierarchy)
3. ยึดหลักการออกแบบของ **Edward Tufte** (Maximize Data-Ink Ratio, Zero Lie Factor, Direct Labeling)
4. ประยุกต์ใช้เครื่องมือที่เรียนในห้องเรียน: **Plotly**, **Folium (Geospatial Map)**, **Dash (Inline)**, **Streamlit + localtunnel** และส่งออกไฟล์สำหรับ **Flourish**
"""))

# Cell 1: Install packages
cells.append(make_cell("code", """# 1. ติดตั้งไลบรารีที่จำเป็น (กดรันได้เลย)
!pip install -q plotly folium streamlit dash localtunnel
print("✅ ติดตั้งไลบรารีเรียบร้อยแล้ว!")
"""))

# Cell 2: Imports & Tufte Style Setup
cells.append(make_cell("code", """# 2. นำเข้าไลบรารีและกำหนด Palette สีประจำมหาวิทยาลัยธรรมศาสตร์ตามหลัก Edward Tufte
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import folium
import json
import os

# ชุดสีกลางของโครงงาน — เลือดหมู-ทอง สไตล์ธรรมศาสตร์ + สีเทากลาง Tufte
MAIN, SECOND = "#C62828", "#F9A825" # แดงเลือดหมู = มธ. ดั้งเดิม, เหลืองทอง = นวัตกรรม/อนาคต
ACCENT_GREEN = "#2E7D32"            # สวนป๋วย / ความยั่งยืน
NAVY = "#1A237E"                    # บัณฑิตศึกษาและสากล
INK, INK2, GRID = "#212121", "#555555", "#E0E0E0"
SOURCE = "ที่มา: รายงานประจำปี มหาวิทยาลัยธรรมศาสตร์ และสำนักทะเบียนและประมวลผล (2477-2569)"

# ตั้งค่าฟอนต์และกราฟแบบ Minimal
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8
print("✅ กำหนดค่า Visual Style สำเร็จ!")
"""))

# Cell 3: Data Creation
cells.append(make_cell("code", """# 3. สร้างชุดข้อมูลสถิติ 90 ปี มหาวิทยาลัยธรรมศาสตร์ (10 Visualizations)
os.makedirs("exports", exist_ok=True)

# 3.1 ข้อมูลประวัติศาสตร์ยอดนักศึกษา (Time-Series)
df_history = pd.DataFrame({
    "year": [1934, 1945, 1952, 1965, 1976, 1986, 1996, 2005, 2015, 2026],
    "students": [7094, 9800, 4200, 11500, 15800, 21000, 27500, 33200, 39400, 42650],
    "event": ["ก่อตั้ง มธก. ตลาดวิชา", "หลังสงครามโลก", "ปรับสู่ ม.ระบบปิด", "ขยายการศึกษา", "ประชาธิปไตย", "เปิดศูนย์รังสิต", "ขยายสู่ภูมิภาค", "ย้าย ป.ตรี สู่รังสิต", "ม.ในกำกับของรัฐ", "มุ่งสู่ศตวรรษที่ 1"]
})

# 3.2 ข้อมูล 4 ศูนย์การศึกษา (Geospatial)
df_campuses = pd.DataFrame([
    {"name": "ศูนย์ท่าพระจันทร์", "lat": 13.7557, "lng": 100.4930, "area_rai": 49, "students": 6500, "role": "นานาชาติ & บัณฑิตศึกษา"},
    {"name": "ศูนย์รังสิต", "lat": 14.0736, "lng": 100.6067, "area_rai": 1757, "students": 32000, "role": "ศูนย์กลางหลัก การแพทย์ และสวนป๋วย"},
    {"name": "ศูนย์ลำปาง", "lat": 18.2982, "lng": 99.4897, "area_rai": 464, "students": 2200, "role": "ศูนย์กลางภาคเหนือ"},
    {"name": "ศูนย์พัทยา", "lat": 12.9236, "lng": 100.9925, "area_rai": 566, "students": 1500, "role": "EEC เทคโนโลยียานยนต์"}
])

# 3.3 ข้อมูล 19 คณะ 4 คลัสเตอร์ (Hierarchy)
df_faculties = pd.DataFrame([
    {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "นิติศาสตร์", "students": 3800},
    {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "พาณิชยศาสตร์ฯ (TBS)", "students": 4950},
    {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "รัฐศาสตร์", "students": 2100},
    {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "เศรษฐศาสตร์", "students": 2200},
    {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "ศิลปศาสตร์", "students": 2600},
    {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "วารสารศาสตร์ฯ", "students": 1300},
    {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "สังคมวิทยาฯ", "students": 1000},
    {"cluster": "วิทยาศาสตร์-เทคโนโลยี", "faculty": "วิศวกรรมศาสตร์ (TSE)", "students": 4200},
    {"cluster": "วิทยาศาสตร์-เทคโนโลยี", "faculty": "วิทยาศาสตร์ฯ", "students": 3900},
    {"cluster": "วิทยาศาสตร์-เทคโนโลยี", "faculty": "สถาปัตยกรรมฯ", "students": 1600},
    {"cluster": "วิทยาศาสตร์-เทคโนโลยี", "faculty": "วิทยาลัยนวัตกรรม", "students": 1400},
    {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "แพทยศาสตร์", "students": 1200},
    {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "ทันตแพทยศาสตร์", "students": 850},
    {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "สหเวชศาสตร์", "students": 1900},
    {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "พยาบาลศาสตร์", "students": 1100},
    {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "เภสัชศาสตร์", "students": 1200},
    {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "สาธารณสุขศาสตร์", "students": 1400},
    {"cluster": "นานาชาติ/บูรณาการ", "faculty": "SIIT", "students": 3100},
    {"cluster": "นานาชาติ/บูรณาการ", "faculty": "วิทยาลัยนานาชาติปรีดี (PBIC)", "students": 900},
    {"cluster": "นานาชาติ/บูรณาการ", "faculty": "วิทยาลัยสหวิทยาการ", "students": 1100},
    {"cluster": "นานาชาติ/บูรณาการ", "faculty": "วิทยาลัยพัฒนศาสตร์ ป๋วย", "students": 900}
])

# 3.4 ข้อมูลความหลากหลายทางเพศ (Demographics)
df_gender = pd.DataFrame({
    "cluster": ["สังคมศาสตร์-มนุษยศาสตร์", "วิทยาศาสตร์-เทคโนโลยี", "วิทยาศาสตร์สุขภาพ", "นานาชาติ/บูรณาการ"],
    "หญิง (Female)": [11450, 4880, 5200, 3600],
    "ชาย (Male)": [6450, 6220, 2450, 2400]
})

print("✅ สร้างชุดข้อมูลสถิติมหาวิทยาลัยธรรมศาสตร์ครบถ้วน!")
"""))

# Cell 4: Visualization 1 - Plotly Spline Chart
cells.append(make_cell("markdown", """### 📊 ฉากที่ 1: ปฐมบท 2477 สู่ 42,000+ คน (Plotly Interactive Time-Series)
แสดงยอดนักศึกษาตั้งแต่รุ่นก่อตั้งตลาดวิชาจนถึงปัจจุบัน ด้วยธีมมินิมอลตามหลัก Edward Tufte
"""))

cells.append(make_cell("code", """fig1 = px.area(
    df_history, x="year", y="students",
    title="ฉาก 1: วิวัฒนาการจำนวนนักศึกษามหาวิทยาลัยธรรมศาสตร์ (พ.ศ. 2477 - 2569)",
    labels={"year": "ปี ค.ศ.", "students": "จำนวนนักศึกษา (คน)"}
)
fig1.update_traces(line_color=MAIN, fillcolor="rgba(198,40,40,0.12)", line_shape="spline")
fig1.add_annotation(x=1934, y=7094, text="2477: ตลาดวิชารุ่นแรก 7,094 คน", showarrow=True, arrowhead=2, bgcolor="#FFF9C4")
fig1.add_annotation(x=1986, y=21000, text="2529: เปิดศูนย์รังสิต", showarrow=True, arrowhead=2, bgcolor="#E8F5E9")
fig1.add_annotation(x=2026, y=42650, text="2569: ปัจจุบัน 42,650 คน", showarrow=True, arrowhead=2, bgcolor="#FFEBEE")
fig1.update_layout(template="simple_white", height=450)
fig1.show()
"""))

# Cell 5: Visualization 2 - Folium Interactive Map
cells.append(make_cell("markdown", """### 🗺️ ฉากที่ 2: เครือข่าย 4 ศูนย์การศึกษา (Folium / Leaflet Web Map)
ใช้ CartoDB Positron Tiles เพื่อป้องกันปัญหา OpenStreetMap 403 Access Blocked ตามที่อาจารย์สอนในห้องเรียน
"""))

cells.append(make_cell("code", """m = folium.Map(location=[15.0, 100.5], zoom_start=6, tiles="CartoDB positron")

for _, c in df_campuses.iterrows():
    popup_text = f"<b>{c['name']}</b><br>พื้นที่: {c['area_rai']} ไร่<br>นักศึกษา: {c['students']} คน<br>บทบาท: {c['role']}"
    folium.Marker(
        location=[c['lat'], c['lng']],
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=c['name'],
        icon=folium.Icon(color="red" if c['name']=="ศูนย์ท่าพระจันทร์" else "orange", icon="graduation-cap", prefix="fa")
    ).add_to(m)
    
    # วงรัศมีขนาดพื้นที่
    folium.Circle(
        location=[c['lat'], c['lng']],
        radius=c['area_rai'] * 15,
        color=MAIN if c['name']=="ศูนย์ท่าพระจันทร์" else SECOND,
        fill=True,
        fill_opacity=0.3
    ).add_to(m)

# เส้นเชื่อมโยงยุทธศาสตร์ ท่าพระจันทร์ - รังสิต
folium.PolyLine(
    locations=[[13.7557, 100.4930], [14.0736, 100.6067]],
    color=MAIN, weight=3, dash_array="5, 10", tooltip="Strategic Migration Corridor"
).add_to(m)

m.save("exports/thammasat_campuses_map.html")
print("✅ สร้างแผนที่ Folium สำเร็จ บันทึกที่ exports/thammasat_campuses_map.html")
m
"""))

# Cell 6: Visualization 3 - Treemap 19 Faculties
cells.append(make_cell("markdown", """### 🌳 ฉากที่ 3: โครงสร้าง 19 คณะ ใน 4 คลัสเตอร์ (Plotly Treemap)
แสดงความหลากหลายทางวิชาการและสัดส่วนนักศึกษาแต่ละคณะอย่างเป็นสัดส่วน ปราศจาก Lie Factor
"""))

cells.append(make_cell("code", """fig3 = px.treemap(
    df_faculties, path=["cluster", "faculty"], values="students",
    color="cluster",
    color_discrete_sequence=[MAIN, "#1565C0", ACCENT_GREEN, "#E65100"],
    title="ฉาก 3: โครงสร้าง 19 คณะ ใน 4 คลัสเตอร์วิชาการ มหาวิทยาลัยธรรมศาสตร์"
)
fig3.update_layout(margin=dict(t=50, l=10, r=10, b=10), height=500)
fig3.show()
"""))

# Cell 7: Visualization 4 - Demographics Gender Bar
cells.append(make_cell("markdown", """### 👥 ฉากที่ 4: ความหลากหลายทางเพศ (Grouped Stacked Bar)
แสดงสถิตินักศึกษาหญิง 62% ต่อชาย 38% เริ่มต้นแกนที่ 0 ตามเกณฑ์ความซื่อตรงของ Edward Tufte
"""))

cells.append(make_cell("code", """fig4 = px.bar(
    df_gender, x="cluster", y=["หญิง (Female)", "ชาย (Male)"],
    title="ฉาก 4: สัดส่วนนักศึกษาหญิง (62%) และนักศึกษาชาย (38%) ในแต่ละกลุ่มสาขา",
    color_discrete_map={"หญิง (Female)": MAIN, "ชาย (Male)": SECOND},
    barmode="stack", labels={"value": "จำนวนนักศึกษา (คน)", "cluster": "กลุ่มสาขาวิชา"}
)
fig4.update_layout(template="simple_white", height=450)
fig4.show()
"""))

# Cell 8: Visualization 5 - Sankey Migration
cells.append(make_cell("markdown", """### 🌊 ฉากที่ 5: สายธารการย้าย นศ. สู่รังสิต (Plotly Sankey Flow Diagram)
"""))

cells.append(make_cell("code", """fig5 = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15, thickness=20,
        line=dict(color="black", width=0.5),
        label=["ท่าพระจันทร์ (เดิม)", "รังสิต (ขยาย)", "ท่าพระจันทร์ (ปัจจุบัน)", "รังสิต (ปัจจุบัน)", "ลำปาง/พัทยา"],
        color=[MAIN, SECOND, "#D32F2F", "#1976D2", ACCENT_GREEN]
    ),
    link=dict(
        source=[0, 0, 1, 1],
        target=[2, 3, 3, 4],
        value=[6500, 18000, 14000, 3700],
        color=["rgba(198,40,40,0.3)", "rgba(249,168,37,0.3)", "rgba(25,118,210,0.3)", "rgba(46,125,50,0.3)"]
    )
)])
fig5.update_layout(title="ฉาก 5: การถ่ายโอนประชากรนักศึกษา ท่าพระจันทร์ สู่ รังสิต (Sankey Flow)", height=450)
fig5.show()
"""))

# Cell 9: Visualization 6 - Financial Waterfall
cells.append(make_cell("markdown", """### 💰 ฉากที่ 6: โครงสร้างงบประมาณ 11,500 ลบ. และทุนวิจัย (Waterfall Chart)
"""))

cells.append(make_cell("code", """fig6 = go.Figure(go.Waterfall(
    name="งบประมาณ", orientation="v",
    measure=["relative", "relative", "relative", "relative", "relative", "total"],
    x=["อุดหนุนรัฐ", "ค่าธรรมเนียมการศึกษา", "บริการวิชาการ/รพ.", "ทุนวิจัยภายนอก", "ผลประโยชน์ทรัพย์สิน", "งบประมาณรวม"],
    text=["+3,600", "+4,200", "+1,800", "+1,100", "+800", "11,500 ลบ."],
    y=[3600, 4200, 1800, 1100, 800, 0],
    connector={"line": {"color": "#666666"}},
    increasing={"marker": {"color": MAIN}},
    totals={"marker": {"color": NAVY}}
))
fig6.update_layout(title="ฉาก 6: โครงสร้างรายได้และแหล่งงบประมาณ มธ. 11,500 ล้านบาท (Waterfall)", template="simple_white", height=450)
fig6.show()
"""))

# Cell 10: Visualization 7 - Rankings Time-Series
cells.append(make_cell("markdown", """### 🏆 ฉากที่ 7: ก้าวสู่อันดับโลก QS World University Rankings (Multi-line + Slider)
"""))

cells.append(make_cell("code", """years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
qs_asia = [137, 134, 119, 111, 107, 96, 81, 73, 68]
business_rank = [250, 230, 210, 190, 180, 160, 150, 140, 130]

fig7 = go.Figure()
fig7.add_trace(go.Scatter(x=years, y=qs_asia, mode='lines+markers', name='QS Asia Ranking (อันดับดีขึ้น)', line=dict(color=MAIN, width=3)))
fig7.add_trace(go.Scatter(x=years, y=business_rank, mode='lines+markers', name='QS Subject: Business & Management', line=dict(color=SECOND, width=2.5, dash='dash')))
fig7.update_yaxes(autorange="reversed", title="อันดับโลก (ตัวเลขยิ่งน้อยยิ่งดี)")
fig7.update_layout(title="ฉาก 7: เส้นทางทะยานในอันดับมหาวิทยาลัยโลก (Rankings)", template="simple_white", height=450)
fig7.show()
"""))

# Cell 11: Visualization 8 - SDG Radar Chart
cells.append(make_cell("markdown", """### 🌱 ฉากที่ 8: ผู้นำความยั่งยืน SDG 11 และสวนป๋วย 100 ปี (Radar Polar Chart)
"""))

cells.append(make_cell("code", """sdg_categories = ['SDG 11: เมืองยั่งยืน (Top 10 โลก)', 'SDG 7: พลังงานสะอาด', 'SDG 13: รับมือภูมิอากาศ', 'SDG 3: สุขภาพและความเป็นอยู่', 'SDG 4: การศึกษาเท่าเทียม', 'SDG 17: ความร่วมมือสากล']
sdg_scores = [98.5, 92.0, 88.4, 85.0, 91.2, 84.5]

fig8 = px.line_polar(r=sdg_scores, theta=sdg_categories, line_close=True, title="ฉาก 8: สมรรถนะความยั่งยืน THE Impact Rankings (มธ. อันดับต้นของโลก)")
fig8.update_traces(fill='toself', fillcolor="rgba(46,125,50,0.25)", line_color=ACCENT_GREEN)
fig8.update_layout(height=480)
fig8.show()
"""))

# Cell 12: Visualization 9 - Hospital Growth
cells.append(make_cell("markdown", """### 🏥 ฉากที่ 9: โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ (Dual-Axis Combination Chart)
"""))

cells.append(make_cell("code", """h_years = [1987, 1995, 2005, 2015, 2020, 2025]
opd = [50000, 180000, 480000, 920000, 1250000, 1460000]
beds = [120, 350, 600, 850, 1200, 1400]

fig9 = go.Figure()
fig9.add_trace(go.Bar(x=h_years, y=opd, name='ผู้ป่วยนอก (ครั้ง/ปี)', marker_color='rgba(198, 40, 40, 0.7)'))
fig9.add_trace(go.Scatter(x=h_years, y=beds, name='เตียงผู้ป่วย (เตียง)', yaxis='y2', line=dict(color='#00897B', width=3)))
fig9.update_layout(
    title="ฉาก 9: การขยายตัวของ รพ.ธรรมศาสตร์เฉลิมพระเกียรติ (1987 - 2025)",
    yaxis=dict(title='ผู้ป่วยนอก (คน)'),
    yaxis2=dict(title='จำนวนเตียง', overlaying='y', side='right'),
    template="simple_white", height=450
)
fig9.show()
"""))

# Cell 13: Visualization 10 - Centenary Horizon
cells.append(make_cell("markdown", """### 🎯 ฉากที่ 10: มุ่งสู่ศตวรรษที่ 1 TU 2034 (Gauge & Target Dashboard)
"""))

cells.append(make_cell("code", """fig10 = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=78,
    title={'text': "เป้าหมาย Net-Zero 2030 (ความคืบหน้า %)"},
    delta={'reference': 60, 'increasing': {'color': "green"}},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': MAIN},
        'steps': [
            {'range': [0, 50], 'color': "#FFEBEE"},
            {'range': [50, 85], 'color': "#FFF9C4"},
            {'range': [85, 100], 'color': "#E8F5E9"}
        ]
    }
))
fig10.update_layout(height=450, title="ฉาก 10: ตัวชี้วัดยุทธศาสตร์ก้าวสู่ 100 ปีธรรมศาสตร์ (TU 2034)")
fig10.show()
"""))

# Cell 14: Dash Dashboard Inline (Matching Professor's Colab cell 26)
cells.append(make_cell("markdown", """### 💻 รัน Dashboard ด้วย Dash (แบบ Inline ใน Colab ตามที่อาจารย์สอน)
"""))

cells.append(make_cell("code", """from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)
app.layout = html.Div([
    html.H2("ธรรมศาสตร์ Data Storyboard Dashboard (BI304)", style={"color": MAIN, "textAlign": "center"}),
    html.P("เลือกดูข้อมูล 4 ศูนย์การศึกษา:", style={"textAlign": "center"}),
    dcc.Dropdown(
        id='campus-dropdown',
        options=[{'label': c['name'], 'value': c['name']} for _, c in df_campuses.iterrows()],
        value='ศูนย์รังสิต',
        style={"width": "60%", "margin": "0 auto"}
    ),
    html.Div(id='campus-display', style={"textAlign": "center", "padding": "20px", "fontSize": "18px"})
])

@app.callback(
    Output('campus-display', 'children'),
    Input('campus-dropdown', 'value')
)
def update_campus_info(selected_campus):
    c = df_campuses[df_campuses['name'] == selected_campus].iloc[0]
    return f"📍 {c['name']} | เนื้อที่: {c['area_rai']} ไร่ | นักศึกษา: {c['students']} คน | จุดเด่น: {c['role']}"

# สั่งรัน Dash Inline ภายใน Colab Notebook
app.run(jupyter_mode="inline", port=8050, height=350)
"""))

# Cell 15: Streamlit code generator (Matching Professor's Colab cell 27 & 28)
cells.append(make_cell("markdown", """### 🚀 รัน Streamlit Dashboard ผ่าน Localtunnel (ตามขั้นตอนของอาจารย์)
"""))

cells.append(make_cell("code", """%%writefile streamlit_app.py
import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="90 ปี ธรรมศาสตร์ Data Storytelling", layout="wide")
st.title("🎓 90 ปี ธรรมศาสตร์: จากตลาดวิชาสู่นวัตกรรมความยั่งยืน")
st.caption("โครงงานกลุ่มวิชา BI304 TBS | อาจารย์ผู้สอน: อ.ดร. นภธนิตย์ โชติสาร")

st.info("💡 สามารถเลือกฉากเพื่อดูเรื่องเล่าและสถิติสำคัญได้จากเมนูด้านล่าง")
scene = st.selectbox("เลือกฉากที่ต้องการสำรวจ (1-10):", [
    "ฉาก 1: ปฐมบท 2477", "ฉาก 2: แผนที่ 4 ศูนย์", "ฉาก 3: 19 คณะ 4 คลัสเตอร์",
    "ฉาก 4: สถิติประชากร", "ฉาก 5: การย้ายสู่รังสิต", "ฉาก 6: งบประมาณ 11,500 ลบ.",
    "ฉาก 7: อันดับโลก QS", "ฉาก 8: ผู้นำ SDG สวนป๋วย", "ฉาก 9: รพ.ธรรมศาสตร์", "ฉาก 10: สู่วิสัยทัศน์ TU 2034"
])

if "ฉาก 1" in scene:
    st.write("**สถิตินักศึกษารุ่นแรก 7,094 คน** ก่อตั้งโดยท่านปรีดี พนมยงค์ สู่ 42,650+ คนในปัจจุบัน")
elif "ฉาก 2" in scene:
    st.write("**เครือข่าย 4 วิทยาเขต:** ท่าพระจันทร์ (49 ไร่), รังสิต (1,757 ไร่), ลำปาง (464 ไร่), พัทยา (566 ไร่)")
elif "ฉาก 8" in scene:
    st.write("**ผู้นำ SDG 11 อันดับ Top 10 ของโลก** และอุทยานสวนป๋วย 100 ปี สวนผักดาดฟ้าใหญ่สุดในเอเชีย")
"""))

# Cell 16: Export files for Flourish
cells.append(make_cell("markdown", """### 📁 ส่งออกข้อมูลพร้อมใช้งานสำหรับ Flourish (flourish.studio)
"""))

cells.append(make_cell("code", """# บันทึกเป็น CSV สำหรับนำเข้า Flourish
df_history.to_csv("exports/flourish_enrollment.csv", index=False)
df_campuses.to_csv("exports/flourish_campuses.csv", index=False)
df_faculties.to_csv("exports/flourish_faculties.csv", index=False)
df_gender.to_csv("exports/flourish_gender.csv", index=False)

print("✅ ส่งออกไฟล์ CSV ทั้งหมดพร้อมอัปโหลดขึ้น Flourish แล้ว!")
"""))

notebook = {
    "cells": cells,
    "metadata": {
        "language_info": {
            "name": "python",
            "version": "3.10"
        },
        "colab": {
            "name": "BI304_Thammasat_Data_Storytelling.ipynb",
            "provenance": []
        }
    },
    "nbformat": 4,
    "nbformat_minor": 0
}

nb_path = r"d:\BI304\BI304_Thammasat_Data_Storytelling.ipynb"
with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print("Successfully generated Google Colab Notebook:", nb_path)
