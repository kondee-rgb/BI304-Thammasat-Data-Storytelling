import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'setMilestoneStep' in l:
        print(''.join(lines[max(0, i-2):min(len(lines), i+25)]))
        break
