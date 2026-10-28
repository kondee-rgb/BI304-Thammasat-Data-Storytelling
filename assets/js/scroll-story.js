/* BI304 Scroll Story v1.1
 * Adds scroll-linked, accessible data scenes using figures already present in the site.
 * Original charts, maps, text, tables, and data remain untouched.
 */
(() => {
  'use strict';

  const PALETTE = {
    crimson: '#bd173e', navy: '#152346', blue: '#1d6fa5', female: '#a82c5f',
    green: '#1e7552', teal: '#0e7490', amber: '#9a5b00', violet: '#6b4fa8',
    slate: '#475569', light: '#cbd3df'
  };
  const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = (n) => Number(n).toLocaleString('en-US');

  const STORIES = {
    'topic-01': {
      kicker: '90-YEAR TIMELINE', title: 'จากตลาดวิชา สู่ประชากรนักศึกษา 42,850 คน',
      intro: 'เลื่อนดู 3 หมุดหมายหลัก เพื่อเห็นขนาดของมหาวิทยาลัยที่เปลี่ยนไปตามช่วงเวลา',
      accent: PALETTE.crimson,
      steps: [
        { period: 'พ.ศ. 2477', title: 'เริ่มต้นด้วยโอกาสทางการศึกษา', text: 'ข้อมูลฉากประวัติศาสตร์ระบุผู้สมัครรุ่นแรก 7,094 คน จุดเริ่มต้นของแนวคิด “ตลาดวิชา” ที่เปิดโอกาสให้ประชาชนเข้าถึงความรู้', metric: '7,094', metricValue: 7094, label: 'ผู้สมัครรุ่นแรก', support: 'พ.ศ. 2477 · มหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง', type: 'vertical', highlight: 0, bars: [
          { label: '2477', value: 7094, display: '7,094' }, { label: '2529', value: 21000, display: '21,000' }, { label: '2567', value: 42850, display: '42,850' }
        ], foot: 'ตัวเลขตามฉากประวัติศาสตร์และตารางตัวอย่างที่มีอยู่ในโปรเจกต์' },
        { period: 'พ.ศ. 2529', title: 'ขยายศูนย์การศึกษาเพื่อรองรับการเติบโต', text: 'การตั้งศูนย์รังสิตเป็นหมุดหมายสำคัญในการขยายพื้นที่เรียนรู้และรองรับหลักสูตรที่ต้องใช้พื้นที่และโครงสร้างพื้นฐานเพิ่มขึ้น', metric: '21,000', metricValue: 21000, label: 'นักศึกษาในข้อมูลหมุดหมาย', support: 'พ.ศ. 2529 · สถาปนาศูนย์รังสิต', type: 'vertical', highlight: 1, bars: [
          { label: '2477', value: 7094, display: '7,094' }, { label: '2529', value: 21000, display: '21,000' }, { label: '2567', value: 42850, display: '42,850' }
        ], foot: 'ตัวเลขตามตารางพัฒนาการในชุดข้อมูลเว็บไซต์' },
        { period: 'พ.ศ. 2567', title: 'มหาวิทยาลัยหลายศาสตร์ใน 4 ศูนย์', text: 'ข้อมูลสรุประบุประชากรนักศึกษารวม 42,850 คน ในโครงสร้าง 26 คณะและวิทยาลัย ตัวเลขนี้เป็นภาพรวมคนละชนิดกับ “ผู้สมัครรุ่นแรก”', metric: '42,850', metricValue: 42850, label: 'นักศึกษารวม', support: '26 คณะและวิทยาลัย · 4 ศูนย์การศึกษา', type: 'vertical', highlight: 2, bars: [
          { label: '2477', value: 7094, display: '7,094' }, { label: '2529', value: 21000, display: '21,000' }, { label: '2567', value: 42850, display: '42,850' }
        ], foot: 'เป็นการเปรียบเทียบหมุดหมายจากชุดข้อมูล ไม่ใช่ชุดข้อมูลรายปีต่อเนื่องทุกปี' }
      ]
    },
    'topic-02': {
      kicker: '4 STRATEGIC CAMPUSES', title: 'พื้นที่เรียนรู้ 4 ศูนย์ มีบทบาทต่างกัน',
      intro: 'สัดส่วนประชากร พื้นที่ และบทบาทของแต่ละศูนย์ช่วยให้เห็นภาพการกระจายตัวของธรรมศาสตร์', accent: PALETTE.teal,
      steps: [
        { period: 'ศูนย์ประวัติศาสตร์', title: 'ท่าพระจันทร์ · รากฐานใจกลางกรุงเทพฯ', text: 'พื้นที่ 104 ไร่ รองรับนักศึกษา 6,310 คน หรือ 14.8% ของประชากรที่ระบุในชุดข้อมูล และคงบทบาทด้านประวัติศาสตร์ นานาชาติ และบัณฑิตศึกษา', metric: '14.8%', label: 'สัดส่วนประชากรนักศึกษา', support: '104 ไร่ · 6,310 คน', type: 'horizontal', highlight: 'ท่าพระจันทร์', bars: [
          { label: 'รังสิต', value: 73.5, display: '73.5%', color: PALETTE.crimson }, { label: 'ท่าพระจันทร์', value: 14.8, display: '14.8%', color: PALETTE.teal }, { label: 'ลำปาง', value: 7.2, display: '7.2%', color: PALETTE.slate }, { label: 'พัทยา', value: 4.5, display: '4.5%', color: PALETTE.amber }
        ], foot: 'สัดส่วนทั้ง 4 ศูนย์รวมกันเป็น 100% ตามค่าที่แสดงในชุดข้อมูล' },
        { period: 'ศูนย์หลัก', title: 'รังสิต · แกนกลางการศึกษาและการแพทย์', text: 'ศูนย์รังสิตมีพื้นที่ 1,757 ไร่ และประชากรนักศึกษา 31,500 คน คิดเป็น 73.5% ตามข้อมูลในเว็บไซต์', metric: '73.5%', label: 'สัดส่วนประชากรนักศึกษา', support: '1,757 ไร่ · 31,500 คน', type: 'horizontal', highlight: 'รังสิต', bars: [
          { label: 'รังสิต', value: 73.5, display: '73.5%', color: PALETTE.crimson }, { label: 'ท่าพระจันทร์', value: 14.8, display: '14.8%', color: PALETTE.teal }, { label: 'ลำปาง', value: 7.2, display: '7.2%', color: PALETTE.slate }, { label: 'พัทยา', value: 4.5, display: '4.5%', color: PALETTE.amber }
        ], foot: 'ค่าเปอร์เซ็นต์ใช้ค่าที่ระบุในข้อมูลวิทยาเขตของโปรเจกต์' },
        { period: 'เครือข่ายภูมิภาค', title: 'ลำปางและพัทยา · ขยายโอกาสเฉพาะพื้นที่', text: 'ศูนย์ลำปางเน้นบริบทภาคเหนือ ส่วนศูนย์พัทยาเชื่อมโยงนวัตกรรมและ EEC ทั้งสองศูนย์รวมสัดส่วนประชากร 11.7% ตามข้อมูลเดิม', metric: '930 ไร่', label: 'พื้นที่รวมลำปางและพัทยา', support: 'ลำปาง 364 ไร่ · พัทยา 566 ไร่', type: 'horizontal', highlight: 'ภูมิภาค', bars: [
          { label: 'รังสิต', value: 73.5, display: '73.5%', color: PALETTE.crimson }, { label: 'ท่าพระจันทร์', value: 14.8, display: '14.8%', color: PALETTE.teal }, { label: 'ลำปาง', value: 7.2, display: '7.2%', color: PALETTE.slate }, { label: 'พัทยา', value: 4.5, display: '4.5%', color: PALETTE.amber }
        ], foot: 'พื้นที่รวม 930 ไร่คำนวณจากพื้นที่ 364 + 566 ไร่ที่ระบุในเว็บไซต์' }
      ]
    },
    'topic-03': {
      kicker: 'FACULTIES & TCAS', title: 'จาก 4 คลัสเตอร์ สู่ 26 คณะและวิทยาลัย',
      intro: 'สำรวจการกระจายตัวของกลุ่มวิชา แล้วค่อยดูตัวชี้วัดการรับเข้าที่เกี่ยวข้อง', accent: PALETTE.navy,
      steps: [
        { period: 'ภาพรวมโครงสร้าง', title: '4 คลัสเตอร์ครอบคลุมหลายสายความรู้', text: 'ชุดข้อมูลฉากโครงสร้างคณะกระจายนักศึกษาใน 4 กลุ่มหลัก ตัวเลขในแต่ละกลุ่มช่วยให้เห็นสัดส่วนความเชี่ยวชาญโดยรวม', metric: '26', label: 'คณะและวิทยาลัย', support: '4 คลัสเตอร์ทางวิชาการ', type: 'horizontal', bars: [
          { label: 'สังคมฯ / มนุษย์', value: 17900, display: '17,900 คน', color: PALETTE.crimson }, { label: 'วิทย์ / เทคโนโลยี', value: 11100, display: '11,100 คน', color: PALETTE.blue }, { label: 'สุขภาพ', value: 7650, display: '7,650 คน', color: PALETTE.green }, { label: 'นานาชาติ / บูรณาการ', value: 6200, display: '6,200 คน', color: PALETTE.violet }
        ], foot: 'จำนวนตามตารางตัวอย่างของฉากโครงสร้างคณะในโปรเจกต์' },
        { period: 'TCAS Admission 2566', title: 'คะแนนช่วยเปรียบเทียบความแข่งขัน', text: 'KPI ที่แสดงในเว็บระบุคะแนนตัดสูงสุด 83.1 คะแนน ค่าเฉลี่ย 72.9 คะแนน และอัตราการแข่งขันสูงสุด 14 เท่า อ่านตัวเลขเหล่านี้คู่กับเกณฑ์ของแต่ละหลักสูตร', metric: '83.1', label: 'คะแนนตัดสูงสุด', support: 'จาก 100 คะแนน · TCAS รอบ 3', type: 'pairs', pairs: [
          { label: 'คะแนนตัดสูงสุด', value: '83.1', note: 'คะแนนเต็ม 100' }, { label: 'ค่าเฉลี่ยรวม', value: '72.9', note: 'คะแนน TCAS' }, { label: 'อัตราแข่งขันสูงสุด', value: '14×', note: 'อัตราแข่งขัน' }, { label: 'ข้อมูลคณะ', value: '25 / 26', note: 'มีสถิติ TCAS ในเว็บ' }
        ], foot: 'ตัวชี้วัดคัดเลือกอ้างอิงจาก KPI และหมายเหตุที่แสดงอยู่ในหัวข้อนี้' },
        { period: 'สำรวจรายคณะ', title: 'คลิกกราฟเดิมเพื่อเจาะลึกหลักสูตร', text: 'เมื่อเข้าใจภาพรวมแล้ว ให้ใช้กราฟและตัวกรองด้านล่างเลือกคลัสเตอร์หรือคณะ เพื่อดูคะแนนตัดและเส้นทางอาชีพ โดยไม่ตีความค่าเฉลี่ยแทนทุกหลักสูตร', metric: '25 / 26', label: 'คณะ/สถาบันที่มีข้อมูล TCAS ในเว็บ', support: 'ใช้ตัวกรองเดิมด้านล่างเพื่อดูข้อมูลรายหลักสูตร', type: 'pairs', pairs: [
          { label: 'กลุ่มสังคมฯ / มนุษย์', value: '17,900', note: 'คนในตารางฉาก' }, { label: 'กลุ่มวิทย์ / เทคโนโลยี', value: '11,100', note: 'คนในตารางฉาก' }
        ], foot: 'เรื่องเล่านี้ไม่แทนที่กราฟ TCAS แบบโต้ตอบด้านล่าง' }
      ]
    },
    'topic-04': {
      kicker: 'STUDENT DEMOGRAPHICS', title: 'สัดส่วนเปลี่ยนไปตามกลุ่มสาขา',
      intro: 'รูปคน 100 รูปแทนสัดส่วนร้อยละ ไม่ใช่จำนวนคนจริง เลื่อนเพื่อเปรียบเทียบมหาวิทยาลัยกับกลุ่มสาขาที่มีข้อมูล', accent: PALETTE.female,
      steps: [
        { period: 'ภาพรวมทั้งมหาวิทยาลัย', title: 'ผู้หญิงคิดเป็น 62.4% ของนักศึกษา', text: 'จากประชากรนักศึกษา 42,850 คน มีนักศึกษาหญิง 26,738 คน และนักศึกษาชาย 16,112 คน ตามตัวเลขที่แสดงในหัวข้อนี้', metric: '62.4%', label: 'นักศึกษาหญิง', support: '26,738 หญิง · 16,112 ชาย · 42,850 คน', type: 'people', female: 62.4, male: 37.6, total: '42,850 คน', foot: 'แต่ละสัญลักษณ์แทนประมาณ 1% ของสัดส่วนรวม ไม่ใช่คนหนึ่งคน' },
        { period: 'วิทยาศาสตร์สุขภาพ', title: 'กลุ่มสุขภาพมีสัดส่วนหญิงสูงสุดในตัวอย่าง', text: 'นักศึกษาหญิง 71.5% และชาย 28.5% ในกลุ่มที่มีนักศึกษา 7,800 คนตามข้อมูลฉากความหลากหลาย', metric: '71.5%', label: 'นักศึกษาหญิงในกลุ่มสุขภาพ', support: '≈5,577 หญิง · 2,223 ชาย · รวม 7,800 คน', type: 'people', female: 71.5, male: 28.5, total: '7,800 คน', foot: 'สัดส่วนและจำนวนตามตารางฉากความหลากหลายที่มีอยู่ในโปรเจกต์' },
        { period: 'สังคมศาสตร์และมนุษยศาสตร์', title: 'กลุ่มใหญ่ที่สุดในตารางตัวอย่าง', text: 'กลุ่มสังคมศาสตร์และมนุษยศาสตร์มี 19,200 คน หญิง 64.2% และชาย 35.8% ตามชุดข้อมูลในเว็บ', metric: '64.2%', label: 'นักศึกษาหญิงในกลุ่มสังคมฯ', support: '12,326 หญิง · 6,874 ชาย · รวม 19,200 คน', type: 'people', female: 64.2, male: 35.8, total: '19,200 คน', foot: 'สัดส่วนและจำนวนตามตารางฉากความหลากหลายที่มีอยู่ในโปรเจกต์' },
        { period: 'วิทยาศาสตร์และเทคโนโลยี', title: 'สัดส่วนใกล้สมดุลที่สุดในตัวอย่าง', text: 'กลุ่มวิทยาศาสตร์และเทคโนโลยีมีหญิง 53.8% และชาย 46.2% รวม 11,450 คน เป็นสัดส่วนที่ใกล้เคียงกันมากกว่ากลุ่มตัวอย่างอื่นที่ยกมา', metric: '53.8%', label: 'นักศึกษาหญิงในกลุ่มวิทย์ฯ', support: '6,160 หญิง · 5,290 ชาย · รวม 11,450 คน', type: 'people', female: 53.8, male: 46.2, total: '11,450 คน', foot: 'สัดส่วนและจำนวนตามตารางฉากความหลากหลายที่มีอยู่ในโปรเจกต์' },
        { period: 'นานาชาติและสถาบันบูรณาการ', title: 'กลุ่มนานาชาติมีผู้หญิง 60.8%', text: 'ตารางข้อมูลความหลากหลายระบุประชากรกลุ่มนานาชาติและสถาบันบูรณาการ 4,400 คน โดยมีสัดส่วนหญิง 60.8% และชาย 39.2%', metric: '60.8%', label: 'นักศึกษาหญิงในกลุ่มนานาชาติ', support: '4,400 คน · 10.3% ของมหาวิทยาลัย', type: 'people', female: 60.8, male: 39.2, total: '4,400 คน', foot: 'สัดส่วนและจำนวนตามตารางในฉากความหลากหลายของเว็บไซต์เดิม' }
      ]
    },
    'topic-05': {
      kicker: 'CAMPUS DISTRIBUTION SHIFT', title: 'การกระจายตัวเปลี่ยนจากศูนย์เดียวสู่เครือข่าย',
      intro: 'แถบเดียวกันแสดงสัดส่วนศูนย์การศึกษาในแต่ละยุค เพื่อเปรียบเทียบการเปลี่ยนแปลงได้ตรง ๆ', accent: PALETTE.teal,
      steps: [
        { period: 'พ.ศ. 2500', title: 'ท่าพระจันทร์เป็นศูนย์กลางทั้งหมด', text: 'ในชุดข้อมูลวิวัฒนาการช่วงต้น ท่าพระจันทร์รองรับนักศึกษา 100% ก่อนข้อจำกัดด้านพื้นที่ผลักดันการขยายศูนย์การศึกษา', metric: '100%', label: 'ท่าพระจันทร์', support: 'ศูนย์กลางเดียวในข้อมูลยุคแรก', type: 'stacked', segments: [
          { label: 'ท่าพระจันทร์', value: 100, color: PALETTE.crimson }, { label: 'รังสิต', value: 0, color: PALETTE.teal }, { label: 'ลำปาง', value: 0, color: PALETTE.amber }, { label: 'พัทยา', value: 0, color: PALETTE.violet }
        ], foot: 'ค่าร้อยละเป็นชุดวิวัฒนาการศูนย์การศึกษาที่มีอยู่ในเว็บไซต์' },
        { period: 'พ.ศ. 2530', title: 'เริ่มเห็นบทบาทของรังสิต', text: 'ข้อมูลระบุว่าท่าพระจันทร์มีสัดส่วน 68% และรังสิต 32% เมื่อเริ่มขยายศูนย์การศึกษาในช่วงดังกล่าว', metric: '32%', label: 'สัดส่วนรังสิตในชุดข้อมูล', support: 'ท่าพระจันทร์ 68% · รังสิต 32%', type: 'stacked', segments: [
          { label: 'ท่าพระจันทร์', value: 68, color: PALETTE.crimson }, { label: 'รังสิต', value: 32, color: PALETTE.teal }, { label: 'ลำปาง', value: 0, color: PALETTE.amber }, { label: 'พัทยา', value: 0, color: PALETTE.violet }
        ], foot: 'ค่าร้อยละเป็นชุดวิวัฒนาการศูนย์การศึกษาที่มีอยู่ในเว็บไซต์' },
        { period: 'พ.ศ. 2545', title: 'ศูนย์รังสิตกลายเป็นศูนย์หลัก', text: 'การกระจายตามตารางข้อมูลยุคนี้คือท่าพระจันทร์ 26% รังสิต 70% ลำปาง 2.5% และพัทยา 1.5%', metric: '70%', label: 'สัดส่วนรังสิตในชุดข้อมูล', support: 'เริ่มเห็นเครือข่ายหลายศูนย์', type: 'stacked', segments: [
          { label: 'ท่าพระจันทร์', value: 26, color: PALETTE.crimson }, { label: 'รังสิต', value: 70, color: PALETTE.teal }, { label: 'ลำปาง', value: 2.5, color: PALETTE.amber }, { label: 'พัทยา', value: 1.5, color: PALETTE.violet }
        ], foot: 'ค่าร้อยละเป็นชุดวิวัฒนาการศูนย์การศึกษาที่มีอยู่ในเว็บไซต์' },
        { period: 'พ.ศ. 2567', title: 'ปัจจุบันมี 4 ศูนย์และบทบาทเฉพาะทาง', text: 'ชุดข้อมูลปัจจุบันระบุรังสิต 73.5% ท่าพระจันทร์ 14.8% ลำปาง 7.2% และพัทยา 4.5%', metric: '73.5%', label: 'สัดส่วนนักศึกษาที่รังสิต', support: 'ท่าพระจันทร์ 14.8% · ลำปาง 7.2% · พัทยา 4.5%', type: 'stacked', segments: [
          { label: 'ท่าพระจันทร์', value: 14.8, color: PALETTE.crimson }, { label: 'รังสิต', value: 73.5, color: PALETTE.teal }, { label: 'ลำปาง', value: 7.2, color: PALETTE.amber }, { label: 'พัทยา', value: 4.5, color: PALETTE.violet }
        ], foot: 'ค่าร้อยละเป็นชุดวิวัฒนาการศูนย์การศึกษาที่มีอยู่ในเว็บไซต์' }
      ]
    },
    'topic-06': {
      kicker: 'FINANCIAL ARCHITECTURE', title: 'งบประมาณรวมเพิ่มขึ้น พร้อมแหล่งรายได้หลายทาง',
      intro: 'ติดตามยอดรวม 5 ปี แล้วเลื่อนเพื่อดูว่าแหล่งรายรับหลักมีสัดส่วนอย่างไร', accent: PALETTE.amber,
      steps: [
        { period: 'ปีงบประมาณ 2563–2567', title: 'งบประมาณรวมเติบโตตลอดช่วงข้อมูล', text: 'ยอดรวมในตารางเพิ่มจาก 13,420 ล้านบาทในปี 2563 เป็น 15,350 ล้านบาทในปี 2567 กราฟด้านล่างแสดงค่ารายปีทั้งห้าจุด', metric: '15,350', label: 'ล้านบาท · ปี 2567', support: 'จาก 13,420 ล้านบาทในปี 2563', type: 'vertical', highlight: 4, bars: [
          { label: '2563', value: 13420, display: '13,420' }, { label: '2564', value: 13850, display: '13,850' }, { label: '2565', value: 14210, display: '14,210' }, { label: '2566', value: 14780, display: '14,780' }, { label: '2567', value: 15350, display: '15,350' }
        ], foot: 'จำนวนเงินตามตารางงบประมาณ 5 ปีในชุดข้อมูลโปรเจกต์' },
        { period: 'โครงสร้างรายได้ปีล่าสุดในข้อมูล', title: 'งบแผ่นดินและค่าเล่าเรียนเป็นฐานหลัก', text: 'งบแผ่นดิน 35.8% และค่าธรรมเนียมการศึกษา 32.4% รวมกันเป็น 68.2% ของโครงสร้างรายได้ตามข้อมูลที่แสดง', metric: '68.2%', label: 'งบแผ่นดิน + ค่าเล่าเรียน', support: '35.8% + 32.4%', type: 'horizontal', bars: [
          { label: 'งบแผ่นดิน', value: 35.8, display: '35.8%', color: PALETTE.crimson }, { label: 'ค่าเล่าเรียน', value: 32.4, display: '32.4%', color: PALETTE.blue }, { label: 'ทรัพย์สิน/ลงทุน', value: 18.2, display: '18.2%', color: PALETTE.amber }, { label: 'วิจัย/บริการ', value: 8.6, display: '8.6%', color: PALETTE.violet }, { label: 'การแพทย์', value: 5, display: '5.0%', color: PALETTE.green }
        ], foot: 'เปอร์เซ็นต์ใช้สัดส่วน 5 แหล่งรายได้ตามตารางงบประมาณที่อยู่ในเว็บ' },
        { period: 'ทรัพย์สินและการลงทุน', title: 'รายได้จากทรัพย์สินเพิ่มจาก 2,340 เป็น 2,794 ล้านบาท', text: 'ในตาราง 5 ปี รายได้จากทรัพย์สินและการลงทุนเติบโตในแต่ละปีจนเป็น 18.2% ของยอดรวมปีล่าสุดในข้อมูล', metric: '2,794', label: 'ล้านบาท · ปี 2567', support: 'สัดส่วน 18.2% ของงบรวม', type: 'vertical', highlight: 4, bars: [
          { label: '2563', value: 2340, display: '2,340' }, { label: '2564', value: 2420, display: '2,420' }, { label: '2565', value: 2540, display: '2,540' }, { label: '2566', value: 2680, display: '2,680' }, { label: '2567', value: 2794, display: '2,794' }
        ], foot: 'จำนวนเงินตามชุดข้อมูลรายได้จากทรัพย์สินและการลงทุนในโปรเจกต์' }
      ]
    },
    'topic-07': {
      kicker: 'GLOBAL EXCELLENCE', title: 'มาตรฐานสากลที่มีทั้งการรับรองและอันดับ',
      intro: 'เรื่องเล่านี้แยกมาตรฐานการรับรอง Triple Crown ออกจากข้อมูลอันดับ เพื่อให้เห็นคนละมิติอย่างชัดเจน', accent: PALETTE.violet,
      steps: [
        { period: 'Triple Crown', title: 'การรับรอง 3 สถาบันครบชุด', text: 'TBS ได้รับการรับรองครบ 3 มาตรฐาน ได้แก่ AACSB, EQUIS และ AMBA ตามข้อมูลในเว็บไซต์', metric: '3 / 3', label: 'มาตรฐานการรับรอง', support: 'AACSB · EQUIS · AMBA', type: 'badges', badges: [
          { icon: 'fa-solid fa-award', title: 'AACSB', note: 'มาตรฐานสหรัฐฯ' }, { icon: 'fa-solid fa-globe', title: 'EQUIS', note: 'มาตรฐานยุโรป' }, { icon: 'fa-solid fa-graduation-cap', title: 'AMBA', note: 'หลักสูตร MBA' }
        ], foot: 'แสดงมาตรฐานที่ระบุไว้ในข้อมูลเดิม ไม่ได้ตีความว่าแต่ละการรับรองมีเกณฑ์เหมือนกัน' },
        { period: 'ข้อมูลอันดับ TBS', title: 'อันดับ Business & Management ดีขึ้นในตารางตัวอย่าง', text: 'ค่าที่แสดงในตารางฉากจากปี 2018 ถึง 2024 เปลี่ยนจากอันดับ 250 เป็น 140 หมายเลขอันดับที่น้อยลงหมายถึงอยู่สูงขึ้นในตารางอันดับนั้น', metric: '140', label: 'อันดับ TBS · 2024', support: 'จากอันดับ 250 ในปี 2018', type: 'vertical', highlight: 6, reverse: true, bars: [
          { label: '2018', value: 250, display: '250' }, { label: '2019', value: 225, display: '225' }, { label: '2020', value: 210, display: '210' }, { label: '2021', value: 195, display: '195' }, { label: '2022', value: 180, display: '180' }, { label: '2023', value: 160, display: '160' }, { label: '2024', value: 140, display: '140' }
        ], foot: 'ใช้เฉพาะค่าจากตาราง TBS Business & Management ในฉากข้อมูลที่มีอยู่' },
        { period: 'การตีความ', title: 'อย่าเอาการรับรองมาแทนผลการจัดอันดับ', text: 'Triple Crown เป็นสถานะการรับรองมาตรฐานของโรงเรียนธุรกิจ ส่วนอันดับมหาวิทยาลัยและอันดับสาขาเป็นตัวชี้วัดคนละชุด ควรอ่านพร้อมปีและแหล่งอ้างอิง', metric: 'แยก 2 มิติ', label: 'การรับรอง ≠ อันดับ', support: 'กลับไปดูตารางเปรียบเทียบและแหล่งอ้างอิงด้านล่าง', type: 'pairs', pairs: [
          { label: 'Accreditation', value: '3 มาตรฐาน', note: 'AACSB / EQUIS / AMBA' }, { label: 'Ranking', value: 'รายปี', note: 'ต้องระบุชุดและปีที่จัดอันดับ' }
        ], foot: 'หัวข้อหลักในเว็บยังมีตัวเลข QS Asia คนละชุดกับตารางฉาก; ควรตรวจยืนยันแหล่งข้อมูลก่อนเผยแพร่' }
      ]
    },
    'topic-08': {
      kicker: 'SUSTAINABILITY & SDG', title: 'คะแนนความยั่งยืนเชื่อมกับแผนพลังงานสะอาด',
      intro: 'เลื่อนจากคะแนนที่มีในข้อมูล ไปสู่กำลังผลิตโซลาร์และโครงการในพื้นที่', accent: PALETTE.green,
      steps: [
        { period: 'THE Impact Rankings · SDG 11', title: 'คะแนนเมืองและชุมชนยั่งยืน 98.4 / 100', text: 'ตารางความยั่งยืนในเว็บแสดง SDG 11 ที่ 98.4 คะแนน พร้อมค่าของ SDG เป้าหมายอื่นเพื่อใช้เปรียบเทียบ', metric: '98.4', label: 'คะแนน SDG 11 จาก 100', support: 'World Top 10 · ตามข้อความในเว็บ', type: 'horizontal', bars: [
          { label: 'SDG 11', value: 98.4, display: '98.4', color: PALETTE.green }, { label: 'SDG 4', value: 92.8, display: '92.8', color: PALETTE.teal }, { label: 'SDG 7', value: 91.5, display: '91.5', color: PALETTE.blue }, { label: 'SDG 17', value: 90.4, display: '90.4', color: PALETTE.violet }, { label: 'SDG 3', value: 88.6, display: '88.6', color: PALETTE.amber }, { label: 'SDG 13', value: 87.2, display: '87.2', color: PALETTE.slate }
        ], foot: 'ค่าคะแนนดึงจากตารางความยั่งยืนในโปรเจกต์เดิม' },
        { period: 'Solar Rooftop', title: 'แผน 15 MW เทียบกับติดตั้งแล้ว 5 MW', text: 'ข้อความบนเว็บไซต์ระบุแผนกำลังผลิตโซลาร์เซลล์ 15 MW และติดตั้งแล้ว 5 MW ตัวชี้วัดนี้ช่วยแยกสิ่งที่ดำเนินการแล้วออกจากเป้าหมาย', metric: '5 / 15 MW', label: 'ติดตั้งแล้วเทียบกับแผน', support: 'เทียบเท่า 1 ใน 3 ของกำลังผลิตเป้าหมาย', type: 'progress', progress: [
          { label: 'ติดตั้งแล้ว', value: 5, target: 15, display: '5 MW', targetDisplay: '15 MW', percent: 33.3, color: PALETTE.green }
        ], foot: 'สัดส่วน 33.3% คำนวณจากตัวเลข 5 ÷ 15 ที่ระบุในเว็บไซต์' },
        { period: 'พื้นที่และผลกระทบ', title: 'พื้นที่เรียนรู้และเป้าหมาย Net-Zero', text: 'ข้อมูลในเว็บไซต์ระบุสวนป๋วย 100 ปี 22,000 ตร.ม. และตัวเลขลดการปล่อยก๊าซเรือนกระจก 25,500 ตันต่อปี ควบคู่กับเป้าหมาย Net-Zero Campus 2030', metric: '25,500', label: 'ตัน CO₂e ต่อปี · ตามข้อมูลในเว็บ', support: 'สวนป๋วย 100 ปี · 22,000 ตร.ม.', type: 'pairs', pairs: [
          { label: 'สวนป๋วย 100 ปี', value: '22,000', note: 'ตารางเมตร' }, { label: 'ลดก๊าซเรือนกระจก', value: '25,500', note: 'ตันต่อปี ตามข้อมูลในเว็บ' }
        ], foot: 'คงค่าที่ระบุในเว็บไซต์ไว้ ควรตรวจนิยามและขอบเขตการคำนวณจากรายงานต้นทางก่อนอ้างอิงภายนอก' }
      ]
    },
    'topic-09': {
      kicker: 'HEALTHCARE CAPACITY', title: 'ขีดความสามารถโรงพยาบาลเติบโตตามความต้องการ',
      intro: 'จากจำนวนผู้ป่วยนอกในข้อมูลประวัติศาสตร์ ไปสู่ความจุเตียงและบทบาทในภาวะวิกฤต', accent: PALETTE.blue,
      steps: [
        { period: 'พ.ศ. 2530', title: 'เริ่มต้นที่ 50,000 ครั้งรับบริการผู้ป่วยนอก/ปี', text: 'ตารางฉากประวัติศาสตร์ของโรงพยาบาลระบุจำนวนผู้ป่วยนอก 50,000 คนต่อปีในปี 2530', metric: '50,000', label: 'ครั้งรับบริการผู้ป่วยนอก/ปี', support: 'พ.ศ. 2530 · จุดเริ่มต้นในตารางตัวอย่าง', type: 'vertical', highlight: 0, bars: [
          { label: '2530', value: 50000, display: '50k' }, { label: '2540', value: 210000, display: '210k' }, { label: '2550', value: 520000, display: '520k' }, { label: '2560', value: 980000, display: '980k' }, { label: '2564', value: 1250000, display: '1.25M' }, { label: '2567', value: 1480000, display: '1.48M' }
        ], foot: 'ค่ารายปีตามตารางพัฒนาการโรงพยาบาลที่บรรจุในโปรเจกต์' },
        { period: 'พ.ศ. 2567', title: 'ผู้ป่วยนอกเพิ่มเป็น 1.48 ล้านครั้งต่อปี', text: 'ค่าปี 2567 ในตารางแสดง 1,480,000 ครั้งต่อปี จึงควรอ่านควบคู่กับบริการผู้ป่วยในและขีดความสามารถของโรงพยาบาล', metric: '1.48M', label: 'ครั้งรับบริการผู้ป่วยนอก/ปี', support: '1,480,000 ครั้ง · พ.ศ. 2567', type: 'vertical', highlight: 5, bars: [
          { label: '2530', value: 50000, display: '50k' }, { label: '2540', value: 210000, display: '210k' }, { label: '2550', value: 520000, display: '520k' }, { label: '2560', value: 980000, display: '980k' }, { label: '2564', value: 1250000, display: '1.25M' }, { label: '2567', value: 1480000, display: '1.48M' }
        ], foot: 'ค่ารายปีตามตารางพัฒนาการโรงพยาบาลที่บรรจุในโปรเจกต์' },
        { period: 'ความจุและภาวะวิกฤต', title: '750 เตียงปัจจุบัน · เป้าหมายขยาย 1,000 เตียง', text: 'ข้อมูลในเว็บไซต์ระบุเตียงเปิดบริการจริง 750 เตียง เป้าหมาย 1,000 เตียง และบทบาทโรงพยาบาลสนาม 308–470 เตียงในช่วงวิกฤตโควิด', metric: '750 / 1,000', label: 'เตียงเปิดบริการเทียบกับเป้าหมาย', support: 'โรงพยาบาลสนาม 308–470 เตียง · ดูรายละเอียดที่หัวข้อด้านล่าง', type: 'pairs', pairs: [
          { label: 'เตียงที่เปิดบริการ', value: '750', note: 'เตียง' }, { label: 'เป้าหมายในเว็บ', value: '1,000', note: 'เตียง' }, { label: 'โรงพยาบาลสนาม', value: '308–470', note: 'เตียงตามข้อมูลในเว็บ' }, { label: 'ผู้ป่วยสะสมที่ระบุ', value: '3,200+', note: 'รายตามคำอธิบายในเว็บ' }
        ], foot: 'ตัวเลขความจุตามข้อความที่มีอยู่ในโปรเจกต์ ไม่ใช่ข้อมูลสถานการณ์ปัจจุบันแบบเรียลไทม์' }
      ]
    },
    'topic-10': {
      kicker: 'TU 2034 STRATEGY', title: 'ติดตาม 4 เสาหลักจากค่าปัจจุบันสู่เป้าหมาย',
      intro: 'ค่าความก้าวหน้าในฉากนี้เป็นตัวเลขในชุดข้อมูลยุทธศาสตร์ ส่วน Cockpit ด้านล่างเป็นตัวจำลองที่ปรับค่าได้', accent: PALETTE.crimson,
      steps: [
        { period: 'เสาหลัก 1 · Global Research', title: 'ยกระดับงานวิจัยสู่มาตรฐานสากล', text: 'ชุดข้อมูลฉากยุทธศาสตร์ระบุ 72.4 คะแนนจากเป้าหมาย 92.0 หรือ 78.7% ของเป้าหมาย', metric: '78.7%', label: 'ความคืบหน้าเทียบเป้าหมาย', support: '72.4 จากเป้าหมาย 92.0 คะแนน', type: 'progress', progressFocus: 'วิจัยระดับสากล', progress: [
          { label: 'วิจัยระดับสากล', value: 72.4, target: 92, display: '72.4', targetDisplay: '92.0', percent: 78.7, color: PALETTE.crimson }, { label: 'ทักษะ AI', value: 78.5, target: 95, display: '78.5', targetDisplay: '95.0', percent: 82.6, color: PALETTE.blue }, { label: '88 SANDBOX', value: 6200, target: 10000, display: '6,200', targetDisplay: '10,000', percent: 62, color: PALETTE.violet }, { label: 'Net-Zero Campus', value: 78, target: 100, display: '78', targetDisplay: '100', percent: 78, color: PALETTE.green }
        ], foot: 'ค่าปัจจุบัน/เป้าหมายจากตารางฉากยุทธศาสตร์เดิม ไม่ใช่ผลประเมินทางการที่อัปเดตอัตโนมัติ' },
        { period: 'เสาหลัก 2 · Future Skills', title: 'เป้าหมายทักษะดิจิทัลและ AI', text: 'ค่าตั้งต้นในชุดข้อมูลระบุ 78.5 คะแนน จากเป้าหมาย 95.0 คะแนน คิดเป็น 82.6% ของเป้าหมาย', metric: '82.6%', label: 'ความคืบหน้าเทียบเป้าหมาย', support: '78.5 จากเป้าหมาย 95.0 คะแนน', type: 'progress', progressFocus: 'ทักษะ AI', progress: [
          { label: 'วิจัยระดับสากล', value: 72.4, target: 92, display: '72.4', targetDisplay: '92.0', percent: 78.7, color: PALETTE.crimson }, { label: 'ทักษะ AI', value: 78.5, target: 95, display: '78.5', targetDisplay: '95.0', percent: 82.6, color: PALETTE.blue }, { label: '88 SANDBOX', value: 6200, target: 10000, display: '6,200', targetDisplay: '10,000', percent: 62, color: PALETTE.violet }, { label: 'Net-Zero Campus', value: 78, target: 100, display: '78', targetDisplay: '100', percent: 78, color: PALETTE.green }
        ], foot: 'ค่าปัจจุบัน/เป้าหมายจากตารางฉากยุทธศาสตร์เดิม ไม่ใช่ผลประเมินทางการที่อัปเดตอัตโนมัติ' },
        { period: 'เสาหลัก 3 · 88 SANDBOX', title: 'เป้าหมายบ่มเพาะสตาร์ทอัพ 10,000 ทีม', text: 'ข้อมูลฉากยุทธศาสตร์ระบุ 6,200 ทีมจากเป้าหมาย 10,000 ทีม หรือ 62% ตามชุดข้อมูลนี้', metric: '6,200', label: 'ทีมจากเป้าหมาย 10,000 ทีม', support: '62.0% ของเป้าหมายตามชุดข้อมูล', type: 'progress', progressFocus: '88 SANDBOX', progress: [
          { label: 'วิจัยระดับสากล', value: 72.4, target: 92, display: '72.4', targetDisplay: '92.0', percent: 78.7, color: PALETTE.crimson }, { label: 'ทักษะ AI', value: 78.5, target: 95, display: '78.5', targetDisplay: '95.0', percent: 82.6, color: PALETTE.blue }, { label: '88 SANDBOX', value: 6200, target: 10000, display: '6,200', targetDisplay: '10,000', percent: 62, color: PALETTE.violet }, { label: 'Net-Zero Campus', value: 78, target: 100, display: '78', targetDisplay: '100', percent: 78, color: PALETTE.green }
        ], foot: 'ค่าปัจจุบัน/เป้าหมายจากตารางฉากยุทธศาสตร์เดิม ไม่ใช่ผลประเมินทางการที่อัปเดตอัตโนมัติ' },
        { period: 'เสาหลัก 4 · Net-Zero Campus', title: 'ขับเคลื่อนวิทยาเขตคาร์บอนต่ำ', text: 'ค่าตั้งต้นพลังงานสะอาดในตารางเท่ากับ 78 จากเป้าหมาย 100 โดยมีปีเป้าหมาย Net-Zero Campus 2030 อยู่ในเนื้อหาหลัก', metric: '78.0%', label: 'ความคืบหน้าเทียบเป้าหมาย', support: 'ค่าปัจจุบัน 78 จากเป้าหมาย 100', type: 'progress', progressFocus: 'Net-Zero Campus', progress: [
          { label: 'วิจัยระดับสากล', value: 72.4, target: 92, display: '72.4', targetDisplay: '92.0', percent: 78.7, color: PALETTE.crimson }, { label: 'ทักษะ AI', value: 78.5, target: 95, display: '78.5', targetDisplay: '95.0', percent: 82.6, color: PALETTE.blue }, { label: '88 SANDBOX', value: 6200, target: 10000, display: '6,200', targetDisplay: '10,000', percent: 62, color: PALETTE.violet }, { label: 'Net-Zero Campus', value: 78, target: 100, display: '78', targetDisplay: '100', percent: 78, color: PALETTE.green }
        ], foot: 'ค่าปัจจุบัน/เป้าหมายจากตารางฉากยุทธศาสตร์เดิม ไม่ใช่ผลประเมินทางการที่อัปเดตอัตโนมัติ' }
      ]
    }
  };

  const INSERT_BEFORE = {
    'topic-01': '.winning-cards-row',
    'topic-02': '.cluster-map-layout',
    'topic-03': '.faculties-white-card',
    'topic-04': '.demographic-white-card',
    'topic-05': '.campus-distribution-card',
    'topic-06': '.cost-cap-white-card',
    'topic-07': '.triple-crown-badges-stage',
    'topic-08': '.green-highlight-box',
    'topic-09': '.hospital-kpi-row',
    'topic-10': '.tu-route-layout'
  };

  function esc(s) {
    return String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  function renderBars(step) {
    const list = step.bars || [];
    const max = Math.max(...list.map(x => Number(x.value) || 0), 1);
    const count = list.length;
    return `<div class="story-vertical-bars" style="--bar-count:${count}">${list.map((item, i) => {
      const ratio = step.reverse ? (Number(item.value) / max) : (Number(item.value) / max);
      const height = Math.max(5, ratio * 100);
      const isActive = i === step.highlight;
      const color = item.color || (isActive ? 'var(--story-accent)' : '#aab4c5');
      return `<div class="story-vertical-bar" style="opacity:${step.highlight == null || isActive ? 1 : .6}">
        <span class="story-vertical-value">${esc(item.display || fmt(item.value))}</span>
        <span class="story-vertical-track"><span class="story-vertical-fill" style="--bar-height:${height}%;--bar-color:${color};"></span></span>
        <span class="story-vertical-label">${esc(item.label)}</span>
      </div>`;
    }).join('')}</div>${step.reverse ? '<p class="story-inline-note">หมายเหตุ: อันดับยิ่งมีตัวเลขน้อยยิ่งอยู่สูงขึ้น</p>' : ''}`;
  }

  function renderHorizontal(step) {
    const bars = step.bars || [];
    const max = Math.max(...bars.map(x => Number(x.value) || 0), 1);
    const normTo100 = bars.every(x => Number(x.value) <= 100);
    return `<div class="story-bar-list">${bars.map(item => {
      const width = normTo100 ? Number(item.value) : (Number(item.value) / max * 100);
      const isSelected = step.highlight && (String(item.label).toLowerCase().includes(String(step.highlight).toLowerCase()));
      return `<div class="story-bar-row" style="opacity:${!step.highlight || isSelected ? 1 : .68}">
        <span class="story-bar-label">${esc(item.label)}</span>
        <span class="story-bar-track"><span class="story-bar-fill" style="--bar-width:${Math.min(100, Math.max(0,width))}%;--bar-color:${item.color || (isSelected ? 'var(--story-accent)' : '#aab4c5')}"></span></span>
        <span class="story-bar-value">${esc(item.display || fmt(item.value))}</span>
      </div>`;
    }).join('')}</div>`;
  }

  function renderStacked(step) {
    const segs = step.segments || [];
    return `<div class="story-stacked-wrap">
      <div class="story-stacked-track" role="img" aria-label="แถบสัดส่วนศูนย์การศึกษาตามปีที่เลือก">${segs.map(s => `<span class="story-stacked-segment" style="--segment-width:${Math.max(0,Number(s.value))}%;--segment-color:${s.color}" title="${esc(s.label)} ${s.value}%"></span>`).join('')}</div>
      <div class="story-stacked-legend">${segs.map(s => `<div class="story-stacked-legend-item"><i class="story-legend-dot" style="--dot-color:${s.color}"></i><span>${esc(s.label)}<strong>${Number(s.value).toLocaleString('en-US')}%</strong></span></div>`).join('')}</div>
    </div>`;
  }

  function renderPeople(step) {
    const female = Math.max(0, Math.min(100, Number(step.female) || 0));
    const femaleCount = Math.round(female);
    let people = '';
    for (let i = 0; i < 100; i++) {
      const group = i < femaleCount ? 'female' : 'male';
      const col = i % 10;
      const row = Math.floor(i / 10);
      const delay = col * 20 + row * 16;
      people += `<span class="story-person ${group}" aria-hidden="true" style="--person-delay:${delay}ms;"></span>`;
    }
    return `<div class="story-viz-legend"><span><i class="story-legend-dot" style="--dot-color:var(--story-female)"></i>หญิง <strong class="story-female-pct">${female.toFixed(1)}%</strong></span><span><i class="story-legend-dot" style="--dot-color:var(--story-male)"></i>ชาย <strong class="story-male-pct">${(Number(step.male)||0).toFixed(1)}%</strong></span></div>
      <div class="story-people-grid" role="img" aria-label="รูปคน 100 รูป แสดงสัดส่วนหญิง ${female.toFixed(1)} เปอร์เซ็นต์ และชาย ${(Number(step.male)||0).toFixed(1)} เปอร์เซ็นต์">${people}</div>
      <p class="story-people-caption">รูปคน 100 รูปแสดงสัดส่วนโดยประมาณ · ประชากรในกลุ่มนี้ ${esc(step.total || 'ไม่ระบุ')}</p>`;
  }

  function renderPairs(step) {
    return `<div class="story-pair-cards">${(step.pairs || []).map(pair => `<div class="story-pair-card"><span class="story-pair-card-label">${esc(pair.label)}</span><strong class="story-pair-card-value">${esc(pair.value)}</strong><span class="story-pair-card-note">${esc(pair.note)}</span></div>`).join('')}</div>`;
  }

  function renderProgress(step) {
    const items = step.progress || [];
    return `<div class="story-progress-list">${items.map(item => `<div class="story-progress-row${item.label === step.progressFocus ? ' story-progress-row-focus' : ''}">
      <div class="story-progress-meta"><span class="story-progress-title">${esc(item.label)}</span><span class="story-progress-ratio"><strong>${esc(item.display)}</strong> / ${esc(item.targetDisplay)} <em class="story-progress-pct">(${Number(item.percent).toFixed(1)}%)</em></span></div>
      <div class="story-progress-track"><span class="story-progress-fill" style="--progress-width:${Math.max(0,Math.min(100,Number(item.percent)||0))}%;--progress-color:${item.color || 'var(--story-accent)'}"></span></div>
    </div>`).join('')}</div>`;
  }

  function renderBadges(step) {
    return `<div class="story-badge-grid">${(step.badges || []).map(b => `<div class="story-badge"><i class="${esc(b.icon)}" aria-hidden="true"></i><strong>${esc(b.title)}</strong><small>${esc(b.note)}</small></div>`).join('')}</div>`;
  }

  function renderVisualMarkup(step) {
    switch (step.type) {
      case 'vertical': return renderBars(step);
      case 'horizontal': return renderHorizontal(step);
      case 'stacked': return renderStacked(step);
      case 'people': return renderPeople(step);
      case 'pairs': return renderPairs(step);
      case 'progress': return renderProgress(step);
      case 'badges': return renderBadges(step);
      default: return '<p class="story-inline-note">ไม่มีข้อมูลภาพสำหรับฉากนี้</p>';
    }
  }

  function setStoryText(element, value, animate = true) {
    if (!element) return;
    const next = String(value ?? '');
    if (element.textContent === next) return;
    if (!animate || reduceMotion || !element.textContent.trim()) {
      element.textContent = next;
      return;
    }
    const token = (Number(element.dataset.swapToken) || 0) + 1;
    element.dataset.swapToken = String(token);
    element.classList.remove('story-copy-out', 'story-copy-in');
    element.classList.add('story-copy-out');
    window.setTimeout(() => {
      if (element.dataset.swapToken !== String(token)) return;
      element.textContent = next;
      element.classList.remove('story-copy-out');
      element.classList.add('story-copy-in');
      window.setTimeout(() => {
        if (element.dataset.swapToken === String(token)) element.classList.remove('story-copy-in');
      }, 300);
    }, 115);
  }

  function parseMetric(value) {
    const match = String(value ?? '').match(/^(\D*?)(-?\d[\d,]*(?:\.\d+)?)(.*)$/);
    if (!match) return null;
    const number = Number(match[2].replace(/,/g, ''));
    if (!Number.isFinite(number)) return null;
    return { prefix: match[1], number, suffix: match[3], decimals: (match[2].split('.')[1] || '').length };
  }

  function updateStoryMetric(element, nextValue, canCount) {
    if (!element) return;
    const next = String(nextValue ?? '');
    const previous = element.textContent.trim();
    if (!previous || previous === next || !canCount || reduceMotion) {
      setStoryText(element, next, Boolean(previous && previous !== next));
      return;
    }
    const from = parseMetric(previous);
    const to = parseMetric(next);
    if (!from || !to || from.prefix !== to.prefix || from.suffix !== to.suffix) {
      setStoryText(element, next, true);
      return;
    }
    const token = (Number(element.dataset.countToken) || 0) + 1;
    element.dataset.countToken = String(token);
    const started = performance.now();
    const duration = 660;
    const decimals = to.decimals;
    const tick = now => {
      if (element.dataset.countToken !== String(token)) return;
      const t = Math.min(1, (now - started) / duration);
      const eased = 1 - Math.pow(1 - t, 4);
      const value = from.number + (to.number - from.number) * eased;
      const numberText = value.toLocaleString('en-US', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals
      });
      element.textContent = `${to.prefix}${numberText}${to.suffix}`;
      if (t < 1) requestAnimationFrame(tick);
      else element.textContent = next;
    };
    requestAnimationFrame(tick);
  }

  function setTextNode(container, value) {
    if (!container) return;
    const textNodes = Array.from(container.childNodes).filter(node => node.nodeType === Node.TEXT_NODE);
    if (textNodes.length) textNodes[textNodes.length - 1].nodeValue = value;
    else container.appendChild(document.createTextNode(value));
  }

  function tryMorphVisual(root, step) {
    if (!root || !step || !step.type) return false;

    if (step.type === 'vertical') {
      const data = step.bars || [];
      const rows = Array.from(root.querySelectorAll('.story-vertical-bar'));
      if (rows.length !== data.length) return false;
      if (Boolean(root.querySelector('.story-inline-note')) !== Boolean(step.reverse)) return false;
      const max = Math.max(...data.map(item => Number(item.value) || 0), 1);
      rows.forEach((row, i) => {
        const item = data[i];
        const ratio = Math.max(5, (Number(item.value) || 0) / max * 100);
        const fill = row.querySelector('.story-vertical-fill');
        const active = step.highlight == null || i === step.highlight;
        setStoryText(row.querySelector('.story-vertical-value'), item.display || fmt(item.value), false);
        setStoryText(row.querySelector('.story-vertical-label'), item.label, false);
        if (fill) {
          fill.style.setProperty('--bar-height', `${ratio}%`);
          fill.style.setProperty('--bar-color', item.color || (active ? 'var(--story-accent)' : '#aab4c5'));
        }
        row.style.opacity = active ? '1' : '.6';
      });
      return true;
    }

    if (step.type === 'horizontal') {
      const data = step.bars || [];
      const rows = Array.from(root.querySelectorAll('.story-bar-row'));
      if (rows.length !== data.length) return false;
      const max = Math.max(...data.map(item => Number(item.value) || 0), 1);
      const normTo100 = data.every(item => Number(item.value) <= 100);
      rows.forEach((row, i) => {
        const item = data[i];
        const width = normTo100 ? Number(item.value) : (Number(item.value) / max * 100);
        const isSelected = step.highlight && String(item.label).toLowerCase().includes(String(step.highlight).toLowerCase());
        setStoryText(row.querySelector('.story-bar-label'), item.label, false);
        setStoryText(row.querySelector('.story-bar-value'), item.display || fmt(item.value), false);
        const fill = row.querySelector('.story-bar-fill');
        if (fill) {
          fill.style.setProperty('--bar-width', `${Math.min(100, Math.max(0, width))}%`);
          fill.style.setProperty('--bar-color', item.color || (isSelected ? 'var(--story-accent)' : '#aab4c5'));
        }
        row.style.opacity = !step.highlight || isSelected ? '1' : '.68';
      });
      return true;
    }

    if (step.type === 'stacked') {
      const data = step.segments || [];
      const fills = Array.from(root.querySelectorAll('.story-stacked-segment'));
      const legends = Array.from(root.querySelectorAll('.story-stacked-legend-item'));
      if (fills.length !== data.length || legends.length !== data.length) return false;
      fills.forEach((fill, i) => {
        const item = data[i];
        fill.style.setProperty('--segment-width', `${Math.max(0, Number(item.value) || 0)}%`);
        fill.style.setProperty('--segment-color', item.color || '#bd173e');
        fill.title = `${item.label} ${item.value}%`;
        const legend = legends[i];
        const label = legend.querySelector('span');
        if (label) setTextNode(label, item.label);
        const value = legend.querySelector('strong');
        setStoryText(value, `${Number(item.value).toLocaleString('en-US')}%`, false);
        const dot = legend.querySelector('.story-legend-dot');
        if (dot) dot.style.setProperty('--dot-color', item.color || '#bd173e');
      });
      const track = root.querySelector('.story-stacked-track');
      if (track) track.setAttribute('aria-label', `แถบสัดส่วนตามฉาก ${step.period || ''}`);
      return true;
    }

    if (step.type === 'people') {
      const grid = root.querySelector('.story-people-grid');
      const people = grid ? Array.from(grid.children) : [];
      if (people.length !== 100) return false;
      const female = Math.max(0, Math.min(100, Number(step.female) || 0));
      const femaleCount = Math.round(female);
      people.forEach((person, i) => {
        const wasFemale = person.classList.contains('female');
        const willBeFemale = i < femaleCount;
        const changed = wasFemale !== willBeFemale;
        const col = i % 10;
        const row = Math.floor(i / 10);
        const delay = col * 20 + row * 16;
        person.style.setProperty('--person-delay', `${delay}ms`);
        person.style.transitionDelay = `${delay}ms`;

        if (changed) {
          person.classList.remove('is-flipping');
          void person.offsetWidth;
          person.classList.add('is-flipping');
        }
        person.classList.toggle('female', willBeFemale);
        person.classList.toggle('male', !willBeFemale);
      });

      window.setTimeout(() => {
        people.forEach(p => p.classList.remove('is-flipping'));
      }, 750);

      if (grid) grid.setAttribute('aria-label', `รูปคน 100 รูป แสดงสัดส่วนหญิง ${female.toFixed(1)} เปอร์เซ็นต์ และชาย ${(Number(step.male) || 0).toFixed(1)} เปอร์เซ็นต์`);
      const femalePct = root.querySelector('.story-female-pct');
      const malePct = root.querySelector('.story-male-pct');
      if (femalePct) setStoryText(femalePct, `${female.toFixed(1)}%`, true);
      else {
        const legend = Array.from(root.querySelectorAll('.story-viz-legend span'));
        if (legend[0]) setTextNode(legend[0], `หญิง ${female.toFixed(1)}%`);
      }
      if (malePct) setStoryText(malePct, `${(Number(step.male) || 0).toFixed(1)}%`, true);
      else {
        const legend = Array.from(root.querySelectorAll('.story-viz-legend span'));
        if (legend[1]) setTextNode(legend[1], `ชาย ${(Number(step.male) || 0).toFixed(1)}%`);
      }
      setStoryText(root.querySelector('.story-people-caption'), `รูปคน 100 รูปแสดงสัดส่วนโดยประมาณ · ประชากรในกลุ่มนี้ ${step.total || 'ไม่ระบุ'}`, false);
      return true;
    }

    if (step.type === 'pairs') {
      const data = step.pairs || [];
      const cards = Array.from(root.querySelectorAll('.story-pair-card'));
      if (cards.length !== data.length) return false;
      cards.forEach((card, i) => {
        setStoryText(card.querySelector('.story-pair-card-label'), data[i].label, false);
        setStoryText(card.querySelector('.story-pair-card-value'), data[i].value, false);
        setStoryText(card.querySelector('.story-pair-card-note'), data[i].note, false);
      });
      return true;
    }

    if (step.type === 'progress') {
      const data = step.progress || [];
      const rows = Array.from(root.querySelectorAll('.story-progress-row'));
      if (rows.length !== data.length) return false;
      rows.forEach((row, i) => {
        const item = data[i];
        row.classList.toggle('story-progress-row-focus', item.label === step.progressFocus);
        const title = row.querySelector('.story-progress-title');
        const ratio = row.querySelector('.story-progress-ratio');
        if (title) setStoryText(title, item.label, false);
        if (ratio) ratio.innerHTML = `<strong>${esc(item.display)}</strong> / ${esc(item.targetDisplay)} <em class="story-progress-pct">(${Number(item.percent).toFixed(1)}%)</em>`;
        const fill = row.querySelector('.story-progress-fill');
        if (fill) {
          fill.style.setProperty('--progress-width', `${Math.max(0, Math.min(100, Number(item.percent) || 0))}%`);
          fill.style.setProperty('--progress-color', item.color || 'var(--story-accent)');
        }
      });
      return true;
    }

    if (step.type === 'badges') {
      const data = step.badges || [];
      const cards = Array.from(root.querySelectorAll('.story-badge'));
      if (cards.length !== data.length) return false;
      cards.forEach((card, i) => {
        const icon = card.querySelector('i');
        if (icon) icon.className = data[i].icon || '';
        setStoryText(card.querySelector('strong'), data[i].title, false);
        setStoryText(card.querySelector('small'), data[i].note, false);
      });
      return true;
    }

    return false;
  }

  function transitionVisualContent(content, step) {
    // If the reader scrolls quickly, settle the current incoming layer before making the next transition.
    if (content.classList.contains('is-crossfading')) {
      if (content._storyTransitionTimer) window.clearTimeout(content._storyTransitionTimer);
      const incoming = content.querySelector(':scope > .story-visual-in');
      if (incoming) content.innerHTML = incoming.innerHTML;
      content.classList.remove('is-crossfading');
      content.style.height = '';
    }

    const oldType = content.dataset.visualType || '';
    if (oldType && oldType === step.type && tryMorphVisual(content, step)) {
      const token = (Number(content.dataset.morphToken) || 0) + 1;
      content.dataset.morphToken = String(token);
      content.classList.add('is-morphing');
      window.setTimeout(() => {
        if (content.dataset.morphToken === String(token)) content.classList.remove('is-morphing');
      }, reduceMotion ? 1 : 900);
      return;
    }

    const nextMarkup = renderVisualMarkup(step);
    const oldMarkup = content.innerHTML;
    const oldHeight = Math.max(content.getBoundingClientRect().height, 40);
    content.dataset.visualType = step.type;

    if (!oldMarkup.trim() || !oldType || reduceMotion) {
      content.innerHTML = nextMarkup;
      content.style.height = '';
      content.classList.remove('is-crossfading', 'is-morphing');
      return;
    }

    content.classList.remove('is-morphing');
    content.classList.add('is-crossfading');
    content.style.height = `${oldHeight}px`;
    content.innerHTML = `<div class="story-visual-layer story-visual-out" aria-hidden="true">${oldMarkup}</div><div class="story-visual-layer story-visual-in">${nextMarkup}</div>`;
    const incoming = content.querySelector(':scope > .story-visual-in');
    requestAnimationFrame(() => {
      if (!incoming || !content.isConnected) return;
      const minHeight = parseFloat(getComputedStyle(content).minHeight) || 0;
      const nextHeight = Math.max(incoming.getBoundingClientRect().height, minHeight);
      content.style.height = `${nextHeight}px`;
    });
    content._storyTransitionTimer = window.setTimeout(() => {
      if (!content.isConnected) return;
      content.innerHTML = nextMarkup;
      content.style.height = '';
      content.classList.remove('is-crossfading');
    }, reduceMotion ? 1 : 720);
  }

  function updateVisual(stage, step, idx, total) {
    const isInitial = stage.dataset.hasRendered !== 'true';
    stage.classList.remove('is-updating');
    void stage.offsetWidth;
    stage.style.setProperty('--story-accent', stage.closest('.scroll-story-module')?.dataset.accent || PALETTE.crimson);
    setStoryText(stage.querySelector('.scroll-story-stage-index'), String(idx + 1).padStart(2, '0'), !isInitial);
    setStoryText(stage.querySelector('.scroll-story-stage-eyebrow'), 'ฉาก ' + (idx + 1) + '/' + total + ' • ' + step.period, !isInitial);
    setStoryText(stage.querySelector('.scroll-story-stage-title'), step.title, !isInitial);
    const metric = stage.querySelector('.scroll-story-metric');
    const metricLabel = stage.querySelector('.scroll-story-metric-label');
    const metricSupport = stage.querySelector('.scroll-story-metric-support');
    const previousLabel = metricLabel?.textContent.trim() || '';
    const nextLabel = step.label || '';
    const sameMetricMeaning = !isInitial && previousLabel === nextLabel && stage.querySelector('.scroll-story-visual-content')?.dataset.visualType === step.type;
    updateStoryMetric(metric, step.metric, sameMetricMeaning);
    setStoryText(metricLabel, nextLabel, !isInitial);
    setStoryText(metricSupport, step.support || '', !isInitial);
    transitionVisualContent(stage.querySelector('.scroll-story-visual-content'), step);
    setStoryText(stage.querySelector('.scroll-story-source-note'), step.foot || 'ดูแหล่งอ้างอิงเดิมท้ายหัวข้อนี้', !isInitial);
    stage.setAttribute('aria-label', `ข้อมูลฉาก ${idx + 1} จาก ${total}: ${step.title}`);
    stage.classList.add('is-updating');
    stage.dataset.hasRendered = 'true';
  }

  function buildModule(id, story) {
    const module = document.createElement('div');
    module.className = 'scroll-story-module';
    module.dataset.storyFor = id;
    module.dataset.accent = story.accent;
    module.style.setProperty('--story-accent', story.accent);
    module.innerHTML = `
      <div class="scroll-story-heading">
        <div><p class="scroll-story-kicker">${esc(story.kicker)}</p><h3 class="scroll-story-title">${esc(story.title)}</h3><p class="scroll-story-intro">${esc(story.intro)}</p></div>
        <div class="scroll-story-hint"><i class="fa-solid fa-arrow-down-long" aria-hidden="true"></i><span>เลื่อนเพื่อสำรวจข้อมูลทีละช่วง</span></div>
      </div>
      <div class="scroll-story-grid">
        <div class="scroll-story-visual-col">
          <div class="scroll-story-stage" role="group" aria-live="polite">
            <div class="scroll-story-stage-head"><div><div class="scroll-story-stage-eyebrow"></div><h4 class="scroll-story-stage-title"></h4></div><span class="scroll-story-stage-index">01</span></div>
            <div class="scroll-story-metric-block"><strong class="scroll-story-metric"></strong><span class="scroll-story-metric-label"></span><p class="scroll-story-metric-support"></p></div>
            <div class="scroll-story-visual-content"></div>
            <p class="scroll-story-source-note"></p>
          </div>
        </div>
        <div class="scroll-story-steps" aria-label="ขั้นตอนการเล่าเรื่องข้อมูล">${story.steps.map((step, i) => `
          <article class="scroll-story-step${i === 0 ? ' is-active' : ''}" data-step-index="${i}" tabindex="0" aria-current="${i === 0 ? 'step' : 'false'}">
            <div class="scroll-story-step-top"><span class="scroll-story-step-number">${String(i + 1).padStart(2, '0')}</span><span class="scroll-story-step-period">${esc(step.period)}</span></div>
            <h4>${esc(step.title)}</h4><p>${esc(step.text)}</p>
            ${step.foot ? `<p class="story-step-foot">${esc(step.foot)}</p>` : ''}
          </article>`).join('')}
        </div>
      </div>`;
    updateVisual(module.querySelector('.scroll-story-stage'), story.steps[0], 0, story.steps.length);
    return module;
  }

  function mount() {
    Object.entries(STORIES).forEach(([id, story]) => {
      const section = document.getElementById(id);
      if (!section || section.querySelector('.scroll-story-module')) return;
      const target = section.querySelector(INSERT_BEFORE[id]);
      if (!target || !target.parentNode) return;
      const module = buildModule(id, story);
      target.parentNode.insertBefore(module, target);
    });
    attachObservers();
  }

  function activateStep(module, index) {
    const story = STORIES[module.dataset.storyFor];
    if (!story || !story.steps[index]) return;
    const steps = Array.from(module.querySelectorAll('.scroll-story-step'));
    steps.forEach((el, i) => {
      const active = i === index;
      el.classList.toggle('is-active', active);
      el.setAttribute('aria-current', active ? 'step' : 'false');
    });
    const stage = module.querySelector('.scroll-story-stage');
    const previousIndex = Number.isFinite(Number(stage.dataset.activeIndex))
      ? Number(stage.dataset.activeIndex) : index;
    if (Number(stage.dataset.activeIndex) === index) return;
    const direction = index >= previousIndex ? 'down' : 'up';
    stage.dataset.entryDirection = direction;
    const visualContent = stage.querySelector('.scroll-story-visual-content');
    if (visualContent) visualContent.dataset.entryDirection = direction;
    stage.dataset.activeIndex = String(index);
    updateVisual(stage, story.steps[index], index, story.steps.length);
  }

  function attachChapterTransitions(modules) {
    if (!('IntersectionObserver' in window) || reduceMotion) return;
    const inReadingBand = new Set();
    let activeModule = null;
    let lastScrollY = window.scrollY || 0;
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) inReadingBand.add(entry.target);
        else inReadingBand.delete(entry.target);
      });
      const currentScrollY = window.scrollY || 0;
      const direction = currentScrollY >= lastScrollY ? 'down' : 'up';
      lastScrollY = currentScrollY;
      const focusY = (window.innerHeight || document.documentElement.clientHeight) * 0.48;
      const next = Array.from(inReadingBand).map(module => {
        const rect = module.getBoundingClientRect();
        const distance = rect.top <= focusY && rect.bottom >= focusY
          ? 0 : Math.min(Math.abs(rect.top - focusY), Math.abs(rect.bottom - focusY));
        return { module, distance };
      }).sort((a, b) => a.distance - b.distance)[0]?.module;
      if (!next || next === activeModule) return;
      activeModule = next;
      next.dataset.entryDirection = direction;
      const token = (Number(next.dataset.chapterMotionToken) || 0) + 1;
      next.dataset.chapterMotionToken = String(token);
      next.classList.remove('is-chapter-entering');
      void next.offsetWidth;
      next.classList.add('is-chapter-entering');
      window.setTimeout(() => {
        if (next.dataset.chapterMotionToken === String(token)) next.classList.remove('is-chapter-entering');
      }, 1250);
    }, { rootMargin: '-24% 0px -24% 0px', threshold: 0.01 });
    modules.forEach(module => observer.observe(module));
  }

  function attachObservers() {
    const modules = Array.from(document.querySelectorAll('.scroll-story-module'));
    if (!modules.length) return;

    // On desktop the stage sits beside the narrative, so the reading line can be higher.
    // On stacked/mobile layouts, keep it below the sticky stage to avoid activating obscured text.
    const getFocusY = (module, vh) => {
      if (window.innerWidth > 980) return vh * 0.42;
      const stageRect = module.querySelector('.scroll-story-stage').getBoundingClientRect();
      return Math.min(vh * 0.78, Math.max(vh * 0.46, stageRect.bottom + 34));
    };

    let framePending = false;
    const updateFromViewport = () => {
      framePending = false;
      const vh = window.innerHeight || document.documentElement.clientHeight;
      modules.forEach(module => {
        const moduleRect = module.getBoundingClientRect();
        // Avoid changing scenes for a chapter that is far away from the current reading position.
        if (moduleRect.bottom < vh * 0.18 || moduleRect.top > vh * 0.82) return;
        // The reading line adapts to side-by-side desktop and stacked/mobile layouts.
        const focusY = getFocusY(module, vh);
        const steps = Array.from(module.querySelectorAll('.scroll-story-step'));
        const candidates = steps.map(el => {
          const r = el.getBoundingClientRect();
          return { el, top: r.top, bottom: r.bottom, center: (r.top + r.bottom) / 2 };
        }).filter(x => x.bottom > vh * 0.16 && x.top < vh * 0.84);
        if (!candidates.length) return;
        const current = candidates.reduce((best, item) =>
          Math.abs(item.center - focusY) < Math.abs(best.center - focusY) ? item : best
        );
        activateStep(module, Number(current.el.dataset.stepIndex) || 0);
      });
    };
    const scheduleViewportUpdate = () => {
      if (framePending) return;
      framePending = true;
      window.requestAnimationFrame(updateFromViewport);
    };

    window.addEventListener('scroll', scheduleViewportUpdate, { passive: true });
    window.addEventListener('resize', scheduleViewportUpdate, { passive: true });
    scheduleViewportUpdate();

    // Click, Enter, or Space can select a scene and bring its narrative step into reading focus.
    modules.forEach(module => {
      module.querySelectorAll('.scroll-story-step').forEach(step => {
        const choose = () => {
          const index = Number(step.dataset.stepIndex) || 0;
          activateStep(module, index);
          const rect = step.getBoundingClientRect();
          const vh = window.innerHeight || document.documentElement.clientHeight;
          const focusY = getFocusY(module, vh);
          const top = window.scrollY + ((rect.top + rect.bottom) / 2 - focusY);
          window.scrollTo({ top, behavior: reduceMotion ? 'auto' : 'smooth' });
        };
        step.addEventListener('click', choose);
        step.addEventListener('keydown', event => {
          if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault(); choose();
          }
        });
      });
    });
    attachChapterTransitions(modules);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount, { once: true });
  else mount();
})();
