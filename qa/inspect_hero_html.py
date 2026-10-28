import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section[^>]*id=["\']hero["\'][\s\S]*?(?=</section>)', text)
if m:
    print(m.group(0))
else:
    print("Hero section not found")
