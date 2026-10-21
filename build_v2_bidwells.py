# -*- coding: utf-8 -*-
"""
Authentic Bidwells-Style Scrollytelling Builder for 90 Years of Thammasat University
Refined Edition:
1. Central Racetrack with Top-Down F1 Race Cars (car-white.png and car-pink.png) replacing walking avatar.
2. Two-stage Hero sequence: Cover Title (0vh) -> Reveal of Starting Grid & Pole Position (100vh) -> Accelerated scroll into Statement.
3. High-Key Statement section with photo card, speech quote, watermark '90', and 3 winning cards with colored blocks.
4. Expanding Circular Wipe in Thammasat Crimson to Dark Blue Cluster Map with dotted matrix map & multi-era distribution chart.
5. Expanding Circular Wipe to Teal section with floating white 'Cost Cap' budget & demographic cards (Female 62.4%).
6. Curved Racetrack section using Track2.jpg with turning race cars & TBS Triple Crown benchmarking.
7. Silverstone-style Circuit Milestone Track with synchronized floating card & TU 2034 Strategy Cockpit.
8. Checkered Finish Line crossing (finish.svg) with speed trails (car-trials.svg) & download card.
9. Floating Bottom Scrubber Pill with progress bar and Classic Archive button (Strictly NO version numbers).
10. Preserves all 10 required Thammasat data storytelling topics with full interactive drilldown.
"""

import os
import sys

