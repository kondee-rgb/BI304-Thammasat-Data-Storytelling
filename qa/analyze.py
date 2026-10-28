import re

with open('d:/BI304/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sections = re.findall(r'<section[^>]+id="([^"]+)"', content)
print('Sections:', sections)
print('Total sections:', len(sections))

lines = content.split('\n')
total_lines = len(lines)
print(f'Total lines in index.html: {total_lines}')

# check for existing nav
nav_matches = re.findall(r'class="([^"]*nav[^"]*)"', content)
print('Nav classes found:', list(set(nav_matches))[:10])

# check existing script/css includes
includes = re.findall(r'<(?:link|script)[^>]+(?:href|src)="([^"]+)"', content)
print('Includes:', includes[:30])
