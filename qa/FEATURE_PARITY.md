# ตารางตรวจสอบความเท่าเทียมของฟังก์ชัน (Feature Parity Matrix)

> **วิชา**: BI304 Thammasat Data Storytelling  
> **สถานะ**: Baseline Recorded (v1-baseline)  
> **เกณฑ์ผ่าน**: ทุกแถวในตารางนี้ต้องมีสถานะ 'คงเดิม' / 'ปรับปรุง' / 'แทนที่ด้วย...' และผ่านการทดสอบด้วยมือครบ 100% ก่อนส่งมอบ

## 1. องค์ประกอบการโต้ตอบหลัก (Major Interactive Features)

| ลำดับ | ฟีเจอร์ / องค์ประกอบ | ประเภท | ตำแหน่ง / ID | พฤติกรรมเดิม (Baseline) | สถานะหลังปรับปรุง | หมายเหตุ / แผนพัฒนา |
|:---:|:---|:---|:---|:---|:---:|:---|
| 01 | **Header Brand Title** | Header Navigation | `header .header-brand` | คลิกเพื่อกลับไปจุดเริ่มต้นของหน้า | **ปรับปรุง** | เปลี่ยนเป็น <a> พร้อม aria-label และ scroll-behavior |
| 02 | **Top Navigation Links (10 Topics)** | Header Menu | `.header-nav-links a` | กดเพื่อกระโดดไปยังแต่ละหัวข้อแบบ Smooth Scroll | **ปรับปรุง** | รองรับ scroll-margin-top ชัดเจน และแสดง active indicator |
| 03 | **Mobile Drawer Toggle** | Mobile UI | `#mobileMenuBtn` | เปิด/ปิด Drawer เมนูบนอุปกรณ์มือถือ | **ปรับปรุง** | เพิ่ม aria-expanded, aria-controls และ Esc key handler |
| 04 | **Colab 1-Click Link** | External Resource | `.header-colab-btn` | เปิด Google Colab โค้ดวิเคราะห์ข้อมูล | **คงเดิม** | คงลิงก์ Colab ไว้บน Header และส่วนสรุปท้ายเว็บ |
| 05 | **Flourish 10-Scenes Modal Trigger** | Modal Trigger | `.header-flourish-btn` | เปิด Flourish Hub รวม 10 Visualizations | **ปรับปรุง** | เพิ่ม Accessibility (Focus Trap, Esc, aria-modal) |
| 06 | **Bottom Scrubber Track & Pips** | Navigation Scrubber | `#scrubberTrack, .scrubber-pip` | แสดงแถบความคืบหน้า 10 หัวข้อ และคลิกเพื่อเลื่อนไปยังหัวข้อนั้น | **ปรับปรุง** | เพิ่ม role='slider', aria-valuenow และ keyboard controls |
| 07 | **Scrubber Topic Indicator Pill** | Navigation Scrubber | `#scrubberTopicIndicator` | แสดงชื่อหัวข้อปัจจุบันที่กำลังอ่านอยู่ | **ปรับปรุง** | ปรับให้อ่านง่ายและแม่นยำขึ้น |
| 08 | **Scroll Down to Race Pill** | Hero CTA | `.hero-scroll-pill-btn` | คลิกเพื่อเลื่อนลงไปยังหัวข้อที่ 1 | **ปรับปรุง** | เปลี่ยนข้อความจากธีมแข่งรถเป็น 'เริ่มต้นการเดินทาง 90 ปี' |
| 09 | **Milestone Stepper (7 Epochs)** | Topic 01 Timeline | `.stepper-node` | คลิกเลือกยุคสมัย 1 ถึง 7 สลับข้อมูลใน Milestone Card | **ปรับปรุง** | เปลี่ยน div เป็น semantic button พร้อม aria-selected |
| 10 | **Campus GIS Map Switcher (Street/Satellite)** | Topic 02 Leaflet Map | `#btnStreetView, #btnSatView` | สลับ Layer แผนที่ถนน Esri และดาวเทียม Esri Satellite | **ปรับปรุง** | เพิ่ม attributionControl ให้ถูกต้องตามสัญญาอนุญาต |
| 11 | **Campus Reset View Button** | Topic 02 Leaflet Map | `.map-tool-btn (resetMapView)` | รีเซ็ตพิกัดและซูมของแผนที่กลับสู่ภาพรวม | **คงเดิม** | ทำงานร่วมกับคีย์บอร์ดได้ |
| 12 | **Campus Selector Pills (4 Campuses)** | Topic 02 Leaflet Map | `.cluster-select-btn` | คลิกสลับดูข้อมูล 4 ศูนย์การศึกษา พร้อม flyTo แผนที่ | **ปรับปรุง** | รองรับการแสดงผลตัวเลขและหน่วย <span class='unit'> |
| 13 | **Leaflet Interactive Pins & Popups** | Topic 02 Leaflet Map | `tuMarkers (Leaflet)` | คลิกหมุดเพื่อเปิด Popup ข้อมูลสถิติของแต่ละศูนย์ | **ปรับปรุง** | เพิ่ม 2-finger scroll บนมือถือ ไม่ให้แย่ง scroll หน้าเว็บ |
| 14 | **Faculties View Mode Toggle (Chart/Grid)** | Topic 03 Faculties | `#btnFacChartView, #btnFacGridView` | สลับมุมมองระหว่างกราฟแท่งแนวนอนกับการ์ด 26 คณะ | **ปรับปรุง** | เพิ่ม aria-pressed และคีย์บอร์ดนำทาง |
| 15 | **Faculties Academic Cluster Filters** | Topic 03 Faculties | `.fac-pill` | กรองคณะตาม 4 คลัสเตอร์วิชาการ | **ปรับปรุง** | ซิงค์ทั้งกราฟแท่งและการ์ด 26 คณะ |
| 16 | **Faculties Horizontal Bar Chart** | Topic 03 Faculties | `#facultiesTcasChartCanvas` | กราฟแท่ง TCAS แสดงคะแนนต่ำสุด คลิกเปิด Modal | **ปรับปรุง** | เลิกตัดแกน (เริ่มที่ 0) หรือเปลี่ยนเป็น Dot plot ที่ถูกต้อง |
| 17 | **Faculty Detail Modal** | Topic 03 Modal | `#facultyModal` | แสดงสถิติเจาะลึก อัตราแข่งขัน เกณฑ์ และอาชีพของคณะ | **ปรับปรุง** | เพิ่ม Esc to close, focus trap, aria-modal และล็อกพื้นหลัง |
| 18 | **Budget 5-Year Multi-Stream Chart** | Topic 06 Financial | `#budgetChartCanvas` | กราฟเส้น Chart.js แสดงงบประมาณ 5 ปี | **ปรับปรุง** | เพิ่ม Sticky Scrollytelling และ Direct Labels |
| 19 | **Budget Stream Drilldown Pills (6 Options)** | Topic 06 Financial | `.drilldown-pill` | สลับดูกราฟ 5 แหล่งรายได้ และงบประมาณรวม 5 ปี | **ปรับปรุง** | ปรับปรุงการเชื่อมต่อกับคำอธิบายข้อมูลและแหล่งที่มา |
| 20 | **Green Sustainability Toggle** | Topic 08 Green | `#greenSustainabilityCanvas` | แผนภูมิแสดงมิติความยั่งยืนและโซลาร์เซลล์ | **ปรับปรุง** | เพิ่ม Annotations และบริบทเปรียบเทียบ |
| 21 | **Hospital Capacity & Patient Volume Toggle** | Topic 09 Hospital | `#btnHospTrend, #btnHospBeds` | สลับดูกราฟผู้ป่วย 6 ปี และสัดส่วนเตียง 1,400 เตียง | **ปรับปรุง** | แก้ปัญหาการสลับกราฟและ Re-render ให้นุ่มนวล |
| 22 | **Centennial Pillars 4 Nodes Selector** | Topic 10 Centennial | `.circuit-milestone-node` | คลิกเลือกเสาหลัก 1-4 สลับภาพและสถิติ | **ปรับปรุง** | เชื่อมโยง 4 ภาพใหม่เฉพาะด้าน และเพิ่ม semantic buttons |
| 23 | **TU 2034 Strategy Cockpit Sliders** | Topic 10 Simulator | `#slideResearch, #slideSkills, ...` | สไลเดอร์ 4 ด้านคำนวณ Composite Score | **ปรับปรุง** | แก้ไขค่าเริ่มต้น 91.95 vs 92.4 ให้ตรงกัน พร้อมปุ่ม Reset |
| 24 | **Scroll-Triggered Animated Counters** | Site-wide Engine | `.stat-counter` | นับตัวเลขขึ้นจาก 0 ด้วย IntersectionObserver | **ปรับปรุง** | รองรับ prefers-reduced-motion แสดงผลทันทีเมื่อตั้งค่าไว้ |

