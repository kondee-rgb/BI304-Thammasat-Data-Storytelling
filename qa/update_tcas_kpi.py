import re

def update_tcas():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    target = """          <div class="fac-kpi-item tu-reveal-slide-up tu-stagger-3">
            <div class="kpi-num stat-counter" style="color: #0369a1;" data-counter-prefix="1 : ">14.0 <span class="unit">อัตราแข่งขัน</span></div>
            <div class="kpi-lbl">อัตราการแข่งขันสูงสุด</div>
          </div>"""

    replacement = """          <div class="fac-kpi-item tu-reveal-slide-up tu-stagger-3" title="อัตราการแข่งขันสูงสุด: วิทยาลัยแพทยศาสตร์นานาชาติจุฬาภรณ์ (CICM) มีอัตราส่วน 1 ที่นั่ง ต่อ ผู้สมัคร 14.0 คน (1 : 14.0)">
            <div class="kpi-num stat-counter" style="color: #0369a1;" data-counter-prefix="1 : ">14.0 <span class="unit" style="font-size: 0.92rem; font-weight: 700; color: #0284c7;">(1 ต่อ 14 คน)</span></div>
            <div class="kpi-lbl">อัตราการแข่งขันสูงสุด • CICM แพทย์อินเตอร์</div>
          </div>"""

    if target in html:
        new_html = html.replace(target, replacement)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully updated Topic 03 TCAS KPI in index.html")
    else:
        # Check normalized line endings
        target_norm = target.replace('\r\n', '\n')
        html_norm = html.replace('\r\n', '\n')
        if target_norm in html_norm:
            new_html = html_norm.replace(target_norm, replacement)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_html)
            print("Successfully updated Topic 03 TCAS KPI (normalized) in index.html")
        else:
            print("Could not find exact target string in index.html!")

if __name__ == '__main__':
    update_tcas()
