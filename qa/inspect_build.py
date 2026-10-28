import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('assets/js/scroll-story.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function buildModule\(.*?\n  \}', text, re.DOTALL)
if m:
    print(m.group(0))
