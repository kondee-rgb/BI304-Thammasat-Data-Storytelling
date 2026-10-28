import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find each topic
topic_matches = list(re.finditer(r'<section[^>]*id=["\']topic-(\d+)["\']', text))
for i, m in enumerate(topic_matches):
    start = m.start()
    end = topic_matches[i+1].start() if i + 1 < len(topic_matches) else len(text)
    num = m.group(1)
    chunk = text[start:end]
    has_bridge = 'narrative-connector-bridge' in chunk
    has_citation = 'section-source-citation' in chunk
    # let's see last 400 chars of chunk before section closing
    last_divs = re.findall(r'<div class=["\']([^"\']+)["\']', chunk)[-4:]
    print(f"Topic {num}: bridge={has_bridge}, citation={has_citation}, last_classes={last_divs}")
