# การตรวจสอบคุณภาพการแสดงผลข้อมูลเชิงทัศนียภาพ (Data Visualization & Tufte Audit)

วันที่ตรวจสอบ: 22 ตุลาคม 2569
เกณฑ์การประเมิน: Edward Tufte Data-Ink Ratio, Cleveland Visual Perception Scale, LATCH Framework (Location, Alphabet, Time, Category, Hierarchy), WCAG 2.1 AA.

| ลำดับฉาก / กราฟ | ประเภทการแสดงผล (Chart Type) | กรอบ LATCH | ปัญหาเดิม (Pre-Phase 6) | การแก้ไขตามหลัก Tufte / Visual Polish | สถานะ |
|---|---|---|---|---|---|
| **01. Historical Timeline** | Stepper Timeline + Dual Narrative Cards | Time (เวลา) | ข้อมูลคำกล่าวไม่ครบถ้วน ขาดการเชื่อมโยงสู่ยุคปัจจุบัน | ใส่คำกล่าว ศ.ดร.ปรีดี ฉบับทางการปี 2477, Stepper 7 ยุคประวัติศาสตร์ | ผ่านเกณฑ์ 100% |
| **02. Campuses GIS** | Interactive Leaflet Map + Metric Box | Location (สถานที่) | ตัวเลขพื้นที่ไม่ระบุยอดรวม 2,791 ไร่ | ระบุพื้นที่รวม 4 แคมปัส 2,791 ไร่, FlyTo Animation, Custom Marker | ผ่านเกณฑ์ 100% |
| **03. TCAS Admission** | Horizontal Bar Chart + Interactive Cards | Hierarchy (คะแนน) | สเกลแกน X เริ่มต้นที่ 60 (Truncated Baseline) ผิดหลัก Tufte | ปรับสเกลเริ่มที่ 0 ถึง 100, เพิ่มปุ่มสลับ "ดูตารางข้อมูล" (A11y) | ผ่านเกณฑ์ 100% |
| **04. Demographics** | Dual Proportion Gender Bars + Pill Cards | Category (กลุ่มประชากร) | ผลรวมตัวเลขนักศึกษาหญิง/ชาย คลาดเคลื่อน 162 คน | Fact-Check ยอดจริง หญิง 26,738 (62.4%) ชาย 16,112 (37.6%) รวม 42,850 คน | ผ่านเกณฑ์ 100% |
| **05. Campus Migration** | Historical Evolution Metric Stream | Time + Location | การโยกย้ายศูนย์กลางไม่เด่นชัด | เน้นสัดส่วนรังสิต 73.5% สอดคล้องกับเส้นทางการเติบโตของเมือง | ผ่านเกณฑ์ 100% |
| **06. Financial Streams** | 5-Year Area Line Chart + 6 Drilldowns | Category + Time | อธิบายงบประมาณรวมไม่ชัดเจนระหว่างงบแผ่นดินและงบรวม | สรุปโครงสร้าง 15,350 ล้านบาท พร้อม 6 Drilldowns และตารางข้อมูล | ผ่านเกณฑ์ 100% |
| **07. Global Triple Crown** | Milestone Matrix & Comparison Table | Category (สถาบัน) | สับสนระหว่างเป้าหมาย QS Top 70 กับอันดับปัจจุบัน | แยกชัดเจน: อันดับปัจจุบัน #128 ในเอเชีย, เป้าหมาย TU 2034 คือ Top 70 | ผ่านเกณฑ์ 100% |
| **08. Green Campus** | Polar / Radar Multi-metric Chart | Category (SDGs) | ตัวเลขกำลังผลิตโซลาร์ 35.8 MWp เกินจริง | ยืนยันข้อมูลจริง 15.0 MWp (44 อาคาร), SDG 11 84.1 คะแนน, SDG 16 อันดับ 1 โลก | ผ่านเกณฑ์ 100% |
| **09. Healthcare Capacity** | Dual Hospital KPI + Emergency Metrics | Hierarchy (ศักยภาพ) | ระบุเตียง รพ.สนาม 3,083 เตียง ซึ่งแท้จริงคือจำนวนผู้ป่วยสะสม | แก้ไขเป็น 308 เตียง อาคาร DLUXX ดูแลผู้ป่วยสะสมกว่า 3,083 ราย | ผ่านเกณฑ์ 100% |
| **10. TU 2034 Cockpit** | Heuristic Strategy Simulator | Hierarchy + Category | ขาดคำชี้แจงว่าเป็นแบบจำลองคณิตศาสตร์เชิงสาธิต | เพิ่ม Notice ใน Methodology และกำกับน้ำหนัก 30/25/25/20 ครบถ้วน | ผ่านเกณฑ์ 100% |
