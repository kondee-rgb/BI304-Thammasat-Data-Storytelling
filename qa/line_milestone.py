with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function setMilestoneStep', text)
if m:
    line = text.count('\n', 0, m.start()) + 1
    print('Line:', line)
