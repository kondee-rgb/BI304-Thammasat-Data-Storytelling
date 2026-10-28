import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function\s+selectCampusCluster\b[\s\S]*?(?=\n\s*function|\Z)', text)
if m:
    print(m.group(0)[:800])
