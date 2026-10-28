import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

topics = re.findall(r'(<section[^>]*id="(topic-\d\d)"[^>]*>.*?)(?=<section|\Z)', text, re.DOTALL)
print(f'Found {len(topics)} topic sections')
for t_full, t_id in topics:
    eyebrow = re.search(r'class="section-eyebrow"[^>]*>(.*?)</div>', t_full)
    headline = re.search(r'class="section-headline"[^>]*>(.*?)</h2>', t_full, re.DOTALL)
    lead = re.search(r'class="section-lead"[^>]*>(.*?)</p>', t_full, re.DOTALL)
    
    eb_text = re.sub(r'<[^>]+>', '', eyebrow.group(1)).strip() if eyebrow else 'NONE'
    hl_text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', headline.group(1))).strip() if headline else 'NONE'
    ld_text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', lead.group(1))).strip()[:70] if lead else 'NONE'
    print(f'[{t_id}]')
    print(f'  Eyebrow: {eb_text}')
    print(f'  Headline: {hl_text}')
    print(f'  Lead: {ld_text}...')
