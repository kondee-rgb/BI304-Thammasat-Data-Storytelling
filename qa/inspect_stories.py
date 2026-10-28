import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/scroll-story.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find STORIES array
match = re.search(r'const STORIES = \[(.*?)\];\s*function', text, re.DOTALL)
if match:
    stories_code = match.group(1)
    # Find each topic block
    blocks = re.findall(r'id:\s*[\'"]([^\'"]+)[\'"].*?title:\s*[\'"]([^\'"]+)[\'"].*?steps:\s*\[(.*?)\]\s*\}', stories_code, re.DOTALL)
    for b_id, b_title, b_steps in blocks:
        step_count = len(re.findall(r'\{\s*type:', b_steps))
        print(f'Topic: {b_id} | Title: {b_title} | Steps: {step_count}')
