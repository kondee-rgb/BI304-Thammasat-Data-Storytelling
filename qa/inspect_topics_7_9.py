import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

targets = ['id="topic-07"', 'id="topic-08"', 'id="topic-09"', 'id="topic-10"']
for i, line in enumerate(lines):
    if any(t in line for t in targets):
        print(f'L{i+1}: {line.strip()[:100]}')
        for j in range(max(0, i-2), min(len(lines), i+20)):
            print(f'   {j+1}: {lines[j].rstrip()}')
        print('='*50)
