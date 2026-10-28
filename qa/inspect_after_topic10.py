import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section[^>]*id=["\']topic-10["\'][\s\S]*?(?=<section[^>]*id=|\Z)', text)
if m:
    print("End of topic-10 found, length:", len(m.group(0)))
    # find next sections
    pos = m.end()
    next_secs = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text[pos:pos+3000])
    print("Next sections after topic-10:", next_secs)
