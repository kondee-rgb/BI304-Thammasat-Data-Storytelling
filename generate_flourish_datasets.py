"""
Generate clean, ready-to-import CSV files for Flourish (flourish.studio)
Designed for BI304: Thammasat University 10-Scene Data Storytelling
"""

import pandas as pd
import os

out_dir = r"d:\BI304\flourish_data"
os.makedirs(out_dir, exist_ok=True)

# 1. Bar Chart Race: Faculty Enrollment over Time (1934 - 2026)
faculties = [
    "Law (นิติศาสตร์)", "Business (พาณิชย์ฯ TBS)", "Political Science (รัฐศาสตร์)",
    "Economics (เศรษฐศาสตร์)", "Liberal Arts (ศิลปศาสตร์)", "Engineering (TSE วิศวกรรม)",
    "Science & Tech (วิทยาศาสตร์)", "Medicine (แพทยศาสตร์)", "Allied Health (สหเวชศาสตร์)",
    "International Institute (SIIT)"
]

years = [1934, 1945, 1955, 1965, 1975, 1985, 1995, 2005, 2015, 2026]
race_data = {
    "Faculty": faculties,
    "Cluster": [
        "Social Sciences", "Business", "Social Sciences", "Social Sciences", "Humanities",
        "Science & Tech", "Science & Tech", "Health Sciences", "Health Sciences", "International"
    ],
    "1934": [7094, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "1945": [6500, 1800, 1500, 0, 0, 0, 0, 0, 0, 0],
    "1955": [1800, 1200, 800, 400, 0, 0, 0, 0, 0, 0],
    "1965": [3200, 2800, 1900, 1600, 2000, 0, 0, 0, 0, 0],
    "1975": [4100, 3600, 2400, 2100, 3200, 0, 0, 0, 0, 0],
    "1985": [4500, 4100, 2600, 2400, 3600, 0, 1500, 0, 0, 0],
    "1995": [4400, 4500, 2400, 2300, 3400, 1800, 2900, 400, 0, 800],
    "2005": [4100, 4800, 2300, 2300, 3100, 3200, 3600, 800, 1100, 2100],
    "2015": [3900, 4900, 2200, 2250, 2800, 3900, 3800, 1100, 1600, 2900],
    "2026": [3800, 4950, 2100, 2200, 2600, 4200, 3900, 1200, 1900, 3100]
}
df_race = pd.DataFrame(race_data)
df_race.to_csv(os.path.join(out_dir, "01_flourish_bar_chart_race_faculties.csv"), index=False, encoding="utf-8-sig")

# 2. Campus Map coordinates (for Flourish Projection Map / Marker Map)
campuses = [
    {"Campus_Name": "ท่าพระจันทร์ (Tha Prachan)", "Latitude": 13.7557, "Longitude": 100.4930, "Area_Rai": 49, "Students": 6500, "Role": "Historic / International Hub", "Founded_Year": 1934},
    {"Campus_Name": "ศูนย์รังสิต (Rangsit Center)", "Latitude": 14.0736, "Longitude": 100.6067, "Area_Rai": 1757, "Students": 32000, "Role": "Main Hub / Medical & Innovation", "Founded_Year": 1986},
    {"Campus_Name": "ศูนย์ลำปาง (Lampang Center)", "Latitude": 18.2982, "Longitude": 99.4897, "Area_Rai": 464, "Students": 2200, "Role": "Northern Education Hub", "Founded_Year": 1996},
    {"Campus_Name": "ศูนย์พัทยา (Pattaya Center)", "Latitude": 12.9236, "Longitude": 100.9925, "Area_Rai": 566, "Students": 1500, "Role": "EEC High-Tech & Automotive", "Founded_Year": 1995}
]
df_map = pd.DataFrame(campuses)
df_map.to_csv(os.path.join(out_dir, "02_flourish_campuses_map.csv"), index=False, encoding="utf-8-sig")

# 3. Hierarchy / Treemap of 19 Faculties
tree_data = [
    {"Cluster": "สังคมศาสตร์-มนุษยศาสตร์", "Faculty": "นิติศาสตร์ (Law)", "Students": 3800, "Color": "#C62828"},
    {"Cluster": "สังคมศาสตร์-มนุษยศาสตร์", "Faculty": "พาณิชยศาสตร์และการบัญชี (TBS)", "Students": 4950, "Color": "#C62828"},
    {"Cluster": "สังคมศาสตร์-มนุษยศาสตร์", "Faculty": "รัฐศาสตร์ (Pol Sci)", "Students": 2100, "Color": "#C62828"},
    {"Cluster": "สังคมศาสตร์-มนุษยศาสตร์", "Faculty": "เศรษฐศาสตร์ (Econ)", "Students": 2200, "Color": "#C62828"},
    {"Cluster": "สังคมศาสตร์-มนุษยศาสตร์", "Faculty": "ศิลปศาสตร์ (Liberal Arts)", "Students": 2600, "Color": "#C62828"},
    {"Cluster": "สังคมศาสตร์-มนุษยศาสตร์", "Faculty": "วารสารศาสตร์ฯ (JC)", "Students": 1300, "Color": "#C62828"},
    {"Cluster": "สังคมศาสตร์-มนุษยศาสตร์", "Faculty": "สังคมวิทยาและมานุษยวิทยา", "Students": 1000, "Color": "#C62828"},
    {"Cluster": "วิทยาศาสตร์และเทคโนโลยี", "Faculty": "วิศวกรรมศาสตร์ (TSE)", "Students": 4200, "Color": "#1565C0"},
    {"Cluster": "วิทยาศาสตร์และเทคโนโลยี", "Faculty": "วิทยาศาสตร์และเทคโนโลยี", "Students": 3900, "Color": "#1565C0"},
    {"Cluster": "วิทยาศาสตร์และเทคโนโลยี", "Faculty": "สถาปัตยกรรมศาสตร์ฯ", "Students": 1600, "Color": "#1565C0"},
    {"Cluster": "วิทยาศาสตร์และเทคโนโลยี", "Faculty": "วิทยาลัยนวัตกรรม", "Students": 1400, "Color": "#1565C0"},
    {"Cluster": "วิทยาศาสตร์สุขภาพ", "Faculty": "แพทยศาสตร์ (Medicine)", "Students": 1200, "Color": "#2E7D32"},
    {"Cluster": "วิทยาศาสตร์สุขภาพ", "Faculty": "ทันตแพทยศาสตร์ (Dentistry)", "Students": 850, "Color": "#2E7D32"},
    {"Cluster": "วิทยาศาสตร์สุขภาพ", "Faculty": "สหเวชศาสตร์ (Allied Health)", "Students": 1900, "Color": "#2E7D32"},
    {"Cluster": "วิทยาศาสตร์สุขภาพ", "Faculty": "พยาบาลศาสตร์ (Nursing)", "Students": 1100, "Color": "#2E7D32"},
    {"Cluster": "วิทยาศาสตร์สุขภาพ", "Faculty": "เภสัชศาสตร์ (Pharmacy)", "Students": 1200, "Color": "#2E7D32"},
    {"Cluster": "วิทยาศาสตร์สุขภาพ", "Faculty": "สาธารณสุขศาสตร์ (Public Health)", "Students": 1400, "Color": "#2E7D32"},
    {"Cluster": "นานาชาติและสถาบันบูรณาการ", "Faculty": "SIIT สถาบันเทคโนโลยีนานาชาติสิรินธร", "Students": 3100, "Color": "#E65100"},
    {"Cluster": "นานาชาติและสถาบันบูรณาการ", "Faculty": "วิทยาลัยนานาชาติปรีดี พนมยงค์ (PBIC)", "Students": 900, "Color": "#E65100"},
    {"Cluster": "นานาชาติและสถาบันบูรณาการ", "Faculty": "วิทยาลัยสหวิทยาการ", "Students": 1100, "Color": "#E65100"},
    {"Cluster": "นานาชาติและสถาบันบูรณาการ", "Faculty": "วิทยาลัยพัฒนศาสตร์ ป๋วย อึ๊งภากรณ์", "Students": 900, "Color": "#E65100"}
]
df_tree = pd.DataFrame(tree_data)
df_tree.to_csv(os.path.join(out_dir, "03_flourish_hierarchy_clusters.csv"), index=False, encoding="utf-8-sig")

# 4. Demographics Gender
df_demo = pd.DataFrame({
    "Academic_Cluster": ["สังคมศาสตร์-มนุษยศาสตร์", "วิทยาศาสตร์และเทคโนโลยี", "วิทยาศาสตร์สุขภาพ", "นานาชาติ/บูรณาการ"],
    "Female_Students": [11450, 4880, 5200, 3600],
    "Male_Students": [6450, 6220, 2450, 2400],
    "Total": [17900, 11100, 7650, 6000]
})
df_demo.to_csv(os.path.join(out_dir, "04_flourish_demographics_gender.csv"), index=False, encoding="utf-8-sig")

# 5. Rankings Time Series
df_ranks = pd.DataFrame({
    "Year": [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "QS_Asia_Rank": [137, 134, 119, 111, 107, 96, 81, 73, 68],
    "QS_Business_Management_World_Rank": [250, 230, 210, 190, 180, 160, 150, 140, 130],
    "QS_Law_World_Rank": [220, 200, 190, 175, 160, 150, 140, 130, 120]
})
df_ranks.to_csv(os.path.join(out_dir, "05_flourish_rankings_time_series.csv"), index=False, encoding="utf-8-sig")

# 6. SDG Radar Scores
df_sdg = pd.DataFrame({
    "SDG_Goal": [
        "SDG 11: Sustainable Cities (Top 10 Global)",
        "SDG 7: Affordable & Clean Energy",
        "SDG 13: Climate Action",
        "SDG 3: Good Health & Well-Being",
        "SDG 4: Quality Education",
        "SDG 17: Partnerships for Goals"
    ],
    "Thammasat_Score": [98.5, 92.0, 88.4, 85.0, 91.2, 84.5],
    "Global_Average": [62.4, 58.1, 54.0, 61.2, 65.0, 52.3]
})
df_sdg.to_csv(os.path.join(out_dir, "06_flourish_sdg_scores.csv"), index=False, encoding="utf-8-sig")

print("All 6 Flourish datasets generated successfully in:", out_dir)
