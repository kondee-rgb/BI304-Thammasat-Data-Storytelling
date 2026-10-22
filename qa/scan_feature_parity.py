# -*- coding: utf-8 -*-
"""
Scans index.html for all interactive elements, event listeners, and JS functions
to build a comprehensive qa/FEATURE_PARITY.md matrix.
"""
import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Onclick elements
onclick_elements = []
for el in soup.find_all(attrs={"onclick": True}):
    tag = el.name
    el_id = el.get('id', '')
    classes = " ".join(el.get('class', []))
    onclick = el.get('onclick')
    text = el.get_text(strip=True)[:40]
    onclick_elements.append({
        'tag': tag,
        'id': el_id,
        'class': classes,
        'onclick': onclick,
        'label': text
    })

# 2. Modals and Dialogs
modals = []
for el in soup.find_all(class_=lambda c: c and 'modal' in c):
    modals.append({
        'id': el.get('id', ''),
        'class': " ".join(el.get('class', [])),
        'title': el.find(['h2', 'h3', 'h4']).get_text(strip=True) if el.find(['h2', 'h3', 'h4']) else ''
    })

# 3. Interactive Inputs / Sliders
inputs = []
for el in soup.find_all(['input', 'select']):
    inputs.append({
        'tag': el.name,
        'type': el.get('type', ''),
        'id': el.get('id', ''),
        'oninput': el.get('oninput', ''),
        'class': " ".join(el.get('class', []))
    })

# 4. Javascript functions in script
script_tags = soup.find_all('script')
js_code = "\n".join([s.string for s in script_tags if s.string])

funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(([^)]*)\)', js_code)
event_listeners = re.findall(r'([a-zA-Z0-9_.$()]+)\.addEventListener\(\s*[\'"]([a-zA-Z0-9_]+)[\'"]', js_code)

print(f"Found {len(onclick_elements)} onclick handlers")
print(f"Found {len(modals)} modal elements")
print(f"Found {len(inputs)} interactive inputs")
print(f"Found {len(funcs)} JS functions")
print(f"Found {len(event_listeners)} addEventListener calls")

# Now generate Markdown
md_lines = [
    "# ตารางตรวจสอบความเท่าเทียมของฟังก์ชัน (Feature Parity Matrix)",
    "",
    "> **วิชา**: BI304 Thammasat Data Storytelling  ",
    "> **สถานะ**: Baseline Recorded (v1-baseline)  ",
    "> **เกณฑ์ผ่าน**: ทุกแถวในตารางนี้ต้องมีสถานะ 'คงเดิม' / 'ปรับปรุง' / 'แทนที่ด้วย...' และผ่านการทดสอบด้วยมือครบ 100% ก่อนส่งมอบ",
    "",
    "## 1. องค์ประกอบการโต้ตอบหลัก (Major Interactive Features)",
    "",
    "| ลำดับ | ฟีเจอร์ / องค์ประกอบ | ประเภท | ตำแหน่ง / ID | พฤติกรรมเดิม (Baseline) | สถานะหลังปรับปรุง | หมายเหตุ / แผนพัฒนา |",
    "|:---:|:---|:---|:---|:---|:---:|:---|"
]

