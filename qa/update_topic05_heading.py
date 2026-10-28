import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_s = '<h3 style="font-size: 1.15rem; font-weight: 700; color: #ffffff;">การกระจายสัดส่วนนักศึกษาตามยุคสมัย (Campus Distribution Shift)</h3>'
new_s = '<h3 style="font-size: 1.18rem; font-weight: 700; color: #0f172a;">การกระจายสัดส่วนนักศึกษาตามยุคสมัย (Campus Distribution Shift)</h3>'
assert old_s in text, 'old_s not found'
text = text.replace(old_s, new_s)

old_p = '<p style="font-size: 0.85rem; color: #94a3b8;">เปรียบเทียบสัดส่วน 4 ศูนย์การศึกษาตั้งแต่ พ.ศ. 2500 ถึง พ.ศ. 2567</p>'
new_p = '<p style="font-size: 0.88rem; color: #475569; margin-top: 3px;">เปรียบเทียบสัดส่วน 4 ศูนย์การศึกษา: ศูนย์ท่าพระจันทร์ • ศูนย์รังสิต • ศูนย์ลำปาง • ศูนย์พัทยา (พ.ศ. 2500 ถึง พ.ศ. 2567)</p>'
assert old_p in text, 'old_p not found'
text = text.replace(old_p, new_p)

# Also update canvas height to 255px for better breathing room
text = text.replace('<div class="tu-reveal-scale" style="height: 240px;">', '<div class="tu-reveal-scale" style="height: 255px;">')

# Update cache buster to v20261029v11
text = text.replace('v=20261029v10', 'v=20261029v11')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated index.html for Campus Distribution Shift heading, subtitle, and legend!")
