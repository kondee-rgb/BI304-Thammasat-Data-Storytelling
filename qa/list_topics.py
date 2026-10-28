with open('assets/js/scroll-story.js', 'r', encoding='utf-8') as f:
    text = f.read()
import re
keys = re.findall(r"'topic-(\d\d)':", text)
print('Topics in STORIES:', keys)
