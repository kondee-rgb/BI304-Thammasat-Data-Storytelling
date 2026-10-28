import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/scroll-story.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r"'topic-04':\s*\{[\s\S]*?(?=\n\s*'topic-05':)", text)
if m:
    print(m.group(0))
else:
    print("topic-04 story not found")