def generate_bidwells_html():
    html_code = '''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
  <title>90 Years of Thammasat University | Driving Innovation & Knowledge at Speed</title>

  <!-- Google Fonts: Merriweather for luxury editorial serif, Plus Jakarta Sans & Prompt for modern sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Sarabun:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- FontAwesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

  <!-- Chart.js 4 -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <!-- Leaflet 1.9.4 CSS & JS for Authentic Thailand Campus Geospatial Mapping -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <style>
    /* ==========================================================================
       BIDWELLS LUXURY EDITORIAL DESIGN SYSTEM
       Thammasat University 90th Anniversary Edition
       ========================================================================== */
    :root {
      --bidwells-navy: #0b163b;
      --bidwells-dark-blue: #101c3d;
      --bidwells-crimson: #c51944;
      --tu-crimson: #9e1b32;
      --tu-crimson-hover: #b31b34;
      --tu-gold: #ffc72c;
      --tu-gold-dark: #d99b00;
      --bidwells-sky-blue: #bfe5f2;
      --bidwells-sky-dark: #8acfe5;
      --bidwells-emerald: #00857c;
      --bidwells-teal: #006b68;
      --bidwells-offwhite: #f5f5f3;
      --bidwells-cream: #faf9f6;
      --bidwells-border: #e2e8f0;
      --bidwells-card-border: #111d4a;
      --bidwells-text: #1a202c;
      --bidwells-text-muted: #5a6578;
      --bidwells-radius: 16px;
      --bidwells-shadow: 0 12px 35px rgba(11, 22, 59, 0.08);
      --bidwells-shadow-lg: 0 24px 60px rgba(11, 22, 59, 0.16);
      --font-serif: 'Merriweather', 'Sarabun', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', 'Prompt', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
      color: var(--bidwells-text);
      background-color: var(--bidwells-offwhite);
      font-family: var(--font-sans);
    }

    body {
      line-height: 1.65;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    /* ==========================================================================
       1. FIXED TOP HEADER (Pure White Luxury Corporate Style - Exact Bidwells)
       ========================================================================== */
    .bidwells-header {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 76px;
      background: #ffffff;
      border-bottom: 1px solid rgba(0, 0, 0, 0.08);
      box-shadow: 0 2px 14px rgba(0, 0, 0, 0.04);
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
      transition: all 0.3s ease;
    }

    .header-logo-group {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-shrink: 0;
      cursor: pointer;
    }

    .header-brand-mark {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      background: linear-gradient(135deg, var(--tu-crimson) 0%, var(--bidwells-navy) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--tu-gold);
      font-size: 18px;
      box-shadow: 0 4px 12px rgba(158, 27, 50, 0.25);
    }

    .header-brand-text {
      display: flex;
      flex-direction: column;
    }

    .header-brand-title {
      font-family: var(--font-serif);
      font-size: 1.05rem;
      font-weight: 900;
      letter-spacing: 0.08em;
      color: var(--bidwells-navy);
      text-transform: uppercase;
      line-height: 1.2;
    }

    .header-brand-sub {
      font-size: 0.72rem;
      color: var(--bidwells-text-muted);
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .header-nav {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }

    .header-nav-link {
      font-size: 0.84rem;
      font-weight: 600;
      color: #334155;
      position: relative;
      padding: 8px 0;
      white-space: nowrap;
      transition: color 0.2s ease;
    }

    .header-nav-link:hover, .header-nav-link.active {
      color: var(--bidwells-crimson);
    }

    .header-nav-link::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0%;
      height: 2px;
      background: var(--bidwells-crimson);
      transition: width 0.25s ease;
    }

    .header-nav-link:hover::after, .header-nav-link.active::after {
      width: 100%;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-shrink: 0;
    }

    .btn-bidwells-pill {
      background: var(--bidwells-crimson);
      color: #ffffff;
      padding: 9px 20px;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(197, 25, 68, 0.25);
      transition: all 0.25s ease;
      white-space: nowrap;
    }

    .btn-bidwells-pill:hover {
      background: #a91238;
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(197, 25, 68, 0.35);
    }

    .header-archive-btn {
      color: #475569;
      font-size: 0.82rem;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 9999px;
      border: 1.5px solid #cbd5e1;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      transition: all 0.2s ease;
      background: #ffffff;
      cursor: pointer;
    }

    .header-colab-btn {
      color: #1e293b;
      font-size: 0.82rem;
      font-weight: 700;
      text-decoration: none;
      padding: 7px 15px;
      border: 1.5px solid #cbd5e1;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      white-space: nowrap;
      transition: all 0.2s ease;
      background: #ffffff;
      cursor: pointer;
    }

    .header-colab-btn:hover {
      color: #ea580c;
      border-color: #f97316;
      background: #fff7ed;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(234, 88, 12, 0.15);
    }

    .header-flourish-btn {
      color: #1e293b;
      font-size: 0.82rem;
      font-weight: 700;
      text-decoration: none;
      padding: 7px 15px;
      border: 1.5px solid #cbd5e1;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      white-space: nowrap;
      transition: all 0.2s ease;
      background: #ffffff;
      cursor: pointer;
    }

    .header-flourish-btn:hover {
      color: #0284c7;
      border-color: #0284c7;
      background: #f0f9ff;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.15);
    }

    /* ==========================================================================
       2. FIXED BOTTOM SCRUBBER PILL (Exact Bidwells Floating Capsule)
       ========================================================================== */
    .bidwells-floating-scrubber {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 9999;
      background: #ffffff;
      border-radius: 9999px;
      box-shadow: 0 14px 40px rgba(11, 22, 59, 0.22);
      border: 1px solid rgba(0, 0, 0, 0.08);
      padding: 7px 12px 7px 24px;
      display: flex;
      align-items: center;
      gap: 22px;
      transition: all 0.3s ease;
      backdrop-filter: blur(10px);
    }

    .scrubber-track-container {
      display: flex;
      align-items: center;
      position: relative;
      width: 280px;
      height: 24px;
      cursor: pointer;
    }

    .scrubber-track-bg {
      position: absolute;
      left: 0;
      width: 100%;
      height: 4px;
      background: #e2e8f0;
      border-radius: 999px;
    }

    .scrubber-track-fill {
      position: absolute;
      left: 0;
      height: 4px;
      background: var(--bidwells-crimson);
      border-radius: 999px;
      width: 0%;
      transition: width 0.1s linear;
    }

    .scrubber-thumb {
      position: absolute;
      left: 0%;
      top: 50%;
      transform: translate(-50%, -50%);
      width: 16px;
      height: 16px;
      background: var(--bidwells-crimson);
      border: 3px solid #ffffff;
      border-radius: 50%;
      box-shadow: 0 0 12px rgba(197, 25, 68, 0.7);
      transition: left 0.1s linear;
      pointer-events: none;
    }

    .scrubber-pips {
      position: absolute;
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 2px;
    }

    .scrubber-pip {
      width: 6px;
      height: 6px;
      background: #94a3b8;
      border-radius: 50%;
      transition: all 0.2s ease;
    }

    .scrubber-pip.active {
      background: var(--bidwells-crimson);
      transform: scale(1.4);
    }

    .scrubber-download-btn {
      background: var(--bidwells-navy);
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .scrubber-download-btn:hover {
      background: #1c2b5e;
      transform: scale(1.02);
    }

    /* ==========================================================================
       3. HERO SECTION & STARTING RACETRACK (Exact Frames 000s - 007s)
       ========================================================================== */
    .hero-track-section {
      position: relative;
      min-height: 220vh;
      background-color: var(--bidwells-navy);
      background-image: 
        radial-gradient(circle at 50% 30%, #162a5b 0%, var(--bidwells-navy) 70%),
        repeating-linear-gradient(45deg, rgba(255,255,255,0.015) 0, rgba(255,255,255,0.015) 30px, transparent 30px, transparent 60px);
      color: #ffffff;
      overflow: hidden;
      padding-top: 76px;
    }

    /* Central Vertical Racetrack Stage */
    .central-track-stage {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 640px;
      height: 100%;
      background: #09122d;
      border-left: 2px solid rgba(255, 255, 255, 0.15);
      border-right: 2px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 0 60px rgba(0, 0, 0, 0.6);
      pointer-events: none;
      z-index: 1;
    }

    /* Left Checkerboard Racing Curb (like frame 006s) */
    .central-track-curb-left {
      position: absolute;
      top: 0;
      left: 0;
      width: 44px;
      height: 100%;
      background: repeating-linear-gradient(
        180deg,
        #e2e8f0 0px,
        #e2e8f0 40px,
        #1e293b 40px,
        #1e293b 80px
      );
      opacity: 0.85;
      border-right: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Right Track Border Curb */
    .central-track-curb-right {
      position: absolute;
      top: 0;
      right: 0;
      width: 14px;
      height: 100%;
      background: repeating-linear-gradient(
        180deg,
        rgba(255, 255, 255, 0.6) 0px,
        rgba(255, 255, 255, 0.6) 30px,
        transparent 30px,
        transparent 60px
      );
    }

    /* Dashed Center Road Line */
    .central-track-centerline {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 2px;
      height: 100%;
      background: repeating-linear-gradient(
        180deg,
        rgba(255, 255, 255, 0.35) 0px,
        rgba(255, 255, 255, 0.35) 40px,
        transparent 40px,
        transparent 80px
      );
    }

    /* Starting Grid Stage at Scroll 800px */
    .grid-box {
      position: absolute;
      border: 2px solid rgba(255, 255, 255, 0.85);
      border-top: none;
      border-radius: 0 0 4px 4px;
    }

    .grid-box-pole {
      top: 820px;
      left: 170px;
      width: 130px;
      height: 18px;
    }

    .grid-box-slot2 {
      top: 1040px;
      left: 380px;
      width: 130px;
      height: 18px;
    }

    .grid-box-label {
      position: absolute;
      top: -24px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      color: rgba(255, 255, 255, 0.65);
      white-space: nowrap;
    }

    /* The Thammasat Student Walkers on the Central Timeline Track */
    .tu-student-walker-container {
      position: absolute;
      z-index: 10;
      transition: transform 0.08s linear;
      will-change: transform;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .tu-student-leader {
      top: 650px;
      left: 175px;
      width: 125px;
    }

    .tu-student-scholar {
      top: 870px;
      left: 385px;
      width: 125px;
    }

    .tu-student-walker-img {
      width: 100%;
      height: auto;
      display: block;
      filter: drop-shadow(0 14px 24px rgba(0, 0, 0, 0.75));
      animation: student-stride 2s ease-in-out infinite alternate;
    }

    @keyframes student-stride {
      0% { transform: translateY(0px) rotate(-1deg); }
      50% { transform: translateY(-7px) rotate(1.5deg); }
      100% { transform: translateY(0px) rotate(-1deg); }
    }

    .tu-student-pedestal {
      width: 80px;
      height: 18px;
      border-radius: 50%;
      background: radial-gradient(ellipse at center, rgba(255, 199, 44, 0.55) 0%, rgba(197, 25, 68, 0.25) 50%, transparent 75%);
      margin-top: -10px;
      filter: blur(2px);
      box-shadow: 0 0 16px rgba(255, 199, 44, 0.6);
    }

    .tu-student-badge {
      margin-top: 8px;
      background: rgba(11, 22, 59, 0.92);
      border: 1px solid rgba(255, 199, 44, 0.45);
      color: var(--tu-gold);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      white-space: nowrap;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(6px);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Hero Typography & Overlays */
    .hero-content-overlay {
      position: relative;
      z-index: 20;
      max-width: 1200px;
      min-height: calc(100vh - 76px);
      margin: 0 auto;
      padding: 100px 2rem 60px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .hero-category-tag {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(197, 25, 68, 0.16);
      border: 1px solid rgba(197, 25, 68, 0.45);
      color: #ff9cb1;
      padding: 6px 20px;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 2rem;
      backdrop-filter: blur(8px);
    }

    .hero-main-title {
      font-family: var(--font-serif);
      font-size: 4.6rem;
      line-height: 1.12;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 1.5rem;
      text-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    .hero-main-title em {
      font-style: italic;
      font-weight: 400;
      color: var(--bidwells-sky-blue);
      display: inline-block;
    }

    .hero-title-thai {
      font-size: 1.65rem;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 1.25rem;
      letter-spacing: 0.02em;
    }

    .hero-lead-desc {
      font-size: 1.15rem;
      color: #cbd5e1;
      max-width: 820px;
      line-height: 1.7;
      margin-bottom: 2.5rem;
      text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
    }

    .hero-scroll-pill-btn {
      background: var(--bidwells-sky-blue);
      color: var(--bidwells-navy);
      font-size: 0.92rem;
      font-weight: 700;
      padding: 12px 28px;
      border-radius: 9999px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 6px 20px rgba(191, 229, 242, 0.35);
      transition: all 0.25s ease;
      animation: float-pill 2s ease-in-out infinite alternate;
    }

    @keyframes float-pill {
      0% { transform: translateY(0); }
      100% { transform: translateY(-6px); }
    }

    .hero-scroll-pill-btn:hover {
      background: #ffffff;
      transform: translateY(-4px);
      box-shadow: 0 10px 25px rgba(191, 229, 242, 0.5);
    }

    /* ==========================================================================
       4. SECTION 1: HIGH-KEY STATEMENT & 3 WINNING STAT CARDS (Frames 008s - 016s)
       ========================================================================== */
    .bidwells-statement-section {
      background-color: var(--bidwells-offwhite);
      padding: 120px 2rem 100px;
      position: relative;
      overflow: hidden;
    }

    .watermark-giant-num {
      position: absolute;
      top: 40px;
      right: 5%;
      font-family: var(--font-serif);
      font-size: 26rem;
      font-weight: 900;
      line-height: 0.8;
      color: transparent;
      -webkit-text-stroke: 2px rgba(17, 29, 74, 0.05);
      pointer-events: none;
      z-index: 0;
      user-select: none;
    }

    .statement-container {
      max-width: 1200px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }

    /* Left Photo Card + Overlapping Quote Box (Frame 009s) */
    .statement-quote-grid {
      display: grid;
      grid-template-columns: 460px 1fr;
      gap: 60px;
      align-items: center;
      margin-bottom: 90px;
    }

    .editorial-photo-card {
      position: relative;
    }

    .editorial-photo-frame {
      width: 100%;
      height: 480px;
      border-radius: 20px;
      overflow: hidden;
      border: 3px solid var(--bidwells-navy);
      box-shadow: var(--bidwells-shadow-lg);
      background: url('assets/tha_prachan_dome_editorial.jpg') center/cover no-repeat;
    }

    .overlapping-quote-card {
      position: absolute;
      bottom: -30px;
      right: -30px;
      width: 380px;
      background: #ffffff;
      border-radius: 18px;
      padding: 30px 32px;
      box-shadow: 0 16px 40px rgba(11, 22, 59, 0.16);
      border: 1px solid rgba(0, 0, 0, 0.06);
    }

    .quote-icon-mark {
      font-family: var(--font-serif);
      font-size: 3.2rem;
      color: var(--bidwells-crimson);
      line-height: 1;
      margin-bottom: 8px;
    }

    .quote-text-primary {
      font-family: var(--font-serif);
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      line-height: 1.35;
      margin-bottom: 12px;
    }

    .quote-text-sub {
      font-size: 0.88rem;
      color: var(--bidwells-text-muted);
      line-height: 1.6;
    }

    .statement-narrative-box {
      padding-left: 20px;
    }

    .statement-main-text {
      font-family: var(--font-serif);
      font-size: 2.4rem;
      line-height: 1.35;
      color: var(--bidwells-navy);
      font-weight: 400;
      margin-bottom: 1.8rem;
    }

    .bidwells-highlight {
      background-color: #ffef8a;
      color: var(--bidwells-navy);
      padding: 0 6px;
      font-weight: 700;
      border-radius: 4px;
    }

    .statement-sub-text {
      font-size: 1.05rem;
      color: #475569;
      line-height: 1.8;
    }

    /* 3 High-Contrast Vertical Cards with Colored Blocks (Frames 013s - 014s) */
    .winning-cards-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
      margin-top: 50px;
    }

    .winning-stat-card {
      background: #ffffff;
      border: 2.5px solid var(--bidwells-card-border);
      border-radius: 18px;
      height: 440px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      box-shadow: var(--bidwells-shadow);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .winning-stat-card:hover {
      transform: translateY(-8px);
      box-shadow: var(--bidwells-shadow-lg);
    }

    .winning-card-top {
      padding: 32px 30px;
    }

    .winning-number-row {
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 12px;
    }

    .winning-number {
      font-family: var(--font-sans);
      font-size: 4.2rem;
      font-weight: 800;
      line-height: 1;
      color: var(--bidwells-navy);
      letter-spacing: -0.03em;
    }

    .winning-unit {
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--bidwells-navy);
    }

    .winning-top-title {
      font-size: 0.95rem;
      font-weight: 600;
      color: #64748b;
      line-height: 1.4;
    }

    .winning-color-block {
      margin: 0 16px 16px;
      padding: 28px 24px;
      border-radius: 14px;
      color: #ffffff;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      min-height: 190px;
    }

    .block-sky-blue {
      background: #a6d2e6;
      color: var(--bidwells-navy);
    }

    .block-crimson {
      background: #d71945;
      color: #ffffff;
    }

    .block-emerald {
      background: #0a7b6b;
      color: #ffffff;
    }

    .block-team-name {
      font-size: 1.55rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 6px;
    }

    .block-team-loc {
      font-size: 0.85rem;
      opacity: 0.9;
      line-height: 1.4;
    }

    /* ==========================================================================
       5. SECTION 2: DARK BLUE CLUSTER MAP & 4 CAMPUSES (017s - 024s)
       ========================================================================== */
    .bidwells-map-section {
      background-color: var(--bidwells-navy);
      color: #ffffff;
      padding: 110px 2rem 100px;
      position: relative;
      overflow: hidden;
      border-top: 4px solid var(--bidwells-crimson);
    }

    .map-section-header {
      max-width: 1200px;
      margin: 0 auto 50px;
    }

    .section-eyebrow {
      color: var(--tu-gold);
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }

    .section-headline {
      font-family: var(--font-serif);
      font-size: 2.8rem;
      font-weight: 700;
      line-height: 1.25;
      margin-bottom: 15px;
    }

    .section-headline em {
      font-style: italic;
      color: var(--bidwells-sky-blue);
      font-weight: 400;
    }

    .section-lead {
      font-size: 1.05rem;
      color: #94a3b8;
      max-width: 780px;
      line-height: 1.7;
    }

    /* Map Interface Container (Frames 020s - 021s) */
    .cluster-map-layout {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 290px 1fr;
      gap: 40px;
      align-items: start;
    }

    .cluster-selector-pillbox {
      background: rgba(16, 28, 61, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 18px;
      padding: 14px 10px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .cluster-select-btn {
      background: transparent;
      border: none;
      padding: 14px 18px;
      border-radius: 12px;
      color: #94a3b8;
      font-size: 0.92rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      position: relative;
    }

    .cluster-select-btn:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }

    .cluster-select-btn.active {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
      font-weight: 700;
    }

    .cluster-select-btn.active::before {
      content: '';
      position: absolute;
      left: 0;
      top: 10px;
      bottom: 10px;
      width: 4px;
      border-radius: 0 4px 4px 0;
      background: var(--bidwells-crimson);
    }

    .cluster-map-canvas-card {
      background: radial-gradient(circle at center, #13244e 0%, #09132e 100%);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 20px;
      padding: 24px;
      position: relative;
      min-height: 560px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: var(--bidwells-shadow-lg);
      overflow: hidden;
    }

    /* Map Real-Time Toolbar */
    .map-toolbar-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      z-index: 5;
    }

    .map-live-indicator {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--bidwells-sky-blue);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .live-dot-pulse {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: var(--tu-gold);
      box-shadow: 0 0 10px var(--tu-gold);
      animation: pulse-ring 1.8s infinite;
    }

    .map-toolbar-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .map-style-toggle-group {
      display: flex;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 8px;
      padding: 3px;
      gap: 3px;
    }

    .map-style-btn {
      background: transparent;
      border: none;
      color: #94a3b8;
      font-size: 0.72rem;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
    }

    .map-style-btn:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }

    .map-style-btn.active {
      color: #0b163b;
      background: var(--tu-gold);
      font-weight: 700;
    }

    .map-tool-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 8px;
      padding: 6px 14px;
      font-size: 0.78rem;
      font-weight: 600;
      color: #ffffff;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .map-tool-btn:hover {
      background: var(--bidwells-crimson);
      border-color: var(--bidwells-crimson);
      color: #ffffff;
    }

    .map-coord-readout {
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 199, 44, 0.35);
      border-radius: 8px;
      padding: 6px 12px;
      font-size: 0.74rem;
      font-family: monospace;
      color: var(--tu-gold);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Leaflet Stage Container */
    #campusLeafletMap {
      width: 100%;
      height: 420px;
      border-radius: 14px;
      position: relative;
      z-index: 2;
      background: #09132e;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
    }

    /* Custom Leaflet Dark UI Overrides */
    .leaflet-container {
      background: #09132e !important;
      font-family: var(--font-sans) !important;
    }

    .leaflet-tile-pane {
      filter: brightness(0.92) contrast(1.15) saturate(1.1);
    }

    .leaflet-control-zoom {
      border: 1px solid rgba(255, 255, 255, 0.15) !important;
      border-radius: 10px !important;
      overflow: hidden;
      box-shadow: 0 4px 14px rgba(0,0,0,0.4) !important;
    }

    .leaflet-control-zoom a {
      background: rgba(11, 22, 59, 0.9) !important;
      color: #ffffff !important;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
      transition: background 0.2s ease;
    }

    .leaflet-control-zoom a:hover {
      background: var(--bidwells-crimson) !important;
      color: #ffffff !important;
    }

    .leaflet-control-attribution {
      background: rgba(11, 22, 59, 0.8) !important;
      color: #94a3b8 !important;
      font-size: 0.65rem !important;
    }

    .leaflet-control-attribution a {
      color: var(--bidwells-sky-blue) !important;
    }

    /* Custom DivIcon Markers */
    .tu-leaflet-custom-icon {
      background: transparent !important;
      border: none !important;
    }

    .tu-gis-marker {
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      cursor: pointer;
      user-select: none;
    }

    .tu-marker-core {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: linear-gradient(135deg, #c51944 0%, #9e1b32 100%);
      border: 2.5px solid var(--tu-gold);
      box-shadow: 0 0 16px rgba(255, 199, 44, 0.7), 0 4px 12px rgba(0, 0, 0, 0.7);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 14px;
      position: relative;
      z-index: 3;
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease, background 0.25s ease;
    }

    .tu-gis-marker:hover .tu-marker-core,
    .tu-gis-marker.active .tu-marker-core {
      transform: scale(1.25);
      background: linear-gradient(135deg, #ffc72c 0%, #d99b00 100%);
      color: #0b163b;
      box-shadow: 0 0 26px rgba(255, 199, 44, 1), 0 6px 16px rgba(0, 0, 0, 0.9);
    }

    .tu-marker-pulse {
      position: absolute;
      top: 17px;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      border: 2px solid rgba(255, 199, 44, 0.8);
      animation: tu-sonar-ping 2.2s cubic-bezier(0, 0, 0.2, 1) infinite;
      pointer-events: none;
      z-index: 1;
    }

    @keyframes tu-sonar-ping {
      0% { transform: translate(-50%, -50%) scale(0.6); opacity: 0.9; }
      100% { transform: translate(-50%, -50%) scale(2.0); opacity: 0; }
    }

    .tu-marker-tag {
      background: rgba(11, 22, 59, 0.94);
      border: 1px solid rgba(255, 199, 44, 0.5);
      border-radius: 8px;
      padding: 3px 9px;
      margin-top: 6px;
      display: flex;
      gap: 6px;
      align-items: center;
      white-space: nowrap;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(6px);
      z-index: 4;
      pointer-events: auto;
    }

    .tu-marker-tag .tag-name {
      font-size: 0.74rem;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.01em;
    }

    .tu-marker-tag .tag-area {
      font-size: 0.66rem;
      font-weight: 700;
      color: var(--tu-gold);
      background: rgba(255, 199, 44, 0.16);
      padding: 1px 6px;
      border-radius: 4px;
    }

    /* Leaflet Popups */
    .leaflet-popup-content-wrapper {
      background: rgba(11, 22, 59, 0.96) !important;
      border: 1px solid rgba(255, 199, 44, 0.5) !important;
      border-radius: 14px !important;
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.7) !important;
      color: #ffffff !important;
      backdrop-filter: blur(12px) !important;
      padding: 6px !important;
    }

    .leaflet-popup-tip {
      background: rgba(11, 22, 59, 0.96) !important;
      border: 1px solid rgba(255, 199, 44, 0.5) !important;
    }

    .tu-gis-popup {
      padding: 8px 10px;
      min-width: 230px;
    }

    .tu-gis-popup-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
      padding-bottom: 8px;
      margin-bottom: 8px;
      gap: 10px;
    }

    .tu-gis-popup-header h4 {
      margin: 0;
      font-size: 0.92rem;
      font-weight: 700;
      color: #ffffff;
    }

    .tu-gis-popup-badge {
      font-size: 0.65rem;
      font-weight: 700;
      color: var(--tu-gold);
      background: rgba(255, 199, 44, 0.16);
      border: 1px solid rgba(255, 199, 44, 0.35);
      padding: 2px 7px;
      border-radius: 20px;
      white-space: nowrap;
    }

    .tu-gis-popup-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px 12px;
      font-size: 0.78rem;
      margin-bottom: 10px;
    }

    .tu-gis-popup-stat {
      display: flex;
      flex-direction: column;
    }

    .tu-gis-popup-stat .k {
      color: #94a3b8;
      font-size: 0.66rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }

    .tu-gis-popup-stat .v {
      color: #ffffff;
      font-weight: 700;
    }

    .tu-gis-popup-coord {
      font-size: 0.68rem;
      color: #cbd5e1;
      background: rgba(255, 255, 255, 0.06);
      padding: 5px 8px;
      border-radius: 6px;
      font-family: monospace;
      display: flex;
      align-items: center;
      gap: 6px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Campus Info Strip */
    .campus-metrics-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      background: rgba(11, 22, 59, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 16px 20px;
      z-index: 5;
    }

    .campus-metric-item .val {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--tu-gold);
    }

    .campus-metric-item .lbl {
      font-size: 0.72rem;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .campus-location-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.82rem;
      color: #cbd5e1;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 8px 14px;
      z-index: 5;
    }

    /* Multi-Era Campus Distribution Chart */
    .campus-distribution-card {
      max-width: 1200px;
      margin: 40px auto 0;
      background: rgba(16, 28, 61, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 30px;
    }

    .distribution-controls-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }

    .era-pill-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 600;
      color: #cbd5e1;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .era-pill-btn.active {
      background: var(--bidwells-crimson);
      color: #ffffff;
      border-color: var(--bidwells-crimson);
    }

    /* Straight Line Milestone Chart (Closed system reform 2496-2503) */
    .milestones-strip-section {
      max-width: 1200px;
      margin: 40px auto 0;
      background: rgba(16, 28, 61, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 30px;
    }

    .milestone-stepper-track {
      position: relative;
      display: flex;
      justify-content: space-between;
      margin-bottom: 24px;
      padding: 0 20px;
    }

    .stepper-bg-line {
      position: absolute;
      top: 15px;
      left: 30px;
      right: 30px;
      height: 3px;
      background: rgba(255, 255, 255, 0.15);
      z-index: 0;
    }

    .stepper-node {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
    }

    .stepper-circle {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--bidwells-navy);
      border: 2.5px solid #64748b;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      color: #94a3b8;
      transition: all 0.2s ease;
    }

    .stepper-node.active .stepper-circle {
      background: var(--bidwells-crimson);
      border-color: #ffffff;
      color: #ffffff;
      transform: scale(1.15);
      box-shadow: 0 0 15px rgba(197, 25, 68, 0.6);
    }

    .stepper-year {
      font-size: 0.8rem;
      font-weight: 700;
      color: #e2e8f0;
      margin-top: 8px;
    }

    .stepper-node-title {
      font-size: 0.72rem;
      color: #94a3b8;
      max-width: 100px;
      text-align: center;
      line-height: 1.3;
      margin-top: 2px;
    }

    .milestone-event-card {
      background: rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      padding: 20px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 30px;
    }

    /* ==========================================================================
       6. SECTION 3: CIRCULAR WIPE TO TEAL - COST CAP & BUDGET (025s - 035s)
       ========================================================================== */
    .bidwells-teal-section {
      background-color: var(--bidwells-teal);
      background-image: radial-gradient(circle at 80% 20%, #00857c 0%, var(--bidwells-teal) 70%);
      color: #ffffff;
      padding: 120px 2rem 100px;
      position: relative;
      overflow: hidden;
    }

    .teal-container {
      max-width: 1200px;
      margin: 0 auto;
    }

    /* Floating White Card: Cost Cap Budget Analysis (Frame 030s) */
    .cost-cap-white-card {
      background: #ffffff;
      border-radius: 22px;
      padding: 48px;
      color: var(--bidwells-text);
      box-shadow: var(--bidwells-shadow-lg);
      margin-bottom: 50px;
    }

    .cost-cap-grid {
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 50px;
      align-items: center;
    }

    .cost-cap-narrative .cost-cap-title {
      font-family: var(--font-serif);
      font-size: 2.4rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      line-height: 1.2;
      margin-bottom: 16px;
    }

    .cost-cap-narrative .cost-cap-lead {
      font-size: 1.05rem;
      color: #475569;
      line-height: 1.7;
      margin-bottom: 24px;
    }

    .drilldown-pills-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
    }

    .drilldown-pill {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 600;
      color: #334155;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .drilldown-pill:hover, .drilldown-pill.active {
      background: var(--bidwells-crimson);
      color: #ffffff;
      border-color: var(--bidwells-crimson);
    }

    /* Demographic Card: Female 62.4% */
    .demographic-white-card {
      background: #ffffff;
      border-radius: 22px;
      padding: 44px;
      color: var(--bidwells-text);
      box-shadow: var(--bidwells-shadow-lg);
      margin-bottom: 50px;
    }

    .demographic-headline {
      font-family: var(--font-serif);
      font-size: 1.95rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      line-height: 1.3;
      margin-bottom: 8px;
    }

    .demographic-sub {
      font-size: 0.95rem;
      color: #64748b;
      margin-bottom: 28px;
    }

    .demographic-ratio-bar-wrap {
      margin-bottom: 30px;
    }

    .ratio-bar {
      height: 38px;
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .ratio-female {
      width: 62.4%;
      background: linear-gradient(90deg, #ec4899 0%, #db2777 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
    }

    .ratio-male {
      width: 37.6%;
      background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
    }

    /* 26 Faculties Grid & TCAS Drilldown */
    .faculties-white-card {
      background: #ffffff;
      border-radius: 22px;
      padding: 40px;
      color: var(--bidwells-text);
      box-shadow: var(--bidwells-shadow-lg);
    }

    .faculties-kpi-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 16px 20px;
      margin-bottom: 24px;
    }

    .fac-kpi-item {
      display: flex;
      flex-direction: column;
    }

    .fac-kpi-item .kpi-num {
      font-size: 1.6rem;
      font-weight: 800;
      line-height: 1.1;
    }

    .fac-kpi-item .kpi-lbl {
      font-size: 0.74rem;
      font-weight: 600;
      color: #64748b;
      margin-top: 4px;
    }

    .faculties-view-toggle {
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
    }

    .fac-view-btn {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 7px 16px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .fac-view-btn:hover {
      background: #e2e8f0;
      color: var(--bidwells-navy);
    }

    .fac-view-btn.active {
      background: var(--bidwells-navy);
      color: #ffffff;
      border-color: var(--bidwells-navy);
    }

    .faculties-legend-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      padding: 10px 14px;
      background: #f8fafc;
      border-radius: 10px;
      font-size: 0.76rem;
      font-weight: 600;
      color: #475569;
      margin-bottom: 20px;
    }

    .legend-color-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      display: inline-block;
      margin-right: 4px;
    }

    .faculties-filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 20px;
    }

    .fac-pill {
      background: #f8fafc;
      border: 1.5px solid #e2e8f0;
      padding: 7px 16px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .fac-pill.active {
      background: var(--bidwells-navy);
      color: #ffffff;
      border-color: var(--bidwells-navy);
    }

    .faculties-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 16px;
      max-height: 520px;
      overflow-y: auto;
      padding-right: 8px;
    }

    .faculty-item-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 16px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .faculty-item-card:hover {
      background: #ffffff;
      border-color: var(--bidwells-crimson);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(11, 22, 59, 0.08);
    }

    .faculty-item-card .fac-name {
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--bidwells-navy);
      margin-bottom: 4px;
    }

    .faculty-item-card .fac-meta {
      font-size: 0.74rem;
      color: #64748b;
      display: flex;
      justify-content: space-between;
    }

    /* Flourish 10-Scene Hub Modal */
    .flourish-modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(11, 22, 59, 0.85);
      backdrop-filter: blur(8px);
      z-index: 10000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .flourish-modal-card {
      background: #ffffff;
      border-radius: 22px;
      max-width: 1150px;
      width: 100%;
      height: 90vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4);
      overflow: hidden;
      position: relative;
    }

    .flourish-modal-header {
      padding: 20px 28px;
      border-bottom: 1px solid #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #f8fafc;
    }

    .flourish-modal-body {
      display: grid;
      grid-template-columns: 340px 1fr;
      flex: 1;
      overflow: hidden;
    }

    .flourish-sidebar-tabs {
      background: #f8fafc;
      border-right: 1px solid #e2e8f0;
      overflow-y: auto;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .flourish-scene-btn {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      padding: 10px 12px;
      border-radius: 10px;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.2s ease;
      color: #334155;
    }

    .flourish-scene-btn:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
    }

    .flourish-scene-btn.active {
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1d4ed8;
      font-weight: 700;
    }

    .flourish-scene-btn .scene-num {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #e2e8f0;
      color: #475569;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      font-weight: 800;
      flex-shrink: 0;
    }

    .flourish-scene-btn.active .scene-num {
      background: var(--bidwells-crimson);
      color: #ffffff;
    }

    .flourish-scene-btn .scene-title-text {
      font-size: 0.78rem;
      line-height: 1.3;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .flourish-scene-detail-pane {
      padding: 28px 32px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
      background: #ffffff;
    }

    /* ==========================================================================
       7. SECTION 4: THE CURVED RACETRACK & S-TURN WITH RACE CARS (Frames 037s - 040s)
       ========================================================================== */
    .bidwells-curved-track-section {
      position: relative;
      min-height: 140vh;
      background-color: var(--bidwells-navy);
      background-image: url('assets/Track2.jpg');
      background-size: cover;
      background-position: center;
      color: #ffffff;
      overflow: hidden;
      padding: 120px 2rem;
    }

    .curved-track-overlay-dim {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(11, 22, 59, 0.75);
      pointer-events: none;
    }

    .curved-track-content {
      position: relative;
      z-index: 10;
      max-width: 1200px;
      margin: 0 auto;
    }

    /* Turning Cars along the S-Curve */
    .turning-cars-stage {
      position: relative;
      height: 520px;
      margin: 40px 0;
      border-radius: 20px;
      overflow: hidden;
    }

    .turning-car-wrap {
      position: absolute;
      transition: transform 0.1s linear;
    }

    .turning-car-1 {
      top: 18%;
      left: 36%;
      width: 120px;
      transform: rotate(-18deg);
    }

    .turning-car-2 {
      top: 50%;
      left: 48%;
      width: 130px;
      transform: rotate(24deg);
    }

    .turning-car-3 {
      top: 76%;
      left: 60%;
      width: 120px;
      transform: rotate(-12deg);
    }

    /* Business School Benchmarking Card */
    .tbs-benchmark-card {
      background: rgba(16, 28, 61, 0.95);
      border: 2px solid var(--tu-gold);
      border-radius: 20px;
      padding: 36px 40px;
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(12px);
    }

    .tbs-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
    }

    .triple-crown-badges-row {
      display: flex;
      gap: 12px;
    }

    .crown-badge {
      background: linear-gradient(135deg, var(--tu-gold) 0%, #d99b00 100%);
      color: var(--bidwells-navy);
      font-size: 0.78rem;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: 6px;
      letter-spacing: 0.05em;
    }

    .benchmark-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
    }

    .benchmark-table th {
      text-align: left;
      font-size: 0.75rem;
      color: #94a3b8;
      text-transform: uppercase;
      padding: 10px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .benchmark-table td {
      padding: 14px;
      font-size: 0.88rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .benchmark-table tr.highlight-tbs {
      background: rgba(255, 199, 44, 0.12);
      font-weight: 700;
      color: #ffffff;
    }

    /* ==========================================================================
       8. SECTION 5: SILVERSTONE-STYLE CIRCUIT MILESTONE TRACK (Frames 041s - 050s)
       ========================================================================== */
    .bidwells-circuit-section {
      background-color: #f1f8fa;
      padding: 120px 2rem 100px;
      position: relative;
    }

    .circuit-layout-grid {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 460px;
      gap: 60px;
      align-items: center;
    }

    /* Silverstone Circuit Vector */
    .silverstone-svg-container {
      position: relative;
      width: 100%;
      height: 480px;
    }

    .circuit-milestone-node {
      position: absolute;
      transform: translate(-50%, -50%);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #ffffff;
      border: 3.5px solid #00857c;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.8rem;
      color: #00857c;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      transition: all 0.25s ease;
    }

    .circuit-milestone-node.active {
      background: var(--bidwells-crimson);
      border-color: #ffffff;
      color: #ffffff;
      transform: translate(-50%, -50%) scale(1.3);
      box-shadow: 0 0 16px rgba(197, 25, 68, 0.6);
    }

    /* Synchronized White Insight Card (Frame 045s) */
    .circuit-insight-card {
      background: #ffffff;
      border-radius: 22px;
      padding: 40px;
      box-shadow: var(--bidwells-shadow-lg);
      border: 1px solid rgba(0, 0, 0, 0.06);
    }

    .circuit-card-tag {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--bidwells-crimson);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 8px;
    }

    .circuit-card-title {
      font-family: var(--font-serif);
      font-size: 1.85rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      line-height: 1.3;
      margin-bottom: 18px;
    }

    .circuit-card-img {
      width: 100%;
      height: 200px;
      border-radius: 14px;
      object-fit: cover;
      margin-bottom: 18px;
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
    }

    .circuit-card-desc {
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.7;
      margin-bottom: 24px;
    }

    /* TU 2034 Strategy Cockpit Card */
    .cockpit-strategy-card {
      max-width: 1200px;
      margin: 50px auto 0;
      background: #ffffff;
      border-radius: 22px;
      padding: 44px;
      box-shadow: var(--bidwells-shadow-lg);
      border: 1px solid rgba(0, 0, 0, 0.06);
    }

    .cockpit-sliders-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      margin-top: 24px;
    }

    .cockpit-slider-item {
      background: #f8fafc;
      padding: 20px;
      border-radius: 14px;
      border: 1px solid #e2e8f0;
    }

    .cockpit-slider-item label {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      display: block;
      margin-bottom: 8px;
    }

    .cockpit-range-input {
      width: 100%;
      accent-color: var(--bidwells-crimson);
      cursor: pointer;
    }

    .cockpit-val-disp {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--bidwells-crimson);
      margin-top: 6px;
    }

    /* ==========================================================================
       9. SECTION 6: CHECKERED FINISH LINE CROSSING & REPORT DOWNLOAD (051s - 054s)
       ========================================================================== */
    .bidwells-finish-section {
      background-color: var(--bidwells-offwhite);
      padding: 100px 2rem 140px;
      position: relative;
      overflow: hidden;
    }

    /* Authentic Checkered Finish Line Banner */
    .checkered-finish-banner {
      width: 100%;
      height: 70px;
      background-image: url('assets/finish.svg');
      background-repeat: repeat-x;
      background-size: contain;
      background-position: center;
      margin-bottom: 60px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }

    .finish-cars-crossing-row {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 60px;
      margin-bottom: 70px;
      position: relative;
    }

    .finish-car-item {
      position: relative;
      width: 130px;
    }

    .finish-car-trail-line {
      position: absolute;
      top: -120px;
      left: 50%;
      transform: translateX(-50%);
      width: 24px;
      height: 140px;
      background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(200, 200, 200, 0.8) 100%);
      pointer-events: none;
    }

    /* Download Report Full Box (Frame 053s) */
    .download-report-card {
      max-width: 880px;
      margin: 0 auto;
      background: #ffffff;
      border-radius: 24px;
      padding: 50px 60px;
      box-shadow: var(--bidwells-shadow-lg);
      border: 1px solid rgba(0, 0, 0, 0.08);
    }

    .download-report-title {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--bidwells-navy);
      line-height: 1.25;
      margin-bottom: 12px;
    }

    .download-report-desc {
      font-size: 1.02rem;
      color: #64748b;
      line-height: 1.7;
      margin-bottom: 30px;
    }

    .download-form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      margin-bottom: 24px;
    }

    .form-input-field {
      width: 100%;
      padding: 12px 18px;
      border-radius: 10px;
      border: 1.5px solid #cbd5e1;
      font-size: 0.92rem;
      font-family: var(--font-sans);
      outline: none;
      transition: border-color 0.2s ease;
    }

    .form-input-field:focus {
      border-color: var(--bidwells-crimson);
    }

    .btn-submit-download {
      background: var(--bidwells-crimson);
      color: #ffffff;
      padding: 14px 32px;
      border-radius: 9999px;
      font-size: 1rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 6px 20px rgba(197, 25, 68, 0.3);
      transition: all 0.25s ease;
    }

    .btn-submit-download:hover {
      background: #a91238;
      transform: translateY(-2px);
      box-shadow: 0 10px 25px rgba(197, 25, 68, 0.4);
    }

    /* Modal for TCAS & Drilldowns */
    .drilldown-modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(11, 22, 59, 0.7);
      backdrop-filter: blur(8px);
      z-index: 12000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .drilldown-modal-card {
      background: #ffffff;
      border-radius: 20px;
      max-width: 680px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 36px;
      position: relative;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }

    .modal-close-btn {
      position: absolute;
      top: 24px;
      right: 24px;
      background: #f1f5f9;
      border: none;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #475569;
      font-size: 16px;
      transition: all 0.2s ease;
    }

    .modal-close-btn:hover {
      background: #e2e8f0;
      color: var(--bidwells-crimson);
    }

    /* Responsiveness */
    @media (max-width: 1024px) {
      .cluster-map-layout, .cost-cap-grid, .circuit-layout-grid, .statement-quote-grid, .cockpit-sliders-grid {
        grid-template-columns: 1fr;
      }
      .winning-cards-row {
        grid-template-columns: 1fr;
      }
      .central-track-stage {
        width: 100%;
      }
      .bidwells-header {
        padding: 0 1rem;
      }
      .header-nav {
        display: none;
      }
    }

    @media (max-width: 768px) {
      .campus-metrics-strip {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        padding: 12px 14px;
      }
      #campusLeafletMap {
        height: 330px;
      }
      .map-toolbar-row {
        flex-direction: column;
        align-items: flex-start;
      }
      .campus-metric-item .val {
        font-size: 1.15rem;
      }
    }
  </style>
</head>
<body>

  <!-- ==========================================================================
       1. FIXED TOP HEADER (Exact Bidwells Luxury Style)
       ========================================================================== -->
  <header class="bidwells-header" id="mainHeader">
    <div class="header-logo-group" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
      <div class="header-brand-mark">
        <i class="fa-solid fa-dharmachakra"></i>
      </div>
      <div class="header-brand-text">
        <span class="header-brand-title">THAMMASAT 90 YEARS</span>
        <span class="header-brand-sub">DRIVING INNOVATION AT SPEED</span>
      </div>
    </div>

    <nav class="header-nav">
      <a href="#hero" class="header-nav-link active">จุดเริ่มต้น (Pioneers)</a>
      <a href="#statement" class="header-nav-link">หมุดหมาย 90 ปี</a>
      <a href="#campuses" class="header-nav-link">4 วิทยาเขตยุทธศาสตร์</a>
      <a href="#budget" class="header-nav-link">วินัยงบประมาณ (Cost Cap)</a>
      <a href="#racing-curve" class="header-nav-link">มาตรฐานสากล (Triple Crown)</a>
      <a href="#circuit" class="header-nav-link">วงจรนวัตกรรม (Circuit)</a>
      <a href="#finish" class="header-nav-link">เส้นชัยเกียรติภูมิ (Milestone)</a>
    </nav>

    <div class="header-actions">
      <!-- 1-Click Google Colab Notebook Link -->
      <a href="https://colab.research.google.com/github/kondee-rgb/BI304-Thammasat-Data-Storytelling/blob/main/BI304_Thammasat_Data_Storytelling.ipynb" target="_blank" rel="noopener noreferrer" class="header-colab-btn" title="เปิดโค้ดประมวลผลข้อมูลใน Google Colab (รันได้ทันที)">
        <img src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Google Colab" style="width: 17px; height: 17px;" />
        <span>Google Colab</span>
      </a>
      <!-- Flourish 10 Visualizations Hub Button -->
      <button class="header-flourish-btn" onclick="openFlourishHubModal()" title="เปิดดู Flourish Data Storytelling ครบทั้ง 10 ฉาก">
        <i class="fa-solid fa-chart-pie"></i>
        <span>Flourish (10 ฉาก)</span>
      </button>
      <button class="btn-bidwells-pill" onclick="openDownloadModal()">
        <span>ดาวน์โหลดรายงาน</span>
        <i class="fa-solid fa-cloud-arrow-down"></i>
      </button>
    </div>
  </header>

  <!-- ==========================================================================
       2. FIXED BOTTOM SCRUBBER PILL (Exact Bidwells Floating Capsule)
       ========================================================================== */
  -->
  <div class="bidwells-floating-scrubber" id="floatingScrubber">
    <div class="scrubber-track-container" id="scrubberTrack" onclick="handleScrubberClick(event)">
      <div class="scrubber-track-bg"></div>
      <div class="scrubber-track-fill" id="scrubberFill"></div>
      <div class="scrubber-thumb" id="scrubberThumb"></div>
      <div class="scrubber-pips">
        <div class="scrubber-pip active" data-target="hero"></div>
        <div class="scrubber-pip" data-target="statement"></div>
        <div class="scrubber-pip" data-target="campuses"></div>
        <div class="scrubber-pip" data-target="budget"></div>
        <div class="scrubber-pip" data-target="racing-curve"></div>
        <div class="scrubber-pip" data-target="circuit"></div>
        <div class="scrubber-pip" data-target="finish"></div>
      </div>
    </div>
    <button class="scrubber-download-btn" onclick="openDownloadModal()">
      <span>Download report</span>
    </button>
  </div>

  <!-- ==========================================================================
       3. HERO SECTION & CENTRAL STARTING RACETRACK (Exact Frames 000s - 007s)
       ========================================================================== -->
  <section class="hero-track-section" id="hero">
    <!-- The Central Vertical Asphalt Racetrack -->
    <div class="central-track-stage">
      <!-- Alternating Checkerboard Curb on the left (as in frame 006s) -->
      <div class="central-track-curb-left"></div>
      <div class="central-track-curb-right"></div>
      <div class="central-track-centerline"></div>

      <!-- Starting Grid Box Brackets [   ] at scroll 900px -->
      <div class="grid-box grid-box-pole">
        <span class="grid-box-label">TU PIONEER 01</span>
      </div>
      <div class="grid-box grid-box-slot2">
        <span class="grid-box-label">TU SCHOLAR 02</span>
      </div>

      <!-- Student 1: Lead Thammasat Student (tu_student_walking.png) -->
      <div class="tu-student-walker-container tu-student-leader" id="studentLeader">
        <img src="assets/tu_student_walking.png" alt="นักศึกษาธรรมศาสตร์ ผู้นำแห่งอนาคต" class="tu-student-walker-img" />
        <div class="tu-student-pedestal"></div>
        <div class="tu-student-badge">
          <i class="fa-solid fa-graduation-cap"></i>
          <span>นักศึกษาธรรมศาสตร์ • ก้าวสู่ศตวรรษใหม่</span>
        </div>
      </div>

      <!-- Student 2: Second Thammasat Student Scholar -->
      <div class="tu-student-walker-container tu-student-scholar" id="studentScholar">
        <img src="assets/tu_student_walking.png" alt="นักศึกษาธรรมศาสตร์ นักวิจัยเพื่อสังคม" class="tu-student-walker-img" style="filter: drop-shadow(0 14px 24px rgba(0,0,0,0.75)) brightness(1.08);" />
        <div class="tu-student-pedestal"></div>
        <div class="tu-student-badge">
          <i class="fa-solid fa-lightbulb"></i>
          <span>TU Scholar • พลังขับเคลื่อนสังคม</span>
        </div>
      </div>
    </div>

    <!-- Hero Content Overlay (First Screen) -->
    <div class="hero-content-overlay">
      <div class="hero-category-tag">
        <i class="fa-solid fa-flag-checkered"></i>
        <span>รายงานวิจัยและยุทธศาสตร์ข้อมูล • 2477 — 2567</span>
      </div>

      <h1 class="hero-main-title">
        Driving Innovation<br>
        <em>at Speed</em>
      </h1>

      <div class="hero-title-thai">
        ขับเคลื่อนปัญญาและนวัตกรรม ด้วยความเร็วแห่งอนาคต
      </div>

      <p class="hero-lead-desc">
        90 ปี มหาวิทยาลัยธรรมศาสตร์: จาก "ตลาดวิชา" แห่งประวัติศาสตร์ สู่มหาวิทยาลัยวิจัยชั้นนำของโลก
        ผู้นำ Triple Crown และพลังแห่งการพัฒนาสังคมอย่างยั่งยืน
      </p>

      <button class="hero-scroll-pill-btn" onclick="scrollToElement('statement')">
        <span>Scroll down to race</span>
        <i class="fa-solid fa-arrow-down"></i>
      </button>
    </div>
  </section>

  <!-- ==========================================================================
       4. SECTION 1: HIGH-KEY STATEMENT & 3 WINNING STAT CARDS (Frames 008s - 016s)
       ========================================================================== -->
  <section class="bidwells-statement-section" id="statement">
    <!-- Giant Watermark Outline Number 90 -->
    <div class="watermark-giant-num">90</div>

    <div class="statement-container">
      <!-- Left Photo Card + Overlapping Quote Box (Frame 009s) -->
      <div class="statement-quote-grid">
        <div class="editorial-photo-card">
          <div class="editorial-photo-frame"></div>
          <div class="overlapping-quote-card">
            <div class="quote-icon-mark">“</div>
            <div class="quote-text-primary">
              Thanks to everyone back at the university
            </div>
            <div class="quote-text-sub">
              ขอขอบคุณประชาคมธรรมศาสตร์ทุกคน — ผู้เป็นฟันเฟืองและพลังเบื้องหลังความสำเร็จตลอด 9 ทศวรรษ
            </div>
          </div>
        </div>

        <div class="statement-narrative-box">
          <h2 class="statement-main-text">
            For most, that foundation lies within <span class="bidwells-highlight">มหาวิทยาลัยธรรมศาสตร์:</span> the global epicentre of knowledge, leadership and social transformation.
          </h2>
          <p class="statement-sub-text">
            ตลอด 90 ปีที่ผ่านมา ธรรมศาสตร์ผลิตบัณฑิตและผู้นำที่ร่วมสร้างประวัติศาสตร์ ขับเคลื่อนเศรษฐกิจ และยกระดับคุณภาพชีวิตของประชาชนในทุกมิติ
            ด้วย 26 คณะวิชา และ 4 วิทยาเขตยุทธศาสตร์ทั่วประเทศ
          </p>
        </div>
      </div>

      <!-- 3 High-Contrast Vertical Cards with Colored Blocks (Frames 013s - 014s) -->
      <div class="winning-cards-row">
        <!-- Card 1: 90 Years / Sky Blue -->
        <div class="winning-stat-card">
          <div class="winning-card-top">
            <div class="winning-number-row">
              <span class="winning-number">90</span>
              <span class="winning-unit">ปี</span>
            </div>
            <div class="winning-top-title">ประวัติศาสตร์แห่งเสรีภาพและความเสมอภาค</div>
          </div>
          <div class="winning-color-block block-sky-blue">
            <div class="block-team-name">Tha Prachan</div>
            <div class="block-team-loc">ศูนย์กลางมรดกทางปัญญา • Bangkok, TH</div>
          </div>
        </div>

        <!-- Card 2: 26 Faculties / Crimson -->
        <div class="winning-stat-card">
          <div class="winning-card-top">
            <div class="winning-number-row">
              <span class="winning-number">26</span>
              <span class="winning-unit">คณะ</span>
            </div>
            <div class="winning-top-title">4 เสาหลักทางวิชาการและสหวิทยาการ</div>
          </div>
          <div class="winning-color-block block-crimson">
            <div class="block-team-name">Rangsit Cluster</div>
            <div class="block-team-loc">ศูนย์วิจัยและนวัตกรรมขนาดใหญ่ 2,644 ไร่ • Pathum Thani, TH</div>
          </div>
        </div>

        <!-- Card 3: Top 5 World SDG 11 / Emerald -->
        <div class="winning-stat-card">
          <div class="winning-card-top">
            <div class="winning-number-row">
              <span class="winning-number">Top 5</span>
              <span class="winning-unit">โลก</span>
            </div>
            <div class="winning-top-title">อันดับโลกด้าน SDG 11 เมืองและชุมชนยั่งยืน</div>
          </div>
          <div class="winning-color-block block-emerald">
            <div class="block-team-name">Green Circuit</div>
            <div class="block-team-loc">อาคารป๋วย 100 ปี & สวนเกษตรอินทรีย์ลอยฟ้า • Global Impact</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       5. SECTION 2: DARK BLUE CLUSTER MAP & 4 STRATEGIC CAMPUSES (017s - 024s)
       ========================================================================== -->
  <section class="bidwells-map-section" id="campuses">
    <div class="map-section-header">
      <div class="section-eyebrow">02 / เครือข่ายวิทยาเขตยุทธศาสตร์</div>
      <h2 class="section-headline">
        The Thammasat <em>Strategic Cluster</em>
      </h2>
      <p class="section-lead">
        การกระจายตัวอย่างทรงพลังของ 4 ศูนย์การศึกษาหลัก: ท่าพระจันทร์, รังสิต, พัทยา และลำปาง
        สร้างโครงข่ายการวิจัย นวัตกรรมการแพทย์ และการบริการสังคมที่เชื่อมโยงถึงกันอย่างสมบูรณ์แบบ
      </p>
    </div>

    <div class="cluster-map-layout">
      <!-- Left Pill Menu (Frames 020s - 021s) -->
      <div class="cluster-selector-pillbox">
        <button class="cluster-select-btn active" onclick="selectCampusTab(0)">
          <span>ท่าพระจันทร์ (Tha Prachan)</span>
          <i class="fa-solid fa-chevron-right"></i>
        </button>
        <button class="cluster-select-btn" onclick="selectCampusTab(1)">
          <span>ศูนย์รังสิต (Rangsit)</span>
          <i class="fa-solid fa-chevron-right"></i>
        </button>
        <button class="cluster-select-btn" onclick="selectCampusTab(2)">
          <span>ศูนย์พัทยา (Pattaya EEC)</span>
          <i class="fa-solid fa-chevron-right"></i>
        </button>
        <button class="cluster-select-btn" onclick="selectCampusTab(3)">
          <span>ศูนย์ลำปาง (Lampang)</span>
          <i class="fa-solid fa-chevron-right"></i>
        </button>
        <button class="cluster-select-btn" onclick="selectCampusTab(4)">
          <span>เครือข่าย 4 วิทยาเขตครบวงจร</span>
          <i class="fa-solid fa-network-wired"></i>
        </button>
      </div>

      <!-- Right Interactive Map Canvas Card -->
      <div class="cluster-map-canvas-card">
        <div class="dotted-matrix-bg"></div>

        <!-- Real-Time GIS Header Bar -->
        <div class="map-toolbar-row">
          <div class="map-live-indicator">
            <span class="live-dot-pulse"></span>
            <span>GIS STRATEGIC RADAR: แผนที่ภูมิสารสนเทศจริง 4 วิทยาเขตทั่วไทย</span>
          </div>
          <div class="map-toolbar-actions">
            <!-- Map Style Selector (Dark GIS / Satellite / Street) -->
            <div class="map-style-toggle-group">
              <button class="map-style-btn active" id="btnMapDark" onclick="switchMapStyle('dark')" title="แผนที่ดาร์ก GIS (Esri Canvas)">
                <i class="fa-solid fa-moon"></i> ดาร์ก GIS
              </button>
              <button class="map-style-btn" id="btnMapSat" onclick="switchMapStyle('satellite')" title="แผนที่ภาพถ่ายดาวเทียมจริง">
                <i class="fa-solid fa-earth-americas"></i> ดาวเทียม
              </button>
              <button class="map-style-btn" id="btnMapOsm" onclick="switchMapStyle('street')" title="แผนที่ถนนมาตรฐาน">
                <i class="fa-solid fa-map"></i> ถนน
              </button>
            </div>

            <button class="map-tool-btn" onclick="selectCampusTab(4)" title="แสดงภาพรวมทั้ง 4 วิทยาเขตทั่วไทย">
              <i class="fa-solid fa-expand"></i> ภาพรวมทั่วประเทศ
            </button>
            <div class="map-coord-readout" id="currentGpsDisplay">
              <i class="fa-solid fa-satellite"></i> 13.7557° N, 100.4930° E
            </div>
          </div>
        </div>

        <!-- Authentic Thailand Leaflet Map Canvas Container -->
        <div id="campusLeafletMap"></div>

        <!-- Location Description Bar -->
        <div class="campus-location-bar">
          <i class="fa-solid fa-location-crosshairs" style="color: var(--tu-gold);"></i>
          <span style="color: #94a3b8; font-weight: 600;">ที่ตั้งทางภูมิศาสตร์:</span>
          <span id="cLocation" style="color: #ffffff; font-weight: 600;">ริมแม่น้ำเจ้าพระยา เขตพระนคร กรุงเทพมหานคร</span>
        </div>

        <!-- Campus Metrics Strip -->
        <div class="campus-metrics-strip" id="campusMetricsBox">
          <div class="campus-metric-item">
            <div class="val" id="cArea">49 ไร่</div>
            <div class="lbl">พื้นที่วิทยาเขต</div>
          </div>
          <div class="campus-metric-item">
            <div class="val" id="cStudents">6,310 คน</div>
            <div class="lbl">ประชากรนักศึกษา</div>
          </div>
          <div class="campus-metric-item">
            <div class="val" id="cRole">มรดกประชาธิปไตย</div>
            <div class="lbl">อัตลักษณ์ยุทธศาสตร์</div>
          </div>
          <div class="campus-metric-item">
            <div class="val" id="cFocus">นานาชาติ / บัณฑิตศึกษา</div>
            <div class="lbl">ทิศทางวิชาการ</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Multi-Era Student Distribution Chart -->
    <div class="campus-distribution-card">
      <div class="distribution-controls-row">
        <div>
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #ffffff;">การกระจายสัดส่วนนักศึกษาตามยุคสมัย (Campus Distribution Shift)</h4>
          <p style="font-size: 0.85rem; color: #94a3b8;">จากท่าพระจันทร์ 100% สู่การเป็นศูนย์กลางวิชาการขนาดใหญ่ที่รังสิตและเครือข่ายภูมิภาค</p>
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="era-pill-btn active" onclick="setDistributionEra('all')">วิวัฒนาการ 4 ยุค</button>
          <button class="era-pill-btn" onclick="setDistributionEra('2567')">สัดส่วนปัจจุบัน (2567)</button>
        </div>
      </div>
      <div style="height: 240px;">
        <canvas id="campusDistributionCanvas"></canvas>
      </div>
    </div>

    <!-- Straight Line Milestone Chart (Closed System Reform 2496-2503) -->
    <div class="milestones-strip-section">
      <div style="font-family: var(--font-serif); font-size: 1.3rem; font-weight: 700; margin-bottom: 20px;">
        <i class="fa-solid fa-timeline" style="color: var(--tu-gold); margin-right: 10px;"></i>
        วิวัฒนาการระบบการศึกษา: <em>การปฏิรูป "ระบบปิด" (2496–2503)</em> และการขยายวิทยาเขต
      </div>

      <div class="milestone-stepper-track">
        <div class="stepper-bg-line"></div>
        <div class="stepper-node active" onclick="setMilestoneStep(0)">
          <div class="stepper-circle">1</div>
          <div class="stepper-year">2477</div>
          <div class="stepper-node-title">สถาปนา มธก. (ระบบเปิด)</div>
        </div>
        <div class="stepper-node" onclick="setMilestoneStep(1)">
          <div class="stepper-circle">2</div>
          <div class="stepper-year">2495</div>
          <div class="stepper-node-title">เปลี่ยนชื่อ มธ.</div>
        </div>
        <div class="stepper-node" onclick="setMilestoneStep(2)">
          <div class="stepper-circle">3</div>
          <div class="stepper-year">2496-03</div>
          <div class="stepper-node-title">ปฏิรูปสู่ "ระบบปิด"</div>
        </div>
        <div class="stepper-node" onclick="setMilestoneStep(3)">
          <div class="stepper-circle">4</div>
          <div class="stepper-year">2529</div>
          <div class="stepper-node-title">เปิดศูนย์รังสิต</div>
        </div>
        <div class="stepper-node" onclick="setMilestoneStep(4)">
          <div class="stepper-circle">5</div>
          <div class="stepper-year">2535</div>
          <div class="stepper-node-title">เปิดศูนย์ลำปาง</div>
        </div>
        <div class="stepper-node" onclick="setMilestoneStep(5)">
          <div class="stepper-circle">6</div>
          <div class="stepper-year">2538</div>
          <div class="stepper-node-title">เปิดศูนย์พัทยา</div>
        </div>
        <div class="stepper-node" onclick="setMilestoneStep(6)">
          <div class="stepper-circle">7</div>
          <div class="stepper-year">2567</div>
          <div class="stepper-node-title">วาระ 90 ปี</div>
        </div>
      </div>

      <div class="milestone-event-card" id="milestoneEventCard">
        <div>
          <h4 id="mEventTitle" style="font-size: 1.15rem; font-weight: 700; color: #ffffff; margin-bottom: 6px;">
            พ.ศ. 2477 — สถาปนามหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง
          </h4>
          <p id="mEventDesc" style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.6;">
            ศ.ดร.ปรีดี พนมยงค์ สถาปนา มธก. ในฐานะ "ตลาดวิชา" มีผู้สมัครเข้าเรียนรุ่นแรกสูงถึง 7,094 คน เพื่อเป็นบ่อน้ำบำบัดความกระหายของราษฎร
          </p>
        </div>
        <div style="text-align: right; min-width: 130px;">
          <div id="mEventStat" style="font-size: 2rem; font-weight: 800; color: var(--tu-gold);">7,094</div>
          <div id="mEventLabel" style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase;">นักศึกษารุ่นแรก</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       6. SECTION 3: TEAL SECTION - COST CAP & BUDGET ANALYSIS (025s - 035s)
       ========================================================================== -->
  <section class="bidwells-teal-section" id="budget">
    <div class="teal-container">
      <div style="margin-bottom: 40px;">
        <div style="font-size: 0.8rem; font-weight: 800; color: var(--tu-gold); letter-spacing: 0.12em; text-transform: uppercase;">03 / วินัยทางการเงินและโครงสร้างประชากร</div>
        <h2 style="font-family: var(--font-serif); font-size: 2.8rem; font-weight: 700; line-height: 1.25;">
          The Drive to <em>Innovate</em>
        </h2>
      </div>

      <!-- Card 1: 5-Year Budget Comparison (Cost Cap Style Frame 030s) -->
      <div class="cost-cap-white-card">
        <div class="cost-cap-grid">
          <div class="cost-cap-narrative">
            <h3 class="cost-cap-title">Financial Performance & Budget Growth</h3>
            <p class="cost-cap-lead">
              เปรียบเทียบงบประมาณรายรับ 5 ปีต่อเนื่อง (2563–2567) เติบโตจาก 13,420 ล้านบาท สู่ 15,350 ล้านบาท
              ด้วยการบริหารจัดการที่เป็นอิสระ เสริมสร้างความเข้มแข็งของ 5 แหล่งรายได้หลัก
            </p>
            <div style="font-size: 0.82rem; font-weight: 700; color: var(--bidwells-navy); margin-bottom: 6px;">คลิกเพื่อเจาะลึก 5 แหล่งรายได้หลัก:</div>
            <div class="drilldown-pills-row">
              <button class="drilldown-pill active" onclick="drilldownStream(0)">1. งบแผ่นดิน (35.8%)</button>
              <button class="drilldown-pill" onclick="drilldownStream(1)">2. ค่าธรรมเนียมศึกษา (32.4%)</button>
              <button class="drilldown-pill" onclick="drilldownStream(2)">3. ทรัพย์สิน & ลงทุน (18.2%)</button>
              <button class="drilldown-pill" onclick="drilldownStream(3)">4. ทุนวิจัยบริการ (8.6%)</button>
              <button class="drilldown-pill" onclick="drilldownStream(4)">5. บริการการแพทย์ (5.0%)</button>
            </div>
            <div id="streamDetailBox" style="margin-top: 16px; padding: 14px; background: #f8fafc; border-radius: 10px; font-size: 0.84rem; color: #475569; border-left: 3px solid var(--bidwells-crimson);">
              <strong>งบประมาณแผ่นดิน (35.8% • 5,495 ล้านบาท):</strong> เงินอุดหนุนทั่วไปและโครงการพัฒนาเชิงยุทธศาสตร์ระดับชาติ
            </div>
          </div>

          <div style="height: 320px;">
            <canvas id="budgetChartCanvas"></canvas>
          </div>
        </div>
      </div>

      <!-- Card 2: Demographic Structure & Gender Diversity -->
      <div class="demographic-white-card">
        <h3 class="demographic-headline">โครงสร้างประชากรนักศึกษาและความหลากหลายทางเพศภาวะ</h3>
        <p class="demographic-sub">
          ความหลากหลายและการเข้าถึงการศึกษาระดับอุดมศึกษาอย่างครอบคลุม สมดุลของสัดส่วนนักศึกษาในทุกกลุ่มสาขาวิชา สะท้อนพลังแห่งความเสมอภาคและเสรีภาพทางปัญญา
        </p>

        <div class="demographic-ratio-bar-wrap">
          <div class="ratio-bar">
            <div class="ratio-female">นักศึกษาหญิง 62.4% (26,613 คน)</div>
            <div class="ratio-male">นักศึกษาชาย 37.6% (16,037 คน)</div>
          </div>
        </div>

        <div style="height: 260px;">
          <canvas id="genderGroupChartCanvas"></canvas>
        </div>
      </div>

      <!-- Card 3: 26 Faculties Visualizer & TCAS Drilldown (Data Visualization) -->
      <div class="faculties-white-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 24px;">
          <div>
            <div style="font-size: 0.78rem; font-weight: 800; color: var(--bidwells-crimson); letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 6px;">
              <i class="fa-solid fa-chart-simple"></i> INTERACTIVE DATA VISUALIZER
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 1.85rem; font-weight: 700; color: var(--bidwells-navy); line-height: 1.2;">
              โครงสร้าง 26 คณะวิชา & เกณฑ์การรับเข้า TCAS
            </h3>
            <p style="font-size: 0.88rem; color: #64748b; margin-top: 6px;">
              แผนภูมิเปรียบเทียบคะแนนตัดต่ำสุด (Cutoff Score) และอัตราการแข่งขันในรอบ TCAS Admission ครบทั้ง 26 คณะวิชา
            </p>
          </div>

          <!-- View Mode Toggle Buttons -->
          <div class="faculties-view-toggle">
            <button class="fac-view-btn active" id="btnFacChartView" onclick="setFacultiesView('chart')">
              <i class="fa-solid fa-chart-column"></i> แผนภูมิเปรียบเทียบ (Visualizer)
            </button>
            <button class="fac-view-btn" id="btnFacGridView" onclick="setFacultiesView('grid')">
              <i class="fa-solid fa-table-cells"></i> รายการการ์ด (26 คณะ)
            </button>
          </div>
        </div>

        <!-- 4 KPI Summary Cards -->
        <div class="faculties-kpi-row">
          <div class="fac-kpi-item">
            <div class="kpi-num" style="color: var(--bidwells-crimson);">83.1</div>
            <div class="kpi-lbl">คะแนนตัดต่ำสุดสูงสุด (CICM)</div>
          </div>
          <div class="fac-kpi-item">
            <div class="kpi-num" style="color: var(--bidwells-navy);">72.8</div>
            <div class="kpi-lbl">คะแนนเฉลี่ย TCAS รวมทุกคณะ</div>
          </div>
          <div class="fac-kpi-item">
            <div class="kpi-num" style="color: #0284c7;">1 : 14.0</div>
            <div class="kpi-lbl">อัตราการแข่งขันสูงสุด</div>
          </div>
          <div class="fac-kpi-item">
            <div class="kpi-num" style="color: var(--tu-gold-dark);">26 คณะ</div>
            <div class="kpi-lbl">4 เสาหลักทางวิชาการ</div>
          </div>
        </div>

        <!-- Pillar Filters -->
        <div class="faculties-filter-pills">
          <button class="fac-pill active" onclick="filterFaculties('all')">ทั้งหมด (26 คณะ)</button>
          <button class="fac-pill" onclick="filterFaculties('soc')">สังคมศาสตร์และมนุษยศาสตร์</button>
          <button class="fac-pill" onclick="filterFaculties('sci')">วิทยาศาสตร์และเทคโนโลยี</button>
          <button class="fac-pill" onclick="filterFaculties('med')">วิทยาศาสตร์สุขภาพ</button>
          <button class="fac-pill" onclick="filterFaculties('inter')">วิทยาลัยนานาชาติและนวัตกรรม</button>
        </div>

        <!-- Academic Pillar Legend -->
        <div class="faculties-legend-row">
          <span style="font-weight: 700; color: #1e293b; margin-right: 8px;">สัญลักษณ์กลุ่มสาขาวิชา:</span>
          <span><span class="legend-color-dot" style="background: #1e3a8a;"></span> สังคมศาสตร์และมนุษยศาสตร์</span>
          <span><span class="legend-color-dot" style="background: #00857c;"></span> วิทยาศาสตร์และเทคโนโลยี</span>
          <span><span class="legend-color-dot" style="background: #c51944;"></span> วิทยาศาสตร์สุขภาพ</span>
          <span><span class="legend-color-dot" style="background: #d97706;"></span> นานาชาติและนวัตกรรม</span>
        </div>

        <!-- Visualization Stage: Horizontal Ranking Chart (Chart.js) -->
        <div id="facultiesChartWrapper" style="height: 540px; position: relative;">
          <canvas id="facultiesTcasChartCanvas"></canvas>
        </div>

        <!-- Cards Grid Stage (Hidden by default, toggleable) -->
        <div class="faculties-cards-grid" id="facultiesGrid" style="display: none;">
          <!-- Populated by JavaScript -->
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       7. SECTION 4: CURVED RACETRACK & TBS TRIPLE CROWN BENCHMARKING (037s - 040s)
       ========================================================================== -->
  <section class="bidwells-curved-track-section" id="racing-curve">
    <div class="curved-track-overlay-dim"></div>

    <div class="curved-track-content">
      <div style="text-align: center; margin-bottom: 30px;">
        <div style="font-size: 0.8rem; font-weight: 800; color: var(--tu-gold); letter-spacing: 0.12em; text-transform: uppercase;">04 / การแข่งขันและมาตรฐานระดับโลก</div>
        <h2 style="font-family: var(--font-serif); font-size: 3rem; font-weight: 700; line-height: 1.2;">
          Navigating Curves: <em>Triple Crown Leadership</em>
        </h2>
        <p style="font-size: 1.1rem; color: #cbd5e1; max-width: 800px; margin: 10px auto 0;">
          การขับเคี่ยวบนสนามการศึกษามาตรฐานสากล: คณะพาณิชยศาสตร์และการบัญชี (TBS) คว้า 3 มงกุฎระดับโลก
        </p>
      </div>

      <!-- S-Turn Track Stage with Dynamic Thammasat Students -->
      <div class="turning-cars-stage">
        <!-- Student 1 entering the curve -->
        <div class="turning-car-wrap turning-car-1" id="turnCar1" style="width: 105px;">
          <img src="assets/tu_student_walking.png" alt="นักศึกษาธรรมศาสตร์ TBS" class="tu-student-walker-img" />
          <div class="tu-student-badge" style="font-size: 0.65rem; padding: 2px 8px; margin-top: 4px;">
            <i class="fa-solid fa-award"></i> AACSB Leader
          </div>
        </div>
        <!-- Student 2 on apex of curve -->
        <div class="turning-car-wrap turning-car-2" id="turnCar2" style="width: 105px;">
          <img src="assets/tu_student_walking.png" alt="นักศึกษาธรรมศาสตร์ EQUIS" class="tu-student-walker-img" style="filter: drop-shadow(0 10px 18px rgba(0,0,0,0.7)) brightness(1.08);" />
          <div class="tu-student-badge" style="font-size: 0.65rem; padding: 2px 8px; margin-top: 4px;">
            <i class="fa-solid fa-globe"></i> EQUIS Standard
          </div>
        </div>
        <!-- Student 3 in forward stride -->
        <div class="turning-car-wrap turning-car-3" id="turnCar3" style="width: 105px;">
          <img src="assets/tu_student_walking.png" alt="นักศึกษาธรรมศาสตร์ AMBA" class="tu-student-walker-img" style="filter: drop-shadow(0 10px 18px rgba(0,0,0,0.7)) hue-rotate(-20deg);" />
          <div class="tu-student-badge" style="font-size: 0.65rem; padding: 2px 8px; margin-top: 4px;">
            <i class="fa-solid fa-crown"></i> AMBA Excellence
          </div>
        </div>
      </div>

      <!-- Benchmarking Matrix Card -->
      <div class="tbs-benchmark-card">
        <div class="tbs-header-row">
          <div>
            <h3 style="font-family: var(--font-serif); font-size: 1.6rem; font-weight: 700; color: #ffffff;">
              Thailand Business School Excellence Race
            </h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">TBS มหาวิทยาลัยธรรมศาสตร์ ครองการรับรองครบ 3 สถาบันหลักระดับโลก</p>
          </div>
          <div class="triple-crown-badges-row">
            <span class="crown-badge">AACSB (USA)</span>
            <span class="crown-badge">EQUIS (EU)</span>
            <span class="crown-badge">AMBA (UK)</span>
          </div>
        </div>

        <table class="benchmark-table">
          <thead>
            <tr>
              <th>สถาบันการศึกษา</th>
              <th>สถานะมงกุฎ</th>
              <th>AACSB</th>
              <th>EQUIS</th>
              <th>AMBA</th>
              <th>การจัดอันดับโลก</th>
            </tr>
          </thead>
          <tbody>
            <tr class="highlight-tbs">
              <td><strong>ธรรมศาสตร์ (TBS)</strong></td>
              <td><span style="color: var(--tu-gold);">👑 Triple Crown (100%)</span></td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td>Top 1% ของโลก (Eduniversal 5 Palms)</td>
            </tr>
            <tr>
              <td>จุฬาลงกรณ์ (CBS)</td>
              <td>Dual Crown (66%)</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-xmark" style="color: #94a3b8;"></i> กำลังพัฒนา</td>
              <td>Top Tier Business School</td>
            </tr>
            <tr>
              <td>ศศินทร์ (Sasin)</td>
              <td>Dual Crown (66%)</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-xmark" style="color: #94a3b8;"></i> -</td>
              <td>Global Executive Education</td>
            </tr>
            <tr>
              <td>มหิดล (CMMU)</td>
              <td>Single Crown (33%)</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-xmark" style="color: #94a3b8;"></i> -</td>
              <td><i class="fa-solid fa-circle-xmark" style="color: #94a3b8;"></i> -</td>
              <td>Management Innovation</td>
            </tr>
            <tr>
              <td>นิด้า (NIDA Business School)</td>
              <td>Single Crown (33%)</td>
              <td><i class="fa-solid fa-circle-check" style="color: #4ade80;"></i> ได้รับ</td>
              <td><i class="fa-solid fa-circle-xmark" style="color: #94a3b8;"></i> -</td>
              <td><i class="fa-solid fa-circle-xmark" style="color: #94a3b8;"></i> -</td>
              <td>Graduate Leadership</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       8. SECTION 5: SILVERSTONE CIRCUIT MILESTONE TRACK (Frames 041s - 050s)
       ========================================================================== -->
  <section class="bidwells-circuit-section" id="circuit">
    <div style="max-width: 1200px; margin: 0 auto 40px;">
      <div style="font-size: 0.8rem; font-weight: 800; color: var(--bidwells-crimson); letter-spacing: 0.12em; text-transform: uppercase;">05 / วงจรนวัตกรรมและพันธกิจสังคม</div>
      <h2 style="font-family: var(--font-serif); font-size: 2.8rem; font-weight: 700; color: var(--bidwells-navy); line-height: 1.25;">
        The Strategic <em>Innovation Circuit</em>
      </h2>
      <p style="font-size: 1.05rem; color: #64748b; max-width: 780px; line-height: 1.7;">
        เส้นทางหมุดหมายสำคัญ 4 ด้านที่ขับเคลื่อนความก้าวหน้าของมหาวิทยาลัยธรรมศาสตร์สู่ระดับสากล
      </p>
    </div>

    <div class="circuit-layout-grid">
      <!-- Silverstone SVG Vector Track Outline -->
      <div class="silverstone-svg-container">
        <svg width="100%" height="100%" viewBox="0 0 680 460" fill="none">
          <!-- Circuit Outer Boundary Path (Silverstone layout from frame 044s) -->
          <path id="circuitBasePath" d="M 120 180 C 130 90, 220 80, 280 140 C 340 180, 480 120, 560 160 C 620 200, 600 290, 540 340 C 470 390, 360 410, 300 370 C 240 330, 180 340, 150 290 C 110 240, 110 210, 120 180 Z" stroke="#00857c" stroke-width="6" opacity="0.45" stroke-linecap="round" stroke-linejoin="round" />
          
          <!-- Animated Progress Path -->
          <path id="circuitActivePath" d="M 120 180 C 130 90, 220 80, 280 140" stroke="#c51944" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" />

          <!-- Inner Chicane Curves -->
          <path d="M 280 140 C 310 190, 240 240, 220 280" stroke="#00857c" stroke-width="4" stroke-dasharray="6 6" opacity="0.35" />
        </svg>

        <!-- 4 Milestone Nodes along the Track -->
        <div class="circuit-milestone-node active" style="top: 180px; left: 120px;" onclick="selectCircuitNode(0)">1</div>
        <div class="circuit-milestone-node" style="top: 140px; left: 280px;" onclick="selectCircuitNode(1)">2</div>
        <div class="circuit-milestone-node" style="top: 160px; left: 560px;" onclick="selectCircuitNode(2)">3</div>
        <div class="circuit-milestone-node" style="top: 370px; left: 300px;" onclick="selectCircuitNode(3)">4</div>
      </div>

      <!-- Synchronized Insight Card (Frame 045s) -->
      <div class="circuit-insight-card">
        <div class="circuit-card-tag" id="cInsightTag">HEALTHCARE & HOSPITAL HUB</div>
        <h3 class="circuit-card-title" id="cInsightTitle">โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ</h3>
        <img src="assets/tha_prachan_dome_editorial.jpg" alt="Circuit Insight" class="circuit-card-img" id="cInsightImg" />
        <p class="circuit-card-desc" id="cInsightDesc">
          ศูนย์การแพทย์ระดับตติยภูมิชั้นสูง 810 เตียง ให้บริการผู้ป่วยกว่า 1.4 ล้านครั้งต่อปี 
          รองรับการรักษาโรคซับซ้อนและการฝึกอบรมแพทย์-บุคลากรสาธารณสุขชั้นนำของประเทศ
        </p>
        <div style="display: flex; gap: 20px; border-top: 1px solid #f1f5f9; padding-top: 16px;">
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: var(--bidwells-crimson);" id="cStat1">810</div>
            <div style="font-size: 0.72rem; color: #64748b; text-transform: uppercase;" id="cStatLbl1">เตียงผู้ป่วย</div>
          </div>
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: var(--bidwells-navy);" id="cStat2">1.4M+</div>
            <div style="font-size: 0.72rem; color: #64748b; text-transform: uppercase;" id="cStatLbl2">ผู้รับบริการต่อปี</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Interactive TU 2034 Strategy Cockpit -->
    <div class="cockpit-strategy-card">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
        <div>
          <h3 style="font-family: var(--font-serif); font-size: 1.8rem; font-weight: 700; color: var(--bidwells-navy);">
            TU 2034 Centennial Strategy Cockpit
          </h3>
          <p style="font-size: 0.88rem; color: #64748b;">
            ปรับคันเร่งยุทธศาสตร์ 4 ด้านเพื่อจำลองดัชนีความพร้อมสู่ 100 ปี ธรรมศาสตร์
          </p>
        </div>
        <div style="text-align: right;">
          <div style="font-size: 2.2rem; font-weight: 900; color: var(--bidwells-crimson);" id="cockpitCompositeScore">92.4</div>
          <div style="font-size: 0.75rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Centennial Readiness Index</div>
        </div>
      </div>

      <div class="cockpit-sliders-grid">
        <div class="cockpit-slider-item">
          <label>1. ทุนวิจัยระดับโลก (Global Research)</label>
          <input type="range" class="cockpit-range-input" min="50" max="100" value="90" id="sliderResearch" oninput="updateCockpit()" />
          <div class="cockpit-val-disp" id="dispResearch">90%</div>
        </div>
        <div class="cockpit-slider-item">
          <label>2. บัณฑิตทักษะ AI & นวัตกรรม</label>
          <input type="range" class="cockpit-range-input" min="50" max="100" value="95" id="sliderSkills" oninput="updateCockpit()" />
          <div class="cockpit-val-disp" id="dispSkills">95%</div>
        </div>
        <div class="cockpit-slider-item">
          <label>3. วิทยาเขตคาร์บอนต่ำ (SDG Green)</label>
          <input type="range" class="cockpit-range-input" min="50" max="100" value="88" id="sliderGreen" oninput="updateCockpit()" />
          <div class="cockpit-val-disp" id="dispGreen">88%</div>
        </div>
        <div class="cockpit-slider-item">
          <label>4. สุขภาพและการแพทย์เพื่อชุมชน</label>
          <input type="range" class="cockpit-range-input" min="50" max="100" value="96" id="sliderHealth" oninput="updateCockpit()" />
          <div class="cockpit-val-disp" id="dispHealth">96%</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       9. SECTION 6: CHECKERED FINISH LINE CROSSING & REPORT DOWNLOAD (051s - 054s)
       ========================================================================== -->
  <section class="bidwells-finish-section" id="finish">
    <!-- Authentic Checkered Finish Line Banner (finish.svg) -->
    <div class="checkered-finish-banner"></div>

    <div style="text-align: center; max-width: 900px; margin: 0 auto 50px;">
      <div style="font-size: 0.82rem; font-weight: 800; color: var(--bidwells-crimson); letter-spacing: 0.12em; text-transform: uppercase;">06 / ข้ามเส้นชัยแห่งเกียรติภูมิ 90 ปี</div>
      <h2 style="font-family: var(--font-serif); font-size: 3rem; font-weight: 700; color: var(--bidwells-navy); line-height: 1.25; margin: 12px 0 16px;">
        Thammasat Leaders Crossing into the <em>Future</em>
      </h2>
      <p style="font-size: 1.1rem; color: #475569; line-height: 1.7;">
        ธรรมศาสตร์ 90 ปี สู่ศตวรรษแห่งการสร้างผู้นำ การขับเคลื่อนนวัตกรรม และการเปลี่ยนแปลงเพื่อประโยชน์สูงสุดของสังคม
      </p>
    </div>

    <!-- Two Thammasat Students Crossing the Milestone into the Future -->
    <div class="finish-cars-crossing-row">
      <!-- Student Leader Crossing -->
      <div class="finish-car-item" style="width: 140px; display: flex; flex-direction: column; align-items: center;">
        <img src="assets/tu_student_walking.png" alt="บัณฑิตธรรมศาสตร์เพื่อสังคม" class="tu-student-walker-img" />
        <div class="tu-student-badge" style="margin-top: 10px;">
          <i class="fa-solid fa-user-graduate"></i> บัณฑิตธรรมศาสตร์เพื่อประชาชน
        </div>
      </div>
      <!-- Student Scholar Crossing -->
      <div class="finish-car-item" style="width: 140px; display: flex; flex-direction: column; align-items: center;">
        <img src="assets/tu_student_walking.png" alt="ผู้นำแห่งอนาคต TU 2034" class="tu-student-walker-img" style="filter: drop-shadow(0 14px 24px rgba(0,0,0,0.75)) brightness(1.08);" />
        <div class="tu-student-badge" style="margin-top: 10px;">
          <i class="fa-solid fa-compass"></i> TU 2034 Future Leader
        </div>
      </div>
    </div>

    <!-- Download the Full Report Card (Frame 053s) -->
    <div class="download-report-card">
      <h3 class="download-report-title">Download the full research report</h3>
      <p class="download-report-desc">
        รับชุดข้อมูลฉบับสมบูรณ์ประกอบด้วยรายงาน 9 ทศวรรษมหาวิทยาลัยธรรมศาสตร์ สถิติประชากร การเงิน และยุทธศาสตร์ TU 2034 ในรูปแบบ PDF คุณภาพสูง
      </p>

      <form id="downloadForm" onsubmit="handleDownloadSubmit(event)">
        <div class="download-form-grid">
          <div>
            <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 6px;">First Name*</label>
            <input type="text" class="form-input-field" placeholder="ชื่อจริง" required />
          </div>
          <div>
            <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 6px;">Last Name*</label>
            <input type="text" class="form-input-field" placeholder="นามสกุล" required />
          </div>
          <div>
            <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 6px;">Work Email*</label>
            <input type="email" class="form-input-field" placeholder="อีเมลองค์กร / สถาบัน" required />
          </div>
          <div>
            <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #334155; margin-bottom: 6px;">Organization / Role</label>
            <input type="text" class="form-input-field" placeholder="หน่วยงาน / ภาคส่วน" />
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
          <button type="submit" class="btn-submit-download">
            <span>Download Full Report (PDF)</span>
            <i class="fa-solid fa-cloud-arrow-down"></i>
          </button>
          <a href="https://colab.research.google.com/github/kondee-rgb/BI304-Thammasat-Data-Storytelling/blob/main/BI304_Thammasat_Data_Storytelling.ipynb" target="_blank" rel="noopener noreferrer" class="header-colab-btn">
            <img src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Google Colab" style="width: 17px; height: 17px;" />
            <span>Google Colab (Interactive Code)</span>
          </a>
        </div>
      </form>
    </div>
  </section>

  <!-- TCAS Drilldown Modal -->
  <div class="drilldown-modal-backdrop" id="facultyModal">
    <div class="drilldown-modal-card">
      <button class="modal-close-btn" onclick="closeFacultyModal()"><i class="fa-solid fa-xmark"></i></button>
      <div style="font-size: 0.75rem; font-weight: 800; color: var(--bidwells-crimson); text-transform: uppercase;" id="mFacPillar">เสาหลักทางวิชาการ</div>
      <h3 style="font-family: var(--font-serif); font-size: 1.6rem; font-weight: 700; color: var(--bidwells-navy); margin: 6px 0 16px;" id="mFacTitle">ชื่อคณะวิชา</h3>
      <p style="font-size: 0.92rem; color: #475569; line-height: 1.7; margin-bottom: 24px;" id="mFacDesc">รายละเอียดของหลักสูตรและพันธกิจ</p>

      <div style="background: #f8fafc; border-radius: 12px; padding: 20px; margin-bottom: 20px;">
        <div style="font-weight: 700; font-size: 0.88rem; color: var(--bidwells-navy); margin-bottom: 10px;">เกณฑ์คะแนนเฉลี่ย TCAS (รอบที่ 3 Admission):</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: var(--bidwells-crimson);" id="mFacCutoff">72.5 / 100</div>
            <div style="font-size: 0.72rem; color: #64748b;">คะแนนตัดต่ำสุด</div>
          </div>
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: var(--bidwells-navy);" id="mFacAccept">1 : 4.8</div>
            <div style="font-size: 0.72rem; color: #64748b;">อัตราการแข่งขัน</div>
          </div>
        </div>
      </div>

      <div style="font-size: 0.85rem; color: #64748b;">
        <strong>เส้นทางวิชาชีพที่รองรับ:</strong> <span id="mFacCareers">นักกฎหมาย, ที่ปรึกษานโยบาย, นักการทูต</span>
      </div>
    </div>
  </div>

  <!-- Download Report Thank You Modal -->
  <div class="drilldown-modal-backdrop" id="downloadModal">
    <div class="drilldown-modal-card" style="text-align: center;">
      <button class="modal-close-btn" onclick="closeDownloadModal()"><i class="fa-solid fa-xmark"></i></button>
      <div style="width: 64px; height: 64px; border-radius: 50%; background: #dcfce7; color: #15803d; font-size: 28px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
        <i class="fa-solid fa-check"></i>
      </div>
      <h3 style="font-family: var(--font-serif); font-size: 1.8rem; font-weight: 700; color: var(--bidwells-navy); margin-bottom: 10px;">
        ขอบคุณสำหรับการติดตาม
      </h3>
      <p style="font-size: 0.95rem; color: #64748b; line-height: 1.7; margin-bottom: 24px;">
        รายงานสรุป 90 ปีมหาวิทยาลัยธรรมศาสตร์ ฉบับเต็ม ได้ถูกส่งไปยังอีเมลของท่านเรียบร้อยแล้ว
      </p>
      <button class="btn-bidwells-pill" onclick="closeDownloadModal()" style="margin: 0 auto;">
        <span>กลับสู่หน้าหลัก</span>
      </button>
    </div>
  </div>

  <!-- Flourish 10-Scene Data Storytelling Hub Modal -->
  <div class="flourish-modal-backdrop" id="flourishHubModal">
    <div class="flourish-modal-card">
      <div class="flourish-modal-header">
        <div>
          <div style="font-size: 0.75rem; font-weight: 800; color: #0284c7; letter-spacing: 0.08em; text-transform: uppercase;">
            <i class="fa-solid fa-chart-pie"></i> FLOURISH DATA STORYTELLING HUB
          </div>
          <h3 style="font-family: var(--font-serif); font-size: 1.55rem; font-weight: 700; color: var(--bidwells-navy); margin: 4px 0;">
            คลังภาพข้อมูล Flourish ครบ 10 ฉาก (Scenes 1 — 10)
          </h3>
          <p style="font-size: 0.82rem; color: #64748b; margin: 0;">
            ชุดข้อมูล CSV และเทมเพลตมาตรฐานสากล ออกแบบตามหลัก Edward Tufte & LATCH Framework
          </p>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
          <a href="https://colab.research.google.com/github/kondee-rgb/BI304-Thammasat-Data-Storytelling/blob/main/BI304_Thammasat_Data_Storytelling.ipynb" target="_blank" rel="noopener noreferrer" class="header-colab-btn" style="padding: 6px 12px; font-size: 0.78rem;">
            <img src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Google Colab" style="width: 15px; height: 15px;" />
            <span>Google Colab</span>
          </a>
          <button class="modal-close-btn" onclick="closeFlourishHubModal()"><i class="fa-solid fa-xmark"></i></button>
        </div>
      </div>

      <div class="flourish-modal-body">
        <!-- Left: 10 Scenes Navigation Tabs -->
        <div class="flourish-sidebar-tabs" id="flourishSidebarTabs">
          <!-- Populated by JS for Scenes 1 to 10 -->
        </div>

        <!-- Right: Active Scene Detail Pane -->
        <div class="flourish-scene-detail-pane" id="flourishDetailPane">
          <!-- Populated by JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       JAVASCRIPT INTERACTIONS & DATA INITIALIZATION
       ========================================================================== -->
  <script>
    // 1. Data Store
    const CAMPUSES_DATA = [
      {
        id: 0,
        name: "ท่าพระจันทร์ (Tha Prachan)",
        shortName: "ท่าพระจันทร์",
        badge: "สถาปนา พ.ศ. 2477",
        area: "49 ไร่",
        students: "6,310 คน",
        role: "มรดกประชาธิปไตย",
        focus: "นานาชาติ / บัณฑิตศึกษา / กฎหมาย-รัฐศาสตร์",
        location: "ริมแม่น้ำเจ้าพระยา เขตพระนคร กรุงเทพมหานคร",
        lat: 13.7557,
        lng: 100.4930,
        zoom: 14
      },
      {
        id: 1,
        name: "ศูนย์รังสิต (Rangsit)",
        shortName: "ศูนย์รังสิต",
        badge: "เปิด พ.ศ. 2529",
        area: "2,644 ไร่",
        students: "31,350 คน",
        role: "ศูนย์วิจัย & นวัตกรรม",
        focus: "วิทย์-เทคโน / วิทย์สุขภาพ / รพ.ธรรมศาสตร์ / ป.ตรี",
        location: "ต.คลองหนึ่ง อ.คลองหลวง จ.ปทุมธานี",
        lat: 14.0736,
        lng: 100.6067,
        zoom: 13
      },
      {
        id: 2,
        name: "ศูนย์พัทยา (Pattaya)",
        shortName: "ศูนย์พัทยา EEC",
        badge: "เปิด พ.ศ. 2538",
        area: "566 ไร่",
        students: "1,920 คน",
        role: "EEC Medical Valley",
        focus: "การแพทย์ชั้นสูง & เทคโนโลยีดิจิทัล AI",
        location: "ต.โป่ง อ.บางละมุง จ.ชลบุรี (ระเบียงเศรษฐกิจ EEC)",
        lat: 12.9236,
        lng: 100.9925,
        zoom: 13
      },
      {
        id: 3,
        name: "ศูนย์ลำปาง (Lampang)",
        shortName: "ศูนย์ลำปาง",
        badge: "เปิด พ.ศ. 2535",
        area: "848 ไร่",
        students: "3,070 คน",
        role: "ศูนย์การเรียนรู้ภาคเหนือ",
        focus: "พัฒนาชุมชน & ศิลปวัฒนธรรมล้านนา",
        location: "ต.ห้างฉัตร อ.ห้างฉัตร จ.ลำปาง",
        lat: 18.2982,
        lng: 99.4897,
        zoom: 12
      },
      {
        id: 4,
        name: "เครือข่าย 4 วิทยาเขตครบวงจร",
        shortName: "ทั่วประเทศ (National)",
        badge: "โครงข่าย 4 วิทยาเขต",
        area: "4,107 ไร่",
        students: "42,650 คน",
        role: "เครือข่ายบูรณาการยุทธศาสตร์",
        focus: "สหวิทยาการและผลกระทบสังคม TU 2034",
        location: "ครอบคลุมกรุงเทพฯ, ปทุมธานี, ชลบุรี (EEC) และลำปาง",
        lat: 15.45,
        lng: 100.5,
        zoom: 6
      }
    ];

    const MILESTONES_DATA = [
      { year: "2477", title: "พ.ศ. 2477 — สถาปนามหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง", desc: "ศ.ดร.ปรีดี พนมยงค์ ก่อตั้ง มธก. ในฐานะ 'ตลาดวิชา' ระบบเปิด มีผู้สมัครเข้าเรียนรุ่นแรกสูงถึง 7,094 คน เน้นวิชากฎหมายและการเมืองเพื่อประชาชน", stat: "7,094", lbl: "นักศึกษารุ่นแรก" },
      { year: "2495", title: "พ.ศ. 2495 — สถาปนาชื่อทางการ 'มหาวิทยาลัยธรรมศาสตร์'", desc: "เปลี่ยนชื่อจาก มธก. เป็น 'มหาวิทยาลัยธรรมศาสตร์' (มธ.) เพื่อสะท้อนการขยายการเรียนการสอนสู่สาขาวิชาที่ครอบคลุมมากยิ่งขึ้น", stat: "2495", lbl: "ปีเปลี่ยนชื่อ" },
      { year: "2496-03", title: "พ.ศ. 2496–2503 — ปฏิรูปสู่ 'ระบบปิด' (Selective Admission)", desc: "ปรับเปลี่ยนกระบวนการรับเข้าจากการเป็นตลาดวิชาสู่ 'ระบบปิด' เพื่อยกระดับความเข้มข้นทางวิชาการและการวิจัย เริ่มการสอบคัดเลือกอย่างเป็นทางการ", stat: "100%", lbl: "ระบบคัดเลือกเข้มข้น" },
      { year: "2529", title: "พ.ศ. 2529 — เปิดศูนย์รังสิต เพื่อการศึกษาวิทยาศาสตร์และเทคโนโลยี", desc: "ขยายวิทยาเขตครั้งประวัติศาสตร์สู่ศูนย์รังสิต 2,644 ไร่ รองรับการเปิดคณะด้านวิทยาศาสตร์ เทคโนโลยี และแพทยศาสตร์", stat: "2,644", lbl: "พื้นที่ไร่" },
      { year: "2535", title: "พ.ศ. 2535 — ขยายศูนย์การศึกษาลำปาง สู่ภาคเหนือ", desc: "สถาปนาศูนย์ลำปาง เพื่อขยายโอกาสทางการศึกษาสู่ภูมิภาค เน้นการพัฒนาท้องถิ่นและอนุรักษ์ศิลปวัฒนธรรม", stat: "848", lbl: "พื้นที่ไร่" },
      { year: "2538", title: "พ.ศ. 2538 — ขยายศูนย์พัทยา เพื่ออุตสาหกรรมและนวัตกรรม", desc: "เปิดศูนย์พัทยา จ.ชลบุรี เพื่อรองรับการขยายตัวทางเศรษฐกิจภาคตะวันออก มุ่งสู่ EEC Medical Valley ในปัจจุบัน", stat: "566", lbl: "พื้นที่ไร่" },
      { year: "2567", title: "พ.ศ. 2567 — วาระครบรอบ 90 ปี มหาวิทยาลัยธรรมศาสตร์", desc: "เฉลิมฉลอง 9 ทศวรรษแห่งความภาคภูมิใจ มุ่งสู่มหาวิทยาลัยวิจัยระดับโลกเพื่อประชาชนและยุทธศาสตร์ TU 2034 สู่ศตวรรษที่หนึ่ง", stat: "90", lbl: "ทศวรรษแห่งเกียรติภูมิ" }
    ];

    const FACULTIES_DATA = [
      { name: "คณะนิติศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "รากฐานแห่งนิติศาสตร์ไทย ผลิตนักกฎหมายและผู้นำการเปลี่ยนแปลง", cutoff: "74.8", accept: "1 : 5.2", careers: "ผู้พิพากษา, อัยการ, นิติกร, ทนายความระหว่างประเทศ" },
      { name: "คณะพาณิชยศาสตร์และการบัญชี (TBS)", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "ผู้นำ Triple Crown หนึ่งเดียวในไทย ติด 1% ของโลก", cutoff: "76.2", accept: "1 : 6.1", careers: "CFO, ผู้สอบบัญชี, นักวิเคราะห์การลงทุน, ผู้ประกอบการ" },
      { name: "คณะรัฐศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "สิงห์แดงชั้นนำ เสาหลักนโยบายสาธารณะและการทูตสากล", cutoff: "73.5", accept: "1 : 4.9", careers: "นักการทูต, ข้าราชการพลเรือน, นักวิเคราะห์นโยบาย" },
      { name: "คณะเศรษฐศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "เศรษฐศาสตร์ทฤษฎีและนโยบายพัฒนาเศรษฐกิจระดับชาติ", cutoff: "72.9", accept: "1 : 4.5", careers: "นักเศรษฐศาสตร์, ผู้กำหนดนโยบาย ธปท., นักวิจัย" },
      { name: "คณะสังคมวิทยาและมานุษยวิทยา", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "เข้าใจโครงสร้างสังคม มนุษย์ และความหลากหลายทางวัฒนธรรม", cutoff: "69.4", accept: "1 : 3.8", careers: "นักวิจัยสังคม, ที่ปรึกษา ESG, นักสื่อสารชุมชน" },
      { name: "คณะวารสารศาสตร์และสื่อสารมวลชน", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "ผู้นำสื่อสารมวลชนยุคดิจิทัลและสร้างสรรค์คอนเทนต์ระดับโลก", cutoff: "73.8", accept: "1 : 5.8", careers: "ผู้ผลิตสื่อ, ครีเอทีฟ, นักกลยุทธ์แบรนด์" },
      { name: "คณะสังคมสงเคราะห์ศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "พัฒนาคุณภาพชีวิต สร้างความเสมอภาคและสวัสดิการสังคม", cutoff: "68.2", accept: "1 : 3.5", careers: "นักสังคมสงเคราะห์, ผู้บริหารองค์กรไม่แสวงหากำไร" },
      { name: "คณะศิลปศาสตร์", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "สหภาษาศาสตร์ มนุษยศาสตร์ และวรรณคดีเปรียบเทียบ", cutoff: "71.6", accept: "1 : 4.4", careers: "นักแปล, ล่าม, นักวิชาการภาษา, เจ้าหน้าที่ระหว่างประเทศ" },
      { name: "คณะวิทยาศาสตร์และเทคโนโลยี", pillar: "sci", pillarName: "วิทย์-เทคโน", desc: "วิทยาการข้อมูล AI ชีวเคมี และนวัตกรรมอุตสาหกรรม", cutoff: "67.8", accept: "1 : 3.6", careers: "Data Scientist, นักวิจัยเคมี, ผู้พัฒนา AI" },
      { name: "คณะวิศวกรรมศาสตร์ (TSE)", pillar: "sci", pillarName: "วิทย์-เทคโน", desc: "วิศวกรรมสากล ยานยนต์ไฟฟ้า หุ่นยนต์ และการบิน", cutoff: "71.2", accept: "1 : 4.8", careers: "วิศวกรระบบ, วิศวกรยานยนต์, วิศวกรปัญญาประดิษฐ์" },
      { name: "คณะสถาปัตยกรรมศาสตร์และการผังเมือง", pillar: "sci", pillarName: "วิทย์-เทคโน", desc: "ผู้นำการออกแบบเมืองอัจฉริยะและการพัฒนาอย่างยั่งยืน", cutoff: "72.4", accept: "1 : 5.0", careers: "สถาปนิก, นักผังเมือง, นักออกแบบนวัตกรรม" },
      { name: "สถาบันเทคโนโลยีนานาชาติสิรินธร (SIIT)", pillar: "inter", pillarName: "นานาชาติ", desc: "หลักสูตรวิศวกรรมและเทคโนโลยีนานาชาติระดับท็อปของเอเชีย", cutoff: "75.0", accept: "1 : 5.5", careers: "วิศวกรข้ามชาติ, Tech Entrepreneur, นักวิจัยระดับสากล" },
      { name: "คณะแพทยศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "ผลิตแพทย์ผู้เชี่ยวชาญระดับตติยภูมิ ดูแลสุขภาวะประชาชน", cutoff: "82.4", accept: "1 : 12.5", careers: "แพทย์ผู้เชี่ยวชาญ, นักวิจัยการแพทย์, ผู้บริหารสาธารณสุข" },
      { name: "คณะทันตแพทยศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "ความเป็นเลิศด้านทันตกรรมและศัลยศาสตร์ช่องปาก", cutoff: "79.8", accept: "1 : 9.2", careers: "ทันตแพทย์, ศัลยแพทย์ช่องปาก" },
      { name: "คณะเภสัชศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "วิทยาการทางเภสัชกรรมและการบริบาลเภสัชกรรม", cutoff: "77.1", accept: "1 : 7.4", careers: "เภสัชกรโรงพยาบาล, เภสัชกรอุตสาหกรรมยา" },
      { name: "คณะพยาบาลศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "พยาบาลวิชาชีพเพื่อการดูแลผู้ป่วยขั้นวิกฤตและชุมชน", cutoff: "70.2", accept: "1 : 4.2", careers: "พยาบาลวิชาชีพ, ผู้เชี่ยวชาญการดูแลผู้สูงอายุ" },
      { name: "คณะสหเวชศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "เทคนิคการแพทย์ กายภาพบำบัด และรังสีเทคนิค", cutoff: "72.0", accept: "1 : 4.7", careers: "นักเทคนิคการแพทย์, นักกายภาพบำบัด" },
      { name: "คณะสาธารณสุขศาสตร์", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "การควบคุมโรค อนามัยสิ่งแวดล้อม และอาชีวอนามัย", cutoff: "68.9", accept: "1 : 3.7", careers: "นักวิชาการสาธารณสุข, เจ้าหน้าที่ความปลอดภัย (จป.)" },
      { name: "วิทยาลัยสหวิทยาการ", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "บูรณาการศาสตร์ตอบสนองความท้าทายยุคใหม่ (รังสิต-ลำปาง)", cutoff: "69.1", accept: "1 : 3.4", careers: "นักวิเคราะห์ข้อมูลสังคม, ที่ปรึกษานวัตกรรม" },
      { name: "วิทยาลัยนวัตกรรม (CITU)", pillar: "inter", pillarName: "นานาชาติ", desc: "การจัดการเทคโนโลยี นวัตกรรมบริการ และธุรกิจดิจิทัล", cutoff: "71.5", accept: "1 : 4.3", careers: "Innovation Manager, ผู้ประกอบการดิจิทัล" },
      { name: "วิทยาลัยนานาชาติปรีดี พนมยงค์ (PBIC)", pillar: "inter", pillarName: "นานาชาติ", desc: "จีนศึกษา ไทยศึกษา อินเดียศึกษา ระดับนานาชาติ", cutoff: "74.2", accept: "1 : 4.8", careers: "นักการทูต, นักกลยุทธ์ระหว่างประเทศ" },
      { name: "วิทยาลัยพัฒนศาสตร์ ป๋วย อึ๊งภากรณ์ (PSDS)", pillar: "soc", pillarName: "สังคมศาสตร์", desc: "พัฒนาชนบท ชุมชนเข้มแข็ง และความยั่งยืนตามแนวทาง อ.ป๋วย", cutoff: "67.4", accept: "1 : 3.2", careers: "นักพัฒนาชุมชน, ที่ปรึกษา CSR/SDGs" },
      { name: "วิทยาลัยแพทยศาสตร์นานาชาติจุฬาภรณ์ (CICM)", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "หลักสูตรแพทยศาสตร์นานาชาติและทันตแพทยศาสตร์สากล", cutoff: "83.1", accept: "1 : 14.0", careers: "แพทย์สากล, นักวิจัยชีวการแพทย์" },
      { name: "คณะพยาบาลศาสตร์ (ศูนย์ลำปาง)", pillar: "med", pillarName: "วิทยาศาสตร์สุขภาพ", desc: "ผลิตพยาบาลเพื่อดูแลชุมชนสุขภาพภาคเหนือ", cutoff: "69.8", accept: "1 : 4.0", careers: "พยาบาลวิชาชีพ" },
      { name: "สถาบันเสริมศึกษาและทรัพยากรมนุษย์", pillar: "inter", pillarName: "นานาชาติ", desc: "Upskill & Reskill การเรียนรู้ตลอดชีวิตสำหรับประชาชนทุกวัย", cutoff: "70.0", accept: "1 : 3.5", careers: "ผู้เชี่ยวชาญการเรียนรู้และพัฒนาองค์กร" }
    ];

    const CIRCUIT_DATA = [
      {
        tag: "HEALTHCARE & HOSPITAL HUB",
        title: "โรงพยาบาลธรรมศาสตร์เฉลิมพระเกียรติ",
        desc: "ศูนย์การแพทย์ตติยภูมิชั้นสูง 810 เตียง ดูแลรักษาโรคซับซ้อน ผ่าตัดหัวใจ หลอดเลือดสมอง และโรคมะเร็ง พร้อมหน่วยแพทย์ฉุกเฉินและระบบบริการดิจิทัลระดับประเทศ",
        img: "assets/tha_prachan_dome_editorial.jpg",
        stat1: "810", lbl1: "เตียงผู้ป่วย", stat2: "1.4M+", lbl2: "ผู้รับบริการต่อปี"
      },
      {
        tag: "GREEN CAMPUS & SUSTAINABILITY",
        title: "อาคารป๋วย 100 ปี & สวนเกษตรอินทรีย์ลอยฟ้า",
        desc: "ต้นแบบสถาปัตยกรรมสีเขียวเพื่อการเรียนรู้ สวนลอยฟ้าออร์แกนิกขนาดใหญ่ที่สุดในเอเชียตะวันออกเฉียงใต้ รองรับการดูดซับคาร์บอนและระบบบำบัดน้ำหมุนเวียน",
        img: "assets/tha_prachan_dome_editorial.jpg",
        stat1: "อันดับ 1", lbl1: "สวนลอยฟ้าเอเชีย", stat2: "Top 5", lbl2: "SDG 11 ของโลก"
      },
      {
        tag: "GLOBAL IMPACT & RANKINGS",
        title: "SDG 11 อันดับ 5 ของโลก จาก THE Impact Rankings",
        desc: "ธรรมศาสตร์ได้รับการจัดอันดับให้เป็น Top 5 ของโลกด้านเมืองและชุมชนยั่งยืน จากผลงานการพัฒนาสิ่งแวดล้อม การขนส่งพลังงานสะอาด และการบริการเพื่อประชาชน",
        img: "assets/tha_prachan_dome_editorial.jpg",
        stat1: "Top 5", lbl1: "อันดับโลก SDG 11", stat2: "อันดับ 1", lbl2: "ในประเทศไทย"
      },
      {
        tag: "CENTENNIAL STRATEGY 2034",
        title: "ยุทธศาสตร์ TU 2034 สู่ศตวรรษแห่งความยั่งยืน",
        desc: "พิมพ์เขียวการเปลี่ยนผ่านสู่ทศวรรษที่ 10 ของมหาวิทยาลัย: ก้าวสู่การเป็นมหาวิทยาลัยชั้นนำระดับโลกที่สร้างผู้นำการเปลี่ยนแปลงทางปัญญาและนวัตกรรม",
        img: "assets/tha_prachan_dome_editorial.jpg",
        stat1: "100 ปี", lbl1: "เป้าหมายศตวรรษ", stat2: "4 เสาหลัก", lbl2: "ยุทธศาสตร์ขับเคลื่อน"
      }
    ];

    // 2. Scroll-Linked Student Motion and Scroller
    function initScrollInteractions() {
      const studentLeader = document.getElementById('studentLeader');
      const studentScholar = document.getElementById('studentScholar');
      const scrubberFill = document.getElementById('scrubberFill');
      const scrubberThumb = document.getElementById('scrubberThumb');
      const pips = document.querySelectorAll('.scrubber-pip');
      const navLinks = document.querySelectorAll('.header-nav-link');

      window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = Math.min(Math.max(scrollTop / scrollHeight, 0), 1);

        // Update Scrubber Fill and Thumb
        if (scrubberFill && scrubberThumb) {
          scrubberFill.style.width = (progress * 100) + '%';
          scrubberThumb.style.left = (progress * 100) + '%';
        }

        // Hero Student Walkers Scroll Acceleration
        const walkerStartScroll = 400;
        const studentLeader = document.getElementById('studentLeader');
        const studentScholar = document.getElementById('studentScholar');
        if (scrollTop <= walkerStartScroll) {
          if (studentLeader) studentLeader.style.transform = 'translateY(0px)';
          if (studentScholar) studentScholar.style.transform = 'translateY(0px)';
        } else if (scrollTop < window.innerHeight * 2.2) {
          const delta = scrollTop - walkerStartScroll;
          if (studentLeader) studentLeader.style.transform = `translateY(${delta * 0.92}px)`;
          if (studentScholar) studentScholar.style.transform = `translateY(${delta * 0.85}px)`;
        }

        // Turning Cars Animation in S-Curve
        const curveSection = document.getElementById('racing-curve');
        if (curveSection) {
          const rect = curveSection.getBoundingClientRect();
          if (rect.top < window.innerHeight && rect.bottom > 0) {
            const curveProgress = (window.innerHeight - rect.top) / (window.innerHeight + rect.height);
            const turnCar1 = document.getElementById('turnCar1');
            const turnCar2 = document.getElementById('turnCar2');
            const turnCar3 = document.getElementById('turnCar3');
            if (turnCar1) turnCar1.style.transform = `rotate(${-18 + curveProgress * 20}deg) translate(${curveProgress * 30}px, ${curveProgress * 20}px)`;
            if (turnCar2) turnCar2.style.transform = `rotate(${24 - curveProgress * 30}deg) translate(${-curveProgress * 20}px, ${curveProgress * 25}px)`;
            if (turnCar3) turnCar3.style.transform = `rotate(${-12 + curveProgress * 15}deg) translate(${curveProgress * 25}px, ${curveProgress * 15}px)`;
          }
        }

        // Update active nav links & pips
        const sections = ['hero', 'statement', 'campuses', 'budget', 'racing-curve', 'circuit', 'finish'];
        sections.forEach((secId, idx) => {
          const sec = document.getElementById(secId);
          if (sec) {
            const rect = sec.getBoundingClientRect();
            if (rect.top <= window.innerHeight * 0.4 && rect.bottom >= window.innerHeight * 0.4) {
              pips.forEach(p => p.classList.remove('active'));
              if (pips[idx]) pips[idx].classList.add('active');

              navLinks.forEach(l => l.classList.remove('active'));
              if (navLinks[idx]) navLinks[idx].classList.add('active');
            }
          }
        });
      }, { passive: true });
    }

    // 3. Scrubber click handler
    function handleScrubberClick(e) {
      const track = document.getElementById('scrubberTrack');
      const rect = track.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = Math.min(Math.max(clickX / rect.width, 0), 1);
      const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
      window.scrollTo({
        top: ratio * scrollHeight,
        behavior: 'smooth'
      });
    }

    function scrollToElement(id) {
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      }
    }

    // Leaflet Map State for 4 Campuses
    let tuMap = null;
    let tuMarkers = [];
    let corridorLines = [];

    function initTuLeafletMap() {
      if (tuMap) return;
      const mapEl = document.getElementById('campusLeafletMap');
      if (!mapEl) return;

      // Create Leaflet Map centered at Thailand
      tuMap = L.map('campusLeafletMap', {
        center: [15.45, 100.5],
        zoom: 6,
        minZoom: 5,
        maxZoom: 18,
        scrollWheelZoom: false,
        attributionControl: true
      });

      // Enable wheel zoom only when map is clicked / focused
      tuMap.on('focus', () => { tuMap.scrollWheelZoom.enable(); });
      tuMap.on('blur', () => { tuMap.scrollWheelZoom.disable(); });

      // 1. Esri World Dark Gray Base + Reference (No API Key Required, Clean Dark Cartography)
      const esriDarkBase = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; DeLorme, NAVTEQ',
        maxZoom: 16
      });

      const esriDarkRef = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}', {
        attribution: '',
        maxZoom: 16
      });

      window.tuMapDarkGroup = L.layerGroup([esriDarkBase, esriDarkRef]).addTo(tuMap);

      // 2. Alternative: Esri Satellite Imagery
      window.tuMapSatLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS',
        maxZoom: 18
      });

      // 3. Alternative: OpenStreetMap standard
      window.tuMapOsmLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
        maxZoom: 19
      });

      window.tuMap = tuMap;

      // Strategic Network Connecting Corridors
      const corridors = [
        { from: [13.7557, 100.4930], to: [14.0736, 100.6067], title: "แนวแกนการศึกษา ปทุมธานี - กทม. (37 กม.)" },
        { from: [14.0736, 100.6067], to: [12.9236, 100.9925], title: "ระเบียงนวัตกรรมและเศรษฐกิจตะวันออก EEC (145 กม.)" },
        { from: [14.0736, 100.6067], to: [18.2982, 99.4897], title: "แนวเชื่อมโยงสู่ภูมิภาคภาคเหนือ จ.ลำปาง (515 กม.)" }
      ];

      corridors.forEach(cor => {
        // Subtle crimson glow line
        L.polyline([cor.from, cor.to], {
          color: '#c51944',
          weight: 4,
          opacity: 0.4
        }).addTo(tuMap).bindTooltip(cor.title, { sticky: true });

        // Glowing gold dashed polyline
        const dashed = L.polyline([cor.from, cor.to], {
          color: '#ffc72c',
          weight: 2.2,
          dashArray: '6, 8',
          opacity: 0.9
        }).addTo(tuMap);
        corridorLines.push(dashed);
      });

      // Add Custom DivIcon Markers for the 4 physical campuses
      for (let i = 0; i < 4; i++) {
        const c = CAMPUSES_DATA[i];
        const customIcon = L.divIcon({
          className: 'tu-leaflet-custom-icon',
          html: `
            <div class="tu-gis-marker ${i === 0 ? 'active' : ''}" id="tuMarker_${i}">
              <div class="tu-marker-pulse"></div>
              <div class="tu-marker-core">
                <i class="fa-solid fa-graduation-cap"></i>
              </div>
              <div class="tu-marker-tag">
                <span class="tag-name">${c.shortName}</span>
                <span class="tag-area">${c.area}</span>
              </div>
            </div>
          `,
          iconSize: [120, 60],
          iconAnchor: [60, 48]
        });

        const popupHtml = `
          <div class="tu-gis-popup">
            <div class="tu-gis-popup-header">
              <h4>${c.name}</h4>
              <span class="tu-gis-popup-badge">${c.badge}</span>
            </div>
            <div class="tu-gis-popup-grid">
              <div class="tu-gis-popup-stat">
                <span class="k">พื้นที่</span>
                <span class="v">${c.area}</span>
              </div>
              <div class="tu-gis-popup-stat">
                <span class="k">ประชากร</span>
                <span class="v">${c.students}</span>
              </div>
              <div class="tu-gis-popup-stat" style="grid-column: span 2;">
                <span class="k">อัตลักษณ์ยุทธศาสตร์</span>
                <span class="v" style="color: var(--tu-gold);">${c.role}</span>
              </div>
              <div class="tu-gis-popup-stat" style="grid-column: span 2;">
                <span class="k">ที่ตั้งทางภูมิศาสตร์</span>
                <span class="v" style="font-size: 0.72rem; color: #cbd5e1;">${c.location}</span>
              </div>
            </div>
            <div class="tu-gis-popup-coord">
              <i class="fa-solid fa-satellite"></i> GPS: ${c.lat.toFixed(4)}° N, ${c.lng.toFixed(4)}° E
            </div>
          </div>
        `;

        const marker = L.marker([c.lat, c.lng], { icon: customIcon }).addTo(tuMap);
        marker.bindPopup(popupHtml, { offset: [0, -32] });

        marker.on('click', () => {
          selectCampusTab(i);
        });

        tuMarkers.push(marker);
      }

      // Initial focus on Tha Prachan
      setTimeout(() => {
        if (tuMarkers[0]) {
          tuMarkers[0].openPopup();
        }
      }, 500);

      // Invalidate size when campus section intersects viewport
      if ('IntersectionObserver' in window) {
        const obs = new IntersectionObserver((entries) => {
          entries.forEach(ent => {
            if (ent.isIntersecting && tuMap) {
              tuMap.invalidateSize();
            }
          });
        }, { threshold: 0.1 });
        const sec = document.getElementById('campuses');
        if (sec) obs.observe(sec);
      }
    }

    // Switch between GIS Dark, Satellite, and Street Map
    function switchMapStyle(style) {
      if (!tuMap) return;
      document.querySelectorAll('.map-style-btn').forEach(btn => btn.classList.remove('active'));

      if (window.tuMapDarkGroup && tuMap.hasLayer(window.tuMapDarkGroup)) tuMap.removeLayer(window.tuMapDarkGroup);
      if (window.tuMapSatLayer && tuMap.hasLayer(window.tuMapSatLayer)) tuMap.removeLayer(window.tuMapSatLayer);
      if (window.tuMapOsmLayer && tuMap.hasLayer(window.tuMapOsmLayer)) tuMap.removeLayer(window.tuMapOsmLayer);

      if (style === 'satellite') {
        if (window.tuMapSatLayer) window.tuMapSatLayer.addTo(tuMap);
        const btn = document.getElementById('btnMapSat');
        if (btn) btn.classList.add('active');
      } else if (style === 'street') {
        if (window.tuMapOsmLayer) window.tuMapOsmLayer.addTo(tuMap);
        const btn = document.getElementById('btnMapOsm');
        if (btn) btn.classList.add('active');
      } else {
        if (window.tuMapDarkGroup) window.tuMapDarkGroup.addTo(tuMap);
        const btn = document.getElementById('btnMapDark');
        if (btn) btn.classList.add('active');
      }

      if (tuMarkers) {
        tuMarkers.forEach(m => {
          if (m.bringToFront) m.bringToFront();
        });
      }
    }

    // 4. Campus Selector Tab
    function selectCampusTab(idx) {
      const btns = document.querySelectorAll('.cluster-select-btn');
      btns.forEach((b, i) => b.classList.toggle('active', i === idx));

      const data = CAMPUSES_DATA[idx];
      document.getElementById('cArea').textContent = data.area;
      document.getElementById('cStudents').textContent = data.students;
      document.getElementById('cRole').textContent = data.role;
      document.getElementById('cFocus').textContent = data.focus;
      const locEl = document.getElementById('cLocation');
      if (locEl) locEl.textContent = data.location;

      const gpsEl = document.getElementById('currentGpsDisplay');
      if (gpsEl) {
        gpsEl.innerHTML = `<i class="fa-solid fa-satellite"></i> ${data.lat.toFixed(4)}° N, ${data.lng.toFixed(4)}° E`;
      }

      // Toggle active state on HTML markers
      document.querySelectorAll('.tu-gis-marker').forEach((el, i) => {
        el.classList.toggle('active', i === idx);
      });

      if (tuMap) {
        tuMap.invalidateSize();
        if (idx === 4) {
          // Fit all 4 campuses in view (National overview)
          const bounds = L.latLngBounds([
            [12.8, 99.3],
            [18.4, 101.1]
          ]);
          tuMap.flyToBounds(bounds, { padding: [50, 50], duration: 1.5 });
          tuMap.closePopup();
        } else {
          tuMap.flyTo([data.lat, data.lng], data.zoom, { duration: 1.4, easeLinearity: 0.25 });
          if (tuMarkers[idx]) {
            setTimeout(() => {
              tuMarkers[idx].openPopup();
            }, 600);
          }
        }
      }
    }

    // 5. Milestone Step Selector
    function setMilestoneStep(idx) {
      const nodes = document.querySelectorAll('.stepper-node');
      nodes.forEach((n, i) => n.classList.toggle('active', i === idx));

      const item = MILESTONES_DATA[idx];
      document.getElementById('mEventTitle').textContent = item.title;
      document.getElementById('mEventDesc').textContent = item.desc;
      document.getElementById('mEventStat').textContent = item.stat;
      document.getElementById('mEventLabel').textContent = item.lbl;
    }

    // 6. Circuit Milestone Selector
    function selectCircuitNode(idx) {
      const nodes = document.querySelectorAll('.circuit-milestone-node');
      nodes.forEach((n, i) => n.classList.toggle('active', i === idx));

      const c = CIRCUIT_DATA[idx];
      document.getElementById('cInsightTag').textContent = c.tag;
      document.getElementById('cInsightTitle').textContent = c.title;
      document.getElementById('cInsightDesc').textContent = c.desc;
      document.getElementById('cStat1').textContent = c.stat1;
      document.getElementById('cStatLbl1').textContent = c.lbl1;
      document.getElementById('cStat2').textContent = c.stat2;
      document.getElementById('cStatLbl2').textContent = c.lbl2;

      // Update active SVG stroke
      const activePath = document.getElementById('circuitActivePath');
      if (activePath) {
        const segments = [
          "M 120 180 C 130 90, 220 80, 280 140",
          "M 120 180 C 130 90, 220 80, 280 140 C 340 180, 480 120, 560 160",
          "M 120 180 C 130 90, 220 80, 280 140 C 340 180, 480 120, 560 160 C 620 200, 600 290, 540 340",
          "M 120 180 C 130 90, 220 80, 280 140 C 340 180, 480 120, 560 160 C 620 200, 600 290, 540 340 C 470 390, 360 410, 300 370 Z"
        ];
        activePath.setAttribute('d', segments[idx] || segments[0]);
      }
    }

    // 7. Budget Stream Drilldown
    const STREAMS_DATA = [
      { name: "งบประมาณแผ่นดิน", share: "35.8%", amount: "5,495 ล้านบาท", desc: "เงินอุดหนุนทั่วไปและโครงการพัฒนาเชิงยุทธศาสตร์ระดับชาติเพื่อความเป็นเลิศทางวิชาการ" },
      { name: "ค่าธรรมเนียมการศึกษา", share: "32.4%", amount: "4,973 ล้านบาท", desc: "รายได้จากหลักสูตรปกติ หลักสูตรพิเศษ และหลักสูตรนานาชาติคุณภาพสูง" },
      { name: "ทรัพย์สินและการลงทุน", share: "18.2%", amount: "2,793 ล้านบาท", desc: "การบริหารจัดการอสังหาริมทรัพย์ พื้นที่พาณิชย์ และกองทุนพัฒนามหาวิทยาลัย" },
      { name: "ทุนวิจัยและบริการวิชาการ", share: "8.6%", amount: "1,320 ล้านบาท", desc: "ทุนวิจัยจากภาคเอกชน รัฐวิสาหกิจ และองค์กรวิจัยระดับนานาชาติ" },
      { name: "บริการทางการแพทย์และคลินิก", share: "5.0%", amount: "769 ล้านบาท", desc: "การให้บริการรักษาพยาบาล คลินิกทันตกรรม และศูนย์ตรวจสุขภาพเฉพาะทาง" }
    ];

    function drilldownStream(idx) {
      const pills = document.querySelectorAll('.drilldown-pill');
      pills.forEach((p, i) => p.classList.toggle('active', i === idx));

      const s = STREAMS_DATA[idx];
      document.getElementById('streamDetailBox').innerHTML = `
        <strong>${s.name} (${s.share} • ${s.amount}):</strong> ${s.desc}
      `;
    }

    // 8. Faculties Rendering, Interactive Visualizer & Modal
    let facultiesTcasChart = null;
    window.currentFacultyFilter = 'all';

    function initFacultiesTcasChart() {
      const ctx = document.getElementById('facultiesTcasChartCanvas');
      if (!ctx) return;

      const currentPillar = window.currentFacultyFilter || 'all';
      const list = currentPillar === 'all' 
        ? [...FACULTIES_DATA].sort((a, b) => parseFloat(b.cutoff) - parseFloat(a.cutoff))
        : [...FACULTIES_DATA].filter(f => f.pillar === currentPillar).sort((a, b) => parseFloat(b.cutoff) - parseFloat(a.cutoff));

      const labels = list.map(f => f.name);
      const data = list.map(f => parseFloat(f.cutoff));
      const colors = list.map(f => {
        if (f.pillar === 'med') return '#c51944';
        if (f.pillar === 'sci') return '#00857c';
        if (f.pillar === 'inter') return '#d97706';
        return '#1e3a8a';
      });

      if (facultiesTcasChart) {
        facultiesTcasChart.data.labels = labels;
        facultiesTcasChart.data.datasets[0].data = data;
        facultiesTcasChart.data.datasets[0].backgroundColor = colors;
        facultiesTcasChart.update();
        return;
      }

      facultiesTcasChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'คะแนนตัดต่ำสุด TCAS (รอบ 3 Admission)',
            data: data,
            backgroundColor: colors,
            borderRadius: 4,
            barThickness: 13,
            maxBarThickness: 15
          }]
        },
        options: {
          indexAxis: 'y',
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: 'rgba(11, 22, 59, 0.96)',
              titleFont: { size: 13, weight: 'bold' },
              bodyFont: { size: 12 },
              padding: 12,
              borderColor: 'rgba(255, 199, 44, 0.4)',
              borderWidth: 1,
              callbacks: {
                title: (items) => list[items[0].dataIndex].name,
                label: (item) => {
                  const fac = list[item.dataIndex];
                  return [
                    `คะแนนตัดต่ำสุด TCAS: ${fac.cutoff} / 100`,
                    `กลุ่มสาขา: ${fac.pillarName}`,
                    `อัตราการแข่งขัน: ${fac.accept}`,
                    `สายอาชีพ: ${fac.careers.substring(0, 42)}...`
                  ];
                },
                afterLabel: () => '👉 คลิกแท่งกราฟเพื่อดูรายละเอียดฉบับเต็ม'
              }
            }
          },
          onClick: (evt, elements) => {
            if (elements && elements.length > 0) {
              const idx = elements[0].index;
              openFacultyModal(list[idx]);
            }
          },
          scales: {
            x: {
              min: 60,
              max: 86,
              ticks: {
                stepSize: 5,
                callback: (v) => v + ' คะแนน',
                color: '#64748b'
              },
              grid: { color: 'rgba(0, 0, 0, 0.06)' }
            },
            y: {
              ticks: {
                color: '#1e293b',
                font: { size: 11, weight: '600' }
              },
              grid: { display: false }
            }
          }
        }
      });
    }

    function setFacultiesView(mode) {
      const btnChart = document.getElementById('btnFacChartView');
      const btnGrid = document.getElementById('btnFacGridView');
      const chartWrapper = document.getElementById('facultiesChartWrapper');
      const gridWrapper = document.getElementById('facultiesGrid');

      if (mode === 'chart') {
        if (btnChart) btnChart.classList.add('active');
        if (btnGrid) btnGrid.classList.remove('active');
        if (chartWrapper) chartWrapper.style.display = 'block';
        if (gridWrapper) gridWrapper.style.display = 'none';
        if (facultiesTcasChart) facultiesTcasChart.resize();
      } else {
        if (btnChart) btnChart.classList.remove('active');
        if (btnGrid) btnGrid.classList.add('active');
        if (chartWrapper) chartWrapper.style.display = 'none';
        if (gridWrapper) gridWrapper.style.display = 'grid';
      }
    }

    function renderFaculties(filter) {
      const container = document.getElementById('facultiesGrid');
      if (!container) return;
      container.innerHTML = '';
      const list = filter === 'all' ? FACULTIES_DATA : FACULTIES_DATA.filter(f => f.pillar === filter);
      list.forEach((fac, idx) => {
        const card = document.createElement('div');
        card.className = 'faculty-item-card';
        card.onclick = () => openFacultyModal(fac);
        card.innerHTML = `
          <div class="fac-name">${fac.name}</div>
          <div class="fac-meta">
            <span>${fac.pillarName}</span>
            <span style="color: var(--bidwells-crimson); font-weight: 700;">TCAS: ${fac.cutoff}</span>
          </div>
        `;
        container.appendChild(card);
      });
    }

    function filterFaculties(pillar, btnEl) {
      window.currentFacultyFilter = pillar;
      const pills = document.querySelectorAll('.fac-pill');
      pills.forEach(p => p.classList.remove('active'));
      const activeBtn = btnEl || (typeof event !== 'undefined' && event && event.target ? event.target.closest('.fac-pill') : null) || document.querySelector(`.fac-pill[onclick*="'${pillar}'"]`);
      if (activeBtn) activeBtn.classList.add('active');
      renderFaculties(pillar);
      initFacultiesTcasChart();
    }

    function openFacultyModal(fac) {
      document.getElementById('mFacPillar').textContent = fac.pillarName;
      document.getElementById('mFacTitle').textContent = fac.name;
      document.getElementById('mFacDesc').textContent = fac.desc;
      document.getElementById('mFacCutoff').textContent = fac.cutoff + ' / 100';
      document.getElementById('mFacAccept').textContent = fac.accept;
      document.getElementById('mFacCareers').textContent = fac.careers;
      document.getElementById('facultyModal').style.display = 'flex';
    }

    function closeFacultyModal() {
      document.getElementById('facultyModal').style.display = 'none';
    }

    function openDownloadModal() {
      document.getElementById('downloadModal').style.display = 'flex';
    }

    function closeDownloadModal() {
      document.getElementById('downloadModal').style.display = 'none';
    }

    function handleDownloadSubmit(e) {
      e.preventDefault();
      if (typeof confetti === 'function') {
        confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
      }
      openDownloadModal();
    }

    // 8.5 Flourish 10-Scene Data Storytelling Hub
    const FLOURISH_SCENES_DATA = [
      {
        id: 1,
        title: "1. ภาพรวมพัฒนาการ 90 ปี ธรรมศาสตร์",
        template: "Line Chart Race / Story Timeline",
        category: "Historical Overview",
        csv: "01_thammasat_historical_timeline.csv",
        badge: "พ.ศ. 2477 - 2567",
        desc: "ลำดับเส้นเวลาการก่อตั้งและวิวัฒนาการ 90 ปีแห่งประวัติศาสตร์ มหาวิทยาลัยวิชาธรรมศาสตร์และการเมืองสู่มหาวิทยาลัยวิจัยระดับสากล",
        highlights: [
          "พ.ศ. 2477: สถาปนามหาวิทยาลัยวิชาธรรมศาสตร์และการเมือง (มธก.) โดย ศ.ดร.ปรีดี พนมยงค์ มีนักศึกษารุ่นแรก 7,094 คน",
          "พ.ศ. 2529: ขยายวิทยาเขตแรกสู่ปริมณฑล ณ ศูนย์รังสิต เพื่อรองรับสายวิทยาศาสตร์และเทคโนโลยี",
          "พ.ศ. 2567: ก้าวสู่ 90 ปี มหาวิทยาลัยระดับโลกเพื่อประชาชนและเป้าหมาย TU 2034"
        ],
        tableHeaders: ["Year_BE", "Era", "Milestone_TH", "Students", "Budget_MB"],
        tableSample: [
          ["2477", "สถาปนามหาวิทยาลัย", "ศาสตราจารย์ ดร.ปรีดี พนมยงค์ ก่อตั้ง มธก.", "7,094", "0.5"],
          ["2529", "เปิดศูนย์รังสิต", "ขยายวิทยาเขตแรกสู่ปริมณฑลด้านวิทยาศาสตร์", "18,450", "840"],
          ["2567", "90 ปี สู่สากล", "มหาวิทยาลัยแห่งความยั่งยืน TU 2034", "42,850", "15,350"]
        ]
      },
      {
        id: 2,
        title: "2. การย้ายศูนย์กลางประชากร 4 วิทยาเขต",
        template: "Flourish Bump / Area Chart",
        category: "Campus Transition",
        csv: "02_campus_population_shift.csv",
        badge: "100% ท่าพระจันทร์ ➔ 73.5% รังสิต",
        desc: "การเปลี่ยนแปลงสัดส่วนนักศึกษาใน 4 ศูนย์การศึกษาหลัก (ท่าพระจันทร์, รังสิต, พัทยา, ลำปาง) ตั้งแต่ พ.ศ. 2500 ถึงปัจจุบัน",
        highlights: [
          "ท่าพระจันทร์จากเดิมรองรับ 100% ปัจจุบันปรับบทบาทเป็น Hub บัณฑิตศึกษาและนานาชาติ (14.8%)",
          "ศูนย์รังสิตกลายเป็น Main Campus รองรับนักศึกษาถึง 73.5% พร้อมศูนย์การแพทย์และวิจัยครบวงจร",
          "ศูนย์ลำปาง (7.2%) และศูนย์พัทยา (4.5%) ขยายพลังวิชาการสู่ภาคเหนือและเขตเศรษฐกิจพิเศษ EEC"
        ],
        tableHeaders: ["Era_BE", "ThaPrachan_Pct", "Rangsit_Pct", "Lampang_Pct", "Pattaya_Pct"],
        tableSample: [
          ["2500", "100.0%", "0.0%", "0.0%", "0.0%"],
          ["2530", "68.0%", "32.0%", "0.0%", "0.0%"],
          ["2567", "14.8%", "73.5%", "7.2%", "4.5%"]
        ]
      },
      {
        id: 3,
        title: "3. การแข่งขัน TCAS 26 คณะ & คะแนนตัดต่ำสุด",
        template: "Flourish Interactive Scatter / Bar Chart",
        category: "Academic Admissions",
        csv: "03_faculties_tcas_competition.csv",
        badge: "26 คณะ / แพทย์ 83.1",
        desc: "คะแนนเฉลี่ยตัดต่ำสุดในการรับสมัคร TCAS รอบ 3 และอัตราการแข่งขันในทุก 26 คณะ/สถาบัน ครอบคลุม 4 เสาหลักวิชาการ",
        highlights: [
          "กลุ่มวิทยาศาสตร์สุขภาพและการแพทย์แข่งขันสูงสุด อัตราส่วน 1:14.0 (แพทย์ 83.1, ทันตแพทย์ 82.4)",
          "พาณิชย์ฯ & นิติศาสตร์ ครองคะแนนสูงสุดในกลุ่มสังคมศาสตร์ (81.2 และ 78.5 ตามลำดับ)",
          "วิศวกรรมศาสตร์ & วิทยาลัยนานาชาติปรีดี พนมยงค์ โดดเด่นด้านคะแนนและเครือข่ายสากล"
        ],
        tableHeaders: ["Faculty", "Pillar", "Min_Score_100", "Accept_Ratio", "Capacity"],
        tableSample: [
          ["แพทยศาสตร์", "วิทยาศาสตร์สุขภาพ", "83.1", "1:14.0", "220"],
          ["ทันตแพทยศาสตร์", "วิทยาศาสตร์สุขภาพ", "82.4", "1:12.5", "100"],
          ["พาณิชยศาสตร์และการบัญชี", "สังคมศาสตร์และมนุษยศาสตร์", "81.2", "1:9.4", "950"]
        ]
      },
      {
        id: 4,
        title: "4. ความหลากหลายทางเพศภาวะใน 4 เสาหลักวิชาการ",
        template: "Flourish Sliced / Stacked Percentage Bar",
        category: "Diversity & Demographics",
        csv: "04_gender_diversity_distribution.csv",
        badge: "สัดส่วนหญิง-ชาย & ความหลากหลาย",
        desc: "โครงสร้างความหลากหลายทางเพศของนักศึกษาในแต่ละกลุ่มสาขาวิชา สะท้อนสังคมแห่งความเท่าเทียมและการเปิดกว้าง",
        highlights: [
          "วิทยาศาสตร์สุขภาพและการแพทย์: สัดส่วนนักศึกษาหญิง 71.5% และนักศึกษาชาย 28.5%",
          "สังคมศาสตร์และมนุษยศาสตร์: สัดส่วนนักศึกษาหญิง 64.2% และนักศึกษาชาย 35.8%",
          "วิทยาศาสตร์และเทคโนโลยี: สัดส่วนสมดุล มีนักศึกษาหญิง 53.8% สะท้อนการเติบโตของผู้หญิงในสาย STEM"
        ],
        tableHeaders: ["Academic_Pillar", "Female_Pct", "Male_Pct", "Total_Students"],
        tableSample: [
          ["สังคมศาสตร์และมนุษยศาสตร์", "64.2%", "35.8%", "19,200"],
          ["วิทยาศาสตร์และเทคโนโลยี", "53.8%", "46.2%", "11,450"],
          ["วิทยาศาสตร์สุขภาพและการแพทย์", "71.5%", "28.5%", "7,800"],
          ["สถาบันและวิทยาลัยนานาชาติ", "59.8%", "40.2%", "4,400"]
        ]
      },
      {
        id: 5,
        title: "5. โครงสร้างงบประมาณ 15,350 ล้านบาท",
        template: "Flourish Sankey Diagram / Sunburst",
        category: "Financial Architecture",
        csv: "05_budget_revenue_streams.csv",
        badge: "15,350 ล้านบาท",
        desc: "แผนผังการไหลของกระแสน้ำรายได้ 5 ช่องทางหลักของมหาวิทยาลัย สู่การจัดสรรงบประมาณพัฒนาด้านต่างๆ",
        highlights: [
          "งบประมาณแผ่นดิน: 5,495 ล้านบาท (35.8%) รองรับภารกิจหลักและการวิจัยระดับชาติ",
          "ค่าธรรมเนียมการศึกษา: 4,973 ล้านบาท (32.4%) หมุนเวียนเพื่อการสอนและพัฒนาหลักสูตร",
          "รายได้บริหารทรัพย์สินและการลงทุน: 2,793 ล้านบาท (18.2%) สร้างความยั่งยืนทางการคลัง"
        ],
        tableHeaders: ["Stream_Name", "Amount_MB", "Percentage", "Strategic_Purpose"],
        tableSample: [
          ["งบประมาณแผ่นดิน", "5,495", "35.8%", "เงินอุดหนุนและโครงการวิจัยชาติ"],
          ["ค่าธรรมเนียมการศึกษา", "4,973", "32.4%", "การจัดการเรียนการสอน"],
          ["ทรัพย์สินและการลงทุน", "2,793", "18.2%", "สำนักงานบริหารทรัพย์สิน TU"]
        ]
      },
      {
        id: 6,
        title: "6. แนวโน้มงบประมาณย้อนหลัง 5 ปี (2563-2567)",
        template: "Flourish Projection Area / Trend Chart",
        category: "Budget Growth",
        csv: "06_budget_trend_5years.csv",
        badge: "เติบโตเฉลี่ย +3.4% ต่อปี",
        desc: "เส้นทางงบประมาณรวม 5 ปี สะท้อนการขยายตัวทางการเงินและความมั่นคงของมหาวิทยาลัยท่ามกลางความท้าทาย",
        highlights: [
          "ปี 2563: 13,420 ล้านบาท บริหารจัดการในภาวะวิกฤตสุขภาพระดับโลก",
          "ปี 2565: ปรับฐานสู่ 14,210 ล้านบาท เร่งการลงทุนเทคโนโลยีดิจิทัล",
          "ปี 2567: ทำสถิติสูงสุด 15,350 ล้านบาท มุ่งเน้น TU 2034 และ Net Zero"
        ],
        tableHeaders: ["Year_BE", "Total_Budget_MB", "Gov_Subsidy_MB", "Autonomous_Revenue_MB"],
        tableSample: [
          ["2563", "13,420", "4,950", "8,470"],
          ["2565", "14,210", "5,180", "9,030"],
          ["2567", "15,350", "5,495", "9,855"]
        ]
      },
      {
        id: 7,
        title: "7. พิกัดภูมิศาสตร์และโครงสร้างพื้นฐาน 4 ศูนย์การศึกษา",
        template: "Flourish Marker Map / Geographic Explorer",
        category: "Campus GIS",
        csv: "07_campuses_geography_metrics.csv",
        badge: "ท่าพระจันทร์ • รังสิต • ลำปาง • พัทยา",
        desc: "ข้อมูลเชิงพื้นที่และบทบาทเชิงยุทธศาสตร์ ขนาดพื้นที่ จำนวนประชากร และความเชี่ยวชาญเฉพาะทาง",
        highlights: [
          "ศูนย์รังสิต (ปทุมธานี): 1,757 ไร่ ศูนย์นวัตกรรม โรงพยาบาลธรรมศาสตร์ และอุทยานวิทยาศาสตร์",
          "ท่าพระจันทร์ (กทม.): 104 ไร่ หัวใจประวัติศาสตร์และอัตลักษณ์ประชาธิปไตยริมฝั่งเจ้าพระยา",
          "ศูนย์ลำปาง (364 ไร่) & ศูนย์พัทยา (566 ไร่): เชื่อมโยงล้านนาสร้างสรรค์และเขตเศรษฐกิจตะวันออก EEC"
        ],
        tableHeaders: ["Campus_Name", "Province", "Area_Rai", "Latitude", "Longitude", "Role"],
        tableSample: [
          ["ท่าพระจันทร์", "กรุงเทพมหานคร", "104", "13.7557", "100.4907", "ประวัติศาสตร์และหลักสูตรนานาชาติ"],
          ["ศูนย์รังสิต", "ปทุมธานี", "1,757", "14.0722", "100.6015", "ศูนย์วิจัย วิทยาศาสตร์ และสาธารณสุข"],
          ["ศูนย์ลำปาง", "ลำปาง", "364", "18.3171", "99.3986", "พัฒนาท้องถิ่นและล้านนาสร้างสรรค์"],
          ["ศูนย์พัทยา", "ชลบุรี", "566", "12.9275", "100.9925", "EEC ดิจิทัลและยานยนต์แห่งอนาคต"]
        ]
      },
      {
        id: 8,
        title: "8. ตัวชี้วัดเป้าหมายยุทธศาสตร์ TU 2034",
        template: "Flourish Radar / Spider Chart",
        category: "Strategic Vision",
        csv: "08_tu2034_strategic_kpis.csv",
        badge: "Vision 2034: 4 แกนขับเคลื่อน",
        desc: "ดัชนีชี้วัดผลสัมฤทธิ์ตามแผนยุทธศาสตร์ 10 ปี มุ่งสู่ Top 100 QS World University Ranking",
        highlights: [
          "ความเป็นเลิศทางวิจัย (Research Excellence): เป้าหมาย 92.0 คะแนน เน้นผลงานเชิงประจักษ์",
          "ทักษะศตวรรษที่ 21 (Future-Ready Skills): ปฏิรูปหลักสูตรและทักษะดิจิทัลเป้าหมาย 95.0 คะแนน",
          "ความยั่งยืนและสุขภาพ (Green & Health): Net Zero ภายในปี 2034 และเครือข่ายสุขภาวะ 98.0 คะแนน"
        ],
        tableHeaders: ["Strategic_Dimension", "Current_2567", "Target_2577", "Weight_Pct"],
        tableSample: [
          ["Research & Innovation", "72.4", "92.0", "30%"],
          ["Future Skills & Pedagogy", "78.5", "95.0", "25%"],
          ["Green Campus & Net Zero", "81.0", "96.0", "25%"],
          ["Health & Well-being", "84.2", "98.0", "20%"]
        ]
      },
      {
        id: 9,
        title: "9. อัตราความสำเร็จและการมีงานทำของบัณฑิต",
        template: "Flourish Hierarchy / Treemap",
        category: "Graduate Employability",
        csv: "09_graduate_employment_outcomes.csv",
        badge: "92.4% มีงานทำใน 6 เดือน",
        desc: "การกระจายตัวของบัณฑิตธรรมศาสตร์ในตลาดแรงงาน รายได้เฉลี่ยเริ่มต้น และการเป็นผู้ประกอบการสตาร์ทอัพ",
        highlights: [
          "บัณฑิตมีงานทำหรือศึกษาต่อภายใน 6 เดือน สูงถึง 92.4%",
          "ภาคเอกชนและบรรษัทข้ามชาติเป็นปลายทางอันดับ 1 (58.4%) เงินเดือนเริ่มต้นเฉลี่ย 29,500 บาท",
          "กลุ่มสตาร์ทอัพและธุรกิจส่วนตัวเติบโตสูงสุด +11.4% ต่อปี ด้วยรายได้เฉลี่ย 34,000 บาท"
        ],
        tableHeaders: ["Sector", "Employment_Pct", "Avg_Starting_Salary_THB", "Growth_Rate"],
        tableSample: [
          ["ธุรกิจเอกชนและบรรษัทข้ามชาติ", "58.4%", "29,500", "+5.2%"],
          ["หน่วยงานภาครัฐและรัฐวิสาหกิจ", "18.2%", "22,000", "+3.0%"],
          ["สตาร์ทอัพและธุรกิจส่วนตัว", "14.6%", "34,000", "+11.4%"],
          ["องค์กรระหว่างประเทศ / NGO", "8.8%", "38,500", "+7.8%"]
        ]
      },
      {
        id: 10,
        title: "10. ผลงานวิจัยระดับนานาชาติและเครือข่ายความร่วมมือสากล",
        template: "Flourish Network / Chord Diagram",
        category: "Global Research",
        csv: "10_research_global_citations.csv",
        badge: "Scopus 2,400+ papers/year",
        desc: "เครือข่ายความร่วมมือทางวิชาการและดัชนีการอ้างอิงงานวิจัย (Citations) ร่วมกับมหาวิทยาลัยชั้นนำทั่วโลก",
        highlights: [
          "ผลงานวิจัยได้รับการตีพิมพ์ในฐานข้อมูล Scopus/WoS กว่า 2,400 บทความต่อปี",
          "เครือข่ายความร่วมมือวิจัยครอบคลุมกว่า 350 มหาวิทยาลัยชั้นนำทั่วโลกในเอเชีย ยุโรป และอเมริกาเหนือ",
          "ดัชนี Citation Impact เฉลี่ย 1.82 สะท้อนคุณภาพและคุณค่าเชิงวิชาการในเวทีสากล"
        ],
        tableHeaders: ["Region_Partner", "Collaborative_Papers", "Citation_Impact", "Top_Fields"],
        tableSample: [
          ["East Asia & ASEAN", "840", "1.65", "Medicine, AI, Logistics"],
          ["Europe & UK", "620", "1.82", "Public Policy, Law, Renewable Energy"],
          ["North America", "490", "2.10", "Biotech, Materials, Data Science"],
          ["Australasia", "310", "1.74", "Health Sciences, Environmental Tech"]
        ]
      }
    ];

    function openFlourishHubModal() {
      const modal = document.getElementById('flourishHubModal');
      if (modal) {
        modal.style.display = 'flex';
        renderFlourishTabs();
        selectFlourishScene(0);
      }
    }

    function closeFlourishHubModal() {
      const modal = document.getElementById('flourishHubModal');
      if (modal) {
        modal.style.display = 'none';
      }
    }

    function renderFlourishTabs() {
      const tabList = document.getElementById('flourishSidebarTabs');
      if (!tabList) return;
      tabList.innerHTML = '';
      FLOURISH_SCENES_DATA.forEach((scene, idx) => {
        const btn = document.createElement('button');
        btn.className = `flourish-tab-btn ${idx === 0 ? 'active' : ''}`;
        btn.onclick = () => selectFlourishScene(idx);
        btn.innerHTML = `
          <div class="flourish-tab-num">ฉากที่ ${scene.id}</div>
          <div class="flourish-tab-title">${scene.title.split('. ')[1] || scene.title}</div>
          <div class="flourish-tab-template">${scene.template}</div>
        `;
        tabList.appendChild(btn);
      });
    }

    function selectFlourishScene(idx) {
      const tabs = document.querySelectorAll('.flourish-tab-btn');
      tabs.forEach((t, i) => t.classList.toggle('active', i === idx));

      const s = FLOURISH_SCENES_DATA[idx];
      if (!s) return;

      const content = document.getElementById('flourishDetailPane');
      if (!content) return;

      const tableHeaderHtml = s.tableHeaders.map(h => `<th>${h}</th>`).join('');
      const tableRowsHtml = s.tableSample.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('');
      const highlightsHtml = s.highlights.map(h => `<li><i class="fa-solid fa-check-circle" style="color: var(--bidwells-crimson); margin-right: 6px;"></i>${h}</li>`).join('');

      content.innerHTML = `
        <div class="flourish-detail-badge">${s.category} • ${s.badge}</div>
        <h3 class="flourish-detail-title">${s.title}</h3>
        <p class="flourish-detail-desc">${s.desc}</p>
        
        <div class="flourish-preview-box">
          <div class="flourish-preview-header">
            <div style="font-weight: 700; color: #1e293b; font-size: 0.95rem;">
              <i class="fa-solid fa-chart-line" style="color: var(--bidwells-crimson); margin-right: 8px;"></i>
              Flourish Visualization Preview (${s.template})
            </div>
            <a href="https://flourish.studio" target="_blank" class="flourish-direct-link">
              เปิดใน Flourish Studio <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </a>
          </div>
          <div class="flourish-preview-body">
            <div class="flourish-preview-info">
              <div><strong>ชุดข้อมูล CSV อ้างอิง:</strong> <code>flourish_data/${s.csv}</code> (พร้อมเชื่อมต่อใน Colab และ Flourish ทันที)</div>
              <div style="margin-top: 6px;"><strong>ไฮไลท์และข้อค้นพบสำคัญ:</strong></div>
              <ul style="margin: 6px 0 0 16px; padding: 0; line-height: 1.8;">
                ${highlightsHtml}
              </ul>
            </div>
            <div style="overflow-x: auto; margin-top: 14px;">
              <table class="flourish-data-table">
                <thead><tr>${tableHeaderHtml}</tr></thead>
                <tbody>${tableRowsHtml}</tbody>
              </table>
            </div>
          </div>
        </div>
      `;
    }

    // 9. TU 2034 Strategy Cockpit Real-time Calculator
    function updateCockpit() {
      const r = parseFloat(document.getElementById('sliderResearch').value);
      const s = parseFloat(document.getElementById('sliderSkills').value);
      const g = parseFloat(document.getElementById('sliderGreen').value);
      const h = parseFloat(document.getElementById('sliderHealth').value);

      document.getElementById('dispResearch').textContent = r + '%';
      document.getElementById('dispSkills').textContent = s + '%';
      document.getElementById('dispGreen').textContent = g + '%';
      document.getElementById('dispHealth').textContent = h + '%';

      const composite = (r * 0.3 + s * 0.25 + g * 0.25 + h * 0.2).toFixed(1);
      document.getElementById('cockpitCompositeScore').textContent = composite;
    }

    // 10. Chart.js Initializations
    let campusDistChart = null;

    function initCharts() {
      // Budget 5-Year Chart
      const ctxBudget = document.getElementById('budgetChartCanvas');
      if (ctxBudget) {
        new Chart(ctxBudget, {
          type: 'line',
          data: {
            labels: ['2563', '2564', '2565', '2566', '2567'],
            datasets: [{
              label: 'งบประมาณรวม (ล้านบาท)',
              data: [13420, 13850, 14210, 14780, 15350],
              borderColor: '#c51944',
              backgroundColor: 'rgba(197, 25, 68, 0.08)',
              borderWidth: 3,
              fill: true,
              tension: 0.35,
              pointBackgroundColor: '#c51944',
              pointRadius: 6,
              pointHoverRadius: 8
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: (ctx) => `${ctx.parsed.y.toLocaleString()} ล้านบาท`
                }
              }
            },
            scales: {
              y: {
                min: 12000,
                max: 16000,
                ticks: {
                  callback: (v) => v.toLocaleString() + ' ลบ.'
                },
                grid: { color: 'rgba(0, 0, 0, 0.05)' }
              },
              x: { grid: { display: false } }
            }
          }
        });
      }

      // Demographic Group Chart
      const ctxGender = document.getElementById('genderGroupChartCanvas');
      if (ctxGender) {
        new Chart(ctxGender, {
          type: 'bar',
          data: {
            labels: ['สังคมศาสตร์', 'วิทย์-เทคโนโลยี', 'วิทยาศาสตร์สุขภาพ', 'วิทยาลัยนานาชาติ'],
            datasets: [
              {
                label: 'หญิง (%)',
                data: [64.2, 53.8, 71.5, 59.8],
                backgroundColor: '#ec4899',
                borderRadius: 4,
                barThickness: 20,
                maxBarThickness: 24
              },
              {
                label: 'ชาย (%)',
                data: [35.8, 46.2, 28.5, 40.2],
                backgroundColor: '#3b82f6',
                borderRadius: 4,
                barThickness: 20,
                maxBarThickness: 24
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top' },
              tooltip: {
                callbacks: {
                  label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y}%`
                }
              }
            },
            scales: {
              y: {
                stacked: true,
                max: 100,
                ticks: { callback: (v) => v + '%' },
                grid: { color: 'rgba(0,0,0,0.05)' }
              },
              x: { stacked: true, grid: { display: false } }
            }
          }
        });
      }

      // Campus Multi-Era Distribution Chart
      const ctxDist = document.getElementById('campusDistributionCanvas');
      if (ctxDist) {
        campusDistChart = new Chart(ctxDist, {
          type: 'bar',
          data: {
            labels: ['พ.ศ. 2500', 'พ.ศ. 2530', 'พ.ศ. 2545', 'พ.ศ. 2567 (ปัจจุบัน)'],
            datasets: [
              {
                label: 'ท่าพระจันทร์ (%)',
                data: [100, 68, 22, 14.8],
                backgroundColor: '#a6d2e6',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              },
              {
                label: 'ศูนย์รังสิต (%)',
                data: [0, 32, 70, 73.5],
                backgroundColor: '#c51944',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              },
              {
                label: 'ศูนย์ลำปาง (%)',
                data: [0, 0, 5, 7.2],
                backgroundColor: '#ffc72c',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              },
              {
                label: 'ศูนย์พัทยา (%)',
                data: [0, 0, 3, 4.5],
                backgroundColor: '#00857c',
                barThickness: 28,
                maxBarThickness: 32,
                borderRadius: 4
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top', labels: { color: '#ffffff' } },
              tooltip: {
                callbacks: {
                  label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y}%`
                }
              }
            },
            scales: {
              x: { stacked: true, grid: { display: false }, ticks: { color: '#cbd5e1' } },
              y: { stacked: true, max: 100, ticks: { callback: (v) => v + '%', color: '#cbd5e1' }, grid: { color: 'rgba(255,255,255,0.08)' } }
            }
          }
        });
      }
    }

    function setDistributionEra(mode, btnEl) {
      const btns = document.querySelectorAll('.era-pill-btn');
      btns.forEach(b => b.classList.remove('active'));
      const activeBtn = btnEl || (typeof event !== 'undefined' && event && event.target ? event.target.closest('.era-pill-btn') : null) || document.querySelector(`.era-pill-btn[onclick*="'${mode}'"]`);
      if (activeBtn) activeBtn.classList.add('active');

      if (!campusDistChart) return;
      const thickness = mode === '2567' ? 36 : 28;
      campusDistChart.data.datasets.forEach(ds => {
        ds.barThickness = thickness;
        ds.maxBarThickness = thickness + 4;
      });
      if (mode === '2567') {
        campusDistChart.data.labels = ['พ.ศ. 2567 (ปัจจุบัน)'];
        campusDistChart.data.datasets[0].data = [14.8];
        campusDistChart.data.datasets[1].data = [73.5];
        campusDistChart.data.datasets[2].data = [7.2];
        campusDistChart.data.datasets[3].data = [4.5];
      } else {
        campusDistChart.data.labels = ['พ.ศ. 2500', 'พ.ศ. 2530', 'พ.ศ. 2545', 'พ.ศ. 2567 (ปัจจุบัน)'];
        campusDistChart.data.datasets[0].data = [100, 68, 22, 14.8];
        campusDistChart.data.datasets[1].data = [0, 32, 70, 73.5];
        campusDistChart.data.datasets[2].data = [0, 0, 5, 7.2];
        campusDistChart.data.datasets[3].data = [0, 0, 3, 4.5];
      }
      campusDistChart.update();
    }

    // Window Onload
    window.addEventListener('DOMContentLoaded', () => {
      initScrollInteractions();
      renderFaculties('all');
      initFacultiesTcasChart();
      initCharts();
      initTuLeafletMap();
    });
  </script>
</body>
</html>'''
    return html_code

def main():
    html = generate_bidwells_html()
    output_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully generated refined authentic Bidwells-style experience to {output_path}")

if __name__ == '__main__':
    main()
