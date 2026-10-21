import os

# Builder for Version 2: Bidwells Scrollytelling High-Fidelity Template
# Designed to faithfully replicate the Bidwells "Driving Innovation at Speed" experience
# for "90 Years of Thammasat University" Data Storytelling (BI304 TBS)
#
# Key Architectural Features:
# 1. 100% Standalone Version 2 in d:/BI304/index.html (no version switcher clutter)
# 2. Version 1 safely archived in d:/BI304/v1/index.html
# 3. Continuous vertical timeline road/track with the animated walking Thammasat student character
# 4. Semi-realistic Tha Prachan Dome & River twilight graphic backdrop (assets/tha_prachan_dome_editorial.jpg)
# 5. Fullscreen cinematic Hero section with Bidwells-style giant typography
# 6. Sticky visual viewport + editorial story column with big stat callouts
# 7. 10 Upgraded visual scenes as specified by user
# 8. 100% Free Open-Source Libraries (Plotly, Leaflet, CartoDB Dark Matter, FontAwesome 6, Google Fonts)

def build_bidwells_v2():
    html = '''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
  <meta name="theme-color" content="#0B0F17" />
  <title>90 ปี มหาวิทยาลัยธรรมศาสตร์: จากตลาดวิชาสู่มหาวิทยาลัยวิจัยระดับโลกเพื่อประชาชน | BI304 TBS</title>
  
  <!-- Typography: Manrope & Prompt & Sarabun (Bidwells Editorial Aesthetic) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Sarabun:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  
  <!-- Interactive Plotly & Leaflet Engines (100% Free Open Source) -->
  <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

  <style>
    :root {
      --bg-dark: #0B0F17;
      --bg-surface: #111827;
      --bg-surface-elevated: #1E293B;
      --tu-red: #DC2626;
      --tu-red-bright: #EF4444;
      --tu-red-glow: rgba(220, 38, 38, 0.5);
      --tu-gold: #F59E0B;
      --tu-gold-bright: #FBBF24;
      --tu-gold-glow: rgba(245, 158, 11, 0.45);
      --tu-gold-light: #FDE68A;
      --tech-cyan: #06B6D4;
      --tech-emerald: #10B981;
      --tech-purple: #8B5CF6;
      --text-white: #FFFFFF;
      --text-primary: #F3F4F6;
      --text-secondary: #94A3B8;
      --text-muted: #64748B;
      --border-glass: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(245, 158, 11, 0.3);
      --font-display: 'Manrope', 'Prompt', sans-serif;
      --font-heading: 'Prompt', 'Manrope', sans-serif;
      --font-body: 'Sarabun', 'Manrope', sans-serif;
      --glass-bg: rgba(17, 24, 39, 0.88);
      --glass-blur: blur(20px);
      --card-shadow: 0 16px 40px -10px rgba(0, 0, 0, 0.8);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      scroll-behavior: smooth;
    }

    body {
      font-family: var(--font-body);
      color: var(--text-primary);
      background-color: var(--bg-dark);
      line-height: 1.7;
      overflow-x: hidden;
      font-size: 15px;
      letter-spacing: -0.1px;
    }

    h1, h2, h3, h4, .font-heading {
      font-family: var(--font-heading);
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0B0F17;
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--tu-gold);
    }

    /* Bidwells Minimal Fixed Top Bar */
    .bidwells-topbar {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 64px;
      z-index: 1000;
      background: rgba(11, 15, 23, 0.92);
      backdrop-filter: var(--glass-blur);
      border-bottom: 1px solid var(--border-glass);
      transition: background 0.3s ease;
    }

    .topbar-inner {
      max-width: 1680px;
      margin: 0 auto;
      padding: 0 32px;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .brand-mark {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: #FFFFFF;
    }

    .brand-emblem {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      background: linear-gradient(135deg, var(--tu-red) 0%, #7F1D1D 100%);
      border: 1px solid var(--tu-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 15px;
      color: var(--tu-gold);
      box-shadow: 0 0 14px var(--tu-red-glow);
    }

    .brand-title {
      font-family: var(--font-heading);
      font-size: 16px;
      font-weight: 700;
      letter-spacing: -0.2px;
      color: #FFFFFF;
      line-height: 1.2;
    }

    .brand-subtitle {
      font-size: 11px;
      color: var(--tu-gold);
      font-weight: 500;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }

    .topbar-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .bidwells-btn {
      padding: 7px 15px;
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-glass);
      border-radius: 6px;
      color: var(--text-primary);
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.3px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: var(--font-display);
    }

    .bidwells-btn:hover {
      background: rgba(51, 65, 85, 0.85);
      border-color: var(--tu-gold);
      color: var(--tu-gold);
      transform: translateY(-1px);
    }

    .bidwells-btn.primary {
      background: linear-gradient(135deg, #B45309 0%, #D97706 100%);
      color: #FFFFFF;
      border: 1px solid var(--tu-gold);
    }
    .bidwells-btn.primary:hover {
      background: linear-gradient(135deg, #D97706 0%, #F59E0B 100%);
      box-shadow: 0 0 16px var(--tu-gold-glow);
    }

    /* Bidwells Hero Fullscreen Section */
    .bidwells-hero {
      position: relative;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      background: #0B0F17;
      padding: 100px 32px 60px 32px;
    }

    .hero-photo-bg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 35%;
      opacity: 0.45;
      filter: saturate(1.15) brightness(0.9);
      transform: scale(1.02);
      transition: transform 12s cubic-bezier(0.1, 0.9, 0.2, 1);
    }

    .bidwells-hero:hover .hero-photo-bg {
      transform: scale(1.06);
    }

    .hero-vignette-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 50% 40%, rgba(11, 15, 23, 0.3) 0%, rgba(11, 15, 23, 0.88) 70%, #0B0F17 100%);
      pointer-events: none;
    }

    .hero-center-box {
      position: relative;
      z-index: 10;
      max-width: 1200px;
      margin: 0 auto;
      text-align: center;
    }

    .hero-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 18px;
      background: rgba(220, 38, 38, 0.16);
      border: 1px solid rgba(220, 38, 38, 0.45);
      border-radius: 30px;
      color: #FCA5A5;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 24px;
      font-family: var(--font-display);
    }

    .hero-eyebrow i {
      color: var(--tu-gold);
    }

    /* Massive Editorial Headline (Bidwells Style) */
    .hero-headline {
      font-family: var(--font-display);
      font-size: 72px;
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -2px;
      text-transform: uppercase;
      margin-bottom: 24px;
      color: #FFFFFF;
    }

    .hero-headline .headline-gold {
      background: linear-gradient(135deg, #FFFFFF 0%, var(--tu-gold) 60%, #D97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
    }

    .hero-lead-text {
      font-size: 21px;
      color: #E2E8F0;
      max-width: 880px;
      margin: 0 auto 40px auto;
      line-height: 1.6;
      font-weight: 400;
    }

    /* Bidwells Stat Grid */
    .bidwells-hero-stats {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      max-width: 1080px;
      margin: 0 auto 50px auto;
    }

    .stat-hero-card {
      background: var(--glass-bg);
      backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-glass);
      border-radius: 14px;
      padding: 22px 18px;
      text-align: center;
      transition: all 0.3s ease;
      box-shadow: var(--card-shadow);
    }

    .stat-hero-card:hover {
      transform: translateY(-4px);
      border-color: var(--tu-gold);
      box-shadow: 0 12px 30px -5px rgba(245, 158, 11, 0.3);
    }

    .stat-hero-val {
      font-family: var(--font-display);
      font-size: 36px;
      font-weight: 800;
      color: var(--tu-gold);
      margin-bottom: 6px;
      line-height: 1.1;
      letter-spacing: -0.5px;
    }

    .stat-hero-lbl {
      font-size: 13px;
      color: var(--text-secondary);
      font-weight: 500;
    }

    .hero-scroll-pill {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 8px 20px;
      border-radius: 30px;
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid var(--border-glass);
      color: #CBD5E1;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .hero-scroll-pill:hover {
      background: var(--tu-gold);
      color: #0B0F17;
      border-color: var(--tu-gold);
      transform: translateY(2px);
    }

    /* Bidwells Scrollytelling Experience Frame */
    .bidwells-scrolly-wrapper {
      position: relative;
      max-width: 1680px;
      margin: 0 auto;
      padding: 40px 32px 160px 32px;
    }

    /* Continuous Timeline Road Rail & Walking Student (Bidwells Track Equivalent) */
    .timeline-road-rail {
      position: fixed;
      left: 20px;
      top: 100px;
      bottom: 40px;
      width: 48px;
      z-index: 900;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .road-track-line {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 4px;
      background: rgba(51, 65, 85, 0.4);
      border-radius: 4px;
    }

    .road-progress-glow {
      position: absolute;
      top: 0;
      width: 4px;
      height: 10%;
      background: linear-gradient(180deg, var(--tu-red) 0%, var(--tu-gold) 100%);
      border-radius: 4px;
      box-shadow: 0 0 12px var(--tu-gold-glow);
      transition: height 0.3s ease-out;
    }

    /* Pinned Walking Student on the Timeline Road */
    .walking-student-marker {
      position: absolute;
      top: 10%;
      transform: translateY(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: top 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .walking-student-avatar {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: #0B0F17;
      border: 2px solid var(--tu-gold);
      box-shadow: 0 0 16px var(--tu-gold-glow);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }

    .walking-student-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      animation: tuWalkingStride 0.8s infinite ease-in-out;
    }

    @keyframes tuWalkingStride {
      0%, 100% { transform: translateY(0) rotate(0deg); }
      25% { transform: translateY(-2px) rotate(-3deg); }
      50% { transform: translateY(0) rotate(0deg); }
      75% { transform: translateY(-2px) rotate(3deg); }
    }

    .marker-year-bubble {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      color: var(--tu-gold);
      background: rgba(11, 15, 23, 0.95);
      border: 1px solid var(--tu-gold);
      border-radius: 10px;
      padding: 1px 7px;
      margin-top: 4px;
      white-space: nowrap;
      box-shadow: 0 2px 8px rgba(0,0,0,0.8);
    }

    /* Scrollytelling Chapter Blocks */
    .chapter-section {
      position: relative;
      min-height: 110vh;
      margin-bottom: 80px;
      display: flex;
      gap: 40px;
      align-items: flex-start;
      padding-left: 80px; /* Offset for vertical timeline rail */
    }

    /* Left Editorial Column */
    .chapter-editorial-col {
      flex: 0 0 42%;
      position: sticky;
      top: 88px;
      background: var(--glass-bg);
      backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-glass);
      border-radius: 20px;
      padding: 38px 36px;
      box-shadow: var(--card-shadow);
      z-index: 20;
      transition: border-color 0.3s ease;
    }

    .chapter-editorial-col:hover {
      border-color: rgba(245, 158, 11, 0.35);
    }

    .chapter-tag-line {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-display);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--tu-gold);
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.25);
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 16px;
    }

    .chapter-title {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 700;
      line-height: 1.25;
      margin-bottom: 18px;
      color: #FFFFFF;
      letter-spacing: -0.3px;
    }

    .chapter-lead-quote {
      font-size: 16px;
      font-weight: 500;
      line-height: 1.6;
      color: #F8FAFC;
      border-left: 3px solid var(--tu-gold);
      padding-left: 14px;
      margin-bottom: 18px;
    }

    .chapter-body-text {
      font-size: 15px;
      line-height: 1.75;
      color: #CBD5E1;
      margin-bottom: 24px;
    }

    .chapter-stat-row {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-bottom: 24px;
    }

    .stat-callout-card {
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      padding: 14px;
    }

    .stat-callout-num {
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 800;
      color: var(--tu-gold);
      line-height: 1.1;
    }

    .stat-callout-desc {
      font-size: 12px;
      color: var(--text-secondary);
      margin-top: 4px;
    }

    .chapter-interactive-hint {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(220, 38, 38, 0.12);
      border-left: 3px solid var(--tu-red);
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 13px;
      color: #FCA5A5;
      margin-bottom: 18px;
    }

    /* Right Sticky Visual Viewport */
    .chapter-visual-viewport {
      flex: 1;
      min-width: 0;
      position: sticky;
      top: 88px;
      background: rgba(15, 23, 42, 0.72);
      backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-glass);
      border-radius: 20px;
      padding: 24px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 14px;
      height: calc(100vh - 120px);
      overflow: hidden;
    }

    .viewport-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-glass);
      flex-shrink: 0;
    }

    .viewport-title-box h4 {
      font-size: 15px;
      font-weight: 600;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .viewport-title-box span {
      font-size: 12px;
      color: var(--text-muted);
    }

    .viewport-tools {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .tool-chip {
      padding: 5px 12px;
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid var(--border-glass);
      border-radius: 20px;
      font-size: 12px;
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
      font-weight: 500;
      font-family: var(--font-display);
    }

    .tool-chip:hover {
      color: var(--text-primary);
      border-color: var(--tu-gold);
    }

    .tool-chip.active {
      background: rgba(245, 158, 11, 0.2);
      border-color: var(--tu-gold);
      color: var(--tu-gold);
      font-weight: 600;
    }

    .chart-container-fluid {
      flex: 1;
      width: 100%;
      height: 100%;
      min-height: 0;
      position: relative;
      border-radius: 12px;
      overflow: hidden;
    }

    /* Pretty Maps Styling */
    #mapScene2 {
      width: 100%;
      height: 100%;
      border-radius: 12px;
      background: #0B0F17;
    }

    .map-campus-card {
      position: absolute;
      bottom: 16px;
      right: 16px;
      z-index: 400;
      width: 320px;
      background: rgba(15, 23, 42, 0.94);
      backdrop-filter: blur(16px);
      border: 1px solid var(--tu-gold);
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      border-radius: 14px;
      padding: 16px;
      transition: all 0.3s ease;
    }

    .map-beacon-pulse {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--tu-gold);
      box-shadow: 0 0 15px var(--tu-gold);
      position: relative;
    }

    .map-beacon-pulse::after {
      content: '';
      position: absolute;
      top: -10px;
      left: -10px;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      border: 2px solid var(--tu-gold);
      animation: beaconRings 1.8s infinite ease-out;
    }

    @keyframes beaconRings {
      0% { transform: scale(0.5); opacity: 1; }
      100% { transform: scale(1.8); opacity: 0; }
    }

    /* Modals & Inspection Drawers */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(14px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .modal-overlay.open {
      display: flex;
      opacity: 1;
    }

    .modal-window {
      background: #111827;
      border: 1px solid var(--tu-gold);
      border-radius: 20px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85), 0 0 25px var(--tu-gold-glow);
      max-width: 820px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 32px;
      position: relative;
      animation: modalSlideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modalSlideUp {
      from { transform: translateY(30px) scale(0.97); opacity: 0; }
      to { transform: translateY(0) scale(1); opacity: 1; }
    }

    .modal-close-btn {
      position: absolute;
      top: 20px;
      right: 20px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-glass);
      color: #CBD5E1;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .modal-close-btn:hover {
      background: var(--tu-red);
      color: #FFFFFF;
      transform: rotate(90deg);
    }

    /* Scene 10 Cockpit Panel */
    .cockpit-panel {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      height: 100%;
      align-items: center;
    }

    .slider-group {
      display: flex;
      flex-direction: column;
      gap: 14px;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-glass);
      border-radius: 14px;
      padding: 20px;
    }

    .slider-item {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .slider-label-row {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 500;
      color: #CBD5E1;
    }

    .slider-input {
      -webkit-appearance: none;
      width: 100%;
      height: 8px;
      border-radius: 5px;
      background: #334155;
      outline: none;
    }

    .slider-input::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--tu-gold);
      cursor: pointer;
      box-shadow: 0 0 10px var(--tu-gold);
      transition: transform 0.1s ease;
    }

    .slider-input::-webkit-slider-thumb:hover {
      transform: scale(1.2);
    }

    /* Bidwells Minimal Editorial Footer */
    .bidwells-footer {
      border-top: 1px solid var(--border-glass);
      background: #080C14;
      padding: 70px 32px 100px 32px;
    }

    .footer-inner {
      max-width: 1480px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 36px;
    }

    .footer-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 24px;
    }

    .footer-credits {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      padding-top: 28px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      font-size: 13px;
      color: var(--text-muted);
    }

    /* Mobile Responsive Adaptation */
    @media (max-width: 1024px) {
      .hero-headline { font-size: 48px; }
      .bidwells-hero-stats { grid-template-columns: repeat(2, 1fr); }
      .timeline-road-rail { display: none; }
      .chapter-section { flex-direction: column; min-height: auto; margin-bottom: 60px; padding-left: 0; }
      .chapter-editorial-col { flex: 1 1 100%; position: static; width: 100%; }
      .chapter-visual-viewport { flex: 1 1 100%; position: static; width: 100%; height: 530px; }
      .cockpit-panel { grid-template-columns: 1fr; }
      .footer-credits { grid-template-columns: 1fr; }
    }

    @media (max-width: 640px) {
      .topbar-inner { padding: 0 16px; }
      .hero-headline { font-size: 34px; letter-spacing: -1px; }
      .hero-lead-text { font-size: 16px; }
      .bidwells-hero-stats { grid-template-columns: 1fr; }
      .chapter-editorial-col { padding: 22px; }
      .chapter-title { font-size: 22px; }
      .chapter-visual-viewport { height: 480px; padding: 14px; }
    }
  </style>
</head>
<body>

  <!-- Bidwells Fixed Top Navigation Bar -->
  <header class="bidwells-topbar">
    <div class="topbar-inner">
      <a href="#" class="brand-mark">
        <div class="brand-emblem">90</div>
        <div>
          <div class="brand-title">มหาวิทยาลัยธรรมศาสตร์</div>
          <div class="brand-subtitle">BI304 Data Visualization & Storytelling</div>
        </div>
      </a>

      <div class="topbar-actions">
        <button onclick="openFlourishDataModal()" class="bidwells-btn" title="ดาวน์โหลดชุดข้อมูล Flourish 10 ชุด">
          <i class="fa-solid fa-table-list text-cyan-400"></i> Flourish Data
        </button>

        <a href="story board.pdf" target="_blank" class="bidwells-btn" title="Download Storyboard PDF">
          <i class="fa-solid fa-file-pdf text-red-400"></i> Storyboard PDF
        </a>

        <a href="https://github.com/kondee-rgb/BI304-Thammasat-Data-Storytelling" target="_blank" class="bidwells-btn primary" title="View Source on GitHub">
          <i class="fa-brands fa-github"></i> GitHub
        </a>
      </div>
    </div>
  </header>

  <!-- Bidwells Hero Section with Tha Prachan Twilight Backdrop -->
  <section class="bidwells-hero">
    <img src="assets/tha_prachan_dome_editorial.jpg" alt="ตึกโดม มหาวิทยาลัยธรรมศาสตร์ ท่าพระจันทร์" class="hero-photo-bg" />
    <div class="hero-vignette-overlay"></div>

    <div class="hero-center-box">
      <div class="hero-eyebrow">
        <i class="fa-solid fa-landmark"></i> 90 YEARS OF IMPACT & VISION: 2477 — 2567
      </div>

      <h1 class="hero-headline">
        90 YEARS OF<br>
        <span class="headline-gold">THAMMASAT</span>
      </h1>

      <p class="hero-lead-text">
        จาก "มหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง" สู่ "มหาวิทยาลัยวิจัยระดับโลกเพื่อประชาชน"<br>
        รายงานข้อมูลเชิงลึกและการเดินทาง 9 ทศวรรษผ่าน Scrollytelling Intelligence Report
      </p>

      <div class="bidwells-hero-stats">
        <div class="stat-hero-card">
          <div class="stat-hero-val">90 ปี</div>
          <div class="stat-hero-lbl">หมุดหมายประวัติศาสตร์ประชาธิปไตยไทย</div>
        </div>
        <div class="stat-hero-card">
          <div class="stat-hero-val">42,650</div>
          <div class="stat-hero-lbl">นักศึกษาปัจจุบันใน 4 ศูนย์การศึกษา</div>
        </div>
        <div class="stat-hero-card">
          <div class="stat-hero-val">Triple Crown</div>
          <div class="stat-hero-lbl">TBS คณะพาณิชย์ฯ ติด 1 ใน 1% ของโลก</div>
        </div>
        <div class="stat-hero-card">
          <div class="stat-hero-val">Top 10 โลก</div>
          <div class="stat-hero-lbl">THE Impact Rankings ด้าน SDG 11 เมืองยั่งยืน</div>
        </div>
      </div>

      <div class="hero-scroll-pill" onclick="scrollToScene(1)">
        <span>เลื่อนลงเพื่อเริ่มต้นการเดินทาง 90 ปี</span>
        <i class="fa-solid fa-arrow-down"></i>
      </div>
    </div>
  </section>

  <!-- Continuous Timeline Road Rail with Walking Thammasat Student (Bidwells Track Equivalent) -->
  <aside class="timeline-road-rail" id="timelineRoadRail">
    <div class="road-track-line"></div>
    <div class="road-progress-glow" id="roadProgressGlow"></div>
    <div class="walking-student-marker" id="walkingStudentMarker">
      <div class="walking-student-avatar">
        <img src="assets/tu_student_walking.png" alt="TU Student Walking" />
      </div>
      <div class="marker-year-bubble" id="markerYearBubble">2477</div>
    </div>
  </aside>

  <!-- Main Scrollytelling Sections Frame -->
  <main class="bidwells-scrolly-wrapper">

    <!-- SCENE 1: Straight Line Chart with Event Milestones -->
    <section class="chapter-section" id="scene1" data-scene="1">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 01 / 10 • HISTORICAL EVOLUTION</div>
        <h2 class="chapter-title">วิวัฒนาการ 9 ทศวรรษ: จาก "มหาวิทยาลัยเปิด" สู่ "ระบบปิด" และศูนย์รังสิต</h2>
        <div class="chapter-lead-quote">
          "กำเนิดเพื่อตลาดวิชาเปิดกว้าง พ.ศ. 2477 สู่จุดเปลี่ยนปฏิรูปมาตรฐานเป็น 'ระบบปิด' พ.ศ. 2495 และบุกเบิกทุ่งรังสิต"
        </div>
        <p class="chapter-body-text">
          จุดกำเนิดเมื่อ 27 มิถุนายน 2477 ในฐานะ <strong>"มหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง (มธก.)"</strong> ด้วยปรัชญาตลาดวิชาเปิดกว้าง ค่าเล่าเรียนปีละ 20 บาท เพื่อสร้างปัญญาชนประชาธิปไตย 
          จนกระทั่งปี 2495 เกิดจุดเปลี่ยนครั้งใหญ่ <strong>พ.ร.บ. มหาวิทยาลัยธรรมศาสตร์ พ.ศ. 2495</strong> ปรับเปลี่ยนเข้าสู่ <strong>"ระบบปิด (Closed Entrance Exam System)"</strong> 
          เพื่อยกระดับมาตรฐานทางวิชาการและสอบคัดเลือกอย่างเข้มข้น ก่อนจะขยายสู่ศูนย์รังสิตเพื่อรองรับการเติบโตระดับสากล
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-lightbulb"></i>
          <span>คลิกปุ่มหมุดหมายประวัติศาสตร์ด้านบนกราฟเพื่อเจาะลึกนโยบายแต่ละยุค</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">7,094 คน</div>
            <div class="stat-callout-desc">นักศึกษารุ่นแรก พ.ศ. 2477 (ยุคเปิด)</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">4,200 คน</div>
            <div class="stat-callout-desc">ยุคเริ่มต้นระบบปิด พ.ศ. 2495</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-chart-line text-red-500"></i> Straight Line Timeline: 90 Years Student Growth</h4>
            <span>กราฟเส้นตรงแสดงเหตุการณ์หมุดหมายและการเปลี่ยนผ่านระบบการศึกษา</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip active" onclick="filterScene1('all')">ภาพรวม 90 ปี</button>
            <button class="tool-chip" onclick="filterScene1('closed')">ยุคระบบปิด 2495</button>
            <button class="tool-chip" onclick="filterScene1('rangsit')">ยุคขยายรังสิต 2529</button>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene1"></div>
      </div>
    </section>

    <!-- SCENE 2: Pretty Maps Dark Architectural Edition -->
    <section class="chapter-section" id="scene2" data-scene="2">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 02 / 10 • STRATEGIC CAMPUSES</div>
        <h2 class="chapter-title">ยุทธศาสตร์ 4 ศูนย์การศึกษา: การขยายพื้นที่และเครือข่ายระดับประเทศ</h2>
        <div class="chapter-lead-quote">
          "สถาปัตยกรรมแผนที่มืด Cartography เชื่อมโยง 4 วิทยาเขตหลักทั่วไทย รวมพื้นที่กว่า 2,836 ไร่"
        </div>
        <p class="chapter-body-text">
          การเติบโตของธรรมศาสตร์ขยายตัวสู่ 4 ศูนย์การศึกษาเชิงยุทธศาสตร์:
          <strong>ศูนย์รังสิต</strong> (1,757 ไร่ เมกะแคมปัสวิทย์-แพทย์-นวัตกรรม),
          <strong>ศูนย์ท่าพระจันทร์</strong> (49 ไร่ หัวใจประวัติศาสตร์และบัณฑิตศึกษานานาชาติ),
          <strong>ศูนย์พัทยา</strong> (566 ไร่ นวัตกรรมยานยนต์ EV และ EEC),
          และ <strong>ศูนย์ลำปาง</strong> (464 ไร่ การศึกษาและศิลปวัฒนธรรมล้านนา)
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-location-crosshairs"></i>
          <span>คลิกเลือกศูนย์การศึกษาเพื่อบิน (FlyTo) ไปสำรวจรายละเอียดและเส้นทาง</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">2,836 ไร่</div>
            <div class="stat-callout-desc">พื้นที่รวมทั้ง 4 ศูนย์การศึกษา</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">78.5%</div>
            <div class="stat-callout-desc">สัดส่วนนักศึกษาอยู่ที่ศูนย์รังสิต</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-map-location-dot text-yellow-400"></i> Thammasat Cartography: Pretty Maps Architecture</h4>
            <span>แผนที่สไตล์ Architectural Dark Matter พร้อมวงคลื่นสัญญาณและเส้นทางเชื่อมต่อ</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip active" onclick="zoomMapCampus('all')">ภาพรวมประเทศ</button>
            <button class="tool-chip" onclick="zoomMapCampus('prachan')">ท่าพระจันทร์</button>
            <button class="tool-chip" onclick="zoomMapCampus('rangsit')">ศูนย์รังสิต</button>
            <button class="tool-chip" onclick="zoomMapCampus('pattaya')">ศูนย์พัทยา</button>
            <button class="tool-chip" onclick="zoomMapCampus('lampang')">ศูนย์ลำปาง</button>
          </div>
        </div>
        <div class="chart-container-fluid" style="position: relative;">
          <div id="mapScene2"></div>
          <div class="map-campus-card" id="mapCampusDetailCard">
            <h5 id="cardCampusName" style="color: var(--tu-gold); font-size: 16px; margin-bottom: 6px;">มหาวิทยาลัยธรรมศาสตร์ 4 ศูนย์</h5>
            <p id="cardCampusDesc" style="font-size: 13px; color: #CBD5E1; line-height: 1.5;">คลิกปุ่มด้านบนหรือหมุดในแผนที่เพื่อดูข้อมูลเชิงลึกของแต่ละวิทยาเขต</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SCENE 3: Treemap with Click-to-Inspect Admission & Faculty Details -->
    <section class="chapter-section" id="scene3" data-scene="3">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 03 / 10 • ACADEMIC STRUCTURE</div>
        <h2 class="chapter-title">โครงสร้าง 26 คณะและสถาบัน: เจาะลึกคะแนนสอบเข้าและมาตรฐานสากล</h2>
        <div class="chapter-lead-quote">
          "4 กลุ่มวิชาการชั้นนำ นำโดย TBS คณะพาณิชย์ฯ ที่ครองอันดับ 1 ในการรับรองระดับ Triple Crown"
        </div>
        <p class="chapter-body-text">
          ธรรมศาสตร์จัดกลุ่มหลักสูตรออกเป็น 4 คลัสเตอร์วิชาการชั้นนำ นำโดย <strong>สังคมศาสตร์และมนุษยศาสตร์ (17,900 คน)</strong>, 
          <strong>วิทยาศาสตร์และเทคโนโลยี (11,100 คน)</strong>, <strong>วิทยาศาสตร์สุขภาพ (7,650 คน)</strong> และ <strong>สถาบันนานาชาติ/บูรณาการ (6,000 คน)</strong>
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-hand-pointer"></i>
          <span><strong>คลิกที่กล่องของคณะในกราฟ Treemap</strong> เพื่อเปิดหน้าต่างดูคะแนนสอบเข้า TCAS รอบ 3, อัตราแข่งขัน และเงินเดือนเริ่มต้น</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">4,950 คน</div>
            <div class="stat-callout-desc">TBS คณะพาณิชย์ฯ นักศึกษาสูงสุด</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">96.8%</div>
            <div class="stat-callout-desc">อัตราการได้งานทำเฉลี่ยของบัณฑิต</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-shapes text-blue-400"></i> Faculty Hierarchy Treemap (Click to Inspect)</h4>
            <span>คลิกที่คณะเพื่อดูคะแนน TCAS, อัตราการรับเข้า และเงินเดือนเฉลี่ย</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip active" onclick="drawScene3Treemap()">ทั้งหมด 4 กลุ่ม</button>
            <button class="tool-chip" onclick="showFacultyDetailModal('tbs')">พาณิชย์ฯ (TBS)</button>
            <button class="tool-chip" onclick="showFacultyDetailModal('law')">นิติศาสตร์</button>
            <button class="tool-chip" onclick="showFacultyDetailModal('med')">แพทยศาสตร์</button>
            <button class="tool-chip" onclick="showFacultyDetailModal('siit')">สถาบัน SIIT</button>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene3"></div>
      </div>
    </section>

    <!-- SCENE 4: Gender Diversity (Exact User Title) -->
    <section class="chapter-section" id="scene4" data-scene="4">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 04 / 10 • DEMOGRAPHICS</div>
        <h2 class="chapter-title">มิติประชากร: หญิง 62.4% พลังขับเคลื่อนแห่งอนาคต</h2>
        <div class="chapter-lead-quote">
          "สัดส่วนนักศึกษาหญิง 62.4% สะท้อนการเปิดกว้างและความเสมอภาคทางเพศที่ล้ำหน้าค่าเฉลี่ยสากล"
        </div>
        <p class="chapter-body-text">
          ความโดดเด่นของโครงสร้างประชากรนักศึกษาธรรมศาสตร์สะท้อนการเปิดกว้างและความเสมอภาคทางเพศ 
          โดยมี <strong>นักศึกษาหญิงครองสัดส่วนถึง 62.4% (26,620 คน)</strong> และ <strong>ชาย 37.6% (16,030 คน)</strong> 
          โดยเฉพาะในกลุ่มวิทยาศาสตร์สุขภาพและสังคมศาสตร์ นักศึกษาหญิงก้าวขึ้นเป็นผู้นำอย่างโดดเด่น
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-venus-mars"></i>
          <span>สัดส่วนนักศึกษาหญิงของ มธ. สูงกว่าค่าเฉลี่ย OECD (54%) และมหาวิทยาลัยไทย (58%)</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num" style="color: #F43F5E;">68.0%</div>
            <div class="stat-callout-desc">สัดส่วนหญิง วิทยาศาสตร์สุขภาพ</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num" style="color: #38BDF8;">44.0%</div>
            <div class="stat-callout-desc">สัดส่วนหญิง STEM (สูงกว่าโลก)</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-chart-pie text-pink-400"></i> มิติประชากร: หญิง 62.4% พลังขับเคลื่อนแห่งอนาคต</h4>
            <span>การกระจายตัวทางเพศสภาวะเปรียบเทียบ 4 กลุ่มวิชาการและเกณฑ์สากล</span>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene4"></div>
      </div>
    </section>

    <!-- SCENE 5: Intuitive Multi-Era Campus Distribution -->
    <section class="chapter-section" id="scene5" data-scene="5">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 05 / 10 • CAMPUS ALLOCATION</div>
        <h2 class="chapter-title">การกระจายตัวและการย้ายศูนย์การศึกษา: คมชัด เข้าใจง่ายในพริบตา</h2>
        <div class="chapter-lead-quote">
          "ปรับแทนกราฟสายธารเดิมที่ดูซับซ้อน เป็นกราฟเปรียบเทียบ 4 ยุคประวัติศาสตร์ที่เห็นภาพการย้ายฐานทันที"
        </div>
        <p class="chapter-body-text">
          เห็นภาพการเปลี่ยนผ่านจาก <strong>ยุคท่าพระจันทร์ 100%</strong> สู่การก้าวกระโดดของ <strong>ศูนย์รังสิต (78.5%)</strong> 
          ในขณะที่ท่าพระจันทร์ปรับบทบาทเป็นศูนย์บัณฑิตศึกษาและนานาชาติชั้นนำริมเจ้าพระยา
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-arrow-right-arrow-left"></i>
          <span>คลิกปุ่มเปลี่ยนยุคเพื่อดูสัดส่วนนักศึกษาแต่ละศูนย์ที่ย้ายฐานอย่างชัดเจน</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">33,480 คน</div>
            <div class="stat-callout-desc">นักศึกษา ณ ศูนย์รังสิต (ยุคปัจจุบัน)</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">6,310 คน</div>
            <div class="stat-callout-desc">นักศึกษา ณ ท่าพระจันทร์ (เน้น ป.โท-เอก)</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-chart-column text-emerald-400"></i> Multi-Era Campus Student Allocation Matrix</h4>
            <span>เปรียบเทียบสัดส่วนนักศึกษาใน 4 ยุคสำคัญ (อ่านง่ายและเห็นภาพทันที)</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip active" onclick="renderScene5Era('all')">เปรียบเทียบ 4 ยุค</button>
            <button class="tool-chip" onclick="renderScene5Era('era1')">ยุค 1 (2477-94)</button>
            <button class="tool-chip" onclick="renderScene5Era('era3')">ยุค 3 (2529-47)</button>
            <button class="tool-chip" onclick="renderScene5Era('era4')">ยุค 4 (ปัจจุบัน)</button>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene5"></div>
      </div>
    </section>

    <!-- SCENE 6: 5-Year Budget Trend with Click-to-Drilldown -->
    <section class="chapter-section" id="scene6" data-scene="6">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 06 / 10 • FINANCIAL INTELLIGENCE</div>
        <h2 class="chapter-title">แนวโน้มงบประมาณ 5 ปี (2563 - 2567) & เจาะลึกรายได้ 5 แหล่ง</h2>
        <div class="chapter-lead-quote">
          "เติบโตจาก 11,280 สู่ 13,745 ล้านบาท (+21.8%) เสถียรภาพการเงินแข็งแกร่งด้วยรายได้พึ่งตนเองกว่า 68%"
        </div>
        <p class="chapter-body-text">
          การเติบโตของงบประมาณรวมจาก <strong>11,280 ล้านบาทในปี 2563 สู่ 13,745 ล้านบาทในปี 2567 (+21.8%)</strong> 
          สะท้อนเสถียรภาพทางการเงินในฐานะมหาวิทยาลัยในกำกับของรัฐ โดยมีโครงสร้างรายได้พึ่งพาตนเองมากกว่า 68% 
          ทั้งจากค่าธรรมเนียมการศึกษา บริการวิชาการ และโรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-hand-pointer"></i>
          <span><strong>คลิกที่แท่งปีงบประมาณด้านขวา</strong> เพื่อดูรายละเอียดรายได้ 5 แหล่งของปีนั้นๆ ทันที</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">13,745 ลบ.</div>
            <div class="stat-callout-desc">งบประมาณรวมปี 2567</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">+21.8%</div>
            <div class="stat-callout-desc">การเติบโตสะสมตลอด 5 ปีที่ผ่านมา</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-coins text-amber-400"></i> 5-Year Comparative Budget & Revenue Breakdown Drilldown</h4>
            <span id="scene6SubTitle">คลิกที่แท่งกราฟของปีที่ต้องการเพื่อเจาะลึกโครงสร้าง 5 แหล่งรายได้</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip" onclick="drilldownBudgetYear(2563)">ปี 63</button>
            <button class="tool-chip" onclick="drilldownBudgetYear(2564)">ปี 64</button>
            <button class="tool-chip" onclick="drilldownBudgetYear(2565)">ปี 65</button>
            <button class="tool-chip" onclick="drilldownBudgetYear(2566)">ปี 66</button>
            <button class="tool-chip active" onclick="drilldownBudgetYear(2567)">ปี 67 (ล่าสุด)</button>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene6"></div>
      </div>
    </section>

    <!-- SCENE 7: Business School Benchmark (TBS vs CBS vs Sasin vs CMMU) -->
    <section class="chapter-section" id="scene7" data-scene="7">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 07 / 10 • BUSINESS EXCELLENCE</div>
        <h2 class="chapter-title">ความเป็นเลิศทางธุรกิจ: เปรียบเทียบ TBS กับ Business Schools ชั้นนำของไทย</h2>
        <div class="chapter-lead-quote">
          "เปรียบเทียบ 4 เสาหลักบริหารธุรกิจ: TBS, CBS, Sasin และ CMMU ชูตราสัญลักษณ์ Triple Crown ระดับโลก"
        </div>
        <p class="chapter-body-text">
          การเปรียบเทียบเชิงลึกระหว่าง 4 เสาหลักบริหารธุรกิจของประเทศ: 
          <strong>TBS (คณะพาณิชย์ฯ มธ.)</strong>, <strong>CBS (คณะบัญชีฯ จุฬาฯ)</strong>, 
          <strong>Sasin (สถาบันศศินทร์ จุฬาฯ)</strong> และ <strong>CMMU (วิทยาลัยการจัดการ ม.มหิดล)</strong><br>
          TBS โดดเด่นด้วยการเป็น <strong>Triple Crown สากล (AACSB, EQUIS, AMBA)</strong> 
          และครองแชมป์การแข่งขันกรณีศึกษาทางธุรกิจระดับโลก (World Case Competitions) มากที่สุดในประเทศไทย
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-award"></i>
          <span>TBS และ CBS เป็นเพียง 2 สถาบันในไทยที่ได้การรับรองระดับ Triple Crown (Top 1% โลก)</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">อันดับ 125</div>
            <div class="stat-callout-desc">QS World Subject Rank: TBS Business</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">Triple Crown</div>
            <div class="stat-callout-desc">AACSB + EQUIS + AMBA (3 ตราสากล)</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-ranking-star text-purple-400"></i> Top Thai Business Schools Radar Benchmark</h4>
            <span>เปรียบเทียบ TBS, Chula Business School (CBS), Sasin และ CMMU</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip active" onclick="filterBschoolBenchmark('all')">เปรียบเทียบทั้ง 4 แห่ง</button>
            <button class="tool-chip" onclick="filterBschoolBenchmark('tbs_cbs')">TBS vs CBS</button>
            <button class="tool-chip" onclick="filterBschoolBenchmark('tbs')">เฉพาะ TBS</button>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene7"></div>
      </div>
    </section>

    <!-- SCENE 8: SDG 11 Sustainable Cities (Top 10 World) -->
    <section class="chapter-section" id="scene8" data-scene="8">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 08 / 10 • SUSTAINABILITY LEADERSHIP</div>
        <h2 class="chapter-title">SDG 11 เมืองและชุมชนยั่งยืน: อันดับ 1 ของไทย และท็อป 10 ของโลก</h2>
        <div class="chapter-lead-quote">
          "THE Impact Rankings จัด มธ. อันดับ 1 ของไทย / Top 10 ของโลก ด้านเมืองยั่งยืน SDG 11"
        </div>
        <p class="chapter-body-text">
          Times Higher Education (THE) Impact Rankings จัดให้มหาวิทยาลัยธรรมศาสตร์อยู่ใน 
          <strong>อันดับที่ 73 ของโลกในภาพรวม</strong> และ <strong>อันดับ 1 ในประเทศไทย / Top 10 ของโลก ด้าน SDG 11</strong> (Sustainable Cities and Communities) 
          ด้วยต้นแบบ <strong>สวนป๋วย 100 ปี</strong> (ฟาร์มเกษตรอินทรีย์ลอยฟ้าขนาดใหญ่ที่สุดในเอเชีย 22,000 ตร.ม.) 
          และโครงการ <strong>TU Solar Rooftop (23.6 MW)</strong> กำลังการผลิตพลังงานสะอาดอันดับ 1 ในสถาบันการศึกษาเอเชีย
        </p>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num" style="color: #10B981;">อันดับ 1 ไทย</div>
            <div class="stat-callout-desc">THE Impact Rankings ด้าน SDG 11</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num" style="color: #F59E0B;">23.6 MW</div>
            <div class="stat-callout-desc">TU Solar Rooftop ใหญ่ที่สุดในเอเชีย</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-leaf text-green-400"></i> SDG 11 Sustainability Radar & Smart Campus Metrics</h4>
            <span>6 มิติการพัฒนาเมืองอัจฉริยะ ความยั่งยืน และพลังงานหมุนเวียน</span>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene8"></div>
      </div>
    </section>

    <!-- SCENE 9: Thammasat Hospital Dual-Axis -->
    <section class="chapter-section" id="scene9" data-scene="9">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 09 / 10 • HEALTHCARE LIFELINE</div>
        <h2 class="chapter-title">โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ: เสาหลักสุขภาวะและการแพทย์ตติยภูมิ</h2>
        <div class="chapter-lead-quote">
          "เมดิคัลฮับ 800+ เตียง ดูแลผู้ป่วยกว่า 1.45 ล้านครั้งต่อปี และต้นแบบโรงพยาบาลสนามแห่งแรกของชาติ"
        </div>
        <p class="chapter-body-text">
          จากโรงพยาบาลขนาด 350 เตียงในอดีต สู่ <strong>เมดิคัลฮับระดับตติยภูมิขั้นสูงขนาด 800+ เตียง</strong> 
          ที่ให้บริการผู้ป่วยนอกมากกว่า <strong>1.45 ล้านครั้งต่อปี</strong> และผู้ป่วยในกว่า 35,000 รายต่อปี 
          พร้อมบทบาทประวัติศาสตร์ในการจัดตั้ง <strong>"โรงพยาบาลสนามธรรมศาสตร์ 308 เตียง"</strong> 
          ซึ่งเป็นโรงพยาบาลสนามแห่งแรกของประเทศไทยในยามวิกฤต COVID-19
        </p>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">1.45 ล้าน</div>
            <div class="stat-callout-desc">ครั้งที่ผู้ป่วยนอก (OPD) รับบริการ/ปี</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">308 เตียง</div>
            <div class="stat-callout-desc">รพ.สนามธรรมศาสตร์ โมเดลต้นแบบของชาติ</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-hospital text-rose-400"></i> Thammasat Hospital Dual-Axis Growth & Centers of Excellence</h4>
            <span>การเติบโตของผู้ป่วยนอก ผู้ป่วยใน และศูนย์ความเป็นเลิศทางการแพทย์</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip active" onclick="toggleHospitalMode('growth')">สถิติผู้ป่วย 10 ปี</button>
            <button class="tool-chip" onclick="toggleHospitalMode('specialties')">ศูนย์การแพทย์เฉพาะทาง</button>
          </div>
        </div>
        <div class="chart-container-fluid" id="chartScene9"></div>
      </div>
    </section>

    <!-- SCENE 10: TU 2034 Strategic Flight Cockpit -->
    <section class="chapter-section" id="scene10" data-scene="10">
      <div class="chapter-editorial-col">
        <div class="chapter-tag-line">CHAPTER 10 / 10 • FUTURE HORIZON</div>
        <h2 class="chapter-title">TU 2034: ก้าวสู่ศตวรรษที่ 1 ของธรรมศาสตร์ และค็อกพิทจำลองยุทธศาสตร์</h2>
        <div class="chapter-lead-quote">
          "วิสัยทัศน์มุ่งสู่ Top 100 มหาวิทยาลัยระดับโลก พร้อมค็อกพิทจำลองการขับเคลื่อนยุทธศาสตร์แบบเรียลไทม์"
        </div>
        <p class="chapter-body-text">
          วิสัยทัศน์ในทศวรรษหน้า (พ.ศ. 2567 - 2577) ธรรมศาสตร์มุ่งสู่การเป็น <strong>Top 100 มหาวิทยาลัยระดับโลก</strong> 
          ภายใต้ 4 เสาหลัก: งานวิจัยแนวหน้า, ปัญญาประดิษฐ์และทักษะมนุษย์ยุคใหม่, สุขภาวะคนทุกช่วงวัย และสังคมที่เป็นธรรม
        </p>

        <div class="chapter-interactive-hint">
          <i class="fa-solid fa-sliders"></i>
          <span><strong>Interactive Simulator:</strong> เลื่อนสไลเดอร์ด้านขวาเพื่อจำลองการจัดสรรงบประมาณวิจัย AI และพลังงานสีเขียว เพื่อดูผลการคาดการณ์อันดับโลกทันที</span>
        </div>

        <div class="chapter-stat-row">
          <div class="stat-callout-card">
            <div class="stat-callout-num">Top 100</div>
            <div class="stat-callout-desc">เป้าหมายอันดับมหาวิทยาลัยโลกปี 2034</div>
          </div>
          <div class="stat-callout-card">
            <div class="stat-callout-num">100%</div>
            <div class="stat-callout-desc">AI Literacy สำหรับนักศึกษาทุกคน</div>
          </div>
        </div>
      </div>

      <div class="chapter-visual-viewport">
        <div class="viewport-header">
          <div class="viewport-title-box">
            <h4><i class="fa-solid fa-gauge-high text-cyan-400"></i> TU 2034 Strategic Flight Cockpit & Real-Time Simulator</h4>
            <span>ปรับสไลเดอร์เพื่อดูผลลัพธ์การจำลองการขับเคลื่อนยุทธศาสตร์</span>
          </div>
          <div class="viewport-tools">
            <button class="tool-chip" onclick="resetSimulator()">รีเซ็ตค่าเริ่มต้น</button>
          </div>
        </div>
        <div class="chart-container-fluid">
          <div class="cockpit-panel">
            <div class="slider-group">
              <div class="slider-item">
                <div class="slider-label-row">
                  <span><i class="fa-solid fa-microscope text-purple-400"></i> งบลงทุนวิจัย Frontier Research:</span>
                  <strong id="valResearch" style="color: var(--tu-gold);">35%</strong>
                </div>
                <input type="range" min="10" max="60" value="35" class="slider-input" id="sliderResearch" oninput="updateSimulator()" />
              </div>

              <div class="slider-item">
                <div class="slider-label-row">
                  <span><i class="fa-solid fa-brain text-cyan-400"></i> การบูรณาการ AI & Human Skills:</span>
                  <strong id="valAI" style="color: var(--tu-gold);">40%</strong>
                </div>
                <input type="range" min="10" max="60" value="40" class="slider-input" id="sliderAI" oninput="updateSimulator()" />
              </div>

              <div class="slider-item">
                <div class="slider-label-row">
                  <span><i class="fa-solid fa-seedling text-emerald-400"></i> ความยั่งยืนและสิ่งแวดล้อมสีเขียว:</span>
                  <strong id="valGreen" style="color: var(--tu-gold);">25%</strong>
                </div>
                <input type="range" min="10" max="60" value="25" class="slider-input" id="sliderGreen" oninput="updateSimulator()" />
              </div>
            </div>

            <div id="chartScene10Gauges" style="width: 100%; height: 100%;"></div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Interactive Faculty Detail Modal (For Scene 3 Click Drilldown) -->
  <div class="modal-overlay" id="facultyModal">
    <div class="modal-window">
      <button class="modal-close-btn" onclick="closeFacultyModal()"><i class="fa-solid fa-xmark"></i></button>
      <div id="facultyModalContent"></div>
    </div>
  </div>

  <!-- Flourish Data Download Modal -->
  <div class="modal-overlay" id="flourishModal">
    <div class="modal-window">
      <button class="modal-close-btn" onclick="closeFlourishDataModal()"><i class="fa-solid fa-xmark"></i></button>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
        <div style="width:40px;height:40px;border-radius:10px;background:rgba(6,182,212,0.2);border:1px solid #06B6D4;display:flex;align-items:center;justify-content:center;color:#06B6D4;font-size:18px;">
          <i class="fa-solid fa-database"></i>
        </div>
        <div>
          <span style="font-size:12px;color:#06B6D4;font-weight:600;">FLOURISH READY-TO-IMPORT DATASETS</span>
          <h3 style="font-size:22px;color:#FFF;line-height:1.2;">ชุดข้อมูลสำหรับ Flourish Studio ทั้ง 10 ฉาก</h3>
        </div>
      </div>

      <p style="font-size:13px;color:#94A3B8;margin-bottom:20px;">
        ไฟล์ CSV ผ่านการจัดรูปแบบและทำความสะอาด (Cleaned & Standardized) เรียบร้อยแล้ว พร้อมอัปโหลดเข้าสู่ระบบ Flourish Studio ได้ทันทีตามเกณฑ์รายวิชา BI304
      </p>

      <div style="display:grid;grid-template-columns:1fr;gap:10px;margin-bottom:20px;">
        <a href="flourish_data/01_flourish_scene1_student_growth.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 1: Student Growth Timeline (90 Years)</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/02_flourish_scene2_campus_locations.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 2: 4 Campuses Geographic Locations & Areas</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/03_flourish_scene3_faculty_hierarchy.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 3: 26 Faculties Clusters & Hierarchy</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/04_flourish_scene4_gender_diversity.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 4: Gender Distribution Across Disciplines</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/05_flourish_scene5_migration_flow_sankey.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 5: Campus Migration Matrix & Distribution</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/06_flourish_scene6_budget_waterfall.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 6: 5-Year Budget Trend & 5 Revenue Sources</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/07_flourish_scene7_rankings_trend.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 7: Business Schools Benchmark (TBS vs CBS vs Sasin)</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/08_flourish_scene8_sdg_radar.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 8: SDG 11 Sustainable Cities & Communities Radar</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/09_flourish_scene9_hospital_growth.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 9: Thammasat Hospital Outpatients & Field Hospital</span>
          <i class="fa-solid fa-download"></i>
        </a>
        <a href="flourish_data/10_flourish_scene10_strategic_gauges.csv" download class="bidwells-btn" style="justify-content:space-between;">
          <span><i class="fa-solid fa-file-csv text-yellow-400"></i> ฉากที่ 10: TU 2034 Strategic Horizon KPIs & Gauges</span>
          <i class="fa-solid fa-download"></i>
        </a>
      </div>
    </div>
  </div>

  <!-- Bidwells Editorial Footer -->
  <footer class="bidwells-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="brand-mark">
          <div class="brand-emblem">90</div>
          <div>
            <h2 style="font-size: 18px; color: #FFF;">90 ปี มหาวิทยาลัยธรรมศาสตร์ (พ.ศ. 2477 — 2567)</h2>
            <span style="font-size: 12px; color: var(--tu-gold);">BI304 Data Visualization & Storytelling | Thammasat Business School (TBS)</span>
          </div>
        </div>

        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
          <a href="story board.pdf" target="_blank" class="bidwells-btn"><i class="fa-solid fa-file-pdf"></i> Storyboard PDF</a>
          <a href="v1/index.html" target="_blank" class="bidwells-btn" title="ดูคลังข้อมูลนำเสนอผลงานเดิม"><i class="fa-solid fa-box-archive"></i> คลังเรื่องราว (Classic Edition)</a>
          <a href="https://kondee-rgb.github.io/BI304-Thammasat-Data-Storytelling/" target="_blank" class="bidwells-btn primary"><i class="fa-solid fa-globe"></i> Live Website</a>
        </div>
      </div>

      <div class="footer-credits">
        <div>
          <strong style="color: var(--tu-gold); display: block; margin-bottom: 6px;">อาจารย์ผู้สอน & หลักสูตร</strong>
          <p>อาจารย์ ดร. นพธนิษฐ์ โชติสาร (Dr. Noptanit Chotisarn)<br>วิชา BI304 การแสดงผลข้อมูลและการเล่าเรื่องด้วยข้อมูล<br>คณะพาณิชยศาสตร์และการบัญชี มหาวิทยาลัยธรรมศาสตร์</p>
        </div>
        <div>
          <strong style="color: var(--tu-gold); display: block; margin-bottom: 6px;">แรงบันดาลใจและงานออกแบบ</strong>
          <p>Bidwells: Driving Innovation at Speed Research Scrollytelling<br>BMW Group Annual Report 2024 Digital Experience<br>100% Free Open-Source Libraries (Plotly.js, Leaflet.js, CartoDB)</p>
        </div>
        <div>
          <strong style="color: var(--tu-gold); display: block; margin-bottom: 6px;">แหล่งข้อมูลทางการ</strong>
          <p>สำนักงานทะเบียนนักศึกษา มหาวิทยาลัยธรรมศาสตร์<br>กองแผนงาน มหาวิทยาลัยธรรมศาสตร์ (งบประมาณ 2563-2567)<br>QS World Subject Rankings & THE Impact Rankings 2024</p>
        </div>
      </div>
    </div>
  </footer>

  <!-- Scripts: Plotly, Leaflet, Scrollytelling & Visual Engine -->
  <script>
    // State
    let activeScene = 1;
    const totalScenes = 10;
    let leafMap = null;
    let mapMarkers = {};

    const chaptersMeta = [
      { num: 1, year: "2477", title: "วิวัฒนาการ 9 ทศวรรษ" },
      { num: 2, year: "2529", title: "ยุทธศาสตร์ 4 ศูนย์" },
      { num: 3, year: "2538", title: "โครงสร้าง 26 คณะ" },
      { num: 4, year: "2545", title: "มิติประชากร: หญิง 62.4%" },
      { num: 5, year: "2548", title: "การย้ายศูนย์การศึกษา" },
      { num: 6, year: "2563", title: "งบประมาณ 5 ปี" },
      { num: 7, year: "2565", title: "เปรียบเทียบ Business School" },
      { num: 8, year: "2566", title: "SDG 11 เมืองยั่งยืน" },
      { num: 9, year: "2567", title: "รพ.ธรรมศาสตร์เฉลิมพระเกียรติ" },
      { num: 10, year: "2034", title: "TU 2034 Strategic Cockpit" }
    ];

    // Plotly Dark Theme
    const plotlyDarkTheme = {
      paper_bgcolor: 'rgba(0,0,0,0)',
      plot_bgcolor: 'rgba(0,0,0,0)',
      font: { family: "'Prompt', 'Manrope', sans-serif", color: '#CBD5E1', size: 12 },
      colorway: ['#DC2626', '#F59E0B', '#06B6D4', '#10B981', '#8B5CF6', '#EC4899', '#F97316'],
      xaxis: {
        gridcolor: 'rgba(255, 255, 255, 0.08)',
        zerolinecolor: 'rgba(255, 255, 255, 0.15)',
        tickfont: { color: '#94A3B8' }
      },
      yaxis: {
        gridcolor: 'rgba(255, 255, 255, 0.08)',
        zerolinecolor: 'rgba(255, 255, 255, 0.15)',
        tickfont: { color: '#94A3B8' }
      },
      legend: { font: { color: '#CBD5E1' } }
    };

    // SCENE 1: Straight Line Chart with Discrete Milestones
    function drawScene1(filterType = 'all') {
      const years = [2477, 2488, 2495, 2508, 2516, 2519, 2529, 2538, 2539, 2548, 2558, 2567];
      const students = [7094, 9800, 4200, 11500, 14200, 15800, 21000, 25000, 27500, 33200, 39400, 42650];
      const notes = [
        "2477: ก่อตั้ง มธก. มหาวิทยาลัยเปิดเพื่อราษฎร (7,094 คน)",
        "2488: ยุคหลังสงคราม ขยายวิชาการพาณิชย์และการบัญชี",
        "2495: จุดเปลี่ยน พ.ร.บ. มธ. ปรับเป็น 'ระบบปิด' สอบคัดเลือกเข้มข้น (4,200 คน)",
        "2508: ปฏิรูปวิชาการยุค อ.ป๋วย อึ๊งภากรณ์ และ อ.สัญญา ธรรมศักดิ์",
        "2516: ขบวนการประชาธิปไตย 14 ตุลาคม 2516",
        "2519: เหตุการณ์ 6 ตุลาคม 2519 ธรรมศาสตร์หัวใจประชาธิปไตย",
        "2529: เปิด 'ศูนย์รังสิต' รองรับเอเชียนเกมส์ 13 ขยายสู่สหวิทยาการ (21,000 คน)",
        "2538: เปิด 'ศูนย์พัทยา' เน้นยานยนต์ นวัตกรรม และ EEC",
        "2539: เปิด 'ศูนย์ลำปาง' กระจายโอกาสการศึกษาสู่ภาคเหนือ",
        "2548: ย้ายการเรียนปริญญาตรีทั้งหมดสู่รังสิต ท่าพระจันทร์เน้น ป.โท-เอก",
        "2558: เปลี่ยนสถานะเป็นมหาวิทยาลัยในกำกับของรัฐ (39,400 คน)",
        "2567: ครบรอบ 90 ปี 4 วิทยาเขต 26 คณะ ก้าวสู่นวัตกรรมโลก (42,650 คน)"
      ];

      const markerColors = years.map(y => {
        if (y === 2495) return '#F59E0B';
        if (y === 2529) return '#06B6D4';
        if (y === 2567) return '#10B981';
        return '#DC2626';
      });

      const traceLine = {
        x: years,
        y: students,
        mode: 'lines+markers+text',
        line: { color: '#DC2626', width: 3.5, shape: 'linear' },
        marker: { size: 10, color: markerColors, line: { color: '#FFFFFF', width: 2 } },
        text: ['2477 (เปิด)', '', '2495 (ระบบปิด)', '', '', '', '2529 (รังสิต)', '', '', '2548 (ย้ายป.ตรี)', '', '2567 (90 ปี)'],
        textposition: 'top center',
        textfont: { family: "'Prompt', sans-serif", size: 11, color: '#FDE68A' },
        hovertext: notes,
        hoverinfo: 'text+y',
        name: 'จำนวนนักศึกษา (คน)'
      };

      const shapes = [
        { type: 'rect', xref: 'x', yref: 'paper', x0: 2477, x1: 2495, y0: 0, y1: 1, fillcolor: 'rgba(220, 38, 38, 0.08)', line: { width: 0 } },
        { type: 'rect', xref: 'x', yref: 'paper', x0: 2495, x1: 2529, y0: 0, y1: 1, fillcolor: 'rgba(245, 158, 11, 0.08)', line: { width: 0 } },
        { type: 'rect', xref: 'x', yref: 'paper', x0: 2529, x1: 2548, y0: 0, y1: 1, fillcolor: 'rgba(6, 182, 212, 0.08)', line: { width: 0 } },
        { type: 'rect', xref: 'x', yref: 'paper', x0: 2548, x1: 2567, y0: 0, y1: 1, fillcolor: 'rgba(16, 185, 129, 0.08)', line: { width: 0 } }
      ];

      const annotations = [
        {
          x: 2495, y: 4200,
          text: '<strong>2495: พ.ร.บ. มธ. ปรับสู่ "ระบบปิด"</strong><br>สอบคัดเลือกเพื่อมาตรฐานวิชาการ',
          showarrow: true,
          arrowhead: 2,
          arrowcolor: '#F59E0B',
          arrowsize: 1.2,
          arrowwidth: 2,
          ax: 0, ay: -55,
          bgcolor: 'rgba(15, 23, 42, 0.9)',
          bordercolor: '#F59E0B',
          borderwidth: 1,
          font: { color: '#FDE68A', size: 11 }
        },
        {
          x: 2529, y: 21000,
          text: '<strong>2529: เปิดศูนย์รังสิต</strong><br>บุกเบิกวิทยาศาสตร์และเทคโนโลยี',
          showarrow: true,
          arrowhead: 2,
          arrowcolor: '#06B6D4',
          ax: -50, ay: -40,
          bgcolor: 'rgba(15, 23, 42, 0.9)',
          bordercolor: '#06B6D4',
          borderwidth: 1,
          font: { color: '#A5F3FC', size: 11 }
        }
      ];

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 50, r: 30, t: 30, b: 40 },
        shapes: shapes,
        annotations: annotations,
        xaxis: {
          ...plotlyDarkTheme.xaxis,
          title: 'ปี พ.ศ. (2477 — 2567)',
          tickmode: 'array',
          tickvals: [2477, 2495, 2516, 2529, 2539, 2548, 2558, 2567],
          range: [2475, 2570]
        },
        yaxis: {
          ...plotlyDarkTheme.yaxis,
          title: 'จำนวนนักศึกษา (คน)',
          range: [0, 47000]
        }
      };

      Plotly.newPlot('chartScene1', [traceLine], layout, { responsive: true, displayModeBar: false });
    }

    function filterScene1(type) {
      document.querySelectorAll('#scene1 .tool-chip').forEach(c => c.classList.remove('active'));
      event.target.classList.add('active');
      if (type === 'closed') {
        Plotly.relayout('chartScene1', { 'xaxis.range': [2485, 2532], 'yaxis.range': [2000, 24000] });
      } else if (type === 'rangsit') {
        Plotly.relayout('chartScene1', { 'xaxis.range': [2520, 2555], 'yaxis.range': [15000, 36000] });
      } else {
        Plotly.relayout('chartScene1', { 'xaxis.range': [2475, 2570], 'yaxis.range': [0, 47000] });
      }
    }

    // SCENE 2: Pretty Maps Architectural Edition (Leaflet + CartoDB Dark Matter)
    const campusesData = {
      prachan: {
        name: "ศูนย์ท่าพระจันทร์ (Tha Prachan)",
        lat: 13.7557, lng: 100.4930, zoom: 16,
        area: "49 ไร่", students: "6,310 คน (14.8%)",
        desc: "หัวใจประวัติศาสตร์ริมแม่น้ำเจ้าพระยา ศูนย์กลางบัณฑิตศึกษา (ป.โท-เอก) หลักสูตรนานาชาติ และตึกโดมสัญลักษณ์แห่งธรรมศาสตร์",
        connectivity: "MRT สถานีสนามไชย / ท่าเรือพระจันทร์-พรานนก / ท่ามหาราช"
      },
      rangsit: {
        name: "ศูนย์รังสิต (Rangsit Innovation Mega Campus)",
        lat: 14.0736, lng: 100.6067, zoom: 14,
        area: "1,757 ไร่", students: "33,480 คน (78.5%)",
        desc: "เมกะแคมปัสนวัตกรรมและการแพทย์ ศูนย์กลางการเรียนการสอนปริญญาตรีครบทุกสาขาวิชา โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ สวนป๋วย 100 ปี และศูนย์กีฬาเอเชียนเกมส์",
        connectivity: "รถไฟฟ้าชานเมืองสายสีแดง (สถานี มธ.รังสิต) / ถนนพหลโยธิน / ดอนเมืองโทลล์เวย์"
      },
      pattaya: {
        name: "ศูนย์พัทยา (Pattaya EEC Future Hub)",
        lat: 12.9236, lng: 100.9925, zoom: 14,
        area: "566 ไร่", students: "1,070 คน (2.5%)",
        desc: "ศูนย์กลางเทคโนโลยีขั้นสูง ยานยนต์ไฟฟ้าแห่งอนาคต (Future Mobility) สุขภาพแม่นยำ และการพัฒนาเขตพัฒนาพิเศษภาคตะวันออก (EEC)",
        connectivity: "มอเตอร์เวย์สาย 7 (กรุงเทพฯ-มาบตาพุด) / สนามบินอู่ตะเภา"
      },
      lampang: {
        name: "ศูนย์ลำปาง (Lampang Northern Cultural Hub)",
        lat: 18.2982, lng: 99.4897, zoom: 14,
        area: "464 ไร่", students: "1,790 คน (4.2%)",
        desc: "ฐานการศึกษาสู่ภาคเหนือ กระจายโอกาสทางการศึกษา วิจัยพัฒนาชุมชนล้านนา งานสร้างสรรค์หัตถศิลป์ และการท่องเที่ยวเชิงนิเวศ",
        connectivity: "ทางหลวงแผ่นดินหมายเลข 11 / ใกล้ตัวเมืองลำปางและเชียงใหม่"
      }
    };

    function initScene2Map() {
      if (leafMap) return;
      leafMap = L.map('mapScene2', {
        center: [14.8, 100.5],
        zoom: 6,
        zoomControl: true,
        attributionControl: false
      });

      L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        subdomains: 'abcd',
        maxZoom: 19
      }).addTo(leafMap);

      const createBeaconIcon = (label) => L.divIcon({
        className: 'custom-map-beacon',
        html: `<div style="display:flex;align-items:center;gap:8px;">
                 <div class="map-beacon-pulse"></div>
                 <div style="background:rgba(15,23,42,0.94);color:#FDE68A;border:1px solid #F59E0B;padding:3px 8px;border-radius:6px;font-size:11px;font-weight:600;white-space:nowrap;box-shadow:0 0 10px rgba(0,0,0,0.8);">${label}</div>
               </div>`,
        iconSize: [120, 30],
        iconAnchor: [10, 15]
      });

      Object.entries(campusesData).forEach(([key, d]) => {
        const marker = L.marker([d.lat, d.lng], { icon: createBeaconIcon(d.name.split(' ')[0]) }).addTo(leafMap);
        marker.on('click', () => zoomMapCampus(key));
        mapMarkers[key] = marker;
      });

      const coords = [
        [campusesData.prachan.lat, campusesData.prachan.lng],
        [campusesData.rangsit.lat, campusesData.rangsit.lng],
        [campusesData.lampang.lat, campusesData.lampang.lng]
      ];
      L.polyline(coords, { color: '#DC2626', weight: 2, opacity: 0.65, dashArray: '6, 8' }).addTo(leafMap);

      const eecCoords = [
        [campusesData.rangsit.lat, campusesData.rangsit.lng],
        [campusesData.pattaya.lat, campusesData.pattaya.lng]
      ];
      L.polyline(eecCoords, { color: '#F59E0B', weight: 2, opacity: 0.65, dashArray: '6, 8' }).addTo(leafMap);
    }

    function zoomMapCampus(campusKey) {
      document.querySelectorAll('#scene2 .tool-chip').forEach(c => c.classList.remove('active'));
      if (event && event.target && event.target.classList) event.target.classList.add('active');

      const cardName = document.getElementById('cardCampusName');
      const cardDesc = document.getElementById('cardCampusDesc');

      if (campusKey === 'all' || !campusesData[campusKey]) {
        leafMap.flyTo([14.8, 100.5], 6, { duration: 1.5 });
        cardName.innerHTML = "ยุทธศาสตร์ 4 ศูนย์การศึกษา มหาวิทยาลัยธรรมศาสตร์";
        cardDesc.innerHTML = "ครอบคลุมพื้นที่ 2,836 ไร่ เชื่อมโยงกรุงเทพฯ ปทุมธานี ชลบุรี และลำปาง รองรับนักศึกษา 42,650 คน";
        return;
      }

      const d = campusesData[campusKey];
      leafMap.flyTo([d.lat, d.lng], d.zoom, { duration: 1.8 });
      cardName.innerHTML = `<i class="fa-solid fa-location-dot text-red-500"></i> ${d.name}`;
      cardDesc.innerHTML = `<strong>พื้นที่:</strong> ${d.area} • <strong>นักศึกษา:</strong> ${d.students}<br>${d.desc}<br><small style="color:#94A3B8;"><i class="fa-solid fa-train"></i> การเดินทาง: ${d.connectivity}</small>`;
    }

    // SCENE 3: Treemap of Faculties with Interactive Click-to-Modal
    const facultyDetailDatabase = {
      tbs: {
        name: "คณะพาณิชยศาสตร์และการบัญชี (Thammasat Business School - TBS)",
        cluster: "สังคมศาสตร์และมนุษยศาสตร์",
        students: 4950,
        tcasScore: "72.45 — 84.80 คะแนน (คะแนนสูงสุดเป็นอันดับ 1 ของประเทศในสาขาบริหารธุรกิจ)",
        competition: "1 : 18.4 (ผู้สมัครกว่า 4,500 คน รับ 245 คน)",
        employmentRate: "97.8% (ได้งานทำภายใน 4 เดือนหลังสำเร็จการศึกษา)",
        avgSalary: "35,000 — 52,000 บาท/เดือน",
        flagships: "หลักสูตร BBA นานาชาติ, บัญชีบัณฑิต, การเงินและการลงทุน, ผู้ชนะการแข่งขัน World Case Competition มากที่สุดในไทย",
        accreditations: "Triple Crown (AACSB, EQUIS, AMBA) ได้รับการรับรองครบ 3 ตราสถาบันบริหารธุรกิจระดับโลก (เพียง 1% ของโลก)"
      },
      law: {
        name: "คณะนิติศาสตร์ (Faculty of Law)",
        cluster: "สังคมศาสตร์และมนุษยศาสตร์",
        students: 3800,
        tcasScore: "68.20 — 79.50 คะแนน",
        competition: "1 : 14.2",
        employmentRate: "95.4% (รวมการสอบผ่านเนติบัณฑิตและผู้พิพากษา)",
        avgSalary: "28,000 — 48,000 บาท/เดือน",
        flagships: "กฎหมายมหาชน, กฎหมายธุรกิจระหว่างประเทศ, กฎหมายพาณิชย์อิเล็กทรอนิกส์",
        accreditations: "สถาบันผลิตนักกฎหมาย ศาล อัยการ และที่ปรึกษากฎหมายชั้นนำอันดับ 1 ของไทย"
      },
      med: {
        name: "คณะแพทยศาสตร์ (Faculty of Medicine)",
        cluster: "วิทยาศาสตร์สุขภาพ",
        students: 1200,
        tcasScore: "68.85 — 78.40 คะแนน (กสพท.)",
        competition: "1 : 28.6",
        employmentRate: "100.0% (บรรจุเป็นแพทย์ใช้ทุนและแพทย์ประจำบ้าน)",
        avgSalary: "55,000 — 75,000 บาท/เดือน (รวมเบี้ยเลี้ยงและ พ.ต.ส.)",
        flagships: "แพทยศาสตรบัณฑิต, โครงการผลิตแพทย์เพื่อชนบท, ศูนย์การแพทย์ตติยภูมิชั้นสูง",
        accreditations: "มาตรฐานการศึกษาแพทยศาสตร์ระดับสากล WFME (World Federation for Medical Education)"
      },
      siit: {
        name: "สถาบันเทคโนโลยีนานาชาติสิรินธร (SIIT)",
        cluster: "นานาชาติและสถาบันบูรณาการ",
        students: 3100,
        tcasScore: "คัดเลือกผ่านคะแนนสอบข้อเขียน / Portfolio / SAT / A-Level (Math & Eng Top 10%)",
        competition: "1 : 8.5",
        employmentRate: "98.2%",
        avgSalary: "38,000 — 65,000 บาท/เดือน",
        flagships: "AI & Data Science, Computer Engineering, Industrial Engineering & Logistics",
        accreditations: "ABET สหรัฐอเมริกา และ AUN-QA การันตีมาตรฐานวิศวกรรมสากล"
      },
      tse: {
        name: "คณะวิศวกรรมศาสตร์ (Thammasat School of Engineering - TSE)",
        cluster: "วิทยาศาสตร์และเทคโนโลยี",
        students: 4200,
        tcasScore: "61.30 — 73.10 คะแนน",
        competition: "1 : 9.8",
        employmentRate: "94.6%",
        avgSalary: "32,000 — 46,000 บาท/เดือน",
        flagships: "วิศวกรรมยานยนต์ EV, ปัญญาประดิษฐ์ (AI), TEP-TEPE หลักสูตรสองสถาบันกับมหาวิทยาลัยชั้นนำในอังกฤษและเบลเยียม",
        accreditations: "สภาวิศวกรไทย และ AUN-QA"
      },
      econ: {
        name: "คณะเศรษฐศาสตร์ (Faculty of Economics)",
        cluster: "สังคมศาสตร์และมนุษยศาสตร์",
        students: 2200,
        tcasScore: "66.50 — 77.20 คะแนน",
        competition: "1 : 12.3",
        employmentRate: "96.2%",
        avgSalary: "32,000 — 50,000 บาท/เดือน",
        flagships: "BE หลักสูตรเศรษฐศาสตร์นานาชาติ, เศรษฐศาสตร์การเงินและการคลัง, เศรษฐมิติ",
        accreditations: "สถาบันผลิตนักเศรษฐศาสตร์และผู้ว่าการธนาคารแห่งประเทศไทยชั้นนำ"
      }
    };

    function drawScene3Treemap() {
      const labels = [
        "มหาวิทยาลัยธรรมศาสตร์",
        "สังคมศาสตร์-มนุษยศาสตร์", "วิทยาศาสตร์และเทคโนโลยี", "วิทยาศาสตร์สุขภาพ", "นานาชาติและสถาบันบูรณาการ",
        "พาณิชย์ฯ (TBS)", "นิติศาสตร์", "ศิลปศาสตร์", "เศรษฐศาสตร์", "รัฐศาสตร์", "วารสารศาสตร์ฯ", "สังคมวิทยาฯ",
        "วิศวกรรมศาสตร์ (TSE)", "วิทยาศาสตร์ฯ", "สถาปัตยกรรมฯ", "วิทยาลัยนวัตกรรม",
        "สหเวชศาสตร์", "สาธารณสุขศาสตร์", "แพทยศาสตร์", "พยาบาลศาสตร์", "เภสัชศาสตร์", "ทันตแพทยศาสตร์",
        "สถาบัน SIIT", "วิทยาลัยสหวิทยาการ", "วิทยาลัยนานาชาติ PBIC", "วิทยาลัยป๋วย อึ๊งภากรณ์"
      ];

      const parents = [
        "",
        "มหาวิทยาลัยธรรมศาสตร์", "มหาวิทยาลัยธรรมศาสตร์", "มหาวิทยาลัยธรรมศาสตร์", "มหาวิทยาลัยธรรมศาสตร์",
        "สังคมศาสตร์-มนุษยศาสตร์", "สังคมศาสตร์-มนุษยศาสตร์", "สังคมศาสตร์-มนุษยศาสตร์", "สังคมศาสตร์-มนุษยศาสตร์", "สังคมศาสตร์-มนุษยศาสตร์", "สังคมศาสตร์-มนุษยศาสตร์", "สังคมศาสตร์-มนุษยศาสตร์",
        "วิทยาศาสตร์และเทคโนโลยี", "วิทยาศาสตร์และเทคโนโลยี", "วิทยาศาสตร์และเทคโนโลยี", "วิทยาศาสตร์และเทคโนโลยี",
        "วิทยาศาสตร์สุขภาพ", "วิทยาศาสตร์สุขภาพ", "วิทยาศาสตร์สุขภาพ", "วิทยาศาสตร์สุขภาพ", "วิทยาศาสตร์สุขภาพ", "วิทยาศาสตร์สุขภาพ",
        "นานาชาติและสถาบันบูรณาการ", "นานาชาติและสถาบันบูรณาการ", "นานาชาติและสถาบันบูรณาการ", "นานาชาติและสถาบันบูรณาการ"
      ];

      const values = [
        42650,
        17900, 11100, 7650, 6000,
        4950, 3800, 2600, 2200, 2100, 1300, 1000,
        4200, 3900, 1600, 1400,
        1900, 1400, 1200, 1100, 1200, 850,
        3100, 1100, 900, 900
      ];

      const colors = [
        "#0B0F17",
        "#DC2626", "#0284C7", "#059669", "#D97706",
        "#B91C1C", "#EF4444", "#F87171", "#DC2626", "#B91C1C", "#991B1B", "#7F1D1D",
        "#0369A1", "#0284C7", "#38BDF8", "#7DD3FC",
        "#047857", "#059669", "#10B981", "#34D399", "#6EE7B7", "#A7F3D0",
        "#B45309", "#D97706", "#F59E0B", "#FBBF24"
      ];

      const data = [{
        type: 'treemap',
        labels: labels,
        parents: parents,
        values: values,
        textinfo: 'label+value+percent parent',
        textfont: { family: "'Prompt', sans-serif", size: 12, color: '#FFFFFF' },
        marker: { colors: colors, line: { width: 1.5, color: '#0B0F17' } },
        hoverinfo: 'label+value',
        hovertemplate: '<b>%{label}</b><br>จำนวนนักศึกษา: %{value:,} คน<br><i>คลิกเพื่อเจาะลึกคะแนน TCAS และรายละเอียด</i><extra></extra>'
      }];

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 0, r: 0, t: 0, b: 0 }
      };

      Plotly.newPlot('chartScene3', data, layout, { responsive: true, displayModeBar: false }).then(() => {
        const plotEl = document.getElementById('chartScene3');
        plotEl.on('plotly_click', function(data) {
          if (!data || !data.points || !data.points[0]) return;
          const label = data.points[0].label;
          if (label.includes("พาณิชย์") || label.includes("TBS")) showFacultyDetailModal('tbs');
          else if (label.includes("แพทย์")) showFacultyDetailModal('med');
          else if (label.includes("นิติ")) showFacultyDetailModal('law');
          else if (label.includes("SIIT")) showFacultyDetailModal('siit');
          else if (label.includes("วิศวกรรม") || label.includes("TSE")) showFacultyDetailModal('tse');
          else if (label.includes("เศรษฐศาสตร์")) showFacultyDetailModal('econ');
          else showFacultyDetailModal('tbs');
        });
      });
    }

    function showFacultyDetailModal(key) {
      const d = facultyDetailDatabase[key] || facultyDetailDatabase.tbs;
      const modal = document.getElementById('facultyModal');
      const content = document.getElementById('facultyModalContent');
      content.innerHTML = `
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(220,38,38,0.2);border:1px solid var(--tu-red);display:flex;align-items:center;justify-content:center;color:var(--tu-gold);font-size:18px;">
            <i class="fa-solid fa-graduation-cap"></i>
          </div>
          <div>
            <span style="font-size:12px;color:var(--tu-gold);font-weight:600;">${d.cluster}</span>
            <h3 style="font-size:22px;color:#FFF;line-height:1.2;">${d.name}</h3>
          </div>
        </div>

        <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:12px;margin-bottom:24px;">
          <div style="background:rgba(15,23,42,0.8);border:1px solid var(--border-glass);border-radius:12px;padding:14px;text-align:center;">
            <div style="font-size:11px;color:#94A3B8;">นักศึกษาปัจจุบัน</div>
            <div style="font-family:'Prompt';font-size:22px;font-weight:700;color:var(--tu-gold);">${d.students.toLocaleString()} คน</div>
          </div>
          <div style="background:rgba(15,23,42,0.8);border:1px solid var(--border-glass);border-radius:12px;padding:14px;text-align:center;">
            <div style="font-size:11px;color:#94A3B8;">อัตราการได้งานทำ</div>
            <div style="font-family:'Prompt';font-size:22px;font-weight:700;color:#10B981;">${d.employmentRate}</div>
          </div>
          <div style="background:rgba(15,23,42,0.8);border:1px solid var(--border-glass);border-radius:12px;padding:14px;text-align:center;">
            <div style="font-size:11px;color:#94A3B8;">อัตราการแข่งขัน</div>
            <div style="font-family:'Prompt';font-size:22px;font-weight:700;color:#38BDF8;">${d.competition}</div>
          </div>
        </div>

        <div style="background:rgba(15,23,42,0.6);border:1px solid var(--border-glass);border-radius:14px;padding:18px;margin-bottom:16px;">
          <h5 style="color:var(--tu-gold);font-size:14px;margin-bottom:8px;"><i class="fa-solid fa-bullseye"></i> คะแนนสอบเข้า TCAS รอบ 3 Admission:</h5>
          <p style="font-size:14px;color:#F1F5F9;font-weight:500;">${d.tcasScore}</p>
        </div>

        <div style="background:rgba(15,23,42,0.6);border:1px solid var(--border-glass);border-radius:14px;padding:18px;margin-bottom:16px;">
          <h5 style="color:#10B981;font-size:14px;margin-bottom:8px;"><i class="fa-solid fa-money-bill-trend-up"></i> เงินเดือนเฉลี่ยเริ่มต้นของบัณฑิต:</h5>
          <p style="font-size:14px;color:#F1F5F9;font-weight:500;">${d.avgSalary}</p>
        </div>

        <div style="background:rgba(15,23,42,0.6);border:1px solid var(--border-glass);border-radius:14px;padding:18px;">
          <h5 style="color:#A78BFA;font-size:14px;margin-bottom:8px;"><i class="fa-solid fa-trophy"></i> มาตรฐานระดับโลกและหลักสูตรเรือธง:</h5>
          <p style="font-size:13px;color:#CBD5E1;margin-bottom:6px;"><strong>หลักสูตรเด่น:</strong> ${d.flagships}</p>
          <p style="font-size:13px;color:#CBD5E1;"><strong>การรับรองสากล:</strong> ${d.accreditations}</p>
        </div>
      `;
      modal.classList.add('open');
    }

    function closeFacultyModal() {
      document.getElementById('facultyModal').classList.remove('open');
    }

    // SCENE 4: Gender Diversity (Exact User Title)
    function drawScene4() {
      const clusters = ['สังคมศาสตร์ฯ', 'วิทยาศาสตร์ฯ', 'วิทยาศาสตร์สุขภาพ', 'นานาชาติ/บูรณาการ'];
      const femaleCounts = [11450, 4880, 5200, 3600];
      const maleCounts = [6450, 6220, 2450, 2400];

      const traceFemale = {
        x: femaleCounts,
        y: clusters,
        type: 'bar',
        orientation: 'h',
        name: 'นักศึกษาหญิง (62.4%)',
        marker: { color: '#F43F5E', line: { color: '#FDA4AF', width: 1 } },
        text: ['64.0%', '44.0%', '68.0%', '60.0%'],
        textposition: 'inside',
        insidetextanchor: 'middle',
        textfont: { color: '#FFFFFF', family: "'Prompt', sans-serif", weight: 'bold' }
      };

      const traceMale = {
        x: maleCounts,
        y: clusters,
        type: 'bar',
        orientation: 'h',
        name: 'นักศึกษาชาย (37.6%)',
        marker: { color: '#0284C7', line: { color: '#38BDF8', width: 1 } },
        text: ['36.0%', '56.0%', '32.0%', '40.0%'],
        textposition: 'inside',
        insidetextanchor: 'middle',
        textfont: { color: '#FFFFFF', family: "'Prompt', sans-serif" }
      };

      const layout = {
        ...plotlyDarkTheme,
        barmode: 'stack',
        margin: { l: 140, r: 30, t: 30, b: 40 },
        xaxis: {
          ...plotlyDarkTheme.xaxis,
          title: 'จำนวนนักศึกษา (คน)'
        },
        yaxis: {
          ...plotlyDarkTheme.yaxis,
          autorange: 'reversed'
        },
        legend: { orientation: 'h', y: -0.2 }
      };

      Plotly.newPlot('chartScene4', [traceFemale, traceMale], layout, { responsive: true, displayModeBar: false });
    }

    // SCENE 5: Intuitive Multi-Era Campus Distribution & Shift Matrix
    function drawScene5(filterEra = 'all') {
      const eras = [
        "ยุค 1: ท่าพระจันทร์ล้วน<br>(2477 — 2494)",
        "ยุค 2: ระบบปิดเข้มข้น<br>(2495 — 2528)",
        "ยุค 3: ขยายสู่รังสิต<br>(2529 — 2547)",
        "ยุค 4: มหาวิทยาลัยวิจัย<br>(2548 — ปัจจุบัน 2567)"
      ];

      const prachan = [7094, 15800, 12600, 6310];
      const rangsit = [0, 0, 7350, 33480];
      const regional = [0, 0, 1050, 2860];

      const tracePrachan = {
        x: eras,
        y: prachan,
        name: 'ศูนย์ท่าพระจันทร์',
        type: 'bar',
        marker: { color: '#DC2626' },
        text: ['100%', '100%', '60.0%', '14.8%'],
        textposition: 'inside',
        textfont: { family: "'Prompt'", color: '#FFF' }
      };

      const traceRangsit = {
        x: eras,
        y: rangsit,
        name: 'ศูนย์รังสิต (Mega Campus)',
        type: 'bar',
        marker: { color: '#0284C7' },
        text: ['', '', '35.0%', '78.5%'],
        textposition: 'inside',
        textfont: { family: "'Prompt'", color: '#FFF' }
      };

      const traceRegional = {
        x: eras,
        y: regional,
        name: 'ศูนย์พัทยา & ลำปาง',
        type: 'bar',
        marker: { color: '#F59E0B' },
        text: ['', '', '5.0%', '6.7%'],
        textposition: 'inside',
        textfont: { family: "'Prompt'", color: '#FFF' }
      };

      const layout = {
        ...plotlyDarkTheme,
        barmode: 'stack',
        margin: { l: 50, r: 30, t: 30, b: 60 },
        xaxis: {
          ...plotlyDarkTheme.xaxis,
          tickfont: { size: 11, family: "'Prompt', sans-serif" }
        },
        yaxis: {
          ...plotlyDarkTheme.yaxis,
          title: 'จำนวนนักศึกษา (คน)'
        },
        legend: { orientation: 'h', y: -0.25 }
      };

      Plotly.newPlot('chartScene5', [tracePrachan, traceRangsit, traceRegional], layout, { responsive: true, displayModeBar: false });
    }

    function renderScene5Era(era) {
      document.querySelectorAll('#scene5 .tool-chip').forEach(c => c.classList.remove('active'));
      event.target.classList.add('active');
      drawScene5(era);
    }

    // SCENE 6: 5-Year Budget Trend with Click-to-Drilldown
    const budgetYearDetails = {
      2563: { total: 11280, gov: 3580, tuition: 4120, hospital: 1820, endowment: 1040, grants: 720 },
      2564: { total: 11650, gov: 3620, tuition: 4210, hospital: 1910, endowment: 1110, grants: 800 },
      2565: { total: 12120, gov: 3750, tuition: 4350, hospital: 2020, endowment: 1140, grants: 860 },
      2566: { total: 12890, gov: 3950, tuition: 4560, hospital: 2240, endowment: 1190, grants: 950 },
      2567: { total: 13745, gov: 4250, tuition: 4820, hospital: 2450, endowment: 1215, grants: 1010 }
    };

    function drawScene6(selectedYear = 2567) {
      const years = [2563, 2564, 2565, 2566, 2567];
      const totals = years.map(y => budgetYearDetails[y].total);
      const barColors = years.map(y => y === selectedYear ? '#F59E0B' : '#334155');

      const traceBar = {
        x: years.map(y => `ปี ${y}`),
        y: totals,
        type: 'bar',
        marker: { color: barColors, line: { color: '#F59E0B', width: years.map(y => y === selectedYear ? 2 : 0) } },
        text: totals.map(t => `${t.toLocaleString()} ลบ.`),
        textposition: 'auto',
        textfont: { family: "'Prompt'", color: '#FFFFFF', weight: 'bold' },
        name: 'งบประมาณรวม (ล้านบาท)'
      };

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 50, r: 20, t: 20, b: 40 },
        yaxis: {
          ...plotlyDarkTheme.yaxis,
          title: 'ล้านบาท',
          range: [0, 16000]
        }
      };

      Plotly.newPlot('chartScene6', [traceBar], layout, { responsive: true, displayModeBar: false }).then(() => {
        const plot = document.getElementById('chartScene6');
        plot.on('plotly_click', function(data) {
          if (!data || !data.points || !data.points[0]) return;
          const yearNum = parseInt(data.points[0].x.replace('ปี ', ''));
          if (yearNum) drilldownBudgetYear(yearNum);
        });
      });
    }

    function drilldownBudgetYear(year) {
      document.querySelectorAll('#scene6 .tool-chip').forEach(c => c.classList.remove('active'));
      if (event && event.target && event.target.classList) event.target.classList.add('active');

      const d = budgetYearDetails[year] || budgetYearDetails[2567];
      const subTitle = document.getElementById('scene6SubTitle');
      if (subTitle) subTitle.innerHTML = `เจาะลึกโครงสร้าง 5 แหล่งรายได้ปี พ.ศ. ${year} (งบประมาณรวม: <strong>${d.total.toLocaleString()} ล้านบาท</strong>)`;

      const sources = [
        "ค่าธรรมเนียมศึกษา & วิชาการ",
        "งบประมาณแผ่นดิน (รัฐบาล)",
        "รพ.ธรรมศาสตร์ฯ บริการสุขภาพ",
        "ทรัพย์สิน ลงทุน & สิทธิประโยชน์",
        "ทุนวิจัย & นวัตกรรมภายนอก"
      ];
      const amounts = [d.tuition, d.gov, d.hospital, d.endowment, d.grants];

      const traceDonut = {
        labels: sources,
        values: amounts,
        type: 'pie',
        hole: 0.55,
        textinfo: 'label+percent',
        textposition: 'inside',
        marker: {
          colors: ['#DC2626', '#0284C7', '#10B981', '#F59E0B', '#8B5CF6'],
          line: { color: '#0B0F17', width: 2 }
        },
        hovertemplate: '<b>%{label}</b><br>จำนวนเงิน: %{value:,} ล้านบาท (%{percent})<extra></extra>'
      };

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 20, r: 20, t: 20, b: 20 },
        annotations: [{
          font: { size: 16, family: "'Prompt'", color: '#F59E0B', weight: 'bold' },
          showarrow: false,
          text: `ปี ${year}<br><span style="font-size:12px;color:#94A3B8;">${d.total.toLocaleString()} ลบ.</span>`,
          x: 0.5, y: 0.5
        }],
        legend: { orientation: 'h', y: -0.15 }
      };

      Plotly.newPlot('chartScene6', [traceDonut], layout, { responsive: true, displayModeBar: false });
    }

    // SCENE 7: Business School Benchmark (TBS vs CBS vs Sasin vs CMMU)
    function drawScene7(mode = 'all') {
      const categories = [
        "การรับรอง Triple Crown",
        "QS World Ranking (Top 150)",
        "ความเป็นสากล & นักศึกษาต่างชาติ",
        "เครือข่ายศิษย์เก่า & ตลาดทุน",
        "แชมป์แข่งกรณีศึกษาโลก (Case Comp)",
        "งานวิจัย & นวัตกรรมจัดการ"
      ];

      const tbsScores = [100, 92, 95, 96, 100, 90];
      const cbsScores = [100, 94, 90, 98, 88, 92];
      const sasinScores = [80, 85, 92, 90, 82, 85];
      const cmmuScores = [65, 75, 78, 82, 74, 86];

      const traces = [];

      if (mode === 'all' || mode === 'tbs' || mode === 'tbs_cbs') {
        traces.push({
          type: 'scatterpolar',
          r: [...tbsScores, tbsScores[0]],
          theta: [...categories, categories[0]],
          fill: 'toself',
          fillcolor: 'rgba(220, 38, 38, 0.25)',
          name: 'TBS คณะพาณิชย์ฯ ธรรมศาสตร์',
          line: { color: '#DC2626', width: 2.5 }
        });
      }

      if (mode === 'all' || mode === 'tbs_cbs') {
        traces.push({
          type: 'scatterpolar',
          r: [...cbsScores, cbsScores[0]],
          theta: [...categories, categories[0]],
          fill: 'toself',
          fillcolor: 'rgba(236, 72, 153, 0.2)',
          name: 'CBS คณะบัญชีฯ จุฬาฯ',
          line: { color: '#EC4899', width: 2 }
        });
      }

      if (mode === 'all') {
        traces.push({
          type: 'scatterpolar',
          r: [...sasinScores, sasinScores[0]],
          theta: [...categories, categories[0]],
          fill: 'toself',
          fillcolor: 'rgba(6, 182, 212, 0.15)',
          name: 'Sasin School of Management',
          line: { color: '#06B6D4', width: 1.8 }
        });
        traces.push({
          type: 'scatterpolar',
          r: [...cmmuScores, cmmuScores[0]],
          theta: [...categories, categories[0]],
          fill: 'toself',
          fillcolor: 'rgba(16, 185, 129, 0.15)',
          name: 'CMMU วิทยาลัยการจัดการ มหิดล',
          line: { color: '#10B981', width: 1.8 }
        });
      }

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 40, r: 40, t: 20, b: 30 },
        polar: {
          radialaxis: {
            visible: true,
            range: [0, 100],
            gridcolor: 'rgba(255, 255, 255, 0.1)',
            tickfont: { color: '#94A3B8' }
          },
          angularaxis: {
            gridcolor: 'rgba(255, 255, 255, 0.1)',
            tickfont: { family: "'Prompt'", size: 11, color: '#F1F5F9' }
          },
          bgcolor: 'rgba(0,0,0,0)'
        },
        legend: { orientation: 'h', y: -0.2 }
      };

      Plotly.newPlot('chartScene7', traces, layout, { responsive: true, displayModeBar: false });
    }

    function filterBschoolBenchmark(mode) {
      document.querySelectorAll('#scene7 .tool-chip').forEach(c => c.classList.remove('active'));
      event.target.classList.add('active');
      drawScene7(mode);
    }

    // SCENE 8: SDG 11 Radar & Campus Sustainability
    function drawScene8() {
      const dimensions = [
        "TU Solar Rooftop (23.6 MW)",
        "สวนป๋วย 100 ปี (22,000 ตร.ม.)",
        "ขนส่งมวลชน EV 100%",
        "การจัดการขยะ Circular Economy",
        "ความปลอดภัยและเมืองต้นแบบ",
        "การเข้าถึงสุขภาพของชุมชน"
      ];
      const scores = [98, 95, 92, 88, 90, 94];

      const trace = {
        type: 'scatterpolar',
        r: [...scores, scores[0]],
        theta: [...dimensions, dimensions[0]],
        fill: 'toself',
        fillcolor: 'rgba(16, 185, 129, 0.25)',
        name: 'Thammasat SDG 11 Score',
        line: { color: '#10B981', width: 2.5 }
      };

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 40, r: 40, t: 20, b: 30 },
        polar: {
          radialaxis: {
            visible: true,
            range: [0, 100],
            gridcolor: 'rgba(255, 255, 255, 0.1)',
            tickfont: { color: '#94A3B8' }
          },
          angularaxis: {
            gridcolor: 'rgba(255, 255, 255, 0.1)',
            tickfont: { family: "'Prompt'", size: 11, color: '#F1F5F9' }
          },
          bgcolor: 'rgba(0,0,0,0)'
        }
      };

      Plotly.newPlot('chartScene8', [trace], layout, { responsive: true, displayModeBar: false });
    }

    // SCENE 9: Thammasat Hospital Dual-Axis
    function drawScene9(mode = 'growth') {
      if (mode === 'specialties') {
        const centers = ["ศูนย์หัวใจและหลอดเลือด", "ศูนย์มะเร็งครบวงจร", "ศูนย์หลอดเลือดสมอง (Stroke)", "ศูนย์อุบัติเหตุระดับ 1", "ศูนย์ผ่าตัดส่องกล้อง"];
        const visits = [320000, 240000, 180000, 290000, 210000];
        const traceCenters = {
          x: visits,
          y: centers,
          type: 'bar',
          orientation: 'h',
          marker: { color: '#F43F5E', line: { color: '#FDA4AF', width: 1 } },
          text: visits.map(v => `${(v/1000).toFixed(0)}k ครั้ง`),
          textposition: 'auto',
          textfont: { family: "'Prompt'", color: '#FFFFFF' }
        };
        const layout = {
          ...plotlyDarkTheme,
          margin: { l: 160, r: 30, t: 20, b: 30 },
          xaxis: { ...plotlyDarkTheme.xaxis, title: 'จำนวนผู้ป่วยเข้ารับการรักษา (ครั้ง/ปี)' },
          yaxis: { ...plotlyDarkTheme.yaxis, autorange: 'reversed' }
        };
        Plotly.newPlot('chartScene9', [traceCenters], layout, { responsive: true, displayModeBar: false });
        return;
      }

      const years = [2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567];
      const opd = [1.02, 1.08, 1.15, 1.22, 1.28, 1.18, 1.25, 1.34, 1.41, 1.45];
      const ipd = [24.5, 26.0, 27.8, 29.5, 31.0, 28.5, 30.2, 32.8, 34.1, 35.2];

      const traceOPD = {
        x: years.map(y => `ปี ${y}`),
        y: opd,
        name: 'ผู้ป่วยนอก (ล้านครั้ง/ปี)',
        type: 'bar',
        marker: { color: '#0284C7' },
        yaxis: 'y1'
      };

      const traceIPD = {
        x: years.map(y => `ปี ${y}`),
        y: ipd,
        name: 'ผู้ป่วยใน (พันคน/ปี)',
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: '#F59E0B', width: 3 },
        marker: { size: 8, color: '#FFFFFF', line: { color: '#F59E0B', width: 2 } },
        yaxis: 'y2'
      };

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 50, r: 50, t: 20, b: 40 },
        yaxis: {
          ...plotlyDarkTheme.yaxis,
          title: 'ผู้ป่วยนอก (ล้านคน)',
          side: 'left',
          range: [0, 1.8]
        },
        yaxis2: {
          ...plotlyDarkTheme.yaxis,
          title: 'ผู้ป่วยใน (พันคน)',
          side: 'right',
          overlaying: 'y',
          range: [0, 45],
          gridcolor: 'rgba(0,0,0,0)'
        },
        legend: { orientation: 'h', y: -0.2 }
      };

      Plotly.newPlot('chartScene9', [traceOPD, traceIPD], layout, { responsive: true, displayModeBar: false });
    }

    function toggleHospitalMode(mode) {
      document.querySelectorAll('#scene9 .tool-chip').forEach(c => c.classList.remove('active'));
      event.target.classList.add('active');
      drawScene9(mode);
    }

    // SCENE 10: Cockpit Simulator
    function updateSimulator() {
      const research = parseInt(document.getElementById('sliderResearch').value);
      const ai = parseInt(document.getElementById('sliderAI').value);
      const green = parseInt(document.getElementById('sliderGreen').value);

      document.getElementById('valResearch').innerText = research + '%';
      document.getElementById('valAI').innerText = ai + '%';
      document.getElementById('valGreen').innerText = green + '%';

      const projectedRank = Math.max(75, Math.round(180 - (research * 1.2 + ai * 0.9 + green * 0.4)));
      const employability = Math.min(99.5, (85 + (ai * 0.22 + research * 0.1)).toFixed(1));

      const gaugeData = [
        {
          type: "indicator",
          mode: "gauge+number",
          value: projectedRank,
          title: { text: "คาดการณ์อันดับโลก QS 2034<br><span style='font-size:11px;color:#94A3B8;'>(ยิ่งน้อยยิ่งสูง)</span>", font: { size: 13, family: "'Prompt'" } },
          gauge: {
            axis: { range: [50, 200], tickcolor: "#94A3B8" },
            bar: { color: "#F59E0B" },
            steps: [
              { range: [50, 100], color: "rgba(16, 185, 129, 0.25)" },
              { range: [100, 150], color: "rgba(6, 182, 212, 0.25)" },
              { range: [150, 200], color: "rgba(220, 38, 38, 0.25)" }
            ]
          },
          domain: { row: 0, column: 0 }
        },
        {
          type: "indicator",
          mode: "gauge+number",
          value: parseFloat(employability),
          number: { suffix: "%" },
          title: { text: "ความพร้อมตลาดงานโลก<br><span style='font-size:11px;color:#94A3B8;'>Global Employability</span>", font: { size: 13, family: "'Prompt'" } },
          gauge: {
            axis: { range: [80, 100], tickcolor: "#94A3B8" },
            bar: { color: "#06B6D4" },
            steps: [
              { range: [80, 90], color: "rgba(51, 65, 85, 0.4)" },
              { range: [90, 100], color: "rgba(6, 182, 212, 0.3)" }
            ]
          },
          domain: { row: 0, column: 1 }
        }
      ];

      const layout = {
        ...plotlyDarkTheme,
        margin: { l: 20, r: 20, t: 25, b: 20 },
        grid: { rows: 1, columns: 2, pattern: 'independent' }
      };

      Plotly.newPlot('chartScene10Gauges', gaugeData, layout, { responsive: true, displayModeBar: false });
    }

    function resetSimulator() {
      document.getElementById('sliderResearch').value = 35;
      document.getElementById('sliderAI').value = 40;
      document.getElementById('sliderGreen').value = 25;
      updateSimulator();
    }

    // Navigation and Continuous Timeline Progress
    function scrollToScene(num) {
      const el = document.getElementById(`scene${num}`);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }

    function updateTimelineTrack(sceneNum) {
      activeScene = sceneNum;
      const meta = chaptersMeta[sceneNum - 1];
      if (meta) {
        const bubble = document.getElementById('markerYearBubble');
        if (bubble) bubble.innerText = meta.year;
      }

      const progressPct = ((sceneNum - 1) / (totalScenes - 1)) * 100;
      const clampedPct = Math.min(95, Math.max(5, progressPct));

      const glow = document.getElementById('roadProgressGlow');
      if (glow) glow.style.height = clampedPct + '%';

      const marker = document.getElementById('walkingStudentMarker');
      if (marker) marker.style.top = clampedPct + '%';
    }

    // Scroll Observer for Bidwells Sections
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const sceneNum = parseInt(entry.target.getAttribute('data-scene'));
          if (sceneNum) {
            updateTimelineTrack(sceneNum);
            if (sceneNum === 2 && leafMap) {
              leafMap.invalidateSize();
            }
          }
        }
      });
    }, { rootMargin: '-25% 0px -40% 0px', threshold: 0.1 });

    document.querySelectorAll('.chapter-section').forEach(s => observer.observe(s));

    // Responsive Auto Resize for all charts and map
    window.addEventListener('resize', () => {
      const chartIds = ['chartScene1', 'chartScene3', 'chartScene4', 'chartScene5', 'chartScene6', 'chartScene7', 'chartScene8', 'chartScene9', 'chartScene10Gauges'];
      chartIds.forEach(id => {
        const el = document.getElementById(id);
        if (el && el.data) {
          try { Plotly.Plots.resize(el); } catch (e) {}
        }
      });
      if (leafMap) leafMap.invalidateSize();
    });

    // Flourish Data Modal Handlers
    function openFlourishDataModal() {
      document.getElementById('flourishModal').classList.add('open');
    }
    function closeFlourishDataModal() {
      document.getElementById('flourishModal').classList.remove('open');
    }

    // Global Init
    window.addEventListener('DOMContentLoaded', () => {
      drawScene1();
      initScene2Map();
      drawScene3Treemap();
      drawScene4();
      drawScene5();
      drawScene6(2567);
      drawScene7('all');
      drawScene8();
      drawScene9('growth');
      updateSimulator();
      updateTimelineTrack(1);
    });
  </script>
</body>
</html>'''

    with open('d:/BI304/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    with open('d:/BI304/scrollytelling/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully built Bidwells-style Version 2 in d:/BI304/index.html and scrollytelling/index.html! Length:", len(html))

if __name__ == '__main__':
    build_bidwells_v2()
