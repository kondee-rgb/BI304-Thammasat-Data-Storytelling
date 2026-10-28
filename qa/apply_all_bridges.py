import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Topic 01
p1 = r'<div class="narrative-connector-bridge">\s*<i class="fa-solid fa-arrow-right-long"></i>\s*<span><strong>สะพานเชื่อมโยงข้อมูล:</strong> จากการปักหมุด ณ ท่าพระจันทร์'
r1 = r'<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-02" aria-label="อ่านต่อหัวข้อถัดไป: 4 ศูนย์การศึกษา">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> จากการปักหมุด ณ ท่าพระจันทร์'
assert re.search(p1, text), "Bridge 1 pattern not found"
text = re.sub(p1, r1, text, count=1)

# 2. Topic 02
p2 = r'<div class="narrative-connector-bridge">\s*<i class="fa-solid fa-arrow-right-long"></i>\s*<span><strong>สะพานเชื่อมโยงข้อมูล:</strong> บนพื้นที่กว่า 2,791 ไร่'
r2 = r'<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-03" aria-label="อ่านต่อหัวข้อถัดไป: 26 คณะวิชา 4 คลัสเตอร์">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> บนพื้นที่กว่า 2,791 ไร่'
assert re.search(p2, text), "Bridge 2 pattern not found"
text = re.sub(p2, r2, text, count=1)

# 3. Topic 03
p3 = r'(\s*</div>\s*</div>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-graduation-cap"></i>)'
r3 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-04" aria-label="อ่านต่อหัวข้อถัดไป: โครงสร้างประชากรนักศึกษาและบุคลากร">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> จากความหลากหลายของ 26 คณะวิชา มหาวิทยาลัยขับเคลื่อนด้วยพลังคนกว่า 44,000 ชีวิต ซึ่งสะท้อนโครงสร้างประชากรและความเสมอภาคทางเพศในทุกระดับ</span>\n        </div>\n        \2'
assert re.search(p3, text), "Bridge 3 pattern not found"
text = re.sub(p3, r3, text, count=1)

# 4. Topic 04
p4 = r'(\s*</div>\s*</div>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-users-viewfinder"></i>)'
r4 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-05" aria-label="อ่านต่อหัวข้อถัดไป: การเปลี่ยนผ่านสู่มหาวิทยาลัยวิจัยและการกระจายตัวของวิทยาเขต">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> เบื้องหลังประชากรนักศึกษาที่ขยายตัว คือการเปลี่ยนผ่านพื้นที่การเรียนรู้ครั้งประวัติศาสตร์ โดยศูนย์รังสิตก้าวขึ้นเป็นหัวใจหลักรองรับนักศึกษากว่า 32,800 คน</span>\n        </div>\n        \2'
assert re.search(p4, text), "Bridge 4 pattern not found"
text = re.sub(p4, r4, text, count=1)

# 5. Topic 05
p5 = r'(\s*</div>\s*</div>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-route"></i>)'
r5 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-06" aria-label="อ่านต่อหัวข้อถัดไป: การบริหารงบประมาณและเสถียรภาพทางการเงิน">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> การขยายตัวของวิทยาเขตและโครงสร้างพื้นฐานวิจัยระดับโลก ได้รับการสนับสนุนจากวินัยทางการเงินและงบประมาณกว่า 1.2 หมื่นล้านบาทต่อปี</span>\n        </div>\n        \2'
assert re.search(p5, text), "Bridge 5 pattern not found"
text = re.sub(p5, r5, text, count=1)

# 6. Topic 06
p6 = r'(\s*</div>\s*</div>\s*</div>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-coins"></i>)'
r6 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-07" aria-label="อ่านต่อหัวข้อถัดไป: มาตรฐานระดับโลก: การจัดอันดับมหาวิทยาลัยและ Triple Crown Accreditation">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> การลงทุนทางปัญญาและการบริหารการคลังที่มั่นคง ผลิดอกออกผลเป็นความเป็นเลิศระดับสากล และการได้รับการรับรองมาตรฐาน Triple Crown ระดับโลก</span>\n        </div>\n        \2'
assert re.search(p6, text), "Bridge 6 pattern not found"
text = re.sub(p6, r6, text, count=1)

