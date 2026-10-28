import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 44688
print(text[pos-100:pos+600])
