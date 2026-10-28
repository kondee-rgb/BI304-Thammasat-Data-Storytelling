import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

topics = re.findall(r'(<section[^>]*id="(topic-\d\d)"[^>]*>.*?)(?=<section|\Z)', text, re.DOTALL)
for t_full, t_id in topics:
    h_tags = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', t_full, re.DOTALL)
    clean_h = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h)).strip() for h in h_tags[:3]]
    print(f'[{t_id}] headings: {clean_h}')
