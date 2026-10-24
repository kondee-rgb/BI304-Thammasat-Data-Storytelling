# -*- coding: utf-8 -*-
"""
Helper script to update build_v2_bidwells.py to:
1. Feature all 10 topics as dedicated, beautifully styled sections matching the classic version:
   - Topic 01: ปฐมบท 2477: ตลาดวิชาเพื่อราษฎรสู่ 4.2 หมื่นคน
   - Topic 02: การกระจายโอกาสสู่ภูมิภาค: 4 ศูนย์การศึกษา
   - Topic 03: 26 คณะวิชา 4 คลัสเตอร์วิชาการ: ความหลากหลายทางปัญญา & TCAS
   - Topic 04: โครงสร้างประชากรนักศึกษาและความหลากหลายทางเพศภาวะ
   - Topic 05: สายธารแห่งการโยกย้าย: กำเนิดศูนย์รังสิตและเครือข่าย
   - Topic 06: ความมั่นคงทางการคลัง: วินัยงบประมาณ 15,350 ล้านบาท
   - Topic 07: ก้าวสู่เวทีโลก: อันดับ QS Asia ทะยานสู่ Top 70 & Triple Crown
   - Topic 08: มหาวิทยาลัยสีเขียว: ผู้นำโลกด้านความยั่งยืน SDG 11 & สวนป๋วย 100 ปี
   - Topic 09: รพ.ธรรมศาสตร์: ที่พึ่งแห่งประชาชนในยามวิกฤต
   - Topic 10: วิสัยทัศน์ TU 2034: ก้าวสู่ 100 ปีแห่งปัญญาและความยั่งยืน
2. Completely remove all download forms, cards, and modals.
3. Update the navigation bar and bottom scrubber pill for all 10 topics.
"""

import re
import os

