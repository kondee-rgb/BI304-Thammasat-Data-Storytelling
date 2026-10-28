with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function setMilestoneStep\(.*?\n\}', text, re.DOTALL)
if m:
    print(m.group(0))
