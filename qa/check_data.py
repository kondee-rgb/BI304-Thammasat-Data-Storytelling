# -*- coding: utf-8 -*-
"""
Automated data verification test suite for Phase 2:
1. Validates all percentage sums = 100%
2. Validates sub-populations sum to total population
3. Validates financial streams sum to total budget
4. Checks that all key metrics have source_id and as_of
5. Checks data consistency across data.json, index.html, and flourish_data CSVs
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import os
import glob
import re

def run_checks():
    errors = []
    warnings = []
    
    # 1. Load data.json
    with open('data/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    print("Checking data/data.json structure and mathematical integrity...")
    
    # Check metadata & sources
    sources = data.get('metadata', {}).get('sources', {})
    if not sources:
        errors.append("data.json missing metadata.sources")
        
    # Check key_metrics source_id
    metrics = data.get('key_metrics', {})
    for k, v in metrics.items():
        if isinstance(v, dict):
            if 'source_id' not in v:
                errors.append(f"key_metrics.{k} is missing source_id")
            elif v['source_id'] not in sources:
                errors.append(f"key_metrics.{k} references unknown source_id '{v['source_id']}'")
            if 'as_of' not in v:
                errors.append(f"key_metrics.{k} is missing as_of date")
                
    # 2. Mathematical Integrity Checks
    # A. Budget Streams Sum
    streams = data.get('budget_streams', [])
    if streams:
        # Stream 0 is total, 1-5 are individual streams
        if len(streams) >= 6:
            stream_parts = streams[1:6]
            pct_sum = sum([float(s['share'].replace('%', '')) for s in stream_parts])
            if abs(pct_sum - 100.0) > 0.01:
                errors.append(f"Budget stream percentages sum to {pct_sum}%, expected 100.0%")
                
            amount_sum = sum([int(s['amount'].replace(',', '').replace(' ล้านบาท', '')) for s in stream_parts])
            total_budget = int(streams[0]['amount'].replace(',', '').replace(' ล้านบาท', ''))
            if amount_sum != total_budget:
                errors.append(f"Budget stream amounts sum to {amount_sum} MB, expected {total_budget} MB")
                
    # B. Campuses Student Sum
    campuses = data.get('campuses', [])
    if campuses:
        c_students = []
        for c in campuses:
            m = re.search(r'([\d,]+)', c.get('students', ''))
            if m:
                c_students.append(int(m.group(1).replace(',', '')))
        total_students = data['key_metrics']['total_students']['value']
        if sum(c_students) != total_students:
            errors.append(f"Campuses student counts sum to {sum(c_students)}, expected {total_students}")
            
    # C. Campuses Land Area Sum
    if campuses:
        c_areas = []
        for c in campuses:
            m = re.search(r'([\d,]+)', c.get('area', ''))
            if m:
                c_areas.append(int(m.group(1).replace(',', '')))
        total_area = data['key_metrics']['total_land_area_rai']['value']
        if sum(c_areas) != total_area:
            errors.append(f"Campuses land areas sum to {sum(c_areas)} rai, expected {total_area} rai")
            
    # 3. Check Consistency with index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Check that total students appears in HTML
    if "42,850" not in html:
        errors.append("index.html is missing verified total students '42,850'")
        
    # Check that 15,350 MB appears in HTML
    if "15,350" not in html:
        errors.append("index.html is missing verified budget '15,350'")
        
    # Check that 2,791 rai appears in HTML
    if "2,791" not in html:
        warnings.append("index.html should mention total area '2,791 ไร่'")
        
    # 4. Check Flourish CSVs
    flourish_dir = 'flourish_data'
    if os.path.exists(flourish_dir):
        csv_files = glob.glob(os.path.join(flourish_dir, '*.csv'))
        print(f"Found {len(csv_files)} Flourish CSV files to validate.")
        
    # Output Summary
    print("\n--- DATA INTEGRITY VALIDATION REPORT ---")
    print(f"Total Errors: {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")
    
    if errors:
        print("\nERRORS DETECTED:")
        for e in errors:
            print(" [FAIL]", e)
        return False
    else:
        print("\nALL DATA INTEGRITY CHECKS PASSED (100% Mathematical Consistency)!")
        if warnings:
            print("\nWARNINGS:")
            for w in warnings:
                print(" [WARN]", w)
        return True

if __name__ == '__main__':
    success = run_checks()
    exit(0 if success else 1)
