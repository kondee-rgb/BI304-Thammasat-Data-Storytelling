import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

for root, _, files in os.walk('assets/css'):
    for f in files:
        if f.endswith('.css'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fh:
                txt = fh.read()
            if 'editorial-hero' in txt or 'tu-student-walker' in txt or '1934' in txt:
                print(f"=== {p} ===")
                for m in re.finditer(r'([^{}]*(?:editorial-hero|student-leader|student-walker|arch)[^{}]*\{[^{}]*\})', txt):
                    print(m.group(0).strip())
