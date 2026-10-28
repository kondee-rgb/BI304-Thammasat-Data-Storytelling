import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ctxDist = document\.getElementById\(\'campusDistributionCanvas\'\);[\s\S]*?(?=\n\s*(?:const|function|let)\s+[a-zA-Z]|\Z)', text)
if m:
    print(m.group(0))