def update_builder():
    path = r'd:\BI304\build_v2_bidwells.py'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS
    # Add Green section, Hospital section, Finish Milestone Card, and Scrubber Topic Indicator styles
    extra_css = '''
    /* ==========================================================================
       TOPIC 8: GREEN CAMPUS & SDG 11 LEADERSHIP
       ========================================================================== */
    .bidwells-green-section {
      background: radial-gradient(circle at 80% 20%, #0d2822 0%, #061517 100%);
      color: #ffffff;
      padding: 110px 2rem 100px;
      position: relative;
      border-top: 4px solid #10b981;
    }

    .green-container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .green-highlight-box {
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 20px;
      padding: 28px 36px;
      margin-bottom: 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    .green-sdg-badge {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .green-sdg-num {
      width: 64px;
      height: 64px;
      border-radius: 14px;
      background: #10b981;
      color: #061517;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 1.4rem;
      line-height: 1;
    }

    .green-cards-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }

    .green-card-item {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 26px 22px;
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .green-card-item:hover {
      background: rgba(255, 255, 255, 0.08);
      transform: translateY(-4px);
      border-color: #10b981;
      box-shadow: 0 10px 25px rgba(16, 185, 129, 0.15);
    }

    .green-card-icon {
      font-size: 1.8rem;
      color: #10b981;
      margin-bottom: 12px;
    }

    .green-card-title {
      font-size: 1.12rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .green-card-desc {
      font-size: 0.85rem;
      color: #94a3b8;
      line-height: 1.6;
    }

    .green-card-stat {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--tu-gold);
      margin-top: 16px;
    }

    /* ==========================================================================
       TOPIC 9: THAMMASAT HOSPITAL & MEDICAL HUB
       ========================================================================== */
    .bidwells-hospital-section {
      background: #ffffff;
      padding: 110px 2rem 100px;
      position: relative;
      border-top: 4px solid var(--bidwells-crimson);
    }

    .hospital-container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .hospital-kpi-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-bottom: 36px;
    }

    .hospital-kpi-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 24px;
      border-top: 4px solid var(--bidwells-crimson);
      transition: all 0.25s ease;
    }

    .hospital-kpi-card:hover {
      box-shadow: 0 10px 25px rgba(0,0,0,0.06);
      transform: translateY(-3px);
    }

    .hospital-kpi-num {
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--bidwells-crimson);
      line-height: 1.1;
    }

    .hospital-kpi-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      margin-top: 6px;
    }

    .hospital-kpi-desc {
      font-size: 0.82rem;
      color: #64748b;
      margin-top: 4px;
      line-height: 1.5;
    }

    .hospital-centers-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    .hospital-center-item {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 18px;
      padding: 26px 28px;
      display: flex;
      gap: 20px;
      align-items: flex-start;
      transition: all 0.25s ease;
    }

    .hospital-center-item:hover {
      border-color: #cbd5e1;
      background: #ffffff;
      box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    }

    .hospital-center-icon {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      background: rgba(197, 25, 68, 0.1);
      color: var(--bidwells-crimson);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.45rem;
      flex-shrink: 0;
    }

    /* ==========================================================================
       FINISH MILESTONE CELEBRATION (STRICTLY NO DOWNLOAD FORM)
       ========================================================================== */
    .finish-milestone-card {
      max-width: 960px;
      margin: 0 auto;
      background: #ffffff;
      border-radius: 28px;
      padding: 50px 60px;
      box-shadow: var(--bidwells-shadow-lg);
      border: 1px solid rgba(0, 0, 0, 0.08);
      position: relative;
      text-align: center;
    }

    .finish-milestone-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 18px;
      border-radius: 9999px;
      background: rgba(255, 199, 44, 0.18);
      color: #92400e;
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 16px;
    }

    .finish-milestone-title {
      font-family: var(--font-serif);
      font-size: 2.4rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      line-height: 1.25;
      margin-bottom: 12px;
    }

    .finish-milestone-sub {
      font-size: 1.05rem;
      color: #64748b;
      max-width: 720px;
      margin: 0 auto 36px;
      line-height: 1.7;
    }

    .milestone-summary-row {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 18px;
      padding: 24px 16px;
      margin-bottom: 36px;
    }

    .milestone-summary-item .num {
      font-size: 1.7rem;
      font-weight: 800;
      color: var(--bidwells-crimson);
      line-height: 1.1;
    }

    .milestone-summary-item .lbl {
      font-size: 0.76rem;
      font-weight: 600;
      color: #64748b;
      margin-top: 4px;
    }

    .milestone-quote-box {
      background: linear-gradient(135deg, rgba(11,22,59,0.03) 0%, rgba(197,25,68,0.04) 100%);
      border-left: 4px solid var(--tu-gold);
      border-radius: 0 16px 16px 0;
      padding: 20px 24px;
      text-align: left;
      margin-bottom: 36px;
    }

    .milestone-quote-text {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: 1.08rem;
      color: var(--bidwells-navy);
      line-height: 1.6;
    }

    .milestone-quote-author {
      font-size: 0.84rem;
      font-weight: 700;
      color: #64748b;
      margin-top: 8px;
    }

    .milestone-actions-group {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .scrubber-topic-indicator {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      background: #f1f5f9;
      padding: 6px 14px;
      border-radius: 9999px;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .scrubber-topic-indicator .pip-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--bidwells-crimson);
      box-shadow: 0 0 8px var(--bidwells-crimson);
    }
    '''

    # Replace download CSS and insert extra CSS
    old_download_css_pattern = re.compile(r'/\* Download Report Full Box .*?\.btn-submit-download:hover \{[^}]*\}', re.DOTALL)
    if old_download_css_pattern.search(content):
        content = old_download_css_pattern.sub(extra_css.strip(), content, count=1)
    else:
        # Fallback append before </style>
        content = content.replace('</style>', extra_css + '\n  </style>', 1)

    print("Updated CSS successfully.")

update_builder()
