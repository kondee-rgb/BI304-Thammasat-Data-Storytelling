import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bridges = list(re.finditer(r'<div class="narrative-connector-bridge"[^>]*>[\s\S]*?</div>', text))
print(f'Total narrative-connector-bridge elements: {len(bridges)}')
for i, b in enumerate(bridges):
    line = text.count('\n', 0, b.start()) + 1
    content = re.sub(r'\s+', ' ', b.group(0))[:120]
    print(f'Bridge {i+1} at L{line}: {content}...')
