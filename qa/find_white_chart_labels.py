import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'new Chart\([^,]+,\s*\{[\s\S]*?(?=\n\s*(?:const|let|function)\s+[a-zA-Z]|\Z)', text):
    chart_code = m.group(0)
    for color_m in re.finditer(r'color:\s*[\'\"#a-zA-Z0-9]+', chart_code):
        color_str = color_m.group(0)
        if '#fff' in color_str.lower() or 'white' in color_str.lower():
            start = max(0, color_m.start() - 60)
            end = min(len(chart_code), color_m.end() + 60)
            print('Found white color in chart:\n', chart_code[start:end], '\n---')
