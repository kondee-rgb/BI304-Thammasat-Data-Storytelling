
    // Global Chart.js Thai Typography Configuration
    if (typeof Chart !== 'undefined') {
      Chart.defaults.font.family = "'Prompt', 'Sarabun', 'Plus Jakarta Sans', sans-serif";
      Chart.defaults.color = '#64748b';
      Chart.defaults.plugins.tooltip.padding = 12;
      Chart.defaults.plugins.tooltip.cornerRadius = 8;
      Chart.defaults.plugins.tooltip.titleFont = {
        family: "'Prompt', sans-serif",
        weight: '600',
        size: 13
      };
      Chart.defaults.plugins.tooltip.bodyFont = {
        family: "'Sarabun', sans-serif",
        size: 12
      };
      // ตั้งค่าเฉพาะคุณสมบัติ ห้ามแทนที่ทั้ง object (จะทำให้ตัวแปลงค่าแอนิเมชันของ Chart.js หายและกราฟค้างกลางทาง)
      Chart.defaults.animation.duration = 1100;
      Chart.defaults.animation.easing = 'easeOutQuart';
    }

    // Thai word segmentation safe wrapper for tooltip text
    function formatThaiTooltipText(text, maxChars = 28) {
      if (!text || text.length <= maxChars) return text;
      if (typeof Intl !== 'undefined' && Intl.Segmenter) {
        try {
          const segmenter = new Intl.Segmenter('th', { granularity: 'word' });
          const words = Array.from(segmenter.segment(text)).map(s => s.segment);
          const lines = [];
          let cur = '';
          for (const w of words) {
            if ((cur + w).length > maxChars && cur.length > 0) {
              lines.push(cur);
              cur = w;
            } else {
              cur += w;
            }
          }
          if (cur) lines.push(cur);
          return lines;
        } catch (e) {
          return text;
        }
      }
      return text;
    }

    // 1. Data Store
    const CAMPUSES_DATA = [
      {
        id: "thaprachan",
        name: "ท่าพระจันทร์ (ศูนย์กลางประวัติศาสตร์)",
        area: '104 <span class="unit">ไร่</span>',
        students: '6,310 <span class="unit">คน</span>',
        role: "มรดกประชาธิปไตย",
        focus: "นานาชาติ / บัณฑิตศึกษา",
        locationDesc: "ริมแม่น้ำเจ้าพระยา เขตพระนคร กรุงเทพมหานคร",
        lat: 13.7557,
        lng: 100.4907,
        zoom: 16
      },
      {
        id: "rangsit",
        name: "ศูนย์รังสิต (Hub วิทยาศาสตร์-การแพทย์)",
        area: '1,757 <span class="unit">ไร่</span>',
        students: '31,500 <span class="unit">คน</span>',
        role: "วิจัยและนวัตกรรม",
        focus: "วิทยาศาสตร์-เทคโน-การแพทย์",
        locationDesc: "อำเภอคลองหลวง จังหวัดปทุมธานี",
        lat: 14.0722,
        lng: 100.6015,
        zoom: 15
      },
      {
        id: "pattaya",
        name: "ศูนย์พัทยา (นวัตกรรม EEC & ดิจิทัล)",
        area: '566 <span class="unit">ไร่</span>',
        students: '1,920 <span class="unit">คน</span>',
        role: "Smart City & EEC",
        focus: "ยานยนต์ไฟฟ้า & AI Hub",
        locationDesc: "ตำบลหนองปรือ อำเภอบางละมุง จังหวัดชลบุรี",
        lat: 12.9275,
        lng: 100.9925,
        zoom: 14
      },
      {
        id: "lampang",
        name: "ศูนย์ลำปาง (ภูมิปัญญาและการพัฒนาล้านนา)",
        area: '364 <span class="unit">ไร่</span>',
        students: '3,120 <span class="unit">คน</span>',
        role: "พัฒนาท้องถิ่นล้านนา",
        focus: "สหวิทยาการเพื่อสังคม",
        locationDesc: "ตำบลห้างฉัตร อำเภอห้างฉัตร จังหวัดลำปาง",
        lat: 18.3171,
        lng: 99.3986,
        zoom: 14
      }
    ];

    const MILESTONES_DATA = [
      { title: "พ.ศ. 2477 — สถาปนามหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง", desc: "ศ.ดร.ปรีดี พนมยงค์ สถาปนา มธก. ในฐานะ 'ตลาดวิชา' มีผู้สมัครเข้าเรียนรุ่นแรกสูงถึง 7,094 คน เพื่อเป็นบ่อน้ำบำบัดความกระหายของราษฎร", stat: "7,094", lbl: "นักศึกษารุ่นแรก" },
      { title: "พ.ศ. 2495 — สถาปนานาม 'มหาวิทยาลัยธรรมศาสตร์'", desc: "เปลี่ยนชื่ออย่างเป็นทางการเป็น 'มหาวิทยาลัยธรรมศาสตร์' (มธ.) ยึดมั่นในปรัชญาความยุติธรรมและรับใช้ประชาชน", stat: "2495", lbl: "หมุดหมายประวัติศาสตร์" },
      { title: "พ.ศ. 2496–2503 — การปฏิรูปสู่ 'ระบบปิด'", desc: "ปรับเปลี่ยนกระบวนการรับเข้าผ่านการสอบคัดเลือก (Entrance) เป็นครั้งแรก ยกระดับมาตรฐานการศึกษาเข้มข้นเทียบชั้นสากล", stat: "ระบบปิด", lbl: "การปฏิรูปคุณภาพ" },
      { title: "พ.ศ. 2529 — ขยายสู่วิทยาเขตศูนย์รังสิต", desc: "เพื่อรองรับการขยายตัวทางวิชาการด้านวิทยาศาสตร์ เทคโนโลยี และแพทยศาสตร์ ก่อกำเนิดศูนย์การศึกษาขนาดใหญ่ 1,757 ไร่", stat: "1,757 ไร่", lbl: "ศูนย์กลางรังสิต" },
      { title: "พ.ศ. 2535 — ก่อตั้งศูนย์ลำปาง", desc: "ขยายโอกาสทางการศึกษาระดับอุดมศึกษาสู่ภาคเหนือ เชื่อมโยงภูมิปัญญาท้องถิ่นและการพัฒนาชุมชนอย่างยั่งยืน", stat: "ภาคเหนือ", lbl: "การกระจายโอกาส" },
      { title: "พ.ศ. 2538 — ก่อตั้งศูนย์พัทยา", desc: "พัฒนาการศึกษาเพื่อตอบโจทย์ระเบียงเศรษฐกิจภาคตะวันออก มุ่งเน้นเทคโนโลยียานยนต์ พลังงานสะอาด และนวัตกรรมอัจฉริยะ", stat: "EEC", lbl: "ยุทธศาสตร์เศรษฐกิจ" },
      { title: "พ.ศ. 2567 — วาระครบรอบ 90 ปี ธรรมศาสตร์", desc: "ก้าวสู่ทศวรรษที่ 10 ในฐานะสถาบันอุดมศึกษาชั้นนำของเอเชีย ขับเคลื่อนยุทธศาสตร์ TU 2034 เพื่อความเป็นเลิศระดับโลก", stat: "90 ปี", lbl: "แห่งเกียรติภูมิ" }
    ];

    const FACULTIES_DATA = [
      { name: "คณะนิติศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "รากฐานกฎหมายประชาธิปไตย คุ้มครองสิทธิมนุษยชนและความยุติธรรมในสังคม", cutoff: "74.8", accept: "1 : 5.2", careers: "ผู้พิพากษา, อัยการ, นิติกร, ทนายความสากล" },
      { name: "คณะพาณิชยศาสตร์และการบัญชี (TBS)", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "ผู้นำ Triple Crown หนึ่งเดียวในไทย ติด 1% ของโลก", cutoff: "76.2", accept: "1 : 6.1", careers: "CFO, ผู้สอบบัญชี, นักวิเคราะห์การลงทุน, ผู้ประกอบการ" },
      { name: "คณะรัฐศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "สิงห์แดงชั้นนำ เสาหลักนโยบายสาธารณะและการทูตสากล", cutoff: "73.5", accept: "1 : 4.9", careers: "นักการทูต, ข้าราชการพลเรือน, นักวิเคราะห์นโยบาย" },
      { name: "คณะเศรษฐศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "เศรษฐศาสตร์ทฤษฎีและนโยบายพัฒนาเศรษฐกิจระดับชาติ", cutoff: "72.9", accept: "1 : 4.5", careers: "นักเศรษฐศาสตร์, ผู้กำหนดนโยบาย ธปท., นักวิจัย" },
      { name: "คณะสังคมวิทยาและมานุษยวิทยา", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "เข้าใจโครงสร้างสังคม มนุษย์ และความหลากหลายทางวัฒนธรรม", cutoff: "69.4", accept: "1 : 3.8", careers: "นักวิจัยสังคม, ที่ปรึกษา ESG, นักสื่อสารชุมชน" },
      { name: "คณะวารสารศาสตร์และสื่อสารมวลชน", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "ผู้นำสื่อสารมวลชนยุคดิจิทัลและสร้างสรรค์คอนเทนต์ระดับโลก", cutoff: "73.8", accept: "1 : 5.8", careers: "ผู้ผลิตสื่อ, ครีเอทีฟ, นักกลยุทธ์แบรนด์" },
      { name: "คณะสังคมสงเคราะห์ศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "พัฒนาคุณภาพชีวิต สร้างความเสมอภาคและสวัสดิการสังคม", cutoff: "68.2", accept: "1 : 3.5", careers: "นักสังคมสงเคราะห์, ผู้บริหารองค์กรไม่แสวงหากำไร" },
      { name: "คณะศิลปศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "สหภาษาศาสตร์ มนุษยศาสตร์ และวรรณคดีเปรียบเทียบ", cutoff: "71.6", accept: "1 : 4.4", careers: "นักแปล, ล่าม, นักวิชาการภาษา, เจ้าหน้าที่ระหว่างประเทศ" },
      { name: "คณะวิทยาศาสตร์และเทคโนโลยี", pillar: "sci", pillarName: "วิทย์-เทคโน", desc: "วิทยาการข้อมูล AI ชีวเคมี และนวัตกรรมอุตสาหกรรม", cutoff: "67.8", accept: "1 : 3.6", careers: "Data Scientist, นักวิจัยเคมี, ผู้พัฒนา AI" },
      { name: "คณะวิศวกรรมศาสตร์ (TSE)", pillar: "sci", pillarName: "วิทย์-เทคโน", desc: "วิศวกรรมสากล ยานยนต์ไฟฟ้า หุ่นยนต์ และการบิน", cutoff: "71.2", accept: "1 : 4.8", careers: "วิศวกรระบบ, วิศวกรยานยนต์, วิศวกรปัญญาประดิษฐ์" },
      { name: "คณะสถาปัตยกรรมศาสตร์และการผังเมือง", pillar: "sci", pillarName: "วิทย์-เทคโน", desc: "ผู้นำการออกแบบเมืองอัจฉริยะและการพัฒนาอย่างยั่งยืน", cutoff: "72.4", accept: "1 : 5.0", careers: "สถาปนิก, นักผังเมือง, นักออกแบบนวัตกรรม" },
      { name: "สถาบันเทคโนโลยีนานาชาติสิรินธร (SIIT)", pillar: "inter", pillarName: "นานาชาติ", desc: "หลักสูตรวิศวกรรมและเทคโนโลยีนานาชาติระดับท็อปของเอเชีย", cutoff: "75.0", accept: "1 : 5.5", careers: "วิศวกรข้ามชาติ, Tech Entrepreneur, นักวิจัยระดับสากล" },
      { name: "คณะแพทยศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "ผลิตแพทย์ผู้เชี่ยวชาญระดับตติยภูมิ ดูแลสุขภาวะประชาชน", cutoff: "82.4", accept: "1 : 12.5", careers: "แพทย์ผู้เชี่ยวชาญ, นักวิจัยการแพทย์, ผู้บริหารสาธารณสุข" },
      { name: "คณะทันตแพทยศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "ความเป็นเลิศด้านทันตกรรมและศัลยศาสตร์ช่องปาก", cutoff: "79.8", accept: "1 : 9.2", careers: "ทันตแพทย์, ศัลยแพทย์ช่องปาก" },
      { name: "คณะเภสัชศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "วิทยาการทางเภสัชกรรมและการบริบาลเภสัชกรรม", cutoff: "77.1", accept: "1 : 7.4", careers: "เภสัชกรโรงพยาบาล, เภสัชกรอุตสาหกรรมยา" },
      { name: "คณะพยาบาลศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "พยาบาลวิชาชีพเพื่อการดูแลผู้ป่วยขั้นวิกฤตและชุมชน", cutoff: "70.2", accept: "1 : 4.2", careers: "พยาบาลวิชาชีพ, ผู้เชี่ยวชาญการดูแลผู้สูงอายุ" },
      { name: "คณะสหเวชศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "เทคนิคการแพทย์ กายภาพบำบัด และรังสีเทคนิค", cutoff: "72.0", accept: "1 : 4.7", careers: "นักเทคนิคการแพทย์, นักกายภาพบำบัด" },
      { name: "คณะสาธารณสุขศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "การควบคุมโรค อนามัยสิ่งแวดล้อม และอาชีวอนามัย", cutoff: "68.9", accept: "1 : 3.7", careers: "นักวิชาการสาธารณสุข, เจ้าหน้าที่ความปลอดภัย (จป.)" },
      { name: "วิทยาลัยสหวิทยาการ", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "บูรณาการศาสตร์ตอบสนองความท้าทายยุคใหม่ (รังสิต-ลำปาง)", cutoff: "69.1", accept: "1 : 3.4", careers: "นักวิเคราะห์ข้อมูลสังคม, ที่ปรึกษานวัตกรรม" },
      { name: "วิทยาลัยนวัตกรรม (CITU)", pillar: "inter", pillarName: "นานาชาติ", desc: "การจัดการเทคโนโลยี นวัตกรรมบริการ และธุรกิจดิจิทัล", cutoff: "71.5", accept: "1 : 4.3", careers: "Innovation Manager, ผู้ประกอบการดิจิทัล" },
      { name: "วิทยาลัยนานาชาติปรีดี พนมยงค์ (PBIC)", pillar: "inter", pillarName: "นานาชาติ", desc: "จีนศึกษา ไทยศึกษา อินเดียศึกษา ระดับนานาชาติ", cutoff: "74.2", accept: "1 : 4.8", careers: "นักการทูต, นักกลยุทธ์ระหว่างประเทศ" },
      { name: "วิทยาลัยพัฒนศาสตร์ ป๋วย อึ๊งภากรณ์ (PSDS)", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "พัฒนาชนบท ชุมชนเข้มแข็ง และความยั่งยืนตามแนวทาง อ.ป๋วย", cutoff: "67.4", accept: "1 : 3.2", careers: "นักพัฒนาชุมชน, ที่ปรึกษา CSR/SDGs" },
      { name: "วิทยาลัยแพทยศาสตร์นานาชาติจุฬาภรณ์ (CICM)", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "หลักสูตรแพทยศาสตร์นานาชาติและทันตแพทยศาสตร์สากล", cutoff: "83.1", accept: "1 : 14.0", careers: "แพทย์สากล, นักวิจัยชีวการแพทย์" },
      { name: "คณะพยาบาลศาสตร์ (ศูนย์ลำปาง)", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "ผลิตพยาบาลเพื่อดูแลชุมชนสุขภาพภาคเหนือ", cutoff: "69.8", accept: "1 : 4.0", careers: "พยาบาลวิชาชีพ" },
      { name: "สถาบันเสริมศึกษาและทรัพยากรมนุษย์", pillar: "inter", pillarName: "นานาชาติ", desc: "Upskill & Reskill การเรียนรู้ตลอดชีวิตสำหรับประชาชนทุกวัย", cutoff: "70.0", accept: "1 : 3.5", careers: "ผู้เชี่ยวชาญการเรียนรู้และพัฒนาองค์กร" }
    ];

    const CIRCUIT_DATA = [
      {
        tag: "CENTENNIAL PILLAR 1: GLOBAL RESEARCH & INNOVATION HUB",
        title: "การวิจัยและนวัตกรรมระดับสากล (Global Research & Innovation Hub)",
        desc: "ยุทธศาสตร์มุ่งสู่ Top 100 QS World University Ranking สร้างองค์ความรู้และนวัตกรรมเปลี่ยนโลกเพื่อประโยชน์ของมนุษยชาติ เชื่อมโยงเครือข่ายวิจัยระดับสากลกว่า 350 สถาบัน และยื่นจดสิทธิบัตร Deep Tech",
        img: "assets/pillar_1_innovation_hub.webp",
        pillarClass: "pillar-card-1",
        stat1: "92.0", lbl1: "คะแนนเป้าหมาย 2577", stat2: "350+", lbl2: "สิทธิบัตรเชิงพาณิชย์"
      },
      {
        tag: "CENTENNIAL PILLAR 2: FUTURE-READY SKILLS & 21ST CENTURY LEARNING",
        title: "ทักษะแห่งอนาคตและการศึกษาดิจิทัล (Future-Ready Skills)",
        desc: "ปฏิรูปการเรียนการสอนบูรณาการ AI, Digital Literacy, และ Active Problem Solving สร้างบัณฑิตที่มีสมรรถนะพร้อมทำงานในตลาดแรงงานสากลระดับสูง และมีจิตวิญญาณประชาธิปไตย",
        img: "assets/pillar_2_future_skills.webp",
        pillarClass: "pillar-card-2",
        stat1: "95.0", lbl1: "คะแนนเป้าหมาย 2577", stat2: "100%", lbl2: "หลักสูตรบูรณาการ AI"
      },
      {
        tag: "CENTENNIAL PILLAR 3: 88 SANDBOX & STARTUP ECOSYSTEM",
        title: "88 SANDBOX ศูนย์บ่มเพาะสตาร์ทอัพเพื่อสังคมและเศรษฐกิจใหม่",
        desc: "ระบบนิเวศนวัตกรรมและบ่มเพาะผู้ประกอบการสตาร์ทอัพเพื่อสังคม เชื่อมโยง Venture Capital ระดับสากล ตั้งเป้าบ่มเพาะทีมสตาร์ทอัพ 10,000 ทีม",
        img: "assets/pillar_3_88sandbox.webp",
        pillarClass: "pillar-card-3",
        stat1: "10,000", lbl1: "ทีมสตาร์ทอัพเป้าหมาย", stat2: "อันดับ 1", lbl2: "Social Sandbox ไทย"
      },
      {
        tag: "CENTENNIAL PILLAR 4: NET-ZERO CAMPUS 2030 & PUEY PARK",
        title: "ความยั่งยืนสู่ Net-Zero Campus 2030 & อุทยานป๋วย 100 ปี",
        desc: "ผู้นำด้านความยั่งยืนระดับโลก ขับเคลื่อนพลังงานสะอาดจากฟาร์มโซลาร์รูฟท็อป 100% อาคารประหยัดพลังงาน และพื้นที่สีเขียวสวนป๋วย 100 ปี บรรลุเป้าหมายคาร์บอนสุทธิเป็นศูนย์ก่อนปี 2573",
        img: "assets/pillar_4_netzero_campus.webp",
        pillarClass: "pillar-card-4",
        stat1: "2573", lbl1: "เป้าหมาย Net Zero", stat2: "100%", lbl2: "Green Campus Model"
      }
    ];

    const STREAMS_DATA = [
      {
        id: "total",
        name: "งบประมาณรวมทุกด้าน (Total Budget)",
        share: "100%",
        amount: "15,350 ล้านบาท",
        data: [13420, 13850, 14210, 14780, 15350],
        color: "#c51944",
        desc: "งบประมาณรวมของมหาวิทยาลัยเติบโตต่อเนื่อง 5 ปีซ้อน จาก 13,420 สู่ 15,350 ล้านบาท (+14.4%) สะท้อนความมั่นคงและวินัยการคลังระดับสูง"
      },
      {
        id: "gov",
        name: "งบประมาณแผ่นดิน (Government Grants)",
        share: "35.8%",
        amount: "5,495 ล้านบาท",
        data: [4920, 5060, 5170, 5320, 5495],
        color: "#1e3a8a",
        desc: "เงินอุดหนุนทั่วไปและโครงการพัฒนาเชิงยุทธศาสตร์ระดับชาติเพื่อความเป็นเลิศทางวิชาการและการวิจัยขั้นแนวหน้า"
      },
      {
        id: "tuition",
        name: "รายได้ค่าธรรมเนียมการศึกษา (Tuition Fees)",
        share: "32.4%",
        amount: "4,973 ล้านบาท",
        data: [4280, 4450, 4610, 4790, 4973],
        color: "#00857c",
        desc: "ค่าธรรมเนียมการศึกษาหลักสูตรไทย หลักสูตรนานาชาติ และบัณฑิตศึกษา พึ่งพาตนเองได้อย่างมั่นคง"
      },
      {
        id: "assets",
        name: "ทรัพย์สินและผลประโยชน์ (Assets & Investments)",
        share: "18.2%",
        amount: "2,794 ล้านบาท",
        data: [2340, 2420, 2540, 2680, 2794],
        color: "#d97706",
        desc: "การบริหารจัดการพื้นที่เชิงพาณิชย์ ทรัพย์สินทางปัญญา และผลตอบแทนจากการลงทุน เติบโตอย่างก้าวกระโดด"
      },
      {
        id: "research",
        name: "ทุนวิจัยและบริการวิชาการ (Research & Services)",
        share: "8.6%",
        amount: "1,320 ล้านบาท",
        data: [1180, 1210, 1240, 1280, 1320],
        color: "#7c3aed",
        desc: "เงินทุนวิจัยจากแหล่งทุนภายนอก ภาครัฐและเอกชน รวมทั้งงานบริการวิชาการแก่สังคมและอุตสาหกรรมเป้าหมาย"
      },
      {
        id: "medical",
        name: "บริการทางการแพทย์และสาธารณสุข (Healthcare Services)",
        share: "5.0%",
        amount: "768 ล้านบาท",
        data: [700, 710, 650, 710, 768],
        color: "#e11d48",
        desc: "รายได้จากการให้บริการทางการแพทย์ คลินิกพิเศษ และศูนย์บริการสุขภาพเฉพาะทางเพื่อส่งเสริมสุขภาวะประชาชน"
      }
    ];

    const FLOURISH_SCENES_DATA = [
      {
        id: 1,
        title: "1. ภาพรวมพัฒนาการ 90 ปี ธรรมศาสตร์",
        template: "Line Chart / Story Timeline",
        templateUrl: "https://app.flourish.studio/@flourish/line-chart",
        category: "Historical Overview",
        badge: "พ.ศ. 2477 — 2567",
        csv: "01_flourish_scene1_student_growth.csv",
        secondaryCsv: "01_flourish_bar_chart_race_faculties.csv",
        secondaryLabel: "Bar Chart Race CSV",
        desc: "ลำดับเส้นเวลาการก่อตั้งและวิวัฒนาการ 90 ปีแห่งประวัติศาสตร์ จากมหาวิทยาลัยวิชาธรรมศาสตร์และการเมืองสู่มหาวิทยาลัยวิจัยระดับสากล",
        highlights: [
          "พ.ศ. 2477: สถาปนามหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง (มธก.) โดย ศ.ดร.ปรีดี พนมยงค์ มีนักศึกษารุ่นแรก 7,094 คน",
          "พ.ศ. 2529: ขยายวิทยาเขตแรกสู่ปริมณฑล ณ ศูนย์รังสิต เพื่อรองรับสายวิทยาศาสตร์และเทคโนโลยี",
          "พ.ศ. 2567: ก้าวสู่ 90 ปี มหาวิทยาลัยระดับโลกเพื่อประชาชน มีนักศึกษารวม 42,850 คน และเป้าหมาย TU 2034"
        ],
        tableHeaders: ["Year_BE", "Year_AD", "Students", "Event_Milestone"],
        tableSample: [
          ["2477", "1934", "7,094", "ตลาดวิชารุ่นแรก (ก่อตั้ง มธก.)"],
          ["2488", "1945", "9,800", "สงครามโลกครั้งที่ 2"],
          ["2495", "1952", "4,200", "ปรับสู่มหาวิทยาลัยระบบปิด"],
          ["2508", "1965", "11,500", "ขยายสายสังคมศาสตร์"],
          ["2519", "1976", "15,800", "ยุคประชาธิปไตย"],
          ["2529", "1986", "21,000", "สถาปนาศูนย์รังสิต"],
          ["2539", "1996", "27,500", "ขยายศูนย์พัทยาและลำปาง"],
          ["2549", "2006", "33,200", "ขยายหลักสูตรนานาชาติ"],
          ["2559", "2016", "39,400", "ศูนย์กลางนวัตกรรม"],
          ["2567", "2024", "42,850", "ปัจจุบัน 4 ศูนย์ 26 คณะ"]
        ]
      },
      {
        id: 2,
        title: "2. พิกัดภูมิศาสตร์ 4 ศูนย์การศึกษา",
        template: "Marker Map / Geographic Explorer",
        templateUrl: "https://app.flourish.studio/@flourish/marker-map",
        category: "Campus GIS",
        badge: "4 ศูนย์การศึกษา • 2,791 ไร่",
        csv: "02_flourish_scene2_campus_locations.csv",
        secondaryCsv: "02_flourish_campuses_map.csv",
        secondaryLabel: "Campuses GIS Coordinates CSV",
        desc: "ข้อมูลเชิงพื้นที่และบทบาทเชิงยุทธศาสตร์ ขนาดพื้นที่ จำนวนประชากรนักศึกษา และความเชี่ยวชาญเฉพาะทางของ 4 ศูนย์",
        highlights: [
          "ศูนย์รังสิต (1,757 ไร่): ศูนย์กลางการศึกษาหลัก ศูนย์การแพทย์ สวนป๋วย 100 ปี และอุทยานนวัตกรรม รองรับนักศึกษา 31,500 คน (73.5%)",
          "ศูนย์ท่าพระจันทร์ (104 ไร่): หัวใจประวัติศาสตร์ มรดกประชาธิปไตย และศูนย์กลางหลักสูตรนานาชาติ/บัณฑิตศึกษา (6,310 คน)",
          "ศูนย์ลำปาง (364 ไร่ • 3,120 คน) & ศูนย์พัทยา (566 ไร่ • 1,920 คน): ประตูการศึกษาล้านนาและศูนย์กลางนวัตกรรม EEC"
        ],
        tableHeaders: ["Campus_Name", "Latitude", "Longitude", "Area_Rai", "Students", "Share_Pct", "Established_BE", "Key_Role"],
        tableSample: [
          ["ศูนย์ท่าพระจันทร์", "13.7557", "100.4907", "104", "6,310", "14.8%", "2477", "ศูนย์กลางประวัติศาสตร์ นานาชาติ และบัณฑิตศึกษา"],
          ["ศูนย์รังสิต", "14.0722", "100.6015", "1,757", "31,500", "73.5%", "2529", "ศูนย์การศึกษาหลัก ศูนย์การแพทย์ สวนป๋วย 100 ปี นวัตกรรม"],
          ["ศูนย์ลำปาง", "18.3171", "99.3986", "364", "3,120", "7.2%", "2535", "ประตูการศึกษาภาคเหนือ ศิลปวัฒนธรรมล้านนา สหวิทยาการ"],
          ["ศูนย์พัทยา", "12.9275", "100.9925", "566", "1,920", "4.5%", "2538", "เขตเศรษฐกิจพิเศษ EEC ยานยนต์ไฟฟ้า นวัตกรรมดิจิทัล"]
        ]
      },
      {
        id: 3,
        title: "3. ลำดับชั้นคณะวิชา & จำนวนนักศึกษา (21 คณะ)",
        template: "Hierarchy Treemap / Sunburst",
        templateUrl: "https://app.flourish.studio/@flourish/hierarchy",
        category: "Academic Hierarchy",
        badge: "21 คณะ • 4 เสาหลักวิชาการ",
        csv: "03_flourish_scene3_faculty_hierarchy.csv",
        secondaryCsv: "03_flourish_faculties_tcas.csv",
        secondaryLabel: "26 คณะ & TCAS Scores CSV",
        desc: "การกระจายตัวของประชากรนักศึกษาในแต่ละกลุ่มสาขาวิชาและคณะ สะท้อนโครงสร้างความเชี่ยวชาญแบบพหุวิทยาการ",
        highlights: [
          "คณะพาณิชยศาสตร์และการบัญชี (TBS): ครองอันดับ 1 กลุ่มสังคมศาสตร์ นักศึกษา 4,950 คน และเป็น Triple Crown",
          "คณะนิติศาสตร์: เสาหลักรากฐานธรรมศาสตร์ นักศึกษา 3,800 คน ผลิตนักกฎหมายชั้นนำระดับประเทศ",
          "คณะวิศวกรรมศาสตร์ & วิทยาศาสตร์ฯ: นำทัพสายเทคโนโลยีรวมกว่า 5,900 คน ขับเคลื่อน AI และ Deep Tech"
        ],
        tableHeaders: ["Cluster", "Faculty", "Students", "Cluster_Total", "Share_In_Cluster"],
        tableSample: [
          ["สังคมศาสตร์-มนุษยศาสตร์", "คณะพาณิชยศาสตร์และการบัญชี (TBS)", "4,950", "17,900", "27.7%"],
          ["สังคมศาสตร์-มนุษยศาสตร์", "คณะนิติศาสตร์", "3,800", "17,900", "21.2%"],
          ["สังคมศาสตร์-มนุษยศาสตร์", "คณะศิลปศาสตร์", "2,600", "17,900", "14.5%"],
          ["สังคมศาสตร์-มนุษยศาสตร์", "คณะเศรษฐศาสตร์", "2,200", "17,900", "12.3%"],
          ["วิทยาศาสตร์และเทคโนโลยี", "คณะวิศวกรรมศาสตร์", "3,100", "11,100", "27.9%"],
          ["วิทยาศาสตร์และเทคโนโลยี", "คณะวิทยาศาสตร์และเทคโนโลยี", "2,800", "11,100", "25.2%"],
          ["วิทยาศาสตร์สุขภาพ", "คณะแพทยศาสตร์", "1,250", "7,650", "16.3%"]
        ]
      },
      {
        id: 4,
        title: "4. ความหลากหลายทางเพศภาวะใน 4 เสาหลัก",
        template: "Grouped & Stacked Bar Chart",
        templateUrl: "https://app.flourish.studio/@flourish/bar-chart",
        category: "Diversity & Demographics",
        badge: "หญิง 62.4% • ชาย 37.6%",
        csv: "04_flourish_scene4_gender_diversity.csv",
        secondaryCsv: "04_flourish_gender_demographics.csv",
        secondaryLabel: "Gender Summary Donut CSV",
        desc: "โครงสร้างความหลากหลายทางเพศของนักศึกษาใน 4 กลุ่มสาขาวิชา สะท้อนสังคมแห่งความเท่าเทียมและการเปิดกว้าง",
        highlights: [
          "วิทยาศาสตร์สุขภาพและการแพทย์: สัดส่วนนักศึกษาหญิงสูงสุด 71.5% (≈5,577 คน จาก 7,800 คน)",
          "สังคมศาสตร์และมนุษยศาสตร์: กลุ่มใหญ่ที่สุด 19,200 คน หญิง 64.2% ชาย 35.8%",
          "วิทยาศาสตร์และเทคโนโลยี: ใกล้สมดุลที่สุด หญิง 53.8% ชาย 46.2% (11,450 คน)"
        ],
        tableHeaders: ["Cluster", "Female_Students", "Male_Students", "Female_Pct", "Male_Pct", "Total_Students"],
        tableSample: [
          ["สังคมศาสตร์-มนุษยศาสตร์", "12,326", "6,874", "64.2%", "35.8%", "19,200"],
          ["วิทยาศาสตร์และเทคโนโลยี", "6,160", "5,290", "53.8%", "46.2%", "11,450"],
          ["วิทยาศาสตร์สุขภาพ", "5,577", "2,223", "71.5%", "28.5%", "7,800"],
          ["นานาชาติและสถาบันบูรณาการ", "2,675", "1,725", "60.8%", "39.2%", "4,400"],
          ["ภาพรวมทั้งมหาวิทยาลัย", "26,738", "16,112", "62.4%", "37.6%", "42,850"]
        ]
      },
      {
        id: 5,
        title: "5. การโยกย้ายศูนย์กลางการศึกษาข้ามยุคสมัย",
        template: "Sankey Diagram",
        templateUrl: "https://app.flourish.studio/@flourish/sankey",
        category: "Campus Migration",
        badge: "ท่าพระจันทร์ ➔ รังสิต 73.5%",
        csv: "05_flourish_scene5_migration_flow_sankey.csv",
        secondaryCsv: "05_flourish_campus_migration_eras.csv",
        secondaryLabel: "Campus Migration Eras CSV",
        desc: "แผนภาพกระแสการโยกย้ายนักศึกษาและหลักสูตรปริญญาตรีจากท่าพระจันทร์สู่ศูนย์รังสิตเต็มรูปแบบ",
        highlights: [
          "พ.ศ. 2500: ศูนย์ท่าพระจันทร์รองรับนักศึกษา 100% ก่อนเริ่มมีข้อจำกัดด้านพื้นที่ขยาย",
          "พ.ศ. 2529 - 2545: การย้ายนักศึกษาสายวิทยาศาสตร์และตามด้วยทุกหลักสูตรปริญญาตรีสู่รังสิต",
          "ปัจจุบัน: รังสิตเป็น Main Campus (73.5%) ขณะที่ท่าพระจันทร์ปรับสู่ Global & Postgrad Hub (14.8%)"
        ],
        tableHeaders: ["Source_Node", "Target_Node", "Student_Flow_Value", "Era_Description"],
        tableSample: [
          ["มธ. ท่าพระจันทร์ (ศูนย์แรก 2477)", "รังสิต ปัจจุบัน (31,500 คน / ป.ตรี)", "17,500", "การย้ายหลักสูตร ป.ตรี สู่รังสิตเต็มรูปแบบ"],
          ["มธ. ท่าพระจันทร์ (ศูนย์แรก 2477)", "ท่าพระจันทร์ ปัจจุบัน (6,310 คน / นานาชาติ)", "6,310", "คงไว้เฉพาะหลักสูตรนานาชาติและ ป.โท-เอก"],
          ["มธ. ท่าพระจันทร์ (ศูนย์แรก 2477)", "ขยายสู่ศูนย์รังสิต (2529)", "14,000", "การก่อตั้งศูนย์รังสิตรองรับเอเชียนเกมส์"],
          ["ขยายสู่ศูนย์รังสิต (2529)", "รังสิต ปัจจุบัน (31,500 คน / ป.ตรี)", "14,000", "การเติบโตของศูนย์รังสิต"],
          ["ขยายสู่ศูนย์ลำปาง (2535)", "ลำปาง ปัจจุบัน (3,120 คน / ล้านนา)", "3,120", "พัฒนาการศึกษาภาคเหนือ"],
          ["ขยายสู่ศูนย์พัทยา (2538)", "พัทยา ปัจจุบัน (1,920 คน / EEC)", "1,920", "รองรับเขตเศรษฐกิจพิเศษ EEC"]
        ]
      },
      {
        id: 6,
        title: "6. โครงสร้างและแนวโน้มงบประมาณ 5 ปี",
        template: "Bar & Waterfall Projection Chart",
        templateUrl: "https://app.flourish.studio/@flourish/bar-chart",
        category: "Financial Architecture",
        badge: "15,350 ล้านบาท • เติบโต +3.4%/ปี",
        csv: "06_flourish_budget_5year_streams.csv",
        secondaryCsv: "06_flourish_scene6_budget_waterfall.csv",
        secondaryLabel: "Budget Waterfall CSV",
        desc: "โครงสร้างงบประมาณ 5 ช่องทางหลักของมหาวิทยาลัยและแนวโน้มการเติบโตต่อเนื่องตลอด 5 ปีงบประมาณ (2563-2567)",
        highlights: [
          "งบประมาณรวมเติบโตจาก 13,420 ล้านบาท (ปี 2563) สู่สถิติสูงสุด 15,350 ล้านบาท (ปี 2567)",
          "งบประมาณแผ่นดิน (35.8% / 5,495 ลบ.) และค่าธรรมเนียมการศึกษา (32.4% / 4,973 ลบ.) เป็นฐานรายรับหลัก",
          "รายได้บริหารทรัพย์สินและการลงทุนเติบโตสู่ 2,794 ล้านบาท (18.2%) สร้างอิสรภาพทางการคลัง"
        ],
        tableHeaders: ["Stream_ID", "Revenue_Stream", "Share_Pct", "Latest_Amount", "FY2563", "FY2564", "FY2565", "FY2566", "FY2567"],
        tableSample: [
          ["total", "งบประมาณรวมทุกด้าน (Total Budget)", "100%", "15,350 ล้านบาท", "13,420", "13,850", "14,210", "14,780", "15,350"],
          ["gov", "งบประมาณแผ่นดิน (Government Grants)", "35.8%", "5,495 ล้านบาท", "4,920", "5,060", "5,170", "5,320", "5,495"],
          ["tuition", "รายได้ค่าธรรมเนียมการศึกษา (Tuition Fees)", "32.4%", "4,973 ล้านบาท", "4,280", "4,450", "4,610", "4,790", "4,973"],
          ["assets", "ทรัพย์สินและผลประโยชน์ (Assets & Investments)", "18.2%", "2,794 ล้านบาท", "2,340", "2,420", "2,540", "2,680", "2,794"],
          ["research", "รายได้วิจัยและบริการวิชาการ (Research & Services)", "8.6%", "1,320 ล้านบาท", "1,180", "1,210", "1,240", "1,280", "1,320"],
          ["medical", "บริการทางการแพทย์ (Healthcare Services)", "5.0%", "768 ล้านบาท", "700", "710", "650", "710", "768"]
        ]
      },
      {
        id: 7,
        title: "7. อันดับมหาวิทยาลัยโลก & มาตรฐาน Triple Crown",
        template: "Rankings / Slope Chart",
        templateUrl: "https://app.flourish.studio/@flourish/slope-chart",
        category: "Global Rankings",
        badge: "QS Asia อันดับ 92 • Triple Crown",
        csv: "07_flourish_scene7_rankings_trend.csv",
        secondaryCsv: "07_flourish_business_schools.csv",
        secondaryLabel: "Business Schools Triple Crown CSV",
        desc: "เส้นทางพัฒนาการอันดับมหาวิทยาลัยระดับโลกและภูมิภาคเอเชีย พร้อมการรับรองมาตรฐาน Triple Crown (AACSB, EQUIS, AMBA)",
        highlights: [
          "QS Asia University Rankings: ไต่ระดับจากอันดับ 137 (2018) สู่ท็อป 100 เอเชีย อันดับ 92 (2024)",
          "TBS Business & Management: อันดับโลกขยับขึ้นต่อเนื่องจาก 250 สู่ 140 ของโลก",
          "Triple Crown: ได้รับการรับรองครบ 3 สถาบันมาตรฐานสากล (AACSB, EQUIS, AMBA) เป็นแห่งแรกในไทย อยู่ในกลุ่มท็อป 1% ของโลก"
        ],
        tableHeaders: ["Year", "QS_Asia_University_Rank", "QS_Business_Management_TBS_Rank", "Benchmark_Top100"],
        tableSample: [
          ["2018", "137", "250", "100"],
          ["2019", "134", "225", "100"],
          ["2020", "119", "210", "100"],
          ["2021", "111", "195", "100"],
          ["2022", "107", "180", "100"],
          ["2023", "98", "160", "100"],
          ["2024", "92", "140", "100"]
        ]
      },
      {
        id: 8,
        title: "8. ตัวชี้วัดความยั่งยืน SDG & Green Campus",
        template: "Radar / Spider Chart",
        templateUrl: "https://app.flourish.studio/@flourish/radar",
        category: "Sustainability SDGs",
        badge: "SDG 11 ท็อป 10 โลก • แผนโซลาร์ 15 MW",
        csv: "08_flourish_scene8_sdg_radar.csv",
        secondaryCsv: "08_flourish_sustainability_metrics.csv",
        secondaryLabel: "Sustainability & Solar Metrics CSV",
        desc: "ผลการประเมินคะแนนเป้าหมายการพัฒนาที่ยั่งยืนแห่งสหประชาชาติ (UN SDGs) และความสำเร็จด้านพลังงานสะอาด",
        highlights: [
          "SDG 11 (Sustainable Cities & Communities): คะแนน 98.4 ติดอันดับ Top 10 ของโลก โดย THE Impact Rankings",
          "SDG 4 (Quality Education): คะแนน 92.8 ยืนยันการเข้าถึงการศึกษาที่มีคุณภาพและเท่าเทียม",
          "แคมปัสสีเขียว: โซลาร์เซลล์แผนติดตั้ง 15 MW (ติดตั้งแล้วเสร็จ 5 MW) และสวนป๋วย 100 ปี พื้นที่ 22,000 ตร.ม. ใหญ่ที่สุดในเอเชีย"
        ],
        tableHeaders: ["SDG_Goal", "Goal_Title", "Thammasat_Score", "World_Class_Benchmark"],
        tableSample: [
          ["SDG 11", "Sustainable Cities & Communities (Top 10 โลก)", "98.4", "90.0"],
          ["SDG 4", "Quality Education (การศึกษาเท่าเทียม)", "92.8", "90.0"],
          ["SDG 7", "Affordable & Clean Energy (แผนพลังงานสะอาด 15 MW)", "91.5", "90.0"],
          ["SDG 17", "Partnerships for the Goals (พันธมิตรความร่วมมือ)", "90.4", "90.0"],
          ["SDG 3", "Good Health & Well-being (สุขภาวะชุมชน)", "88.6", "90.0"],
          ["SDG 13", "Climate Action (การรับมือโลกร้อน)", "87.2", "90.0"]
        ]
      },
      {
        id: 9,
        title: "9. การเติบโตของ รพ.ธรรมศาสตร์เฉลิมพระเกียรติ",
        template: "Column Chart",
        templateUrl: "https://app.flourish.studio/@flourish/bar-chart",
        category: "Healthcare Infrastructure",
        badge: "1.48 ล้านคน/ปี • 750 เตียง",
        csv: "09_flourish_scene9_hospital_growth.csv",
        secondaryCsv: "09_flourish_hospital_capacity.csv",
        secondaryLabel: "Hospital Capacity Services CSV",
        desc: "วิวัฒนาการ 37 ปีของโรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ สู่ศูนย์การแพทย์ระดับตติยภูมิชั้นสูงและเสาหลักสู้ภัยสุขภาพ",
        highlights: [
          "ผู้ป่วยนอก (OPD): เติบโตจาก 50,000 คน/ปี (ปี 2530) สู่ 1,480,000 คน/ปีในปัจจุบัน",
          "เตียงผู้ป่วยตติยภูมิเปิดบริการจริง 750 เตียง (มติ ครม. เป้าหมาย 1,000 เตียง) พร้อมศูนย์เฉพาะทางครบวงจร",
          "บทบาทประวัติศาสตร์: โรงพยาบาลสนามแห่งแรกของไทยในวิกฤตโควิด-19 และศูนย์ฉีดวัคซีนระดับชาติ"
        ],
        tableHeaders: ["Year_BE", "Year_AD", "Outpatient_Visits", "Notable_Events"],
        tableSample: [
          ["2530", "1987", "50,000", "เริ่มเปิดให้บริการ รพ.ธรรมศาสตร์"],
          ["2540", "1997", "210,000", "ขยายอาคารบริการทางการแพทย์"],
          ["2550", "2007", "520,000", "ยกระดับสู่ศูนย์การแพทย์ระดับตติยภูมิ"],
          ["2560", "2017", "980,000", "รองรับผู้ป่วยตติยภูมิขั้นสูง"],
          ["2564", "2021", "1,250,000", "โรงพยาบาลสนามแห่งแรกสู้ภัยโควิด-19"],
          ["2567", "2024", "1,480,000", "ศูนย์การแพทย์เพื่อประชาชน 750 เตียง (เป้าหมาย 1,000 เตียง)"]
        ]
      },
      {
        id: 10,
        title: "10. ยุทธศาสตร์ TU 2034 และ 4 เสาหลักสู่ 100 ปี",
        template: "Cards & Progress Gauges",
        templateUrl: "https://app.flourish.studio/@flourish/cards",
        category: "Strategic Centennial",
        badge: "Vision 2034 • 4 เสาหลัก",
        csv: "10_flourish_scene10_strategic_gauges.csv",
        secondaryCsv: "10_flourish_centennial_pillars.csv",
        secondaryLabel: "4 Centennial Pillars Vision CSV",
        desc: "เป้าหมายเชิงยุทธศาสตร์สู่ทศวรรษที่ 10 (พ.ศ. 2577) ภายใต้วิสัยทัศน์มหาวิทยาลัยระดับโลกเพื่อประชาชน",
        highlights: [
          "Pillar 1 (Global Research): มุ่งสู่ Top 100 QS World University Ranking และเครือข่ายวิจัย 350+ มหาวิทยาลัย",
          "Pillar 2 (Future Skills): ปฏิรูปหลักสูตรบูรณาการ AI 100% และ Lifelong Learning",
          "Pillar 3 & 4: 88 SANDBOX บ่มเพาะสตาร์ทอัพ 10,000 ทีม และ Net-Zero Campus ก่อนปี 2030"
        ],
        tableHeaders: ["KPI_Name", "Current_Value", "Target_Value", "Unit", "Progress_Pct", "Target_Year"],
        tableSample: [
          ["Pillar 1: วิจัยสากล (Global Research)", "72.4", "92.0", "คะแนนดัชนีวิจัย", "78.7%", "พ.ศ. 2577 (ค.ศ. 2034)"],
          ["Pillar 2: ทักษะดิจิทัล & AI (Future Skills)", "78.5", "95.0", "คะแนนหลักสูตร AI", "82.6%", "พ.ศ. 2577 (ค.ศ. 2034)"],
          ["Pillar 3: 88 SANDBOX Startups", "6,200", "10,000", "ทีมสตาร์ทอัพบ่มเพาะ", "62.0%", "พ.ศ. 2577 (ค.ศ. 2034)"],
          ["Pillar 4: TU Net-Zero Campus 2030", "78.0", "100.0", "เปอร์เซ็นต์พลังงานสะอาด", "78.0%", "พ.ศ. 2573 (ค.ศ. 2030)"]
        ]
      }
    ];

    // 2. Scroll Interactions & Navigation Tracking
    const SECTION_TRACKS = [
      { id: 'hero', name: 'หน้าแรก' },
      { id: 'topic-01', name: '1. ปฐมบท 2477' },
      { id: 'topic-02', name: '2. ศูนย์การศึกษา' },
      { id: 'topic-03', name: '3. คณะและเกณฑ์ TCAS' },
      { id: 'topic-04', name: '4. มิติประชากร' },
      { id: 'topic-05', name: '5. การโยกย้ายศูนย์กลาง' },
      { id: 'topic-06', name: '6. วินัยการคลัง' },
      { id: 'topic-07', name: '7. มาตรฐานสากล' },
      { id: 'topic-08', name: '8. แคมปัสสีเขียว' },
      { id: 'topic-09', name: '9. รพ.ธรรมศาสตร์' },
      { id: 'topic-10', name: '10. ยุทธศาสตร์ TU 2034' },
      { id: 'finish', name: 'ศตวรรษ 90 ปี' }
    ];

    // ==========================================================================
    // HERO WALKERS: นักศึกษาเดินลงตามเลนแบบทแยงไปทางที่หันหน้า (ขวา)
    //  - ระยะทางผูกกับตำแหน่งสกรอลล์ (ไม่กระโดด ไม่หลุดออกนอกฉาก)
    //  - ก้าวเท้า (ยก-ลง + เอียงตัว) ตามระยะที่เดินจริง จึงหยุดเมื่อผู้ใช้หยุดเลื่อน
    //  - เลื่อนขึ้น = เดินกลับ ตัวละครหันหลังกลับ (กลับด้านภาพ) ไม่เดินถอยหลัง
    // ==========================================================================
        function scrollToElement(id) {
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      }
    }
    window.scrollToElement = scrollToElement;

const heroWalkerState = { lastY: 0, facing: 1, ticking: false };

    function requestHeroWalkerFrame() {
      if (heroWalkerState.ticking) return;
      heroWalkerState.ticking = true;
      requestAnimationFrame(() => { heroWalkerState.ticking = false; updateHeroWalkers(); });
    }

    // จัดตำแหน่งเริ่มของนักศึกษาและป้ายปีให้อยู่ "ใต้ปุ่มเริ่มต้นสำรวจ" เสมอ
    // (กันไม่ให้ทับข้อความเมื่อจอเตี้ย ซูมเบราว์เซอร์ หรือฟอนต์ใหญ่)
    let heroLayoutKey = '';
    function layoutHeroWalkers(force) {
      const hero = document.getElementById('hero');
      const cta = hero && hero.querySelector('.hero-scroll-pill-btn');
      const leader = document.getElementById('studentLeader');
      const scholar = document.getElementById('studentScholar');
      if (!hero || !cta || !leader || !scholar) return;
      const key = window.innerWidth + 'x' + window.innerHeight + ':' + cta.offsetHeight;
      if (!force && key === heroLayoutKey) return;
      heroLayoutKey = key;
      const heroTop = hero.getBoundingClientRect().top + window.pageYOffset;
      const ctaBottom = cta.getBoundingClientRect().bottom + window.pageYOffset - heroTop;
      const mobile = window.innerWidth <= 768;
      const labelGap = 16, labelH = 28;
      const poleTop = ctaBottom + (mobile ? 22 : 34);
      const leaderTop = poleTop + labelH + labelGap;
      const scholarTop = leaderTop + (mobile ? 70 : 95);
      leader.style.top = leaderTop + 'px';
      scholar.style.top = scholarTop + 'px';
      const pole = hero.querySelector('.grid-box-pole');
      if (pole) pole.style.top = poleTop + 'px';
      // ให้ฉากยาวพอสำหรับเส้นทางเดิน (อย่างน้อย 520px หลังจุดเริ่ม)
      const needed = scholarTop + scholar.offsetHeight + (mobile ? 480 : 620);
      hero.style.minHeight = Math.max(needed, window.innerHeight * (mobile ? 1.95 : 2.05)) + 'px';
    }

    function updateHeroWalkers() {
      const hero = document.getElementById('hero');
      const stage = hero && hero.querySelector('.central-track-stage');
      if (!hero || !stage) return;
      layoutHeroWalkers(false);
      const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const y = Math.max(0, window.pageYOffset || document.documentElement.scrollTop);
      const heroH = hero.offsetHeight;
      const vh = window.innerHeight;
      const span = Math.max(1, heroH - vh * 0.55);
      const p = Math.min(Math.max(y / span, 0), 1);

      const dy = y - heroWalkerState.lastY;
      if (Math.abs(dy) > 0.5) heroWalkerState.facing = dy >= 0 ? 1 : -1;
      heroWalkerState.lastY = y;

      const laneW = stage.clientWidth;
      const stageH = stage.offsetHeight || heroH;
      const slot2 = stage.querySelector('.grid-box-slot2');
      const slot2Top = slot2 ? slot2.offsetTop : (stageH - 110 - 28);
      const slot2H = slot2 ? slot2.offsetHeight : 28;
      const slot2Bottom = slot2Top + slot2H;

      [['studentLeader', 0.24, 0], ['studentScholar', 0.18, Math.PI / 2]].forEach(([id, dxRatio, phase]) => {
        const el = document.getElementById(id);
        if (!el) return;
        const img = el.querySelector('.tu-student-walker-img');
        const startTop = el.offsetTop;                 // ตำแหน่งก่อน transform
        const h = el.offsetHeight;

        // ล็อกระยะสิ้นสุดสูงสุด (Clamp): หยุดสนิทพอดีที่ระดับหมุด "2567 — ครบ 90 ปี" ห้ามเคลื่อนที่เกินระดับหมุดเด็ดขาด
        const targetStopBottom = (id === 'studentScholar') ? (slot2Top - 10) : (slot2Top - 45);
        const maxTravelY = Math.max(0, targetStopBottom - h - startTop);
        const travelX = laneW * dxRatio;
        const maxX = Math.max(0, laneW - el.offsetLeft - el.offsetWidth - 8);
        const tx = Math.min(travelX * p, maxX);
        const ty = Math.min(maxTravelY * p, maxTravelY);
        el.style.transform = `translate3d(${tx.toFixed(1)}px, ${ty.toFixed(1)}px, 0)`;

        if (img) {
          const dist = Math.hypot(tx, ty);
          const stepPhase = dist / 22 + phase;         // 1 ก้าว ≈ 70px ของระยะทาง
          const bob = reduce ? 0 : -Math.abs(Math.sin(stepPhase)) * 6;
          const tilt = reduce ? 0 : Math.sin(stepPhase) * 1.8;
          const flip = heroWalkerState.facing;
          img.style.transform = `translateY(${bob.toFixed(2)}px) rotate(${(tilt * flip).toFixed(2)}deg) scaleX(${flip})`;
        }
      });
    }

    function initScrollInteractions() {
      window.addEventListener('resize', requestHeroWalkerFrame, { passive: true });
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => { layoutHeroWalkers(true); requestHeroWalkerFrame(); });
      window.addEventListener('load', () => { layoutHeroWalkers(true); requestHeroWalkerFrame(); });
      requestHeroWalkerFrame();
      const studentLeader = document.getElementById('studentLeader');
      const studentScholar = document.getElementById('studentScholar');
      const scrubberFill = document.getElementById('scrubberFill');
      const scrubberThumb = document.getElementById('scrubberThumb');
      const pips = document.querySelectorAll('.scrubber-pip');
      const navLinks = document.querySelectorAll('.header-nav-link');
      const topicText = document.getElementById('scrubberTopicText');

      window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = Math.min(Math.max(scrollTop / scrollHeight, 0), 1);

        // Header Background Transition
        const header = document.getElementById('mainHeader');
        if (header) {
          if (scrollTop > 40) header.classList.add('scrolled');
          else header.classList.remove('scrolled');
        }

        // Update Scrubber Fill, Thumb, and Top Reading Progress Bar (Part E)
        if (scrubberFill && scrubberThumb) {
          scrubberFill.style.width = (progress * 100) + '%';
          scrubberThumb.style.left = (progress * 100) + '%';
        }
        const topBar = document.getElementById('topReadingProgress');
        if (topBar) {
          topBar.style.width = (progress * 100) + '%';
          topBar.setAttribute('aria-valuenow', Math.round(progress * 100));
        }

        // Update Desktop Dot Navigation Active Dot
        const dotNavItems = document.querySelectorAll('.desktop-dot-nav .desktop-dot');
        const trackSecs = ['hero', 'topic-01', 'topic-02', 'topic-03', 'topic-04', 'topic-05', 'topic-06', 'topic-07', 'topic-08', 'topic-09', 'topic-10', 'finish'];
        let activeSec = 'hero';
        trackSecs.forEach(secId => {
          const secEl = document.getElementById(secId);
          if (secEl) {
            const rect = secEl.getBoundingClientRect();
            if (rect.top <= window.innerHeight * 0.45 && rect.bottom >= window.innerHeight * 0.15) {
              activeSec = secId;
            }
          }
        });
        dotNavItems.forEach(dot => {
          if (dot.getAttribute('href') === '#' + activeSec) {
            dot.classList.add('active');
          } else {
            dot.classList.remove('active');
          }
        });

        // Hero Student Walkers — เดินตามการเลื่อนหน้าแบบต่อเนื่อง (ดู updateHeroWalkers)
        requestHeroWalkerFrame();

        // Update Active Nav Link, Scrubber Pip, and Topic Indicator
        SECTION_TRACKS.forEach((sec, idx) => {
          const el = document.getElementById(sec.id);
          if (el) {
            const rect = el.getBoundingClientRect();
            if (rect.top <= window.innerHeight * 0.45 && rect.bottom >= window.innerHeight * 0.45) {
              pips.forEach(p => p.classList.remove('active'));
              if (pips[idx]) pips[idx].classList.add('active');

              navLinks.forEach(l => l.classList.remove('active'));
              if (navLinks[idx]) {
                navLinks[idx].classList.add('active');
                autoScrollHeaderNavToActive(navLinks[idx]);
              }

              if (topicText) topicText.textContent = sec.name;
            }
          }
        });
      }, { passive: true });
    }

    // 3. Scrubber Click Handler
    function handleScrubberClick(e) {
      const track = document.getElementById('scrubberTrack');
      const rect = track.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = Math.min(Math.max(clickX / rect.width, 0), 1);
      const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
      window.scrollTo({
        top: ratio * scrollHeight,
        behavior: 'smooth'
      });
    }

    // 4. Leaflet Map Engine
    let tuMap = null;
    let tuMarkers = [];
    let corridorLines = [];

    function initTuLeafletMap() {
      if (tuMap) return;

      tuMap = L.map('campusLeafletMap', {
        center: [14.8, 100.5],
        zoom: 6,
        scrollWheelZoom: false,
        attributionControl: true,
        touchZoom: true,
        dragging: true
      });

      // High-detail Street Basemap with visible streets, corners, avenues & landmarks (Free, No API Key)
      window.tuTileStreet = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 19,
        attribution: 'Esri, HERE, Garmin, USGS, NGA'
      }).addTo(tuMap);

      // High-resolution Satellite Imagery Basemap (Free, No API Key)
            // Add accessible aria labels to Leaflet zoom controls
      setTimeout(() => {
        const zoomIn = document.querySelector('.leaflet-control-zoom-in');
        if (zoomIn) zoomIn.setAttribute('aria-label', 'ซูมเข้าแผนที่');
        const zoomOut = document.querySelector('.leaflet-control-zoom-out');
        if (zoomOut) zoomOut.setAttribute('aria-label', 'ซูมออกแผนที่');
      }, 500);

      window.tuTileSat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 18,
        attribution: 'Esri, Maxar, Earthstar Geographics'
      });

      const campusCoordinates = [];
      CAMPUSES_DATA.forEach((camp, idx) => {
        campusCoordinates.push([camp.lat, camp.lng]);

        const customIcon = L.divIcon({
          className: 'custom-tu-pin',
          html: `<div style="width: 22px; height: 22px; border-radius: 50%; background: #c51944; border: 3px solid #ffc72c; box-shadow: 0 0 12px #ffc72c;"></div>`,
          iconSize: [22, 22],
          iconAnchor: [11, 11]
        });

        const marker = L.marker([camp.lat, camp.lng], { 
          icon: customIcon,
          title: `หมุดที่ตั้ง ${camp.name}`,
          alt: `หมุดที่ตั้ง ${camp.name}`
        }).addTo(tuMap);
        marker.on('add', () => {
          if (marker._icon) {
            marker._icon.setAttribute('aria-label', `หมุดแผนที่ ${camp.name}`);
            marker._icon.setAttribute('role', 'button');
            marker._icon.setAttribute('tabindex', '0');
          }
        });
        marker.bindPopup(`
          <div style="font-family: sans-serif; padding: 6px;">
            <strong style="color: #c51944; font-size: 14px;">${camp.name}</strong><br/>
            <span style="font-size: 12px; color: #334155;">พื้นที่: ${camp.area} • นักศึกษา ${camp.students}</span><br/>
            <span style="font-size: 11px; color: #64748b;">${camp.locationDesc}</span>
          </div>
        `);
        marker.on('click', () => selectCampusCluster(idx));
        tuMarkers.push(marker);
      });

      for (let i = 0; i < campusCoordinates.length; i++) {
        for (let j = i + 1; j < campusCoordinates.length; j++) {
          const line = L.polyline([campusCoordinates[i], campusCoordinates[j]], {
            color: '#c51944',
            weight: 2,
            dashArray: '5, 8',
            opacity: 0.65
          }).addTo(tuMap);
          corridorLines.push(line);
        }
      }
    }

    function setMapTileStyle(style) {
      const btnStreet = document.getElementById('btnMapStyleStreet');
      const btnSat = document.getElementById('btnMapStyleSat');

      if (style === 'sat') {
        if (tuMap.hasLayer(window.tuTileStreet)) tuMap.removeLayer(window.tuTileStreet);
        window.tuTileSat.addTo(tuMap);
        if (btnStreet) btnStreet.classList.remove('active');
        if (btnSat) btnSat.classList.add('active');
      } else {
        if (tuMap.hasLayer(window.tuTileSat)) tuMap.removeLayer(window.tuTileSat);
        window.tuTileStreet.addTo(tuMap);
        if (btnStreet) btnStreet.classList.add('active');
        if (btnSat) btnSat.classList.remove('active');
      }
    }

    function resetMapView() {
      selectCampusCluster(4);
    }

    function selectCampusCluster(idx) {
      const btns = document.querySelectorAll('.cluster-select-btn');
      btns.forEach((b, i) => b.classList.toggle('active', i === idx));

      const data = CAMPUSES_DATA[idx];
      if (data) {
        document.getElementById('cLocation').textContent = data.locationDesc;
        document.getElementById('cArea').innerHTML = data.area;
        document.getElementById('cStudents').innerHTML = data.students;
        document.getElementById('cRole').textContent = data.role;
        document.getElementById('cFocus').textContent = data.focus;
        document.getElementById('currentGpsDisplay').innerHTML = `<i class="fa-solid fa-satellite"></i> ${data.lat.toFixed(4)}° N, ${data.lng.toFixed(4)}° E`;

        if (tuMap) {
          tuMap.flyTo([data.lat, data.lng], data.zoom, { duration: 1.4, easeLinearity: 0.25 });
          if (tuMarkers[idx]) {
            setTimeout(() => { tuMarkers[idx].openPopup(); }, 600);
          }
        }
      } else if (idx === 4 && tuMap) {
        const bounds = L.latLngBounds([
          [12.8, 99.2],
          [18.4, 101.1]
        ]);
        tuMap.flyToBounds(bounds, { padding: [50, 50], duration: 1.5 });
        tuMap.closePopup();
        document.getElementById('cLocation').textContent = "เครือข่าย 4 วิทยาเขตยุทธศาสตร์ทั่วประเทศ";
        document.getElementById('cArea').textContent = "2,791 ไร่";
        document.getElementById('cStudents').textContent = "42,850 คน";
        document.getElementById('cRole').textContent = "บูรณาการ 4 ภาค";
        document.getElementById('cFocus').textContent = "วิจัย • เทคโนโลยี • สังคม";
      }
    }

    // 5. Milestone Stepper Selector
    function setMilestoneStep(idx) {
      const nodes = document.querySelectorAll('.stepper-node');
      nodes.forEach((n, i) => n.classList.toggle('active', i === idx));

      const item = MILESTONES_DATA[idx];
      document.getElementById('mEventTitle').textContent = item.title;
      document.getElementById('mEventDesc').textContent = item.desc;
      document.getElementById('mEventStat').textContent = item.stat;
      document.getElementById('mEventLabel').textContent = item.lbl;
    }

    // 6. TU 2034 — เส้นทางบนแผนที่ศูนย์รังสิต + การ์ด 4 เสาหลักแบบซ้อนทับ (stacking cards)
    const PILLAR_PROGRESS = [
      { current: 72.4, target: 92.0, unit: 'คะแนน', metric: 'ดัชนีวิจัยระดับสากล', year: 'พ.ศ. 2577' },
      { current: 78.5, target: 95.0, unit: 'คะแนน', metric: 'หลักสูตรบูรณาการ AI', year: 'พ.ศ. 2577' },
      { current: 6200, target: 10000, unit: 'ทีม', metric: 'ทีมสตาร์ทอัพบ่มเพาะ', year: 'พ.ศ. 2577' },
      { current: 78.0, target: 100, unit: '%', metric: 'สัดส่วนพลังงานสะอาด', year: 'พ.ศ. 2573' }
    ];
    const PILLAR_PLACES = ['หอสมุดป๋วย อึ๊งภากรณ์', 'คณะวิทยาศาสตร์และเทคโนโลยี', 'ศูนย์ประชุมธรรมศาสตร์รังสิต', 'อุทยานการเรียนรู้ป๋วย 100 ปี'];
    const PILLAR_SHORT = ['วิจัยและนวัตกรรมระดับสากล', 'ทักษะแห่งอนาคตและ AI', '88 SANDBOX สตาร์ทอัพเพื่อสังคม', 'Net-Zero Campus 2030'];

    function fmtPillar(v, unit) {
      if (unit === 'ทีม') return Math.round(v).toLocaleString('th-TH');
      return Number(v).toFixed(1).replace(/\.0$/, '');
    }

    function renderPillarStack() {
      const stack = document.getElementById('tuPillarStack');
      if (!stack) return;
      stack.innerHTML = CIRCUIT_DATA.map((c, i) => {
        const d = PILLAR_PROGRESS[i];
        const pct = d.current / d.target * 100;
        return `
        <article class="tu-pillar-card" data-idx="${i}" style="--i:${i}" aria-labelledby="tuPillarTitle${i}">
          <header class="tu-pillar-head">
            <span class="tu-pillar-num">${i + 1}</span>
            <div class="tu-pillar-head-text">
              <div class="tu-pillar-tag">เสาหลักที่ ${i + 1} • ${PILLAR_PLACES[i]}</div>
              <h3 class="tu-pillar-title" id="tuPillarTitle${i}">${PILLAR_SHORT[i]}</h3>
            </div>
          </header>
          <div class="tu-pillar-body">
            <img class="tu-pillar-img" src="${c.img}" alt="" width="540" height="200" loading="lazy" decoding="async" onerror="this.style.display='none'" />
            <p class="tu-pillar-desc">${c.desc}</p>
            <figure class="tu-pillar-chart" aria-label="${d.metric}: ปัจจุบัน ${fmtPillar(d.current, d.unit)} จากเป้าหมาย ${fmtPillar(d.target, d.unit)} ${d.unit} (${pct.toFixed(1)}%)">
              <figcaption>${d.metric} <span>(${d.unit})</span></figcaption>
              <div class="tu-bar-row">
                <span class="tu-bar-label">ปัจจุบัน</span>
                <div class="tu-bar-track"><div class="tu-bar-fill" style="--w:${pct.toFixed(2)}%"></div></div>
                <span class="tu-bar-val">${fmtPillar(d.current, d.unit)}</span>
              </div>
              <div class="tu-bar-row tu-bar-row--target">
                <span class="tu-bar-label">เป้าหมาย ${d.year}</span>
                <div class="tu-bar-track"><div class="tu-bar-fill" style="--w:100%"></div></div>
                <span class="tu-bar-val">${fmtPillar(d.target, d.unit)}</span>
              </div>
              <div class="tu-pillar-pct"><b>${pct.toFixed(1)}%</b> ของเป้าหมาย • เหลืออีก ${fmtPillar(d.target - d.current, d.unit)} ${d.unit === '%' ? 'จุด%' : d.unit}</div>
            </figure>
          </div>
        </article>`;
      }).join('') + '<div class="tu-pillar-stack-end" aria-hidden="true"></div>';
    }

    // ความยาวเส้นทางสะสมถึงแต่ละจุด (คำนวณจาก path จริงใน SVG)
    let routeLens = null;
    function measureRoute() {
      const base = document.getElementById('tuRouteBase');
      if (!base || typeof base.getTotalLength !== 'function') return null;
      const svgNS = 'http://www.w3.org/2000/svg';
      const segs = ['M342 452 V300 H221 V268', 'V210 H443', 'H483 V369 H595', 'H620 V245 H540'];
      let d = '';
      const out = [];
      segs.forEach(seg => {
        d += (d ? ' ' : '') + seg;
        const tmp = document.createElementNS(svgNS, 'path');
        tmp.setAttribute('d', d);
        base.parentNode.appendChild(tmp);
        out.push(tmp.getTotalLength());
        tmp.remove();
      });
      return { nodes: out, total: base.getTotalLength() };
    }

    let routeActiveIdx = -1;
    let routeTicking = false;
    function requestRouteFrame() {
      if (routeTicking) return;
      routeTicking = true;
      requestAnimationFrame(() => { routeTicking = false; updateRouteProgress(); });
    }

    function updateRouteProgress() {
      const stack = document.getElementById('tuPillarStack');
      const active = document.getElementById('tuRouteActive');
      const walker = document.getElementById('tuRouteWalker');
      if (!stack || !active || !walker) return;
      if (!routeLens) routeLens = measureRoute();
      if (!routeLens) return;
      const cards = stack.querySelectorAll('.tu-pillar-card');
      if (!cards.length) return;

      // ระยะเลื่อนที่การ์ดแต่ละใบ "ติด" (stick) — คำนวณจากตำแหน่งในโฟลว์ปกติ
      const stackTop = stack.getBoundingClientRect().top;
      const scrolled = -stackTop;
      const marks = [];
      let y = 0;
      cards.forEach((card, i) => {
        const cs = getComputedStyle(card);
        const stickTop = parseFloat(cs.top) || 0;
        marks.push(y - stickTop);
        y += card.offsetHeight + (parseFloat(cs.marginBottom) || 0);
      });
      const approach = window.innerHeight * 0.7;          // ช่วงเดินจากประตูไปจุดที่ 1
      let p;                                               // -1 = ประตู, 0..3 = จุดที่ 1..4
      if (scrolled <= marks[0] - approach) p = -1;
      else if (scrolled < marks[0]) p = -1 + (scrolled - (marks[0] - approach)) / approach;
      else {
        p = cards.length - 1;
        for (let i = 0; i < cards.length - 1; i++) {
          if (scrolled < marks[i + 1]) { p = i + (scrolled - marks[i]) / (marks[i + 1] - marks[i]); break; }
        }
      }
      const L = routeLens.nodes;
      let len;
      if (p <= -1) len = 0;
      else if (p < 0) len = (p + 1) * L[0];
      else { const i = Math.min(Math.floor(p), L.length - 1); const f = p - i; len = i >= L.length - 1 ? L[L.length - 1] : L[i] + (L[i + 1] - L[i]) * f; }

      active.style.strokeDasharray = routeLens.total;
      active.style.strokeDashoffset = routeLens.total - len;
      const pt = document.getElementById('tuRouteBase').getPointAtLength(len);
      walker.setAttribute('transform', `translate(${pt.x.toFixed(1)} ${pt.y.toFixed(1)})`);

      const idx = p < -0.15 ? -1 : Math.min(cards.length - 1, Math.max(0, Math.round(p)));
      if (idx !== routeActiveIdx) {
        routeActiveIdx = idx;
        document.querySelectorAll('.tu-route-node').forEach((n, i) => {
          n.classList.toggle('active', i === idx);
          n.classList.toggle('done', idx >= 0 && i < idx);
        });
        cards.forEach((c, i) => {
          c.classList.toggle('is-active', i === idx);
          if (i <= idx) c.classList.add('is-revealed-bars');
        });
      }
    }

    // กดหมายเลขบนแผนที่ = เลื่อนไปยังการ์ดเสาหลักนั้น
    function selectCircuitNode(idx) {
      const stack = document.getElementById('tuPillarStack');
      const card = stack && stack.querySelectorAll('.tu-pillar-card')[idx];
      if (!card) return;
      let y = 0;
      const cards = stack.querySelectorAll('.tu-pillar-card');
      for (let i = 0; i < idx; i++) y += cards[i].offsetHeight + (parseFloat(getComputedStyle(cards[i]).marginBottom) || 0);
      const stickTop = parseFloat(getComputedStyle(card).top) || 0;
      const target = stack.getBoundingClientRect().top + window.pageYOffset + y - stickTop + 2;
      window.scrollTo({ top: target, behavior: 'smooth' });
    }

    function initPillarRoute() {
      renderPillarStack();
      routeLens = null;
      window.addEventListener('scroll', requestRouteFrame, { passive: true });
      window.addEventListener('resize', () => { routeLens = null; requestRouteFrame(); }, { passive: true });
      requestRouteFrame();
    }

    // 7. Budget Stream Drilldown & Interactive Chart Update
    let budgetChartInstance = null;

    function drilldownStream(idx) {
      const pills = document.querySelectorAll('.drilldown-pill');
      pills.forEach((p, i) => p.classList.toggle('active', i === idx));

      const s = STREAMS_DATA[idx];
      if (!s) return;

      document.getElementById('streamDetailBox').innerHTML = `
        <strong>${s.name} (${s.share} • ${s.amount}):</strong> ${s.desc}
      `;

      if (budgetChartInstance) {
        budgetChartInstance.data.datasets[0].label = `${s.name} (ล้านบาท)`;
        budgetChartInstance.data.datasets[0].data = s.data;
        budgetChartInstance.data.datasets[0].borderColor = s.color;
        budgetChartInstance.data.datasets[0].pointBackgroundColor = s.color;
        budgetChartInstance.data.datasets[0].backgroundColor = s.color.startsWith('#')
          ? s.color + '18'
          : 'rgba(197, 25, 68, 0.08)';

        const minVal = Math.min(...s.data);
        const maxVal = Math.max(...s.data);
        const pad = Math.max((maxVal - minVal) * 0.35, 100);
        budgetChartInstance.options.scales.y.min = Math.max(0, Math.floor((minVal - pad) / 100) * 100);
        budgetChartInstance.options.scales.y.max = Math.ceil((maxVal + pad) / 100) * 100;

        budgetChartInstance.update();
      }
    }

    // 8. Faculties TCAS Chart (Horizontal Dot/Lollipop Plot - Master Prompt v4 A5)
    let facultiesTcasChart = null;
    window.currentFacultyFilter = 'all';

    function initFacultiesTcasChart() {
      const ctx = document.getElementById('facultiesTcasChartCanvas');
      if (!ctx) return;

      const currentPillar = window.currentFacultyFilter || 'all';
      const list = currentPillar === 'all' 
        ? [...FACULTIES_DATA].sort((a, b) => parseFloat(b.cutoff) - parseFloat(a.cutoff))
        : [...FACULTIES_DATA].filter(f => f.pillar === currentPillar).sort((a, b) => parseFloat(b.cutoff) - parseFloat(a.cutoff));

      const labels = list.map(f => f.name);
      const data = list.map(f => parseFloat(f.cutoff));
      const colors = list.map(f => {
        if (f.pillar === 'med') return '#c51944';
        if (f.pillar === 'sci') return '#00857c';
        if (f.pillar === 'inter') return '#d97706';
        return '#1e3a8a';
      });

      // Plugin for drawing crisp cluster-colored circular dots at the lollipop tip
      const lollipopDotPlugin = {
        id: 'lollipopDotMarkers',
        afterDatasetsDraw(chart) {
          const { ctx: c } = chart;
          const meta = chart.getDatasetMeta(0);
          if (!meta || !meta.data) return;
          meta.data.forEach((element, index) => {
            const { x, y } = element.tooltipPosition();
            const color = colors[index] || '#c51944';
            c.save();
            c.beginPath();
            c.arc(x, y, 6.5, 0, 2 * Math.PI);
            c.fillStyle = color;
            c.fill();
            c.lineWidth = 2.5;
            c.strokeStyle = '#ffffff';
            c.stroke();
            c.restore();
          });
        }
      };

      // สร้างกราฟใหม่ทุกครั้งที่เปลี่ยนตัวกรอง เพื่อให้ tooltip / การคลิก / สีจุด ตรงกับรายการคณะที่กรองแล้ว
      if (facultiesTcasChart) {
        facultiesTcasChart.destroy();
        facultiesTcasChart = null;
      }
      const wrap = document.getElementById('facultiesChartWrapper');
      if (wrap) wrap.style.height = Math.max(220, list.length * 21 + 60) + 'px';
      if (wrap && wrap.style.display === 'none') return; // ซ่อนอยู่ (มุมมองการ์ด) — จะสร้างเมื่อกลับมามุมมองกราฟ

      facultiesTcasChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'คะแนนตัดต่ำสุด TCAS (รอบ 3 Admission)',
            data: data,
            backgroundColor: colors.map(c => c + 'aa'),
            borderRadius: 2,
            barThickness: 3,
            maxBarThickness: 3
          }]
        },
        plugins: [lollipopDotPlugin],
        options: {
          indexAxis: 'y',
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: 'rgba(11, 22, 59, 0.96)',
              titleFont: { size: 13, weight: 'bold' },
              bodyFont: { size: 12 },
              padding: 12,
              borderColor: 'rgba(255, 199, 44, 0.4)',
              borderWidth: 1,
              callbacks: {
                title: (items) => list[items[0].dataIndex].name,
                label: (item) => {
                  const fac = list[item.dataIndex];
                  return [
                    `คะแนนตัดต่ำสุด TCAS: ${fac.cutoff} / 100`,
                    `กลุ่มสาขา: ${fac.pillarName}`,
                    `อัตราการแข่งขัน: ${fac.accept}`,
                    `สายอาชีพ: ${fac.careers.substring(0, 42)}...`
                  ];
                },
                afterLabel: () => '👉 คลิกแท่ง/จุดเพื่อดูรายละเอียดฉบับเต็ม'
              }
            }
          },
          onClick: (evt, elements) => {
            if (elements && elements.length > 0) {
              const idx = elements[0].index;
              openFacultyModal(list[idx]);
            }
          },
          scales: {
            x: {
              min: 60,
              max: 85,
              ticks: {
                stepSize: 5,
                callback: (v) => v + ' คะแนน',
                color: '#64748b'
              },
              grid: { color: 'rgba(0, 0, 0, 0.06)' }
            },
            y: {
              ticks: {
                color: '#1e293b',
                font: { size: 11, weight: '600' }
              },
              grid: { display: false }
            }
          }
        }
      });
    }

    function setFacultiesView(mode) {
      const btnChart = document.getElementById('btnFacChartView');
      const btnGrid = document.getElementById('btnFacGridView');
      const chartWrapper = document.getElementById('facultiesChartWrapper');
      const gridWrapper = document.getElementById('facultiesGrid');

      if (mode === 'chart') {
        if (btnChart) btnChart.classList.add('active');
        if (btnGrid) btnGrid.classList.remove('active');
        if (chartWrapper) chartWrapper.style.display = 'block';
        if (gridWrapper) gridWrapper.style.display = 'none';
        initFacultiesTcasChart();
      } else {
        if (btnChart) btnChart.classList.remove('active');
        if (btnGrid) btnGrid.classList.add('active');
        if (chartWrapper) chartWrapper.style.display = 'none';
        if (gridWrapper) gridWrapper.style.display = 'grid';
      }
    }

    function renderFaculties(filter) {
      const container = document.getElementById('facultiesGrid');
      if (!container) return;
      container.innerHTML = '';
      const list = filter === 'all' ? FACULTIES_DATA : FACULTIES_DATA.filter(f => f.pillar === filter);
      list.forEach((fac) => {
        const card = document.createElement('div');
        card.className = 'faculty-item-card';
        card.onclick = () => openFacultyModal(fac);
        card.innerHTML = `
          <div class="fac-name">${fac.name}</div>
          <div class="fac-meta">
            <span>${fac.pillarName}</span>
            <span style="color: var(--tu-crimson); font-weight: 700;">TCAS: ${fac.cutoff}</span>
          </div>
        `;
        container.appendChild(card);
      });
    }

    function filterFaculties(pillar, btnEl) {
      window.currentFacultyFilter = pillar;
      const pills = document.querySelectorAll('.fac-pill');
      pills.forEach(p => p.classList.remove('active'));
      const activeBtn = btnEl || (typeof event !== 'undefined' && event && event.target ? event.target.closest('.fac-pill') : null) || document.querySelector(`.fac-pill[onclick*="'${pillar}'"]`);
      if (activeBtn) activeBtn.classList.add('active');
      renderFaculties(pillar);
      renderTcasTable(pillar);
      initFacultiesTcasChart();
    }

    // ตารางข้อมูล TCAS สร้างจากชุดข้อมูลเดียวกับกราฟ (ไม่ให้ตัวเลขขัดกัน)
    function renderTcasTable(filter) {
      const body = document.getElementById('tcasTableBody');
      if (!body) return;
      const list = (filter && filter !== 'all' ? FACULTIES_DATA.filter(f => f.pillar === filter) : [...FACULTIES_DATA])
        .sort((a, b) => parseFloat(b.cutoff) - parseFloat(a.cutoff));
      body.innerHTML = list.map(f => `<tr><td>${f.name}</td><td>${f.pillarName}</td><td>${parseFloat(f.cutoff).toFixed(2)}</td><td>${f.accept}</td></tr>`).join('');
    }

    let lastActiveFocusElement = null;
    let flourishTrapKeyHandler = null;
    let facultyTrapKeyHandler = null;

    function handleModalFocusTrap(modalEl, e, closeFn) {
      if (e.key === 'Escape') {
        closeFn();
        return;
      }
      if (e.key !== 'Tab') return;
      const focusables = modalEl.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (e.shiftKey) {
        if (document.activeElement === first) {
          last.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === last) {
          first.focus();
          e.preventDefault();
        }
      }
    }

    function openFacultyModal(fac) {
      lastActiveFocusElement = document.activeElement;
      document.getElementById('mFacPillar').textContent = fac.pillarName;
      document.getElementById('mFacTitle').textContent = fac.name;
      document.getElementById('mFacDesc').textContent = fac.desc;
      document.getElementById('mFacCutoff').textContent = fac.cutoff + ' / 100';
      document.getElementById('mFacAccept').textContent = fac.accept;
      document.getElementById('mFacCareers').textContent = fac.careers;
      const modal = document.getElementById('facultyModal');
      if (modal) {
        modal.style.display = 'flex';
        const closeBtn = modal.querySelector('.modal-close-btn');
        if (closeBtn) closeBtn.focus();
        facultyTrapKeyHandler = (e) => handleModalFocusTrap(modal, e, closeFacultyModal);
        document.addEventListener('keydown', facultyTrapKeyHandler);
      }
    }

    function closeFacultyModal() {
      const modal = document.getElementById('facultyModal');
      if (modal) {
        modal.style.display = 'none';
        if (facultyTrapKeyHandler) {
          document.removeEventListener('keydown', facultyTrapKeyHandler);
          facultyTrapKeyHandler = null;
        }
        if (lastActiveFocusElement && typeof lastActiveFocusElement.focus === 'function') {
          lastActiveFocusElement.focus();
        }
      }
    }

    // 9. TU 2034 Strategy Cockpit Calculator (A7 default sync & aria attributes)
    function updateCockpit() {
      const sliderR = document.getElementById('sliderResearch');
      const sliderS = document.getElementById('sliderSkills');
      const sliderG = document.getElementById('sliderGreen');
      const sliderH = document.getElementById('sliderHealth');
      if (!sliderR || !sliderS || !sliderG || !sliderH) return;

      const r = parseFloat(sliderR.value);
      const s = parseFloat(sliderS.value);
      const g = parseFloat(sliderG.value);
      const h = parseFloat(sliderH.value);

      document.getElementById('dispResearch').textContent = r + '%';
      document.getElementById('dispSkills').textContent = s + '%';
      document.getElementById('dispGreen').textContent = g + '%';
      document.getElementById('dispHealth').textContent = h + '%';

      sliderR.setAttribute('aria-valuenow', r);
      sliderR.setAttribute('aria-valuetext', r + '%');
      sliderS.setAttribute('aria-valuenow', s);
      sliderS.setAttribute('aria-valuetext', s + '%');
      sliderG.setAttribute('aria-valuenow', g);
      sliderG.setAttribute('aria-valuetext', g + '%');
      sliderH.setAttribute('aria-valuenow', h);
      sliderH.setAttribute('aria-valuetext', h + '%');

      const composite = (r * 0.3 + s * 0.25 + g * 0.25 + h * 0.2).toFixed(1);
      const scoreEl = document.getElementById('cockpitCompositeScore');
      if (scoreEl) scoreEl.textContent = composite;
    }

    // 10. Flourish Hub Modal & Live Visual Preview Engine
    let flourishModalChartInstance = null;

    function openFlourishHubModal() {
      lastActiveFocusElement = document.activeElement;
      const modal = document.getElementById('flourishHubModal');
      if (modal) {
        modal.style.display = 'flex';
        renderFlourishTabs();
        selectFlourishScene(0);
        const closeBtn = modal.querySelector('.modal-close-btn');
        if (closeBtn) closeBtn.focus();
        flourishTrapKeyHandler = (e) => handleModalFocusTrap(modal, e, closeFlourishHubModal);
        document.addEventListener('keydown', flourishTrapKeyHandler);
      }
    }

    function closeFlourishHubModal() {
      const modal = document.getElementById('flourishHubModal');
      if (modal) {
        modal.style.display = 'none';
        if (flourishTrapKeyHandler) {
          document.removeEventListener('keydown', flourishTrapKeyHandler);
          flourishTrapKeyHandler = null;
        }
        if (flourishModalChartInstance) {
          flourishModalChartInstance.destroy();
          flourishModalChartInstance = null;
        }
        if (lastActiveFocusElement && typeof lastActiveFocusElement.focus === 'function') {
          lastActiveFocusElement.focus();
        }
      }
    }

    function renderFlourishTabs() {
      const tabList = document.getElementById('flourishSidebarTabs');
      if (!tabList) return;
      tabList.innerHTML = '';
      FLOURISH_SCENES_DATA.forEach((scene, idx) => {
        const btn = document.createElement('button');
        btn.className = `flourish-tab-btn ${idx === 0 ? 'active' : ''}`;
        btn.onclick = () => selectFlourishScene(idx);
        btn.innerHTML = `
          <div class="flourish-tab-num">ฉากที่ ${scene.id}</div>
          <div class="flourish-tab-title">${scene.title.split('. ')[1] || scene.title}</div>
          <div class="flourish-tab-template"><i class="fa-solid fa-chart-simple" style="font-size: 0.65rem;"></i> ${scene.template}</div>
        `;
        tabList.appendChild(btn);
      });
    }

    function renderFlourishModalLiveChart(idx) {
      const canvas = document.getElementById('flourishModalChartCanvas');
      if (!canvas) return;

      if (flourishModalChartInstance) {
        flourishModalChartInstance.destroy();
        flourishModalChartInstance = null;
      }

      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      let config = null;

      if (idx === 0) {
        // Scene 1: Line Chart (Student Growth 90 Years)
        const years = ['2477', '2488', '2495', '2508', '2519', '2529', '2539', '2549', '2559', '2567'];
        const students = [7094, 9800, 4200, 11500, 15800, 21000, 27500, 33200, 39400, 42850];
        const notes = [
          'ตลาดวิชารุ่นแรก (7,094 คน)',
          'สงครามโลกครั้งที่ 2',
          'ปรับสู่ระบบปิด',
          'ขยายสายสังคมศาสตร์',
          'ยุคประชาธิปไตย',
          'สถาปนาศูนย์รังสิต',
          'ขยายพัทยา-ลำปาง',
          'ขยายหลักสูตรนานาชาติ',
          'ศูนย์กลางนวัตกรรม',
          'ปัจจุบัน 4 ศูนย์ 42,850 คน'
        ];
        config = {
          type: 'line',
          data: {
            labels: years,
            datasets: [{
              label: 'จำนวนนักศึกษาทั้งหมด (คน)',
              data: students,
              borderColor: '#c51944',
              backgroundColor: 'rgba(197, 25, 68, 0.12)',
              fill: true,
              tension: 0.35,
              borderWidth: 3,
              pointRadius: 5,
              pointBackgroundColor: '#ffffff',
              pointBorderColor: '#c51944',
              pointBorderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => `นักศึกษา: ${ctx.parsed.y.toLocaleString()} คน`,
                  afterLabel: ctx => `เหตุการณ์: ${notes[ctx.dataIndex] || ''}`
                }
              }
            },
            scales: {
              y: {
                beginAtZero: true,
                ticks: { callback: v => (v / 1000).toFixed(0) + 'k' }
              }
            }
          }
        };
      } else if (idx === 1) {
        // Scene 2: 4 Campuses — จำนวนนักศึกษา (แกนเดียว) พื้นที่แสดงใน tooltip
        const campusArea = [1757, 104, 364, 566];
        config = {
          type: 'bar',
          data: {
            labels: ['ศูนย์รังสิต', 'ศูนย์ท่าพระจันทร์', 'ศูนย์ลำปาง', 'ศูนย์พัทยา (EEC)'],
            datasets: [{
              label: 'จำนวนนักศึกษา (คน)',
              data: [31500, 6310, 3120, 1920],
              backgroundColor: ['#c51944', '#a6d2e6', '#ffc72c', '#00857c'],
              borderRadius: 6,
              maxBarThickness: 90
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => `นักศึกษา: ${ctx.parsed.y.toLocaleString()} คน (${(ctx.parsed.y / 42850 * 100).toFixed(1)}%)`,
                  afterLabel: ctx => `พื้นที่: ${campusArea[ctx.dataIndex].toLocaleString()} ไร่`
                }
              }
            },
            scales: {
              y: {
                beginAtZero: true,
                title: { display: true, text: 'นักศึกษา (คน)' },
                ticks: { callback: v => v.toLocaleString() }
              }
            }
          }
        };
      } else if (idx === 2) {
        // Scene 3: Faculty Hierarchy & Student Count
        config = {
          type: 'bar',
          data: {
            labels: [
              'พาณิชย์ฯ (TBS)',
              'นิติศาสตร์',
              'วิศวกรรมศาสตร์',
              'วิทยาศาสตร์ฯ',
              'ศิลปศาสตร์',
              'เศรษฐศาสตร์',
              'รัฐศาสตร์',
              'วารสารศาสตร์',
              'สหเวชศาสตร์',
              'แพทยศาสตร์'
            ],
            datasets: [{
              label: 'จำนวนนักศึกษา (คน)',
              data: [4950, 3800, 3100, 2800, 2600, 2200, 2100, 1950, 1600, 1250],
              backgroundColor: [
                '#c51944', '#c51944', '#0284c7', '#0284c7', '#c51944',
                '#c51944', '#c51944', '#c51944', '#10b981', '#10b981'
              ],
              borderRadius: 6
            }]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => `นักศึกษา: ${ctx.parsed.x.toLocaleString()} คน`
                }
              }
            },
            scales: {
              x: {
                beginAtZero: true,
                ticks: { callback: v => v.toLocaleString() }
              }
            }
          }
        };
      } else if (idx === 3) {
        // Scene 4: Gender Diversity — ตัวเลขเดียวกับหัวข้อ 04
        config = {
          type: 'bar',
          data: {
            labels: ['สังคมศาสตร์-มนุษยศาสตร์', 'วิทยาศาสตร์และเทคโนโลยี', 'วิทยาศาสตร์สุขภาพ', 'นานาชาติ & บูรณาการ'],
            datasets: [
              {
                label: 'หญิง (Female %)',
                data: [64.2, 53.8, 71.5, 60.8],
                backgroundColor: '#c51944'
              },
              {
                label: 'ชาย (Male %)',
                data: [35.8, 46.2, 28.5, 39.2],
                backgroundColor: '#0b163b'
              }
            ]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top' },
              tooltip: {
                callbacks: {
                  label: ctx => `${ctx.dataset.label}: ${ctx.parsed.x}%`
                }
              }
            },
            scales: {
              x: {
                stacked: true,
                min: 0,
                max: 100,
                ticks: { callback: v => v + '%' }
              },
              y: { stacked: true }
            }
          }
        };
      } else if (idx === 4) {
        // Scene 5: Campus Migration Eras
        config = {
          type: 'line',
          data: {
            labels: ['พ.ศ. 2500', 'พ.ศ. 2530', 'พ.ศ. 2545', 'พ.ศ. 2567 (ปัจจุบัน)'],
            datasets: [
              {
                label: 'ศูนย์ท่าพระจันทร์ (%)',
                data: [100.0, 68.0, 22.0, 14.8],
                borderColor: '#c51944',
                backgroundColor: 'rgba(197, 25, 68, 0.08)',
                tension: 0.3,
                borderWidth: 3,
                pointRadius: 5
              },
              {
                label: 'ศูนย์รังสิต (%)',
                data: [0.0, 32.0, 70.0, 73.5],
                borderColor: '#0284c7',
                backgroundColor: 'rgba(2, 132, 199, 0.08)',
                tension: 0.3,
                borderWidth: 3,
                pointRadius: 5
              },
              {
                label: 'ศูนย์ลำปาง (%)',
                data: [0.0, 0.0, 5.0, 7.2],
                borderColor: '#f59e0b',
                tension: 0.3,
                borderWidth: 2,
                pointRadius: 4
              },
              {
                label: 'ศูนย์พัทยา (%)',
                data: [0.0, 0.0, 3.0, 4.5],
                borderColor: '#10b981',
                tension: 0.3,
                borderWidth: 2,
                pointRadius: 4
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top' },
              tooltip: {
                callbacks: {
                  label: ctx => `${ctx.dataset.label}: ${ctx.parsed.y}%`
                }
              }
            },
            scales: {
              y: {
                max: 100,
                beginAtZero: true,
                ticks: { callback: v => v + '%' }
              }
            }
          }
        };
      } else if (idx === 5) {
        // Scene 6: 5-Year Budget Streams — แท่งซ้อน 5 แหล่งรายได้ ความสูงรวม = งบประมาณรวม
        const streams = STREAMS_DATA.slice(1);
        const streamColors = ['#0284c7', '#c51944', '#f59e0b', '#7c3aed', '#00857c'];
        config = {
          type: 'bar',
          data: {
            labels: ['2563', '2564', '2565', '2566', '2567'],
            datasets: streams.map((st, i) => ({
              label: st.name.split(' (')[0],
              data: st.data,
              backgroundColor: streamColors[i],
              maxBarThickness: 70
            }))
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: 'index', intersect: false },
            plugins: {
              legend: { position: 'top', labels: { boxWidth: 12, font: { size: 11 } } },
              tooltip: {
                callbacks: {
                  label: ctx => `${ctx.dataset.label}: ${ctx.parsed.y.toLocaleString()} ล้านบาท`,
                  footer: items => `รวมทุกด้าน: ${STREAMS_DATA[0].data[items[0].dataIndex].toLocaleString()} ล้านบาท`
                }
              }
            },
            scales: {
              x: { stacked: true },
              y: {
                stacked: true,
                beginAtZero: true,
                ticks: { callback: v => (v / 1000).toFixed(0) + 'k' }
              }
            }
          }
        };
      } else if (idx === 6) {
        // Scene 7: Rankings Progression
        config = {
          type: 'line',
          data: {
            labels: ['2018', '2019', '2020', '2021', '2022', '2023', '2024'],
            datasets: [
              {
                label: 'QS Asia University Rank (อันดับเอเชีย)',
                data: [137, 134, 119, 111, 107, 98, 92],
                borderColor: '#c51944',
                backgroundColor: 'rgba(197, 25, 68, 0.1)',
                borderWidth: 3.5,
                pointRadius: 6,
                pointBackgroundColor: '#ffffff',
                pointBorderColor: '#c51944',
                pointBorderWidth: 2.5,
                tension: 0.3
              },
              {
                label: 'TBS Business & Management (อันดับโลก)',
                data: [250, 225, 210, 195, 180, 160, 140],
                borderColor: '#0284c7',
                borderWidth: 2.5,
                borderDash: [5, 5],
                pointRadius: 5,
                tension: 0.3
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top' },
              tooltip: {
                callbacks: {
                  label: ctx => `${ctx.dataset.label}: อันดับที่ ${ctx.parsed.y}`
                }
              }
            },
            scales: {
              y: {
                reverse: true,
                min: 60,
                max: 270,
                title: { display: true, text: 'อันดับ Rank (ยิ่งน้อยยิ่งสูง)' }
              }
            }
          }
        };
      } else if (idx === 7) {
        // Scene 8: SDG Radar
        config = {
          type: 'radar',
          data: {
            labels: [
              'SDG 11: เมืองยั่งยืน (Top 10)',
              'SDG 4: การศึกษาเท่าเทียม',
              'SDG 7: พลังงานสะอาด (แผน 15 MW)',
              'SDG 17: หุ้นส่วนความร่วมมือ',
              'SDG 3: สุขภาพและสุขภาวะ',
              'SDG 13: รับมือภูมิอากาศ'
            ],
            datasets: [
              {
                label: 'คะแนน ม.ธรรมศาสตร์',
                data: [98.4, 92.8, 91.5, 90.4, 88.6, 87.2],
                borderColor: '#10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.25)',
                pointBackgroundColor: '#10b981',
                borderWidth: 2.5,
                pointRadius: 4
              },
              {
                label: 'เกณฑ์ระดับโลก (Benchmark = 90)',
                data: [90.0, 90.0, 90.0, 90.0, 90.0, 90.0],
                borderColor: '#94a3b8',
                borderDash: [4, 4],
                backgroundColor: 'rgba(148, 163, 184, 0.08)',
                borderWidth: 1.5,
                pointRadius: 0
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              r: {
                min: 75,
                max: 100,
                ticks: { stepSize: 5 }
              }
            },
            plugins: {
              legend: { position: 'top' }
            }
          }
        };
      } else if (idx === 8) {
        // Scene 9: Thammasat Hospital — ผู้ป่วยนอก (แกนเดียว)
        config = {
          type: 'bar',
          data: {
            labels: ['2530', '2540', '2550', '2560', '2564', '2567'],
            datasets: [{
              label: 'ผู้ป่วยนอก OPD (คน/ปี)',
              data: [50000, 210000, 520000, 980000, 1250000, 1480000],
              backgroundColor: '#0284c7',
              borderRadius: 4,
              maxBarThickness: 70
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => `ผู้ป่วยนอก: ${ctx.parsed.y.toLocaleString()} คน/ปี`
                }
              }
            },
            scales: {
              y: {
                beginAtZero: true,
                title: { display: true, text: 'ผู้ป่วยนอก (คน/ปี)' },
                ticks: { callback: v => (v / 1000000).toFixed(1) + 'M' }
              }
            }
          }
        };
      } else if (idx === 9) {
        // Scene 10: Centennial Strategic Pillars Progress
        config = {
          type: 'bar',
          data: {
            labels: [
              'Pillar 1: วิจัยสากล (Top 100 QS)',
              'Pillar 2: ทักษะ AI (AI Pedagogy 100%)',
              'Pillar 3: 88 SANDBOX (10,000 ทีม)',
              'Pillar 4: Net-Zero Campus 2030'
            ],
            datasets: [
              {
                label: 'ระดับความสำเร็จปัจจุบัน (Current %)',
                data: [72.4, 78.5, 62.0, 78.0],
                backgroundColor: '#0284c7',
                borderRadius: 4
              },
              {
                label: 'เป้าหมาย 100 ปี TU 2034 (Target %)',
                data: [92.0, 95.0, 100.0, 100.0],
                backgroundColor: '#c51944',
                borderRadius: 4
              }
            ]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top' },
              tooltip: {
                callbacks: {
                  label: ctx => `${ctx.dataset.label}: ${ctx.parsed.x}%`
                }
              }
            },
            scales: {
              x: {
                max: 100,
                beginAtZero: true,
                ticks: { callback: v => v + '%' }
              }
            }
          }
        };
      }

      if (config) {
        flourishModalChartInstance = new Chart(ctx, config);
      }
    }

    function selectFlourishScene(idx) {
      const tabs = document.querySelectorAll('.flourish-tab-btn');
      tabs.forEach((t, i) => t.classList.toggle('active', i === idx));

      const s = FLOURISH_SCENES_DATA[idx];
      if (!s) return;

      const content = document.getElementById('flourishDetailPane');
      if (!content) return;

      const tableHeaderHtml = s.tableHeaders.map(h => `<th>${h}</th>`).join('');
      const tableRowsHtml = s.tableSample.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('');
      const highlightsHtml = s.highlights.map(h => `<li><i class="fa-solid fa-check-circle" style="color: var(--tu-crimson); margin-top: 3px;"></i><span>${h}</span></li>`).join('');

      content.innerHTML = `
        <div class="flourish-detail-badge">${s.category} • ${s.badge}</div>
        <h3 class="flourish-detail-title">${s.title}</h3>
        <p class="flourish-detail-desc">${s.desc}</p>

        <!-- ACTION TOOLBAR: DOWNLOAD BUTTONS & FLOURISH TEMPLATE -->
        <div class="flourish-actions-toolbar">
          <a href="flourish_data/${s.csv}" download="${s.csv}" class="flourish-action-btn flourish-btn-primary" title="ดาวน์โหลดไฟล์ CSV นี้">
            <i class="fa-solid fa-file-arrow-down"></i>
            <span>ดาวน์โหลด CSV: <strong>${s.csv}</strong></span>
          </a>
          ${s.secondaryCsv ? `
          <a href="flourish_data/${s.secondaryCsv}" download="${s.secondaryCsv}" class="flourish-action-btn flourish-btn-secondary" title="ดาวน์โหลดชุดข้อมูลเสริม">
            <i class="fa-solid fa-download"></i>
            <span>${s.secondaryLabel}</span>
          </a>` : ''}
          <a href="${s.templateUrl}" target="_blank" rel="noopener noreferrer" class="flourish-action-btn flourish-btn-outline" title="เปิดเทมเพลตบน Flourish Studio">
            <i class="fa-solid fa-arrow-up-right-from-square"></i>
            <span>เปิดเทมเพลต <strong>${s.template}</strong> บน Flourish Studio</span>
          </a>
        </div>

        <!-- LIVE INTERACTIVE VISUAL PREVIEW -->
        <div class="flourish-preview-box">
          <div class="flourish-preview-header">
            <div class="flourish-preview-title">
              <i class="fa-solid fa-chart-line" style="color: var(--tu-crimson);"></i>
              <span>พรีวิวการแสดงผลชาร์ตสด (Live Interactive Visual Preview)</span>
            </div>
            <span class="flourish-template-pill">
              <i class="fa-solid fa-shapes"></i> Flourish Template: ${s.template}
            </span>
          </div>
          <div class="flourish-chart-stage">
            <canvas id="flourishModalChartCanvas"></canvas>
          </div>
        </div>

        <!-- 3-STEP GUIDE ON HOW TO UPLOAD TO FLOURISH -->
        <div class="flourish-guide-card">
          <div class="flourish-guide-title">
            <i class="fa-solid fa-wand-magic-sparkles"></i>
            <span>วิธีนำเข้าไฟล์ CSV ใน Flourish Studio (เพียง 3 ขั้นตอนง่ายๆ)</span>
          </div>
          <div class="flourish-guide-steps">
            <div class="flourish-step-item">
              <div class="flourish-step-num">1</div>
              <div class="flourish-step-text"><strong>ดาวน์โหลด CSV:</strong> กดปุ่มสีแดงด้านบนเพื่อบันทึกไฟล์ <code>${s.csv}</code> ลงในคอมพิวเตอร์ของคุณ</div>
            </div>
            <div class="flourish-step-item">
              <div class="flourish-step-num">2</div>
              <div class="flourish-step-text"><strong>เปิดเทมเพลต:</strong> ไปที่ Flourish Studio หรือกดปุ่ม <em>เปิดเทมเพลต</em> ด้านบน แล้วคลิก <em>+ New visualisation</em></div>
            </div>
            <div class="flourish-step-item">
              <div class="flourish-step-num">3</div>
              <div class="flourish-step-text"><strong>อัปโหลดข้อมูล:</strong> กดแท็บ <em>Data</em> ด้านบน > คลิก <em>Upload data file</em> แล้วเลือกไฟล์ CSV — กราฟสร้างเสร็จ 100%!</div>
            </div>
          </div>
        </div>

        <!-- INSIGHTS & FINDINGS -->
        <div class="flourish-insights-box">
          <div class="flourish-insights-title">
            <i class="fa-solid fa-lightbulb" style="color: #f59e0b;"></i>
            <span>ข้อค้นพบและสาระสำคัญจากข้อมูลชุดนี้ (Key Findings &amp; Story Arc)</span>
          </div>
          <ul class="flourish-highlights-list">
            ${highlightsHtml}
          </ul>
        </div>

        <!-- DATA TABLE PREVIEW -->
        <div class="flourish-table-container">
          <div class="flourish-table-header">
            <div style="font-weight: 700; color: #1e293b; font-size: 0.85rem;">
              <i class="fa-solid fa-table" style="color: #0284c7; margin-right: 6px;"></i>
              ตัวอย่างข้อมูลในไฟล์ CSV (Preview — <code>${s.csv}</code>)
            </div>
            <span style="font-size: 0.74rem; color: #64748b;">แสดง ${s.tableSample.length} แถวตัวอย่าง</span>
          </div>
          <div style="overflow-x: auto;">
            <table class="flourish-data-table">
              <thead><tr>${tableHeaderHtml}</tr></thead>
              <tbody>${tableRowsHtml}</tbody>
            </table>
          </div>
        </div>
      `;

      // Render the live chart preview on the new canvas!
      renderFlourishModalLiveChart(idx);
    }

        // 11. Chart.js Initializations
    let campusDistChart = null;

    // Mobile Nav Drawer Handlers
    function toggleMobileNav() {
      const drawer = document.getElementById('mobileNavDrawer');
      const backdrop = document.getElementById('mobileNavBackdrop');
      if (drawer && backdrop) {
        const isOpen = drawer.classList.contains('open');
        if (isOpen) {
          closeMobileNav();
        } else {
          drawer.classList.add('open');
          backdrop.classList.add('open');
          document.body.style.overflow = 'hidden';
        }
      }
    }

    function closeMobileNav() {
      const drawer = document.getElementById('mobileNavDrawer');
      const backdrop = document.getElementById('mobileNavBackdrop');
      if (drawer && backdrop) {
        drawer.classList.remove('open');
        backdrop.classList.remove('open');
        document.body.style.overflow = '';
      }
    }

    // Topic 08 Green Sustainability Chart Switcher
    let greenChartInstance = null;
    function initGreenSustainabilityChart() {
      const ctx = document.getElementById('greenSustainabilityCanvas');
      if (!ctx) return;
      if (greenChartInstance) { greenChartInstance.destroy(); greenChartInstance = null; }

      // ข้อมูลสอดคล้องกับตัวเลขในหน้า: ติดตั้งแล้ว 5 MW (Bangkok Post) → 6.8 MW ปี 2566 (อบก./TGO)
      // → แผนยุทธศาสตร์ 15 MW → เป้าหมาย 25 MW ปี 2030 (ตามตารางข้อมูล)
      const labels = ['ติดตั้งแล้ว (2561)', 'ติดตั้งแล้ว (2566)', 'แผนยุทธศาสตร์', 'เป้าหมาย 2030'];
      const values = [5, 6.8, 15, 25];
      const isPlan = [false, false, true, true];
      greenChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
          labels,
          datasets: [{
            label: 'กำลังผลิตโซลาร์เซลล์ (MW)',
            data: values,
            backgroundColor: isPlan.map(p => p ? 'rgba(16, 185, 129, 0.35)' : 'rgba(16, 185, 129, 0.9)'),
            borderColor: '#10b981',
            borderWidth: isPlan.map(p => p ? 2 : 0),
            borderDash: [4, 3],
            borderRadius: 6,
            maxBarThickness: 64
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: (c) => `${c.parsed.y} MW ${isPlan[c.dataIndex] ? '(แผน/เป้าหมาย)' : '(ติดตั้งแล้ว)'}`
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              max: 30,
              title: { display: true, text: 'เมกะวัตต์ (MW)', color: '#94a3b8' },
              ticks: { color: '#94a3b8', callback: (v) => v + ' MW' },
              grid: { color: 'rgba(255, 255, 255, 0.08)' }
            },
            x: {
              ticks: { color: '#ffffff', font: { family: 'Prompt' } },
              grid: { display: false }
            }
          }
        }
      });
    }

    function switchGreenVisual(mode) {
      const btnEnergy = document.getElementById('btnGreenEnergy');
      const btnRadar = document.getElementById('btnGreenRadar');
      const ctx = document.getElementById('greenSustainabilityCanvas');
      if (!ctx || typeof Chart === 'undefined') return;
      if (btnEnergy) { btnEnergy.classList.toggle('active', mode !== 'radar'); btnEnergy.setAttribute('aria-pressed', mode !== 'radar'); }
      if (btnRadar) { btnRadar.classList.toggle('active', mode === 'radar'); btnRadar.setAttribute('aria-pressed', mode === 'radar'); }
      if (greenChartInstance) { greenChartInstance.destroy(); greenChartInstance = null; }

      if (mode === 'radar') {
        greenChartInstance = new Chart(ctx, {
          type: 'radar',
          data: {
            labels: [
              'มรดก & ศิลปวัฒนธรรม',
              'อาคารเขียว & พลังงาน',
              'ขนส่งคาร์บอนต่ำ (EV)',
              'พื้นที่สีเขียว & สวนป๋วย'
            ],
            datasets: [{
              label: 'คะแนนองค์ประกอบ SDG 11 (เต็ม 100)',
              data: [99.2, 97.8, 98.6, 98.0],
              backgroundColor: 'rgba(16, 185, 129, 0.35)',
              borderColor: '#10b981',
              borderWidth: 2.5,
              pointBackgroundColor: '#ffc72c',
              pointRadius: 5
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'top',
                labels: { color: '#ffffff', font: { family: 'Prompt', size: 12 } }
              },
              tooltip: { callbacks: { label: (c) => `${c.label}: ${c.parsed.r} / 100` } }
            },
            scales: {
              r: {
                min: 0,
                max: 100,
                ticks: { stepSize: 25, color: '#94a3b8', backdropColor: 'transparent' },
                pointLabels: { color: '#ffffff', font: { family: 'Prompt', size: 11 } },
                grid: { color: 'rgba(255, 255, 255, 0.15)' },
                angleLines: { color: 'rgba(255, 255, 255, 0.2)' }
              }
            }
          }
        });
      } else {
        initGreenSustainabilityChart();
      }
    }

    // Topic 09 Hospital Service Capacity Chart Switcher
    let hospitalChartInstance = null;
    const HOSPITAL_YEARS = ['2562', '2563', '2564 (วิกฤตโควิด)', '2565', '2566', '2567'];
    const HOSPITAL_OPD = [1050000, 1180000, 1320000, 1380000, 1420000, 1480000]; // ครั้ง/ปี
    const HOSPITAL_IPD = [38000, 42000, 49000, 51000, 54000, 58400];             // ราย/ปี

    function initHospitalCapacityChart(mode) {
      const ctx = document.getElementById('hospitalCapacityCanvas');
      if (!ctx || typeof Chart === 'undefined') return;
      if (hospitalChartInstance) { hospitalChartInstance.destroy(); hospitalChartInstance = null; }
      const isIpd = mode === 'ipd';
      const data = isIpd ? HOSPITAL_IPD : HOSPITAL_OPD;
      const color = isIpd ? '#0b163b' : '#c51944';
      const unit = isIpd ? 'ราย' : 'คน';

      hospitalChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: HOSPITAL_YEARS,
          datasets: [{
            label: isIpd ? 'ผู้ป่วยใน IPD (ราย/ปี)' : 'ผู้ป่วยนอก OPD (คน/ปี)',
            data,
            borderColor: color,
            backgroundColor: isIpd ? 'rgba(11, 22, 59, 0.10)' : 'rgba(197, 25, 68, 0.12)',
            borderWidth: 3,
            fill: true,
            tension: 0.35,
            pointBackgroundColor: color,
            pointRadius: 5,
            pointHoverRadius: 7
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          interaction: { mode: 'index', intersect: false },
          plugins: {
            legend: {
              position: 'top',
              labels: { color: '#0f172a', font: { family: 'Prompt', size: 12 } }
            },
            tooltip: {
              callbacks: {
                label: (c) => `${c.dataset.label.split(' (')[0]}: ${c.parsed.y.toLocaleString()} ${unit}`
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                color: '#64748b',
                callback: (v) => isIpd ? (v / 1000) + 'k' : (v / 1000000).toFixed(1) + 'M'
              },
              grid: { color: 'rgba(0, 0, 0, 0.05)' }
            },
            x: {
              ticks: { color: '#334155', font: { family: 'Prompt' } },
              grid: { display: false }
            }
          }
        }
      });
    }

    function switchHospitalVisual(mode) {
      const btnTrend = document.getElementById('btnHospTrend');
      const btnIpd = document.getElementById('btnHospBeds');
      const isIpd = mode === 'ipd';
      if (btnTrend) { btnTrend.classList.toggle('active', !isIpd); btnTrend.setAttribute('aria-pressed', !isIpd); }
      if (btnIpd) { btnIpd.classList.toggle('active', isIpd); btnIpd.setAttribute('aria-pressed', isIpd); }
      initHospitalCapacityChart(isIpd ? 'ipd' : 'opd');
    }

        function initCharts() {
      // Budget 5-Year Chart (Topic 06 - Interactive Multi-Stream)
      const ctxBudget = document.getElementById('budgetChartCanvas');
      if (ctxBudget) {
        budgetChartInstance = new Chart(ctxBudget, {
          type: 'line',
          data: {
            labels: ['2563', '2564', '2565', '2566', '2567'],
            datasets: [{
              label: 'งบประมาณรวมทุกด้าน (ล้านบาท)',
              data: STREAMS_DATA[0].data,
              borderColor: '#c51944',
              backgroundColor: 'rgba(197, 25, 68, 0.08)',
              borderWidth: 3,
              fill: true,
              tension: 0.35,
              pointBackgroundColor: '#c51944',
              pointRadius: 6,
              pointHoverRadius: 8
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                display: true,
                position: 'top',
                labels: { color: '#0f172a', font: { family: 'Prompt', size: 12 } }
              },
              tooltip: {
                callbacks: {
                  label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y.toLocaleString()} ล้านบาท`
                }
              }
            },
            scales: {
              y: {
                min: 12000,
                max: 16000,
                ticks: { callback: (v) => v.toLocaleString() + ' ลบ.' },
                grid: { color: 'rgba(0, 0, 0, 0.05)' }
              },
              x: { grid: { display: false } }
            }
          }
        });
      }

      // Demographic Group Chart (Topic 04)
      const ctxGender = document.getElementById('genderGroupChartCanvas');
      if (ctxGender) {
        new Chart(ctxGender, {
          type: 'bar',
          data: {
            labels: ['สังคมศาสตร์', 'วิทย์-เทคโนโลยี', 'วิทยาศาสตร์สุขภาพ', 'วิทยาลัยนานาชาติ'],
            datasets: [
              {
                label: 'หญิง (%)',
                data: [64.2, 53.8, 71.5, 60.8],
                backgroundColor: '#ec4899',
                borderRadius: 4,
                maxBarThickness: 90
              },
              {
                label: 'ชาย (%)',
                data: [35.8, 46.2, 28.5, 39.2],
                backgroundColor: '#3b82f6',
                borderRadius: 4,
                maxBarThickness: 90
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top' },
              tooltip: {
                callbacks: {
                  label: (ctx) => {
                    const totals = [19200, 11450, 7800, 4400];
                    const n = Math.round(totals[ctx.dataIndex] * ctx.parsed.y / 100);
                    return `${ctx.dataset.label}: ${ctx.parsed.y}% (≈ ${n.toLocaleString()} คน)`;
                  }
                }
              }
            },
            scales: {
              y: {
                stacked: true,
                min: 0,
                max: 100,
                ticks: { callback: (v) => v + '%' },
                grid: { color: 'rgba(0,0,0,0.05)' }
              },
              x: { stacked: true, grid: { display: false } }
            }
          }
        });
      }

      // Campus Multi-Era Distribution Chart (Topic 05)
      const ctxDist = document.getElementById('campusDistributionCanvas');
      if (ctxDist) {
        campusDistChart = new Chart(ctxDist, {
          type: 'bar',
          data: {
            labels: ['พ.ศ. 2500', 'พ.ศ. 2530', 'พ.ศ. 2545', 'พ.ศ. 2567 (ปัจจุบัน)'],
            datasets: [
              {
                label: 'ท่าพระจันทร์ (%)',
                data: [100, 68, 22, 14.8],
                backgroundColor: '#a6d2e6',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              },
              {
                label: 'ศูนย์รังสิต (%)',
                data: [0, 32, 70, 73.5],
                backgroundColor: '#c51944',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              },
              {
                label: 'ศูนย์ลำปาง (%)',
                data: [0, 0, 5, 7.2],
                backgroundColor: '#ffc72c',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              },
              {
                label: 'ศูนย์พัทยา (%)',
                data: [0, 0, 3, 4.5],
                backgroundColor: '#00857c',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top', labels: { color: '#ffffff' } },
              tooltip: {
                callbacks: {
                  label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y}%`
                }
              }
            },
            scales: {
              x: { stacked: true, grid: { display: false }, ticks: { color: '#cbd5e1' } },
              y: { stacked: true, min: 0, max: 100, ticks: { callback: (v) => v + '%', color: '#cbd5e1' }, grid: { color: 'rgba(255,255,255,0.08)' } }
            }
          }
        });
      }
    }

    function setDistributionEra(mode, btnEl) {
      const btns = document.querySelectorAll('.era-pill-btn');
      btns.forEach(b => b.classList.remove('active'));
      const activeBtn = btnEl || (typeof event !== 'undefined' && event && event.target ? event.target.closest('.era-pill-btn') : null) || document.querySelector(`.era-pill-btn[onclick*="'${mode}'"]`);
      if (activeBtn) activeBtn.classList.add('active');

      if (!campusDistChart) return;
      const thickness = mode === '2567' ? 36 : 28;
      campusDistChart.data.datasets.forEach(ds => {
        ds.barThickness = thickness;
        ds.maxBarThickness = thickness + 4;
      });
      if (mode === '2567') {
        campusDistChart.data.labels = ['พ.ศ. 2567 (ปัจจุบัน)'];
        campusDistChart.data.datasets[0].data = [14.8];
        campusDistChart.data.datasets[1].data = [73.5];
        campusDistChart.data.datasets[2].data = [7.2];
        campusDistChart.data.datasets[3].data = [4.5];
      } else {
        campusDistChart.data.labels = ['พ.ศ. 2500', 'พ.ศ. 2530', 'พ.ศ. 2545', 'พ.ศ. 2567 (ปัจจุบัน)'];
        campusDistChart.data.datasets[0].data = [100, 68, 22, 14.8];
        campusDistChart.data.datasets[1].data = [0, 32, 70, 73.5];
        campusDistChart.data.datasets[2].data = [0, 0, 5, 7.2];
        campusDistChart.data.datasets[3].data = [0, 0, 3, 4.5];
      }
      campusDistChart.update();
    }


    // ==========================================================================
    // SCROLL-TRIGGERED ANIMATED COUNTERS (IntersectionObserver with Easing)
    // ==========================================================================
    function initAnimatedCounters() {
      const counters = document.querySelectorAll('.stat-counter');
      if (!counters.length) return;

      const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            runCounterAnimation(el);
            obs.unobserve(el); // Run only once!
          }
        });
      }, {
        threshold: 0.35,
        rootMargin: '0px 0px -40px 0px'
      });

      counters.forEach(el => observer.observe(el));
    }

    function stepFrame(cb) {
      let called = false;
      if (typeof window.requestAnimationFrame === 'function') {
        window.requestAnimationFrame((time) => {
          if (!called) {
            called = true;
            cb(time);
          }
        });
      }
      setTimeout(() => {
        if (!called) {
          called = true;
          cb(performance.now());
        }
      }, 25);
    }

    function runCounterAnimation(el) {
      const unitSpan = el.querySelector('.unit');
      // Respect prefers-reduced-motion
      if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return; // Retain already rendered target text
      }
      let unitHtml = '';
      let targetText = '';
      
      if (unitSpan) {
        unitHtml = unitSpan.outerHTML;
        const clone = el.cloneNode(true);
        const cloneUnit = clone.querySelector('.unit');
        if (cloneUnit) cloneUnit.remove();
        targetText = el.getAttribute('data-counter-target') || clone.textContent.trim();
      } else {
        targetText = el.getAttribute('data-counter-target') || el.textContent.trim();
      }

      // Match optional prefix, the number (with comma/decimal), and optional suffix
      const match = targetText.match(/^([^\d]*?)([\d,]+(?:\.\d+)?)(.*)$/);
      if (!match) return;

      const prefix = el.getAttribute('data-counter-prefix') !== null 
        ? el.getAttribute('data-counter-prefix') 
        : match[1];
      const numRaw = match[2].replace(/,/g, '');
      const targetVal = parseFloat(numRaw);
      const suffix = el.getAttribute('data-counter-suffix') !== null 
        ? el.getAttribute('data-counter-suffix') 
        : match[3];

      const hasCommas = match[2].includes(',');
      const decimalMatch = numRaw.match(/\.(\d+)/);
      const decimals = decimalMatch ? decimalMatch[1].length : 0;
      const duration = parseInt(el.getAttribute('data-counter-duration') || '1800', 10);
      const startTime = performance.now();

      // Start at 0 immediately
      const zeroFormatted = decimals > 0 ? (0).toFixed(decimals) : '0';
      if (unitHtml) {
        el.innerHTML = `${prefix}${zeroFormatted}${suffix} ${unitHtml}`;
      } else {
        el.textContent = `${prefix}${zeroFormatted}${suffix}`;
      }

      function update(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Ease-out cubic formula: 1 - (1 - progress)^3
        const ease = 1 - Math.pow(1 - progress, 3);
        const currentNum = targetVal * ease;

        let numStr = decimals > 0 ? currentNum.toFixed(decimals) : Math.round(currentNum).toString();
        
        if (hasCommas) {
          const parts = numStr.split('.');
          parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
          numStr = parts.join('.');
        }

        if (unitHtml) {
          el.innerHTML = `${prefix}${numStr}${suffix} ${unitHtml}`;
        } else {
          el.textContent = `${prefix}${numStr}${suffix}`;
        }

        if (progress < 1) {
          stepFrame(update);
        } else {
          // Exact final target value matching
          let finalNum = targetVal.toFixed(decimals);
          if (hasCommas) {
            const parts = finalNum.split('.');
            parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
            finalNum = parts.join('.');
          }
          if (unitHtml) {
            el.innerHTML = `${prefix}${finalNum}${suffix} ${unitHtml}`;
          } else {
            el.textContent = `${prefix}${finalNum}${suffix}`;
          }
          el.classList.add('counter-completed');
        }
      }

      stepFrame(update);
    }

    // Window Onload Initialization
    window.addEventListener('DOMContentLoaded', () => {
      initHeaderNavInteractions();
      initScrollInteractions();
      renderFaculties('all');
      renderTcasTable('all');
      initFacultiesTcasChart();
      initCharts();
      initTuLeafletMap();
      initGreenSustainabilityChart();
      initHospitalCapacityChart();
      initAnimatedCounters();
      initBidwellsScrollMotions();
      updateCockpit();
      initPillarRoute();
    });

    // ==========================================================================
    // HEADER NAVIGATION HORIZONTAL SCROLLBAR & INTERACTIONS
    // ==========================================================================
    function autoScrollHeaderNavToActive(activeLink) {
      const nav = document.getElementById('headerNav');
      if (!nav || !activeLink) return;
      const linkLeft = activeLink.offsetLeft;
      const linkWidth = activeLink.offsetWidth;
      const navWidth = nav.clientWidth;
      const targetScroll = linkLeft - (navWidth / 2) + (linkWidth / 2);
      nav.scrollTo({ left: Math.max(0, targetScroll), behavior: 'smooth' });
    }

    function initHeaderNavInteractions() {
      const nav = document.getElementById('headerNav');
      if (!nav) return;

      // 1. Mouse wheel horizontal scrolling over navigation bar
      nav.addEventListener('wheel', (e) => {
        if (e.deltaY !== 0) {
          e.preventDefault();
          nav.scrollLeft += e.deltaY * 0.95;
        }
      }, { passive: false });

      // 2. Click and drag to scroll (Grab to scroll)
      let isDown = false;
      let startX = 0;
      let initialScroll = 0;
      let hasDragged = false;

      nav.addEventListener('mousedown', (e) => {
        isDown = true;
        hasDragged = false;
        startX = e.pageX - nav.offsetLeft;
        initialScroll = nav.scrollLeft;
      });

      window.addEventListener('mouseup', () => {
        if (isDown) isDown = false;
      });

      nav.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        hasDragged = true;
        const x = e.pageX - nav.offsetLeft;
        const walk = (x - startX) * 1.4;
        nav.scrollLeft = initialScroll - walk;
      });

      // Prevent link navigation if the user was dragging
      nav.querySelectorAll('.header-nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
          if (hasDragged) {
            e.preventDefault();
            hasDragged = false;
          }
        });
      });
    }

    // ==========================================================================
    // BIDWELLS SCROLL-TRIGGERED MOTION DESIGN (Luxury Editorial Entrance)
    // ==========================================================================
    function initBidwellsScrollMotions() {
      const revealElements = document.querySelectorAll(
        '.tu-reveal, .tu-reveal-slide-up, .tu-reveal-slide-right, .tu-reveal-slide-left, .tu-reveal-scale'
      );
      if (!revealElements.length) return;

      // Check prefers-reduced-motion
      const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (prefersReduced) {
        revealElements.forEach(el => el.classList.add('is-revealed'));
        return;
      }

      const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            el.classList.add('is-revealed');
            obs.unobserve(el); // Reveal only once!

            // Trigger smooth chart animation on scroll entrance if a canvas is inside
            const canvases = el.tagName === 'CANVAS' ? [el] : Array.from(el.querySelectorAll('canvas'));
            canvases.forEach(canvas => {
              if (typeof Chart !== 'undefined' && Chart.getChart) {
                const chart = Chart.getChart(canvas);
                if (chart && !canvas.dataset.entranceAnimated) {
                  canvas.dataset.entranceAnimated = 'true';
                  chart.reset();
                  requestAnimationFrame(() => {
                    chart.update(); // Chart.js v4: update() รับ mode เป็นสตริงเท่านั้น (ส่ง object ทำให้แอนิเมชันพัง)
                  });
                }
              }
            });

            // If this element contains Leaflet map, invalidateSize after slide transition
            if (el.querySelector('#campusLeafletMap') || el.id === 'campusLeafletMap') {
              setTimeout(() => {
                if (tuMap && typeof tuMap.invalidateSize === 'function') {
                  tuMap.invalidateSize();
                }
              }, 950);
            }
          }
        });
      }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
      });

      revealElements.forEach(el => observer.observe(el));
    }


    // Accessible Data Table Toggle
    function toggleDataTable(id, btnEl) {
      const el = document.getElementById(id);
      if (!el) return;
      const isHidden = (el.style.display === 'none' || el.style.display === '');
      el.style.display = isHidden ? 'block' : 'none';
      const btn = btnEl || document.querySelector(`[onclick*="toggleDataTable('${id}'"]`);
      if (btn) {
        btn.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
        const icon = isHidden ? '<i class="fa-solid fa-eye-slash"></i>' : '<i class="fa-solid fa-table"></i>';
        const label = isHidden ? ' ซ่อนตารางข้อมูล' : ' แสดงตารางข้อมูล';
        btn.innerHTML = icon + label;
      }
    }


    // Cockpit Reset to Strategic Baseline
    function resetCockpit() {
      const r = document.getElementById('sliderResearch');
      const s = document.getElementById('sliderSkills');
      const g = document.getElementById('sliderGreen');
      const h = document.getElementById('sliderHealth');
      if (r) r.value = 90;
      if (s) s.value = 95;
      if (g) g.value = 88;
      if (h) h.value = 96;
      updateCockpit();
    }


    // Accessibility: Global Escape key modal dismisser
    window.addEventListener('keydown', (e) => {
      if (e.target && e.target.closest && e.target.closest('.tu-runner')) return;
      if (e.key === 'Escape') {
        const facModal = document.getElementById('facultyModal');
        if (facModal && facModal.style.display !== 'none') {
          closeFacultyModal();
        }
        const fHubModal = document.getElementById('flourishHubModal');
        if (fHubModal && fHubModal.style.display === 'flex') {
          closeFlourishHubModal();
        }
      }
    });

    // Accessibility: Scrubber keyboard navigation (Left/Right/Home/End)
    document.addEventListener('DOMContentLoaded', () => {
      const scrubberTrack = document.getElementById('scrubberTrack');
      if (scrubberTrack) {
        const sections = ['hero', 'key-findings', 'topic-01', 'topic-02', 'topic-03', 'topic-04', 'topic-05', 'topic-06', 'topic-07', 'topic-08', 'topic-09', 'topic-10', 'finish'];
        scrubberTrack.addEventListener('keydown', (e) => {
          if (e.target && e.target.closest && e.target.closest('.tu-runner')) return;
          let currentVal = parseInt(scrubberTrack.getAttribute('aria-valuenow') || '0', 10);
          let nextIdx = currentVal;

          if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === 'PageDown') {
            e.preventDefault();
            nextIdx = Math.min(currentVal + 1, sections.length - 1);
          } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'PageUp') {
            e.preventDefault();
            nextIdx = Math.max(currentVal - 1, 0);
          } else if (e.key === 'Home') {
            e.preventDefault();
            nextIdx = 0;
          } else if (e.key === 'End') {
            e.preventDefault();
            nextIdx = sections.length - 1;
          } else {
            return;
          }

          scrubberTrack.setAttribute('aria-valuenow', nextIdx);
          const targetId = sections[nextIdx];
          const targetEl = document.getElementById(targetId);
          if (targetEl) {
            targetEl.scrollIntoView({ behavior: 'smooth' });
          }
        });
      }
    });
