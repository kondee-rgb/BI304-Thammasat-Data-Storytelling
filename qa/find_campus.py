import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function\s+selectCampus\b[\s\S]*?(?=\n\s*function|\Z)', text)
if m:
    print("selectCampus found:\n", m.group(0)[:500])
else:
    print("selectCampus not found, searching campus click handlers:")
    for m in re.finditer(r'selectCampus|\.campus-card|\.campus-metric', text):
        print("Found:", m.group(0), "at pos", m.start())
