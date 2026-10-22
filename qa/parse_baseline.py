# -*- coding: utf-8 -*-
import json
import os
import glob

with open('qa/baseline_lighthouse_mobile.json', 'r', encoding='utf-8') as f:
    mob = json.load(f)

with open('qa/baseline_lighthouse_desktop.json', 'r', encoding='utf-8') as f:
    desk = json.load(f)

def extract_summary(data):
    cats = data.get('categories', {})
    audits = data.get('audits', {})
    
    return {
        'scores': {
            'performance': int((cats.get('performance', {}).get('score') or 0) * 100),
            'accessibility': int((cats.get('accessibility', {}).get('score') or 0) * 100),
            'best_practices': int((cats.get('best-practices', {}).get('score') or 0) * 100),
            'seo': int((cats.get('seo', {}).get('score') or 0) * 100),
        },
        'metrics': {
            'FCP': audits.get('first-contentful-paint', {}).get('displayValue'),
            'LCP': audits.get('largest-contentful-paint', {}).get('displayValue'),
            'CLS': audits.get('cumulative-layout-shift', {}).get('displayValue'),
            'TBT': audits.get('total-blocking-time', {}).get('displayValue'),
            'SpeedIndex': audits.get('speed-index', {}).get('displayValue')
        },
        'page_weight': {
            'total_bytes': audits.get('total-byte-weight', {}).get('numericValue'),
            'total_display': audits.get('total-byte-weight', {}).get('displayValue')
        }
    }

# Asset statistics
assets_stats = {}
total_asset_bytes = 0
for f in glob.glob('assets/*'):
    if os.path.isfile(f):
        sz = os.path.getsize(f)
        assets_stats[os.path.basename(f)] = sz
        total_asset_bytes += sz

summary = {
    'audit_date': '2026-10-22T14:41:00+07:00',
    'url': 'http://localhost:8080/index.html',
    'tag': 'v1-baseline',
    'mobile': extract_summary(mob),
    'desktop': extract_summary(desk),
    'assets': {
        'count': len(assets_stats),
        'total_bytes': total_asset_bytes,
        'total_kb': round(total_asset_bytes / 1024, 2),
        'total_mb': round(total_asset_bytes / (1024 * 1024), 2),
        'details': assets_stats
    },
    'index_html_size_bytes': os.path.getsize('index.html'),
    'index_html_size_kb': round(os.path.getsize('index.html') / 1024, 2)
}

with open('qa/baseline_lighthouse.json', 'w', encoding='utf-8') as out:
    json.dump(summary, out, indent=2, ensure_ascii=False)

print("Saved qa/baseline_lighthouse.json successfully!")
print("Mobile Scores:", summary['mobile']['scores'])
print("Desktop Scores:", summary['desktop']['scores'])
print("Assets count:", summary['assets']['count'], "Total MB:", summary['assets']['total_mb'])