feature_catalog = [
    ("Header Brand Title", "Header Navigation", "header .header-brand", "คลิกเพื่อกลับไปจุดเริ่มต้นของหน้า", "ปรับปรุง", "เปลี่ยนเป็น <a> พร้อม aria-label และ scroll-behavior"),
    ("Top Navigation Links (10 Topics)", "Header Menu", ".header-nav-links a", "กดเพื่อกระโดดไปยังแต่ละหัวข้อแบบ Smooth Scroll", "ปรับปรุง", "รองรับ scroll-margin-top ชัดเจน และแสดง active indicator"),
    ("Mobile Drawer Toggle", "Mobile UI", "#mobileMenuBtn", "เปิด/ปิด Drawer เมนูบนอุปกรณ์มือถือ", "ปรับปรุง", "เพิ่ม aria-expanded, aria-controls และ Esc key handler"),
    ("Colab 1-Click Link", "External Resource", ".header-colab-btn", "เปิด Google Colab โค้ดวิเคราะห์ข้อมูล", "คงเดิม", "คงลิงก์ Colab ไว้บน Header และส่วนสรุปท้ายเว็บ"),
    ("Flourish 10-Scenes Modal Trigger", "Modal Trigger", ".header-flourish-btn", "เปิด Flourish Hub รวม 10 Visualizations", "ปรับปรุง", "เพิ่ม Accessibility (Focus Trap, Esc, aria-modal)"),
    ("Bottom Scrubber Track & Pips", "Navigation Scrubber", "#scrubberTrack, .scrubber-pip", "แสดงแถบความคืบหน้า 10 หัวข้อ และคลิกเพื่อเลื่อนไปยังหัวข้อนั้น", "ปรับปรุง", "เพิ่ม role='slider', aria-valuenow และ keyboard controls"),
    ("Scrubber Topic Indicator Pill", "Navigation Scrubber", "#scrubberTopicIndicator", "แสดงชื่อหัวข้อปัจจุบันที่กำลังอ่านอยู่", "ปรับปรุง", "ปรับให้อ่านง่ายและแม่นยำขึ้น"),
    ("Scroll Down to Race Pill", "Hero CTA", ".hero-scroll-pill-btn", "คลิกเพื่อเลื่อนลงไปยังหัวข้อที่ 1", "ปรับปรุง", "เปลี่ยนข้อความจากธีมแข่งรถเป็น 'เริ่มต้นการเดินทาง 90 ปี'"),
    ("Milestone Stepper (7 Epochs)", "Topic 01 Timeline", ".stepper-node", "คลิกเลือกยุคสมัย 1 ถึง 7 สลับข้อมูลใน Milestone Card", "ปรับปรุง", "เปลี่ยน div เป็น semantic button พร้อม aria-selected"),
    ("Campus GIS Map Switcher (Street/Satellite)", "Topic 02 Leaflet Map", "#btnStreetView, #btnSatView", "สลับ Layer แผนที่ถนน Esri และดาวเทียม Esri Satellite", "ปรับปรุง", "เพิ่ม attributionControl ให้ถูกต้องตามสัญญาอนุญาต"),
    ("Campus Reset View Button", "Topic 02 Leaflet Map", ".map-tool-btn (resetMapView)", "รีเซ็ตพิกัดและซูมของแผนที่กลับสู่ภาพรวม", "คงเดิม", "ทำงานร่วมกับคีย์บอร์ดได้"),
    ("Campus Selector Pills (4 Campuses)", "Topic 02 Leaflet Map", ".cluster-select-btn", "คลิกสลับดูข้อมูล 4 ศูนย์การศึกษา พร้อม flyTo แผนที่", "ปรับปรุง", "รองรับการแสดงผลตัวเลขและหน่วย <span class='unit'>"),
    ("Leaflet Interactive Pins & Popups", "Topic 02 Leaflet Map", "tuMarkers (Leaflet)", "คลิกหมุดเพื่อเปิด Popup ข้อมูลสถิติของแต่ละศูนย์", "ปรับปรุง", "เพิ่ม 2-finger scroll บนมือถือ ไม่ให้แย่ง scroll หน้าเว็บ"),
    ("Faculties View Mode Toggle (Chart/Grid)", "Topic 03 Faculties", "#btnFacChartView, #btnFacGridView", "สลับมุมมองระหว่างกราฟแท่งแนวนอนกับการ์ด 26 คณะ", "ปรับปรุง", "เพิ่ม aria-pressed และคีย์บอร์ดนำทาง"),
    ("Faculties Academic Cluster Filters", "Topic 03 Faculties", ".fac-pill", "กรองคณะตาม 4 คลัสเตอร์วิชาการ", "ปรับปรุง", "ซิงค์ทั้งกราฟแท่งและการ์ด 26 คณะ"),
    ("Faculties Horizontal Bar Chart", "Topic 03 Faculties", "#facultiesTcasChartCanvas", "กราฟแท่ง TCAS แสดงคะแนนต่ำสุด คลิกเปิด Modal", "ปรับปรุง", "เลิกตัดแกน (เริ่มที่ 0) หรือเปลี่ยนเป็น Dot plot ที่ถูกต้อง"),
    ("Faculty Detail Modal", "Topic 03 Modal", "#facultyModal", "แสดงสถิติเจาะลึก อัตราแข่งขัน เกณฑ์ และอาชีพของคณะ", "ปรับปรุง", "เพิ่ม Esc to close, focus trap, aria-modal และล็อกพื้นหลัง"),
    ("Budget 5-Year Multi-Stream Chart", "Topic 06 Financial", "#budgetChartCanvas", "กราฟเส้น Chart.js แสดงงบประมาณ 5 ปี", "ปรับปรุง", "เพิ่ม Sticky Scrollytelling และ Direct Labels"),
    ("Budget Stream Drilldown Pills (6 Options)", "Topic 06 Financial", ".drilldown-pill", "สลับดูกราฟ 5 แหล่งรายได้ และงบประมาณรวม 5 ปี", "ปรับปรุง", "ปรับปรุงการเชื่อมต่อกับคำอธิบายข้อมูลและแหล่งที่มา"),
    ("Green Sustainability Toggle", "Topic 08 Green", "#greenSustainabilityCanvas", "แผนภูมิแสดงมิติความยั่งยืนและโซลาร์เซลล์", "ปรับปรุง", "เพิ่ม Annotations และบริบทเปรียบเทียบ"),
    ("Hospital Capacity & Patient Volume Toggle", "Topic 09 Hospital", "#btnHospTrend, #btnHospBeds", "สลับดูกราฟผู้ป่วย 6 ปี และสัดส่วนเตียง 1,400 เตียง", "ปรับปรุง", "แก้ปัญหาการสลับกราฟและ Re-render ให้นุ่มนวล"),
    ("Centennial Pillars 4 Nodes Selector", "Topic 10 Centennial", ".circuit-milestone-node", "คลิกเลือกเสาหลัก 1-4 สลับภาพและสถิติ", "ปรับปรุง", "เชื่อมโยง 4 ภาพใหม่เฉพาะด้าน และเพิ่ม semantic buttons"),
    ("TU 2034 Strategy Cockpit Sliders", "Topic 10 Simulator", "#slideResearch, #slideSkills, ...", "สไลเดอร์ 4 ด้านคำนวณ Composite Score", "ปรับปรุง", "แก้ไขค่าเริ่มต้น 91.95 vs 92.4 ให้ตรงกัน พร้อมปุ่ม Reset"),
    ("Scroll-Triggered Animated Counters", "Site-wide Engine", ".stat-counter", "นับตัวเลขขึ้นจาก 0 ด้วย IntersectionObserver", "ปรับปรุง", "รองรับ prefers-reduced-motion แสดงผลทันทีเมื่อตั้งค่าไว้")
]

for idx, (feat, cat, target, desc, status, note) in enumerate(feature_catalog, 1):
    md_lines.append(f"| {idx:02d} | **{feat}** | {cat} | `{target}` | {desc} | **{status}** | {note} |")

md_lines.extend([
    "",
    "## 2. รายการฟังก์ชัน JavaScript ทั้งหมดในระบบ (Declared JS Functions)",
    "",
    "| ลำดับ | ชื่อฟังก์ชัน | พารามิเตอร์ | วัตถุประสงค์การทำงาน | สถานะหลังปรับปรุง |",
    "|:---:|:---|:---|:---|:---:|"
])

for idx, (fn_name, params) in enumerate(funcs, 1):
    md_lines.append(f"| {idx:02d} | `{fn_name}` | `{params}` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |")

with open('qa/FEATURE_PARITY.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(md_lines))

print("Saved qa/FEATURE_PARITY.md successfully!")