## 2. รายการฟังก์ชัน JavaScript ทั้งหมดในระบบ (Declared JS Functions)

| ลำดับ | ชื่อฟังก์ชัน | พารามิเตอร์ | วัตถุประสงค์การทำงาน | สถานะหลังปรับปรุง |
|:---:|:---|:---|:---|:---:|
| 01 | `initScrollInteractions` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 02 | `handleScrubberClick` | `e` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 03 | `initTuLeafletMap` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 04 | `setMapTileStyle` | `style` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 05 | `resetMapView` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 06 | `selectCampusCluster` | `idx` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 07 | `setMilestoneStep` | `idx` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 08 | `selectCircuitNode` | `idx` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 09 | `drilldownStream` | `idx` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 10 | `initFacultiesTcasChart` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 11 | `setFacultiesView` | `mode` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 12 | `renderFaculties` | `filter` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 13 | `filterFaculties` | `pillar, btnEl` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 14 | `openFacultyModal` | `fac` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 15 | `closeFacultyModal` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 16 | `updateCockpit` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 17 | `openFlourishHubModal` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 18 | `closeFlourishHubModal` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 19 | `renderFlourishTabs` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 20 | `selectFlourishScene` | `idx` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 21 | `toggleMobileNav` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 22 | `closeMobileNav` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 23 | `initGreenSustainabilityChart` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 24 | `switchGreenVisual` | `mode` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 25 | `initHospitalCapacityChart` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 26 | `switchHospitalVisual` | `mode` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 27 | `initCharts` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 28 | `setDistributionEra` | `mode, btnEl` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 29 | `initAnimatedCounters` | `` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 30 | `stepFrame` | `cb` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 31 | `runCounterAnimation` | `el` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |
| 32 | `update` | `now` | การทำงานของฟังก์ชันในระบบ | **ปรับปรุง** |