import re

def apply_doorway_effect():
    # 1. Update index.html to add doorway-threshold
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    target_html = """    <!-- The Central Vertical Asphalt Racetrack -->
    <div class="central-track-stage">
      <!-- Alternating Checkerboard Curb on the left -->"""

    replace_html = """    <!-- The Central Vertical Asphalt Racetrack (Thammasat Centennial Archway) -->
    <div class="central-track-stage">
      <!-- Architectural Doorway Threshold Stone -->
      <div class="doorway-threshold"></div>

      <!-- Alternating Checkerboard Curb on the left -->"""

    if "class=\"doorway-threshold\"" not in html:
        if target_html in html:
            html = html.replace(target_html, replace_html)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print("Added doorway-threshold to index.html")
        else:
            print("Could not find target_html in index.html!")
    else:
        print("doorway-threshold already present in index.html")

    # 2. Update assets/css/editorial-refinement.css
    with open('assets/css/editorial-refinement.css', 'r', encoding='utf-8') as f:
        css = f.read()

    old_stage_css = """.central-track-stage {
  top: 14% !important;
  right: clamp(28px, 7.3vw, 112px) !important;
  left: auto !important;
  bottom: 7% !important;
  width: min(34vw, 460px) !important;
  min-width: 0 !important;
  height: auto !important;
  transform: none !important;
  border: 1px solid rgba(16,26,53,.08) !important;
  border-radius: 49% 49% 18px 18px;
  background: linear-gradient(160deg, #ecece7 0%, #f1e8e4 58%, #e8eaf0 100%) !important;
  box-shadow: none !important;
  opacity: 1;
  overflow: hidden;
}"""

    new_stage_css = """.central-track-stage {
  top: 13% !important;
  right: clamp(28px, 7.3vw, 112px) !important;
  left: auto !important;
  bottom: 6.5% !important;
  width: min(34vw, 460px) !important;
  min-width: 0 !important;
  height: auto !important;
  transform: none !important;
  border: 2px solid rgba(255, 255, 255, 0.95) !important;
  outline: 1px solid rgba(16, 26, 53, 0.12);
  border-radius: 49% 49% 18px 18px;
  background: radial-gradient(ellipse 85% 75% at 50% 36%, #ffffff 0%, #f4f3ec 50%, #e5e2d6 100%) !important;
  box-shadow: inset 0 32px 64px rgba(16, 26, 53, 0.13), inset 0 0 0 10px rgba(255, 255, 255, 0.65), inset 0 -16px 36px rgba(16, 26, 53, 0.08), 0 22px 55px rgba(16, 26, 53, 0.09) !important;
  opacity: 1;
  overflow: visible !important;
}

.doorway-threshold {
  position: absolute;
  bottom: -4px;
  left: 6%;
  width: 88%;
  height: 18px;
  background: linear-gradient(180deg, #ffffff 0%, #dedcd2 40%, #c4c1b3 100%);
  border-radius: 8px;
  border: 1px solid rgba(16, 26, 53, 0.15);
  border-top: 1.5px solid rgba(255, 255, 255, 0.95);
  box-shadow: 0 6px 16px rgba(16, 26, 53, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.85);
  z-index: 2;
  pointer-events: none;
}"""

    old_leader_css = """.tu-student-leader {
  top: auto !important;
  left: 50% !important;
  bottom: 2px !important;
  width: min(58%, 265px) !important;
  transform: translateX(-50%) !important;
  z-index: 2;
}
.tu-student-leader .tu-student-walker-img { filter: drop-shadow(0 16px 24px rgba(16,26,53,.13)); }
.tu-student-leader .tu-student-ground-shadow { opacity: .14; box-shadow: none; }
.tu-student-leader .tu-student-badge {
  background: rgba(255,255,255,.9);
  border: 1px solid rgba(16,26,53,.12);
  box-shadow: none;
  color: var(--edit-navy);
  font-size: .64rem;
  white-space: normal;
  text-align: center;
}"""

    new_leader_css = """.tu-student-leader {
  top: auto !important;
  left: 50% !important;
  bottom: -20px !important;
  width: min(58%, 270px) !important;
  transform: translateX(-50%) !important;
  z-index: 6 !important;
  animation: student-doorway-entrance 1.6s cubic-bezier(0.16, 1, 0.3, 1) forwards, student-stride-living 3.6s ease-in-out 1.6s infinite alternate;
}
.tu-student-leader .tu-student-walker-img {
  filter: drop-shadow(0 22px 36px rgba(16, 26, 53, 0.28)) drop-shadow(0 6px 14px rgba(189, 23, 62, 0.16)) !important;
  transform-origin: center bottom;
  will-change: transform, filter;
}
.tu-student-leader .tu-student-ground-shadow {
  position: absolute !important;
  bottom: -10px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: 200px !important;
  height: 32px !important;
  background: radial-gradient(ellipse at center, rgba(16, 26, 53, 0.44) 0%, rgba(16, 26, 53, 0.18) 50%, transparent 75%) !important;
  border-radius: 50% !important;
  filter: blur(5px) !important;
  opacity: 1 !important;
  box-shadow: none !important;
  z-index: 1 !important;
  animation: shadow-stride-living 3.6s ease-in-out 1.6s infinite alternate !important;
}
.tu-student-leader .tu-student-badge {
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(16, 26, 53, 0.14);
  box-shadow: 0 8px 22px rgba(16, 26, 53, 0.10);
  color: var(--edit-navy);
  font-size: .66rem;
  font-weight: 700;
  white-space: normal;
  text-align: center;
  z-index: 7;
}

@keyframes student-doorway-entrance {
  0% {
    transform: translateX(-50%) translateY(-38px) scale(0.84);
    opacity: 0;
    filter: brightness(0.88);
  }
  30% {
    opacity: 1;
  }
  75% {
    transform: translateX(-50%) translateY(3px) scale(1.02);
    filter: brightness(1.02);
  }
  100% {
    transform: translateX(-50%) translateY(0) scale(1);
    filter: brightness(1);
  }
}

@keyframes student-stride-living {
  0% {
    transform: translateX(-50%) translateY(0) scale(1);
  }
  50% {
    transform: translateX(-50%) translateY(-6px) scale(1.015);
  }
  100% {
    transform: translateX(-50%) translateY(0) scale(1);
  }
}

@keyframes shadow-stride-living {
  0% {
    transform: translateX(-50%) scale(1);
    opacity: 1;
  }
  50% {
    transform: translateX(-50%) scale(0.88);
    opacity: 0.72;
  }
  100% {
    transform: translateX(-50%) scale(1);
    opacity: 1;
  }
}"""

    # Check and replace stage css
    if old_stage_css in css:
        css = css.replace(old_stage_css, new_stage_css)
        print("Updated central-track-stage in editorial-refinement.css")
    else:
        old_stage_norm = old_stage_css.replace('\r\n', '\n')
        css_norm = css.replace('\r\n', '\n')
        if old_stage_norm in css_norm:
            css = css_norm.replace(old_stage_norm, new_stage_css)
            print("Updated central-track-stage (normalized) in editorial-refinement.css")
        else:
            print("Could not match old_stage_css!")

    # Check and replace leader css
    if old_leader_css in css:
        css = css.replace(old_leader_css, new_leader_css)
        print("Updated tu-student-leader in editorial-refinement.css")
    else:
        old_leader_norm = old_leader_css.replace('\r\n', '\n')
        css_norm = css.replace('\r\n', '\n')
        if old_leader_norm in css_norm:
            css = css_norm.replace(old_leader_norm, new_leader_css)
            print("Updated tu-student-leader (normalized) in editorial-refinement.css")
        else:
            print("Could not match old_leader_css!")

    # Update mobile media query if needed
    mobile_target = """.central-track-stage::after { font-size: 7.5rem; bottom: 8px; }
  .tu-student-leader { width: 155px !important; bottom: -4px !important; }"""
    
    mobile_replace = """.central-track-stage::after { font-size: 7.5rem; bottom: 8px; }
  .central-track-stage { overflow: visible !important; }
  .tu-student-leader { width: 160px !important; bottom: -12px !important; }
  .tu-student-leader .tu-student-ground-shadow { width: 135px !important; bottom: -6px !important; }"""

    if mobile_target in css:
        css = css.replace(mobile_target, mobile_replace)
        print("Updated mobile tu-student-leader in editorial-refinement.css")
    else:
        mobile_target_norm = mobile_target.replace('\r\n', '\n')
        css_norm = css.replace('\r\n', '\n')
        if mobile_target_norm in css_norm:
            css = css_norm.replace(mobile_target_norm, mobile_replace)
            print("Updated mobile tu-student-leader (normalized) in editorial-refinement.css")

    with open('assets/css/editorial-refinement.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Saved assets/css/editorial-refinement.css successfully.")

if __name__ == '__main__':
    apply_doorway_effect()