# 7. Topic 07
p7 = r'(\s*</table>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-award"></i>)'
r7 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-08" aria-label="อ่านต่อหัวข้อถัดไป: ธรรมศาสตร์เพื่อสังคมและการพัฒนาที่ยั่งยืน: SDG Impact">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> นอกเหนือจากความเป็นเลิศทางวิชาการระดับโลก ธรรมศาสตร์ยังคงยึดมั่นในอุดมการณ์เพื่อประชาชน โดยบูรณาการเป้าหมาย SDG สู่ทุกมิติของการพัฒนา</span>\n        </div>\n        \2'
assert re.search(p7, text), "Bridge 7 pattern not found"
text = re.sub(p7, r7, text, count=1)

# 8. Topic 08
p8 = r'(\s*</div>\s*</div>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-leaf"></i>)'
r8 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-09" aria-label="อ่านต่อหัวข้อถัดไป: โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ: ที่พึ่งทางสุขภาพของประชาชน">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> ความยั่งยืนของสังคมไม่อาจสมบูรณ์ได้หากปราศจากสุขภาวะที่ดี โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติจึงเป็นเสาหลักที่พร้อมดูแลผู้ป่วยกว่า 1.4 ล้านรายต่อปี</span>\n        </div>\n        \2'
assert re.search(p8, text), "Bridge 8 pattern not found"
text = re.sub(p8, r8, text, count=1)

# 9. Topic 09
p9 = r'(\s*</div>\s*</div>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-hospital"></i>)'
r9 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#topic-10" aria-label="อ่านต่อหัวข้อถัดไป: TU 2034: ก้าวสู่ศตวรรษที่ 2 อย่างยั่งยืน">\n          <i class="fa-solid fa-arrow-right-long"></i>\n          <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> จากอดีตสู่ปัจจุบัน และจากพลังการดูแลสุขภาพสู่ก้าวต่อไป มหาวิทยาลัยธรรมศาสตร์พร้อมมุ่งสู่วิสัยทัศน์ TU 2034 สู่ศตวรรษแห่งความยั่งยืน</span>\n        </div>\n        \2'
assert re.search(p9, text), "Bridge 9 pattern not found"
text = re.sub(p9, r9, text, count=1)

# 10. Topic 10
p10 = r'(\s*</div>\s*</div>\s*)(<div class="section-source-citation">\s*<i class="fa-solid fa-compass"></i>)'
r10 = r'\1<div class="narrative-connector-bridge" role="button" tabindex="0" data-next-target="#finish" aria-label="ไปยังบทสรุปและแบบทดสอบส่งท้าย">\n        <i class="fa-solid fa-arrow-right-long"></i>\n        <span><strong>สะพานเชื่อมโยงข้อมูล:</strong> สำรวจบทสรุปภาพรวมทั้งหมด และร่วมทดสอบความรู้เพื่อรับประกาศนียบัตรผู้นำการเรียนรู้ 90 ปี มหาวิทยาลัยธรรมศาสตร์</span>\n      </div>\n      \2'
assert re.search(p10, text), "Bridge 10 pattern not found"
text = re.sub(p10, r10, text, count=1)

# Update cache buster versions to v20261029v9
text = text.replace('scroll-story.css?v=20261029v8', 'scroll-story.css?v=20261029v9')
text = text.replace('scroll-story-v8-overrides.css?v=20261029v8', 'scroll-story-v8-overrides.css?v=20261029v9')
text = text.replace('scroll-story.js?v=20261029v8', 'scroll-story.js?v=20261029v9')
text = text.replace('app.js?v=20261028', 'app.js?v=20261029v9')
text = text.replace('tu-interactive.js?v=20261029v8', 'tu-interactive.js?v=20261029v9')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("index.html updated successfully with all 10 narrative connector bridges and cache busters!")
