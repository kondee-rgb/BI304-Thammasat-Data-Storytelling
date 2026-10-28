import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'new Chart\(([^,]+),', text):
    canvas_id = m.group(1).strip()
    chart_end = text.find('new Chart', m.end())
    if chart_end == -1:
        chart_end = len(text)
    chunk = text[m.start():m.start()+1500]
    if '#ffffff' in chunk or '#fff' in chunk:
        print(f"Canvas: {canvas_id}")
        for line in chunk.split('\n'):
            if 'color:' in line and ('#fff' in line.lower() or 'white' in line.lower()):
                print("   ", line.strip())
