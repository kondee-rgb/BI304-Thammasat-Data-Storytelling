import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for t_num in range(3, 10):
    t_id = f"topic-{t_num:02d}"
    m = re.search(rf'<section[^>]*id=["\']{t_id}["\'][\s\S]*?(?=<!-- =+|<section[^>]*id=["\']topic-|\Z)', text)
    if m:
        sec = m.group(0)
        cit_m = re.search(r'<div class=["\']section-source-citation["\'][^>]*>[\s\S]*?</div>', sec)
        if cit_m:
            print(f"{t_id}: citation found:\n{cit_m.group(0)[:120]}...\n")
        else:
            print(f"{t_id}: NO citation found")
