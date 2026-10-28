import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect Topic 01 bridge:
m1 = re.search(r'<div class="narrative-connector-bridge">[\s\S]*?</div>', content)
if m1:
    print("Found Bridge 1:", m1.group(0))

m2 = re.search(r'<div class="narrative-connector-bridge">[\s\S]*?</div>', content[m1.end():])
if m2:
    print("Found Bridge 2:", m2.group(0))
