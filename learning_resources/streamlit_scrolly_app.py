"""
BI304: Streamlit Interactive Storytelling Dashboard
Course: BI304 Empowering Data Through Storytelling and Visualization, TBS
Topic: Thammasat University 10-Scene Data Narrative
To run: streamlit run d:\\BI304\\learning_resources\\streamlit_scrolly_app.py
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="90 ปี ธรรมศาสตร์: Data Narrative Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Thammasat Theme & Tufte Clean Palette)
st.markdown("""
<style>
    .main-header {
        color: #C62828;
        font-family: 'Prompt', sans-serif;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        color: #F57F17;
        font-family: 'Prompt', sans-serif;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #FFF9C4;
        border-left: 5px solid #FBC02D;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Thammasat_University_Emblem.svg/1200px-Thammasat_University_Emblem.svg.png", width=110)
st.sidebar.title("BI304 Data Narrative")
st.sidebar.caption("มหาวิทยาลัยธรรมศาสตร์ (TBS)")

scenes = [
    "ฉากที่ 1: ปฐมบท 2477 (The Democratic Genesis)",
    "ฉากที่ 2: เครือข่าย 4 ศูนย์การศึกษา (The 4-Campus Network)",
    "ฉากที่ 3: สัดส่วน 19 คณะ 4 คลัสเตอร์ (Academic Clusters)",
    "ฉากที่ 4: ความหลากหลายและประชากร นศ. (Inclusivity Matrix)",
    "ฉากที่ 5: สายธารการย้ายสู่รังสิต (The Great Migration Flow)",
    "ฉากที่ 6: เครื่องยนต์งบประมาณ 11,500 ลบ. (Financial Stewardship)",
    "ฉากที่ 7: ก้าวสู่เวทีโลก World Rankings (Global Ascent)",
    "ฉากที่ 8: ผู้นำ SDG สวนป๋วย 100 ปี (Green TU & SDG Leadership)",
    "ฉากที่ 9: โรงพยาบาลธรรมศาสตร์เพื่อประชาชน (Healthcare for Society)",
    "ฉากที่ 10: มุ่งสู่ศตวรรษที่ 1 TU 2034 (The Centenary Horizon)"
]

selected_scene = st.sidebar.radio("เลือกลำดับฉากนำเสนอ (10 Scenes):", scenes)
scene_idx = scenes.index(selected_scene) + 1

# Header
st.markdown("<h1 class='main-header'>90 ปี ธรรมศาสตร์: จากตลาดวิชาสู่นวัตกรรมความยั่งยืน</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>BI304 การเสริมพลังแก่ข้อมูลผ่านการเล่าเรื่องและการแสดงภาพ | นำเสนอวันที่ 30 ต.ค.</p>", unsafe_allow_html=True)
st.divider()

col_narrative, col_viz = st.columns([4, 6], gap="large")

with col_narrative:
    st.subheader(selected_scene)
    
    if scene_idx == 1:
        st.markdown("""
        **ปณิธานแห่งการก่อตั้ง (27 มิ.ย. 2477):**
        ท่านผู้ประศาสน์การ **ศ.ดร.ปรีดี พนมยงค์** ริเริ่มมหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง (มธก.) 
        เพื่อเป็นบ่อน้ำบำบัดความกระหายความรู้ของราษฎรในระบอบประชาธิปไตย
        
        <div class='metric-card'>
            <b>สถิติสำคัญ:</b> ผู้สมัครปีแรก <b>7,094 คน</b> (เทียบเท่างบประมาณแผ่นดินและจำนวนข้าราชการยุคนั้น)
            ก่อนปรับสู่มหาวิทยาลัยปิดในปี 2495 และเติบโตสู่กว่า 42,500 คนในปัจจุบัน
        </div>
        
        *หลักการ Edward Tufte:* ใช้เส้นเดี่ยวแบบ Spline พร้อมจุดเน้นปีประวัติศาสตร์ กำจัด Chartjunk ให้ความสำคัญกับ Data-Ink Ratio
        """, unsafe_allow_html=True)

    elif scene_idx == 2:
        st.markdown("""
        **ก้าวข้ามขีดจำกัดเชิงพื้นที่:**
        จากท่าพระจันทร์ 49 ไร่ สู่เครือข่าย 4 วิทยาเขตทั่วประเทศ:
        - **ท่าพระจันทร์:** 49 ไร่ (ศูนย์กลางบัณฑิตศึกษาและนานาชาติ)
        - **รังสิต:** 1,757 ไร่ (ศูนย์การศึกษาหลักและวิจัยนวัตกรรม)
        - **ลำปาง:** 464 ไร่ (ประตูวิชาการภาคเหนือ)
        - **พัทยา:** 566 ไร่ (เทคโนโลยียานยนต์ EEC)
        
        <div class='metric-card'>
            <b>โมเดล LATCH (Location):</b> ใช้พิกัดจริงและขนาดพื้นที่สะท้อนการกระจายโอกาสสู่ภูมิภาค
        </div>
        """, unsafe_allow_html=True)

    elif scene_idx == 3:
        st.markdown("""
        **การผลิบานของศาสตร์ความรู้:**
        ธรรมศาสตร์ก้าวข้ามจากมหาวิทยาลัยกฎหมายและการเมือง สู่มหาวิทยาลัยวิจัยครบวงจร 19 คณะ ใน 4 คลัสเตอร์:
        - สังคมศาสตร์-มนุษยศาสตร์ (42%) รวมคณะพาณิชย์ฯ TBS (Triple Crown)
        - วิทยาศาสตร์และเทคโนโลยี (26%)
        - วิทยาศาสตร์สุขภาพและแพทย์ (18%)
        - นานาชาติและบูรณาการ (14%)
        
        <div class='metric-card'>
            <b>โมเดล LATCH (Category & Hierarchy):</b> Treemap แสดงสัดส่วนตามขนาดนักศึกษาจริง ปราศจาก Lie Factor
        </div>
        """, unsafe_allow_html=True)

    elif scene_idx == 4:
        st.markdown("""
        **ความเท่าเทียมและการเปิดรับสากล:**
        - สัดส่วนนักศึกษาหญิงเพิ่มขึ้นแตะ **62%**
        - ปริญญาตรี 78% (33,500 คน) และบัณฑิตศึกษา 22% (9,150 คน)
        - โควตานักเรียนชนบทและผู้ด้อยโอกาสกว่า 2,500 คน/ปี
        - นักศึกษาต่างชาติกว่า 50 สัญชาติ
        
        <div class='metric-card'>
            <b>Edward Tufte:</b> กราฟแท่งเริ่มต้นที่แกน 0 เสมอ แสดงสัดส่วนร้อยละชัดเจน
        </div>
        """, unsafe_allow_html=True)

    elif scene_idx == 5:
        st.markdown("""
        **มหาการย้ายถิ่นฐาน (2529-2548):**
        การย้ายนักศึกษาปี 1 สู่ศูนย์รังสิตในปี 2529 และการย้าย ป.ตรี ภาคปกติทั้งหมดในปี 2548
        ปลดล็อกความแออัดของท่าพระจันทร์ และสร้างอาณาจักรการเรียนรู้ใหม่ ณ ปทุมธานี
        
        <div class='metric-card'>
            <b>Sankey / Alluvial Flow:</b> สื่อสารการเดินทางและสายธารการจัดสรรประชากรข้ามวิทยาเขต
        </div>
        """, unsafe_allow_html=True)

    elif scene_idx == 6:
        st.markdown("""
        **เครื่องยนต์การเงินและทุนวิจัย (ม.ในกำกับของรัฐ 2558):**
        - งบประมาณรวมต่อปีแตะ **11,500 ล้านบาท**
        - ลดการพึ่งพางบประมาณแผ่นดินเหลือราว 31%
        - ทุนวิจัยภายนอกจากภาคอุตสาหกรรมเติบโต **+140%** ใน 10 ปี (แตะ 1,100 ลบ.)
        
        <div class='metric-card'>
            <b>Waterfall Chart:</b> แจกแจงการไหลเข้าของรายได้แต่ละส่วนจนครบงบประมาณรวม
        </div>
        """, unsafe_allow_html=True)

    elif scene_idx == 7:
        st.markdown("""
        **ทะยานสู่อันดับโลก (World Rankings):**
        - **QS Asia Rankings:** ทะยานสู่ Top 100 อย่างต่อเนื่อง
        - **Business & Management (TBS):** Top 200 ของโลก
        - **Law & Social Sciences:** Top 150 ของโลก
        - อัตราการได้งานทำและความพึงพอใจของนายจ้าง (Employer Reputation) สูงลิ่ว
        """, unsafe_allow_html=True)

    elif scene_idx == 8:
        st.markdown("""
        **ผู้นำความยั่งยืนระดับโลก (UN SDGs):**
        - **SDG 11 (เมืองและชุมชนยั่งยืน):** อันดับ Top 10 ของโลก
        - **อุทยานการเรียนรู้ป๋วย 100 ปี:** สวนผักออร์แกนิกบนหลังคาใหญ่ที่สุดในเอเชีย (22,000 ตร.ม.)
        - พลังงานโซลาร์รูฟ **35 MW** และรถบัส EV 100%
        - ลดคาร์บอนฟุตพริ้นท์ **24,000 ตัน CO2/ปี**
        """, unsafe_allow_html=True)

    elif scene_idx == 9:
        st.markdown("""
        **ธรรมศาสตร์เพื่อประชาชน: สาธารณสุขยามวิกฤต:**
        - รพ.ธรรมศาสตร์เฉลิมพระเกียรติ ให้บริการผู้ป่วยนอกกว่า **1,450,000 ครั้ง/ปี**
        - เปิดโรงพยาบาลสนามแห่งแรกของไทยช่วงโควิด-19 รองรับผู้ป่วย 3,000+ เตียง
        - ระบบการแพทย์ทางไกล (Telemedicine) ครอบคลุมผู้ป่วยทั่วประเทศ
        """, unsafe_allow_html=True)

    elif scene_idx == 10:
        st.markdown("""
        **สู่วิสัยทัศน์ศตวรรษที่ 1: TU 2034:**
        - **Net-Zero Campus 2030:** มุ่งสู่ความเป็นกลางทางคาร์บอน
        - **88 SANDBOX:** บ่มเพาะ 10,000 สตาร์ทอัพเพื่อสังคม
        - ผลิตบัณฑิตที่มี DNA เพื่อประชาธิปไตย ความเท่าเทียม และการสร้างสรรค์
        """, unsafe_allow_html=True)

with col_viz:
    if scene_idx == 1:
        years = [1934, 1945, 1952, 1965, 1976, 1986, 1996, 2005, 2015, 2026]
        students = [7094, 9800, 4200, 11500, 15800, 21000, 27500, 33200, 39400, 42650]
        fig = px.area(x=years, y=students, title="จำนวนนักศึกษา มธ. (1934 - 2026)", labels={"x": "ปี ค.ศ.", "y": "นักศึกษา (คน)"})
        fig.update_traces(line_color="#C62828", fillcolor="rgba(198,40,40,0.15)")
        fig.add_annotation(x=1934, y=7094, text="ปี 2477: รุ่นแรก 7,094 คน", showarrow=True, arrowhead=2)
        fig.update_layout(template="simple_white", height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 2:
        df_geo = pd.DataFrame([
            {"campus": "ท่าพระจันทร์", "lat": 13.7557, "lon": 100.4930, "rai": 49, "students": 6500},
            {"campus": "ศูนย์รังสิต", "lat": 14.0736, "lon": 100.6067, "rai": 1757, "students": 32000},
            {"campus": "ศูนย์ลำปาง", "lat": 18.2982, "lon": 99.4897, "rai": 464, "students": 2200},
            {"campus": "ศูนย์พัทยา", "lat": 12.9236, "lon": 100.9925, "rai": 566, "students": 1500}
        ])
        fig = px.scatter_geo(
            df_geo, lat="lat", lon="lon", hover_name="campus", size="rai",
            color="campus", title="ที่ตั้งและขนาดพื้นที่ 4 ศูนย์การศึกษา (ไร่)",
            color_discrete_sequence=["#C62828", "#F57C00", "#2E7D32", "#1565C0"]
        )
        fig.update_geos(fitbounds="locations", showcountries=True, countrycolor="#CCC", showsubunits=True)
        fig.update_layout(height=450, margin=dict(l=0, r=0, t=40, b=0))
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 3:
        df_tree = pd.DataFrame([
            {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "นิติศาสตร์", "students": 3800},
            {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "พาณิชยศาสตร์ฯ (TBS)", "students": 4900},
            {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "รัฐศาสตร์", "students": 2100},
            {"cluster": "สังคมศาสตร์-มนุษยศาสตร์", "faculty": "เศรษฐศาสตร์", "students": 2200},
            {"cluster": "วิทยาศาสตร์-เทคโนโลยี", "faculty": "วิศวกรรมศาสตร์ (TSE)", "students": 4200},
            {"cluster": "วิทยาศาสตร์-เทคโนโลยี", "faculty": "วิทยาศาสตร์ฯ", "students": 3900},
            {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "แพทยศาสตร์", "students": 1200},
            {"cluster": "วิทยาศาสตร์สุขภาพ", "faculty": "สหเวชศาสตร์", "students": 1900},
            {"cluster": "นานาชาติ/บูรณาการ", "faculty": "SIIT", "students": 3100},
            {"cluster": "นานาชาติ/บูรณาการ", "faculty": "วิทยาลัยนานาชาติปรีดี", "students": 900}
        ])
        fig = px.treemap(df_tree, path=['cluster', 'faculty'], values='students', color='cluster',
                         color_discrete_sequence=['#C62828', '#1565C0', '#2E7D32', '#F57C00'],
                         title="โครงสร้างคณะวิชาและสัดส่วนนักศึกษา")
        fig.update_layout(height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 4:
        df_demo = pd.DataFrame({
            "กลุ่มสาขา": ['สังคมศาสตร์', 'วิทย์-เทคโนโลยี', 'สุขภาพและการแพทย์', 'นานาชาติ'],
            "หญิง": [11450, 4880, 5200, 3600],
            "ชาย": [6450, 6220, 2450, 2400]
        })
        fig = px.bar(df_demo, x="กลุ่มสาขา", y=["หญิง", "ชาย"], title="สัดส่วนเพศนักศึกษาในแต่ละกลุ่มสาขา (คน)",
                     color_discrete_map={"หญิง": "#C62828", "ชาย": "#F9A825"}, barmode="stack")
        fig.update_layout(template="simple_white", height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 5:
        fig = go.Figure(data=[go.Sankey(
            node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5),
                      label=["ท่าพระจันทร์ (เดิม)", "รังสิต (ขยาย)", "ท่าพระจันทร์ (ปัจจุบัน)", "รังสิต (ปัจจุบัน)", "ลำปาง/พัทยา"],
                      color=["#C62828", "#F57C00", "#D32F2F", "#1976D2", "#2E7D32"]),
            link=dict(source=[0, 0, 1, 1], target=[2, 3, 3, 4], value=[6500, 18000, 14000, 3700])
        )])
        fig.update_layout(title="สายธารการโยกย้ายศูนย์การศึกษา (Sankey Diagram)", height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 6:
        fig = go.Figure(go.Waterfall(
            name="2025", orientation="v",
            measure=["relative", "relative", "relative", "relative", "relative", "total"],
            x=['อุดหนุนรัฐ', 'ค่าธรรมเนียม', 'บริการ/รพ.', 'ทุนวิจัยภายนอก', 'ทรัพย์สิน', 'รวม'],
            text=["+3,600", "+4,200", "+1,800", "+1,100", "+800", "11,500 ลบ."],
            y=[3600, 4200, 1800, 1100, 800, 0],
            connector={"line": {"color": "gray"}},
            increasing={"marker": {"color": "#C62828"}},
            totals={"marker": {"color": "#1A237E"}}
        ))
        fig.update_layout(title="โครงสร้างรายได้และงบประมาณ มธ. 11,500 ลบ.", template="simple_white", height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 7:
        years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
        qs = [137, 134, 119, 111, 107, 96, 81, 73, 68]
        fig = px.line(x=years, y=qs, markers=True, title="อันดับ QS Asia University Rankings (อันดับดียิ่งขึ้น)",
                      labels={"x": "ปี", "y": "อันดับ"})
        fig.update_yaxes(autorange="reversed")
        fig.update_traces(line_color="#C62828", line_width=3)
        fig.update_layout(template="simple_white", height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 8:
        categories = ['SDG 11: เมืองยั่งยืน', 'SDG 7: พลังงานสะอาด', 'SDG 13: ภูมิอากาศ', 'SDG 3: สุขภาพ', 'SDG 4: การศึกษา']
        scores = [98.5, 92.0, 88.4, 85.0, 91.2]
        fig = px.line_polar(r=scores, theta=categories, line_close=True, title="คะแนน THE Impact Rankings ด้านความยั่งยืน")
        fig.update_traces(fill='toself', fillcolor="rgba(46,125,50,0.25)", line_color="#2E7D32")
        fig.update_layout(height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 9:
        years = [1987, 1995, 2005, 2015, 2020, 2025]
        patients = [50000, 180000, 480000, 920000, 1250000, 1460000]
        fig = px.bar(x=years, y=patients, title="สถิติผู้ป่วยนอก รพ.ธรรมศาสตร์ (คน/ปี)",
                     labels={"x": "ปี ค.ศ.", "y": "ผู้ป่วยนอก (คน)"}, color_discrete_sequence=["#C62828"])
        fig.update_layout(template="simple_white", height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif scene_idx == 10:
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=78,
            title={'text': "เป้าหมาย Net-Zero 2030 ความคืบหน้า (%)"},
            delta={'reference': 60, 'increasing': {'color': "green"}},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#C62828"},
                'steps': [
                    {'range': [0, 50], 'color': "#FFEBEE"},
                    {'range': [50, 85], 'color': "#FFF9C4"},
                    {'range': [85, 100], 'color': "#E8F5E9"}
                ]
            }
        ))
        fig.update_layout(height=450)
        st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("จัดทำขึ้นสำหรับวิชา BI304 มหาวิทยาลัยธรรมศาสตร์ | ข้อมูลอ้างอิงจากรายงานประจำปี มธ. และสำนักทะเบียนฯ")
