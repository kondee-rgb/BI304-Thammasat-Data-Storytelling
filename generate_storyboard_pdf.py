"""
Script to generate publication-quality Storyboard PDF for BI304 Thammasat Project
Using ReportLab with Tahoma Font for Thai language support.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Register Tahoma fonts
pdfmetrics.registerFont(TTFont('Tahoma', 'C:/Windows/Fonts/tahoma.ttf'))
pdfmetrics.registerFont(TTFont('Tahoma-Bold', 'C:/Windows/Fonts/tahomabd.ttf'))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Tahoma", 8)
        self.setFillColor(colors.HexColor("#666666"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(40, 810, "BI304 Data Storytelling | Thammasat Storyboard (10 Visualizations)")
            self.drawRightString(555, 810, "Thammasat Business School (TBS)")
            self.setStrokeColor(colors.HexColor("#D32F2F"))
            self.setLineWidth(1)
            self.line(40, 804, 555, 804)
        
        # Footer
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(40, 40, 555, 40)
        self.drawString(40, 28, "โครงงานกลุ่มวิชา BI304: วันนำเสนอที่ 30 ตุลาคม | มหาวิทยาลัยธรรมศาสตร์")
        self.drawRightString(555, 28, f"หน้า {self._pageNumber} จาก {page_count}")
        self.restoreState()

def build_pdf(filename="Storyboard_Thammasat_BI304.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Tahoma-Bold',
        fontSize=20,
        leading=26,
        textColor=colors.HexColor('#C62828'), # TU Crimson
        alignment=1, # Center
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        fontName='Tahoma-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#F57F17'), # TU Warm Gold
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        fontName='Tahoma-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#C62828'),
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        fontName='Tahoma-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1A237E'), # Deep Navy
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        fontName='Tahoma',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#212121')
    )

    body_bold = ParagraphStyle(
        'Body_Bold',
        fontName='Tahoma-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#212121')
    )

    caption_style = ParagraphStyle(
        'Caption_Custom',
        fontName='Tahoma',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#37474F'),
        backColor=colors.HexColor('#ECEFF1'),
        borderPadding=6,
        spaceAfter=6
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        fontName='Tahoma-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        fontName='Tahoma',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#212121')
    )

    story = []

    # ================= COVER / HEADER =================
    story.append(Spacer(1, 10))
    story.append(Paragraph("STORYBOARD DATA SCROLLYTELLING & FLOURISH STORY", title_style))
    story.append(Paragraph("90 ปี ธรรมศาสตร์: จากตลาดวิชาเพื่อราษฎร สู่นวัตกรรมความยั่งยืนระดับโลก", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2.5, color=colors.HexColor('#C62828'), spaceAfter=15))

    meta_data = [
        [
            Paragraph("<b>วิชา:</b> BI304 การเสริมพลังแก่ข้อมูลผ่านการเล่าเรื่องและการแสดงภาพ", body_style),
            Paragraph("<b>คณะ:</b> พาณิชยศาสตร์และการบัญชี (TBS) มธ.", body_style)
        ],
        [
            Paragraph("<b>กำหนดนำเสนอ:</b> วันที่ 30 ตุลาคม | ภาคการศึกษา 1/2569", body_style),
            Paragraph("<b>อาจารย์ผู้สอน:</b> อ.ดร. นภธนิตย์ โชติสาร", body_style)
        ],
        [
            Paragraph("<b>ชิ้นงานส่งมอบหลัก:</b> 1. Storyboard (PDF) &nbsp; 2. Data Scrollytelling (Web Application)", body_style),
            Paragraph("<b>เครื่องมือหลัก:</b> Google Colab, Plotly, Leaflet.js, Flourish Studio", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[270, 245])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF8E1')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FFB300')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#FFE082')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 12))

    # ================= 1. NARRATIVE ARCHITECTURE & TUFTE PRINCIPLES =================
    story.append(Paragraph("1. กรอบแนวคิดและการออกแบบตามหลักวิชาการ (Storytelling & Design Principles)", h1_style))
    p_intro = Paragraph(
        "โครงงานนี้ได้รับการออกแบบตามกระบวนการ <b>Data Storytelling</b> โดยนำสถิติตลอด 9 ทศวรรษของมหาวิทยาลัยธรรมศาสตร์ (พ.ศ. 2477 - 2569) "
        "มาร้อยเรียงด้วยเส้นเรื่องเชิงอรรถรส (Narrative Arc) ผสานกับกรอบการจัดระเบียบข้อมูล <b>LATCH</b> และยึดหลักเกณฑ์ความซื่อตรงของข้อมูลและ Data-Ink Ratio "
        "ตามกฎของ <b>Edward Tufte</b> เพื่อให้เกิดผลลัพธ์ที่ช่วยให้ผู้ฟัง 'เข้าใจ รู้สึก และเห็นทิศทางขับเคลื่อนในอนาคต'",
        body_style
    )
    story.append(p_intro)
    story.append(Spacer(1, 6))

    latch_intro = Paragraph(
        "<b>การประยุกต์ใช้โมเดล LATCH ใน 10 Visualizations:</b><br/>"
        "• <b>Location (สถานที่):</b> ฉากที่ 2 (เครือข่าย 4 ศูนย์การศึกษาทั่วไทย) และ ฉากที่ 5 (เส้นทางย้ายหลักสูตรปริญญาตรีสู่รังสิต)<br/>"
        "• <b>Alphabet (ตัวอักษร/การจัดหมวด):</b> ฉากที่ 3 (ดัชนีจำแนก 19 คณะตามลำดับหมวดหมู่และชื่อสากล)<br/>"
        "• <b>Time (เวลา/ลำดับ):</b> ฉากที่ 1 (วิวัฒนาการจำนวนผู้สมัครตั้งแต่ พ.ศ. 2477) และ ฉากที่ 7 (พัฒนาการอันดับโลก QS/THE Time-Series)<br/>"
        "• <b>Category (หมวดหมู่):</b> ฉากที่ 4 (โครงสร้างความหลากหลายทางเพศและระดับการศึกษา) และ ฉากที่ 8 (ตัวชี้วัด SDGs 17 ด้าน)<br/>"
        "• <b>Hierarchy (ลำดับชั้น/ขนาด):</b> ฉากที่ 6 (สัดส่วนงบประมาณและทุนวิจัย) และ ฉากที่ 9-10 (ผลกระทบทางการแพทย์และเป้าหมายสู่ 100 ปี)",
        body_style
    )
    story.append(latch_intro)
    story.append(Spacer(1, 6))

    tufte_intro = Paragraph(
        "<b>การยึดถือหลักการ Edward Tufte ในโปรเจกต์:</b><br/>"
        "1. <b>Maximize Data-Ink Ratio:</b> ตัดกรอบหนาและเงาฟุ้งที่ไม่จำเป็น ให้หมึกเกือบ 100% สื่อความหมายของข้อมูลโดยตรง<br/>"
        "2. <b>Direct Labeling:</b> วางป้ายข้อมูลแนบชิดกับกราฟ/จุดสำคัญ ลดการสลับสายตามอง Legend ระยะไกล<br/>"
        "3. <b>Avoid Chartjunk & False 3D:</b> หลีกเลี่ยง 3D Scatter หรือกราฟแท่ง 3 มิติที่มุมมองหลอกตา<br/>"
        "4. <b>Truthful Scale (Zero Lie Factor):</b> เริ่มต้นแกน Bar Chart ที่ 0 เสมอ และใช้สเกลที่สอดคล้องกับขนาดการเปลี่ยนแปลงจริง<br/>"
        "5. <b>Accessible Color Palette:</b> เลือกใช้เฉดสีเลือดหมู-ทองของธรรมศาสตร์ คู่กับสีเทากลาง รองรับผู้มีภาวะตาบอดสี (Colorblind-Safe)",
        body_style
    )
    story.append(tufte_intro)
    story.append(Spacer(1, 10))

    # ================= 2. THE 10 SCENES STORYBOARD =================
    story.append(Paragraph("2. รายละเอียด Storyboard ทั้ง 10 ฉาก (The 10-Scene Storyboard)", h1_style))
    story.append(Paragraph("จำลองโครงสร้างตามแนวทาง Storyboard ของอาจารย์ (Visual Focus, Narrative Caption, Data Points, Tool, Flourish Template)", body_style))
    story.append(Spacer(1, 8))

    scenes = [
        {
            "num": "ฉากที่ 1",
            "title": "ปฐมบท 2477: ตลาดวิชาเพื่อราษฎร (The Democratic Genesis)",
            "hook": "จากความตั้งใจของท่านปรีดี พนมยงค์ ในการสร้างบ่อน้ำบำบัดความกระหายความรู้ของราษฎร สู่สถิตินักศึกษารุ่นแรกที่ล้นหลามเกินความคาดหมาย",
            "visual": "Interactive Step & Area Timeline (สีแดงเลือดหมูมินิมอล) ย้อนรอยยอดผู้สมัครปี 2477 จำนวน 7,094 คน เทียบกับการปรับสู่ระบบปิด และขยายตัวสู่ 42,650 คนในปัจจุบัน มี Annotation ไฮไลต์จุดเปลี่ยนสำคัญทางการเมือง",
            "data": "ปี 2477 (7,094 คน) → ปี 2495 (ปรับสู่ระบบมหาวิทยาลัยปิด) → ปี 2519 → ปี 2569 (42,650 คน รวมทุกระดับ)",
            "tool": "Plotly Time-Series with Annotations / Flourish Bar Chart Race (01_flourish_bar_chart_race_faculties.csv)",
            "latch": "Time (เวลา/ลำดับประวัติศาสตร์)"
        },
        {
            "num": "ฉากที่ 2",
            "title": "การกระจายสู่ภูมิภาค: 4 ศูนย์การศึกษาแห่งพลังปัญญา (The 4-Campus Network)",
            "hook": "เมื่อท่าพระจันทร์ 49 ไร่ ไม่อาจรองรับความใฝ่รู้ได้อีกต่อไป ธรรมศาสตร์จึงขยายรากแก้วสู่ ปทุมธานี ลำปาง และชลบุรี",
            "visual": "Interactive Folium / Leaflet Web Map พร้อม CartoDB Positron Tiles ปักหมุด 4 ศูนย์ พร้อมวงรัศมีขนาดพื้นที่ (Rai) และการ์ดข้อมูลเปรียบเทียบจุดเด่นของแต่ละวิทยาเขต",
            "data": "ท่าพระจันทร์ (49 ไร่, 6,500 นศ.) | รังสิต (1,757 ไร่, 32,000 นศ.) | ลำปาง (464 ไร่, 2,200 นศ.) | พัทยา (566 ไร่, 1,500 นศ.)",
            "tool": "Folium / Leaflet.js / Flourish Marker Map (02_flourish_campuses_map.csv)",
            "latch": "Location (พิกัดสถานที่ทางภูมิศาสตร์)"
        },
        {
            "num": "ฉากที่ 3",
            "title": "การผลิบานทางวิชาการ: จาก 1 คณะกฎหมาย สู่ 19 คณะ 4 คลัสเตอร์ (Academic Clusters)",
            "hook": "ธรรมศาสตร์ไม่ได้มีเพียงนิติศาสตร์และรัฐศาสตร์ แต่เติบโตสู่สถาบันสหวิทยาการชั้นนำที่ครอบคลุมการแพทย์ นวัตกรรม และบริหารธุรกิจระดับ Triple Crown (TBS)",
            "visual": "Interactive Treemap / Sunburst Chart จัดกลุ่มคณะ 19 คณะ ออกเป็น 4 คลัสเตอร์หลัก ขนาดบล็อกตามจำนวนนักศึกษาและสัดส่วนหลักสูตรนานาชาติ",
            "data": "สังคมศาสตร์-มนุษยศาสตร์ (42%) | วิทยาศาสตร์และเทคโนโลยี (26%) | วิทยาศาสตร์สุขภาพ/แพทย์ (18%) | บูรณาการ/นานาชาติ (14%)",
            "tool": "Plotly Treemap / Flourish Hierarchy Treemap (03_flourish_hierarchy_clusters.csv)",
            "latch": "Category & Hierarchy (หมวดหมู่วิชาการและขนาดสัดส่วน)"
        },
        {
            "num": "ฉากที่ 4",
            "title": "สถิติประชากรนักศึกษา: มิติความเท่าเทียมและการเปิดรับสากล (Inclusivity Matrix)",
            "hook": "ภาพสะท้อนสังคมไทยผ่านพีระมิดนักศึกษา จากอดีตที่ผู้ชายครองส่วนใหญ่ สู่ปัจจุบันที่ผู้หญิงครองสัดส่วน 62% พร้อมนักศึกษาต่างชาติจากกว่า 50 ประเทศ",
            "visual": "Grouped Stacked Bar & Diversity Donut ชี้ให้เห็นสัดส่วน เพศ ชาย/หญิง (38% vs 62%), ปริญญาตรี vs บัณฑิตศึกษา, และโควตานักเรียนชนบทผู้ด้อยโอกาส",
            "data": "ป.ตรี (78%), ป.โท-เอก (22%) | หญิง 62%, ชาย 38% | นักศึกษาต่างชาติ 1,800+ คน | โควตาเรียนดีชนบท 2,500+ คน/ปี",
            "tool": "Plotly Clean Bar Chart / Flourish Grouped Bar (04_flourish_demographics_gender.csv)",
            "latch": "Category & Magnitude (การจัดกลุ่มประชากรและสัดส่วน)"
        },
        {
            "num": "ฉากที่ 5",
            "title": "มหาการย้ายถิ่นฐาน: จากแม่น้ำเจ้าพระยาสู่ทุ่งรังสิต (The Great Migration Flow)",
            "hook": "การตัดสินใจครั้งประวัติศาสตร์ในปี 2529 ย้ายนักศึกษาปี 1 สู่รังสิต จนถึงปี 2548 ที่ย้าย ป.ตรี ทั้งหมด พลิกโฉมท่าพระจันทร์สู่ Hub นานาชาติและบัณฑิตศึกษา",
            "visual": "Sankey Flow Diagram แสดงสายธารการโยกย้ายของคณะและนักศึกษาจากท่าพระจันทร์ไปยังศูนย์รังสิตตามช่วงทศวรรษอย่างเด่นชัด",
            "data": "ปี 2529 (นศ.ปี 1 ย้าย 4,000 คน) → ปี 2542 (คณะวิทย์-แพทย์เปิดตัวเต็มรูปแบบ) → ปี 2548 (ป.ตรี ภาคปกติย้ายครบ 100%)",
            "tool": "Plotly Sankey / RAWGraphs Alluvial Architecture",
            "latch": "Location & Flow (การเดินทางและการจัดสรรเชิงพื้นที่)"
        },
        {
            "num": "ฉากที่ 6",
            "title": "เครื่องยนต์การเงินและทุนวิจัย: มหาวิทยาลัยในกำกับของรัฐ (Financial Stewardship)",
            "hook": "การเปลี่ยนผ่านสู่มหาวิทยาลัยในกำกับของรัฐในปี 2558 ทำให้ธรรมศาสตร์บริหารงบประมาณได้อย่างคล่องตัวและพึ่งพาทุนวิจัยภายนอกเพิ่มขึ้นกว่า 140%",
            "visual": "Waterfall & Stacked Area Chart แจกแจงโครงสร้างรายได้ ~11,500 ล้านบาท (เงินอุดหนุนรัฐ, ค่าธรรมเนียมการศึกษา, รายได้วิจัยและทรัพย์สิน)",
            "data": "งบประมาณรวม ~11,500 ล้านบาท | ทุนวิจัยภายนอกเติบโตก้าวกระโดดจาก 450 ล้านสู่ 1,100+ ล้านบาท ในรอบ 10 ปี",
            "tool": "Plotly Waterfall & Clean Stacked Bar (Tufte Minimalist Palette)",
            "latch": "Hierarchy & Magnitude (ลำดับสัดส่วนงบประมาณ)"
        },
        {
            "num": "ฉากที่ 7",
            "title": "ก้าวสู่เวทีโลก: เส้นทางทะยานใน World Rankings (Global Ascent)",
            "hook": "ธรรมศาสตร์ไม่ได้หยุดอยู่แค่เบอร์ต้นของประเทศ แต่ทะยานสู่ท็อป 100 เอเชีย และโดดเด่นติดอันดับโลกในกลุ่มสาขา Law, Business และ Social Sciences",
            "visual": "Multi-Series Line Chart with Range Slider เปรียบเทียบอันดับ QS Asia และ THE World Ranking พร้อมแถบแรเงาแสดงความโดดเด่นรายสาขาวิชา",
            "data": "QS Asia Ranking: ทะยานสู่ Top 100 | สาขา Business & Management: Top 200 โลก | นิติศาสตร์ & สังคมศาสตร์: Top 150 โลก",
            "tool": "Plotly Time-Series Slider / Flourish Line Chart (05_flourish_rankings_time_series.csv)",
            "latch": "Time & Hierarchy (ลำดับเวลาและระดับความเป็นเลิศ)"
        },
        {
            "num": "ฉากที่ 8",
            "title": "ธรรมศาสตร์สีเขียว: ผู้นำ SDG และสวนป๋วย 100 ปี (Green TU & SDG Leadership)",
            "hook": "อุทยานเรียนรู้ป๋วย 100 ปี สวนผักออร์แกนิกบนดาดฟ้าที่ใหญ่ที่สุดในเอเชีย (22,000 ตร.ม.) ควบคู่พลังงานแสงอาทิตย์ 35+ MW และรถบัส EV 100%",
            "visual": "Radar / Spider Polar Chart & Gauge Bar แสดงคะแนนการขับเคลื่อน 17 เป้าหมาย SDGs ของสหประชาชาติ โดยเด่นที่สุดใน SDG 11 (Sustainable Cities)",
            "data": "SDG 11 ติดท็อป 10 ของโลก | กำลังผลิตโซลาร์รูฟ 35 MW | สวนป๋วยดาดฟ้า 22,000 ตร.ม. | ลดคาร์บอนฟุตพริ้นท์ได้กว่า 24,000 ตัน CO2/ปี",
            "tool": "Plotly Polar Radar / Flourish Radar Chart (06_flourish_sdg_scores.csv)",
            "latch": "Category & Hierarchy (หมวดหมู่เป้าหมายความยั่งยืน)"
        },
        {
            "num": "ฉากที่ 9",
            "title": "โรงพยาบาลธรรมศาสตร์: ที่พึ่งแห่งประชาชนในยามวิกฤต (Healthcare for Society)",
            "hook": "จิตวิญญาณ 'ธรรมศาสตร์เพื่อประชาชน' ที่เห็นเด่นชัดที่สุดในยามวิกฤตชาติ จากโรงพยาบาลสนามแห่งแรกของไทยช่วงโควิด-19 สู่ศูนย์การแพทย์ 1.45 ล้านเคส/ปี",
            "visual": "Dual-Axis Combination Chart แสดงจำนวนผู้ป่วยนอกที่เติบโตต่อเนื่องคู่กับขีดความสามารถการบริการเตียงวิกฤตและการให้คำปรึกษาทางไกล (Telemedicine)",
            "data": "ผู้ป่วยนอก 1987 (50,000 คน) → 2025 (1,450,000+ คน) | รพ.สนามโควิด 3,000+ เตียง | ระบบแพทย์ทางไกลดูแลชุมชน 80,000+ รายการ",
            "tool": "Plotly Dual-Axis Line + Bar Chart with Direct Data Point Callouts",
            "latch": "Time & Magnitude (ลำดับเวลาและขนาดผลกระทบต่อชีวิต)"
        },
        {
            "num": "ฉากที่ 10",
            "title": "มุ่งสู่ศตวรรษที่ 1: วิสัยทัศน์ TU 2034 สู่ 100 ปีมหาวิทยาลัยเพื่ออนาคต (The Centenary Horizon)",
            "hook": "อีกเพียงไม่กี่ปีจะถึงหลักชัย 100 ปีธรรมศาสตร์ ก้าวต่อไปคือการบ่มเพาะสตาร์ทอัพเพื่อสังคม และเป้าหมาย Carbon Neutrality มหาวิทยาลัยคาร์บอนเป็นศูนย์",
            "visual": "Interactive Target Gauge & Strategic Milestone Roadmap แสดงความก้าวหน้าสู่ 4 เป้าหมายใหญ่: Net Zero 2030, 88 Sandbox Startups, Global Micro-credentials",
            "data": "เป้าหมาย Net Zero Campus (2030) | บ่มเพาะ 10,000 สตาร์ทอัพ (88 Sandbox) | ผลิตพลเมืองโลกที่พร้อมรับมือ AI Disruption",
            "tool": "Plotly Gauge Dashboard & Flourish Milestone Progress Pipeline",
            "latch": "Time & Hierarchy (เป้าหมายยุทธศาสตร์สู่อนาคต)"
        }
    ]

    for sc in scenes:
        scene_box = [
            [
                Paragraph(f"<b>{sc['num']}: {sc['title']}</b>", h2_style),
                Paragraph(f"<b>LATCH:</b> {sc['latch']}", body_style)
            ],
            [
                Paragraph("<b>เรื่องเล่า/อรรถรส (Narrative Caption):</b>", body_bold),
                Paragraph(sc['hook'], body_style)
            ],
            [
                Paragraph("<b>การจัดวางภาพ (Visual & Composition):</b>", body_bold),
                Paragraph(sc['visual'], body_style)
            ],
            [
                Paragraph("<b>ชุดข้อมูลสำคัญ (Data Points):</b>", body_bold),
                Paragraph(sc['data'], body_style)
            ],
            [
                Paragraph("<b>เครื่องมือ & Flourish Template:</b>", body_bold),
                Paragraph(sc['tool'], body_style)
            ]
        ]
        t = Table(scene_box, colWidths=[150, 365])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F5F5F5')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CFD8DC')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#ECEFF1')),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(t)
        story.append(Spacer(1, 7))

    story.append(PageBreak())

    # ================= 3. TEAM ROLE ALLOCATION =================
    story.append(Paragraph("3. การแบ่งบทบาทหน้าที่ในกลุ่ม (Team Work Breakdown)", h1_style))
    p_team = Paragraph(
        "เพื่อให้การดำเนินงานโครงงานข้อมูลเป็นไปอย่างมีประสิทธิภาพและครอบคลุมทุกมิติตามหลักการ Data Storytelling จึงได้วางโครงสร้างการแบ่งหน้าที่รับผิดชอบออกเป็น 5 ฝ่ายหลักอย่างเป็นระบบ:",
        body_style
    )
    story.append(p_team)
    story.append(Spacer(1, 6))

    team_data = [
        [
            Paragraph("ฝ่าย/ตำแหน่ง", table_header_style),
            Paragraph("จำนวน (คน)", table_header_style),
            Paragraph("ความรับผิดชอบหลัก (Key Responsibilities)", table_header_style),
            Paragraph("เครื่องมือที่รับผิดชอบ", table_header_style)
        ],
        [
            Paragraph("<b>1. Data & Analytics Lead</b>", table_cell_style),
            Paragraph("2-3", table_cell_style),
            Paragraph("รวบรวมตัวเลขสถิติ มธ., ทำ Data Cleaning ใน Pandas, คำนวณ KPI และสัดส่วนที่ถูกต้อง", table_cell_style),
            Paragraph("Python, Pandas, Excel, Google Colab", table_cell_style)
        ],
        [
            Paragraph("<b>2. Data Viz Developers</b>", table_cell_style),
            Paragraph("3-4", table_cell_style),
            Paragraph("เขียนโค้ดสร้างกราฟิกทั้ง 10 ชิ้น (Plotly, Folium Map, Treemap, Sankey, Radar Chart, Flourish)", table_cell_style),
            Paragraph("Plotly, Folium, Leaflet.js, Flourish.studio", table_cell_style)
        ],
        [
            Paragraph("<b>3. Scrollytelling Web Engineers</b>", table_cell_style),
            Paragraph("2", table_cell_style),
            Paragraph("พัฒนาเว็บ Scrollytelling & Flourish Story, เชื่อมโยงระบบสลับฉาก, ตกแต่ง UI/UX สไตล์ มธ.", table_cell_style),
            Paragraph("HTML5, CSS3, JavaScript, Batch Launcher", table_cell_style)
        ],
        [
            Paragraph("<b>4. Story Narrative & Presenters</b>", table_cell_style),
            Paragraph("2", table_cell_style),
            Paragraph("เขียนสคริปต์บรรยายทั้ง 10 ฉาก, ออกแบบ Hook อารมณ์ร่วม, เตรียมสไลด์และฝึกซ้อมการนำเสนอวันที่ 30", table_cell_style),
            Paragraph("Storyboard Script, Presentation Deck", table_cell_style)
        ],
        [
            Paragraph("<b>5. Quality & Tufte Auditor</b>", table_cell_style),
            Paragraph("1-2", table_cell_style),
            Paragraph("ตรวจทานความถูกต้องสถิติ ตรวจสอบ Data-Ink Ratio, Lie Factor, เช็ก Colorblind Accessibility", table_cell_style),
            Paragraph("ColorBrewer, Edward Tufte Audit Sheet", table_cell_style)
        ]
    ]

    team_table = Table(team_data, colWidths=[120, 60, 215, 120])
    team_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#C62828')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#B71C1C')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#EEEEEE')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(team_table)
    story.append(Spacer(1, 12))

    # ================= 4. TECHNICAL ARCHITECTURE & HOW TO RUN =================
    story.append(Paragraph("4. สถาปัตยกรรมเทคนิคและขั้นตอนการเปิดรันชิ้นงาน (How to Run & Submit)", h1_style))
    tech_info = Paragraph(
        "<b>วิธีการเปิดใช้งานและตรวจสอบชิ้นงานที่ส่งมอบ (1-Click Run):</b><br/>"
        "1. <b>เปิดเว็บ Scrollytelling ทันที:</b> ดับเบิลคลิกไฟล์ <code>คลิกเพื่อเปิดเว็บ_RUN_SCROLLYTELLING.bat</code> หรือดับเบิลคลิก <code>index.html</code> ในโฟลเดอร์โครงการเพื่อนำเสนอได้ทันที<br/>"
        "2. <b>รันโค้ดทั้งหมดบน Google Colab:</b> นำไฟล์ <code>BI304_Thammasat_Data_Storytelling.ipynb</code> อัปโหลดขึ้น Google Colab แล้วคลิก 'Runtime -> Run all' (สามารถรันผ่าน 100% โดยไม่ต้องแก้ไขโค้ด)<br/>"
        "3. <b>นำเข้าข้อมูลบน Flourish:</b> ชุดไฟล์ในโฟลเดอร์ <code>flourish_data/</code> มีฟอร์แมตตรงตามเทมเพลตของ flourish.studio เพื่อกดสร้าง Story นำเสนอได้ทันที<br/><br/>"
        "<b>แหล่งอ้างอิงข้อมูลทุติยภูมิ (Official Secondary Data Sources):</b><br/>"
        "• รายงานประจำปี มหาวิทยาลัยธรรมศาสตร์ (Thammasat University Annual Report 2558 - 2568)<br/>"
        "• สถิติจำนวนนักศึกษาและหลักสูตร สำนักทะเบียนและประมวลผล มหาวิทยาลัยธรรมศาสตร์ (Reg TU)<br/>"
        "• Times Higher Education (THE) Impact Rankings & QS World University Rankings by Subject<br/>"
        "• รายงานประจำปี โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ และสถิติเตียงโรงพยาบาลสนาม<br/>"
        "• รายงานโครงการ Green Thammasat และอุทยานเรียนรู้ป๋วย 100 ปี (Puey Centenary Hall)",
        body_style
    )
    story.append(tech_info)
    story.append(Spacer(1, 10))

    end_box = [
        [
            Paragraph("<b>สรุปสิ่งที่ต้องส่ง (พร้อมส่งมอบ):</b><br/>"
                      "1. <b>Storyboard (PDF):</b> ไฟล์เอกสารฉบับนี้ (Storyboard_Thammasat_BI304.pdf)<br/>"
                      "2. <b>Data Scrollytelling (Web):</b> เว็บไซต์ index.html ที่รองรับทั้งโหมด Scrollytelling และ Flourish Story<br/>"
                      "3. <b>Google Colab Notebook:</b> ไฟล์ BI304_Thammasat_Data_Storytelling.ipynb พร้อมรัน 100%",
                      caption_style)
        ]
    ]
    end_table = Table(end_box, colWidths=[515])
    end_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#00897B')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(end_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}, size: {os.path.getsize(filename)} bytes")

if __name__ == "__main__":
    build_pdf()
