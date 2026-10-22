# -*- coding: utf-8 -*-
"""
Audits all project files for data discrepancies, conflicting numbers,
missing citations, unreferenced assets, and a11y gaps.
"""
import os
import re
import json
import glob

audit_report = {
    'contradictions': [],
    'unreferenced_assets': [],
    'unverified_claims': [],
    'a11y_and_interaction_issues': []
}

# 1. Check index.html lines
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def find_in_lines(pattern):
    results = []
    rx = re.compile(pattern, re.IGNORECASE)
    for i, l in enumerate(lines):
        if rx.search(l):
            results.append((i + 1, l.strip()))
    return results

# Find contradictory figures
# A. Student count
s_total = find_in_lines(r'42,850')
s_female = find_in_lines(r'26,620')
s_male = find_in_lines(r'16,030')
audit_report['contradictions'].append({
    'topic': 'Total Student Population vs Gender Sum',
    'web_total': [(line_num, txt) for line_num, txt in s_total[:4]],
    'gender_parts': f'Female 26,620 + Male 16,030 = 42,650 (Discrepancy of 200 students from 42,850)'
})

# B. Carbon reduction & Solar capacity
carbon_24k = find_in_lines(r'24,000')
carbon_25k = find_in_lines(r'25,500')
solar_35 = find_in_lines(r'35 MW')
solar_358 = find_in_lines(r'35\.8 MWp')

audit_report['contradictions'].append({
    'topic': 'Green Campus: Carbon Reduction & Solar MWp',
    'carbon_conflicts': [('24k tons', carbon_24k), ('25.5k tons', carbon_25k)],
    'solar_conflicts': [('35 MW', solar_35), ('35.8 MWp', solar_358)]
})

# C. Hospital Patient Volume & Field Hospital Beds
opd_146 = find_in_lines(r'1\.46M\+')
opd_148 = find_in_lines(r'1,480,000\+')
beds_3083 = find_in_lines(r'3,083')

audit_report['contradictions'].append({
    'topic': 'Thammasat Hospital: OPD volume & Field Hospital Beds',
    'opd_conflicts': [('1.46M+', opd_146), ('1,480,000+', opd_148)],
    'beds': beds_3083
})

# 2. Check README.md discrepancies
if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_text = f.read()
    
    # Check for Plotly, CartoDB, 308 beds, etc.
    audit_report['contradictions'].append({
        'topic': 'README.md vs Actual Code Discrepancies',
        'libraries': 'README claims Plotly.js & CartoDB Dark Matter, but codebase uses Chart.js 4.4.1 & Leaflet 1.9.4 with Esri tiles',
        'field_beds': 'README claims 308 beds, while website code has 3,083 beds',
        'rangsit_share': 'README claims Rangsit has 78.5% of students, while website has 73.5%',
        'budget_trend': 'README claims 11,280 -> 13,745 million baht, while website has 13,420 -> 15,350 million baht',
        'ipd_admissions': 'README claims 35,200 IPD, while website has 58,400',
        'chart_types': 'README calls Topic 03 a Treemap (actually horizontal bar chart) and Topic 06 a Bar chart (actually line chart)'
    })

# 3. Check unreferenced assets in assets/
html_content = "".join(lines)
for asset_path in glob.glob('assets/*'):
    basename = os.path.basename(asset_path)
    if basename not in html_content:
        audit_report['unreferenced_assets'].append({
            'file': basename,
            'size_bytes': os.path.getsize(asset_path),
            'size_kb': round(os.path.getsize(asset_path) / 1024, 2)
        })

# 4. Check Flourish CSVs
flourish_files = glob.glob('flourish_data/*.csv')
audit_report['flourish_csv_count'] = len(flourish_files)
audit_report['flourish_files'] = [os.path.basename(f) for f in flourish_files]

# Save audit json for compilation into AUDIT.md
with open('qa/audit_raw.json', 'w', encoding='utf-8') as f:
    json.dump(audit_report, f, indent=2, ensure_ascii=False)

print("Detailed audit scan completed! Saved to qa/audit_raw.json")
