import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'class="section-source-citation"' in line:
        print(f"Line {idx+1}:")
        start = max(0, idx - 4)
        end = min(len(lines), idx + 6)
        for j in range(start, end):
            print(f"  {j+1}: {lines[j]}", end='')
        print("-" * 50)
