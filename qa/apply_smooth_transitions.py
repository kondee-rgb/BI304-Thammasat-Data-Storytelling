import os, sys, re

def update_v8_overrides():
    path = r'assets/css/scroll-story-v8-overrides.css'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the crossfading styles
    old_crossfade = """/* Cross-type transition container */
.scroll-story-visual-content.is-crossfading {
  overflow: hidden;
  isolation: isolate;
  will-change: height;
  transition: height .48s cubic-bezier(.16, 1, .3, 1);
}
.scroll-story-visual-content .story-visual-out {
  animation: story-viz-out-down-v8 .44s cubic-bezier(.4, 0, .7, .2) both !important;
}
.scroll-story-visual-content .story-visual-in {
  animation: story-viz-in-down-v8 .72s cubic-bezier(.16, 1, .3, 1) both !important;
  will-change: opacity, transform, filter;
}
.scroll-story-visual-content[data-entry-direction="up"] .story-visual-out {
  animation-name: story-viz-out-up-v8 !important;
}
.scroll-story-visual-content[data-entry-direction="up"] .story-visual-in {
  animation-name: story-viz-in-up-v8 !important;
}

@keyframes story-viz-out-down-v8 {
  to { opacity: 0; transform: translate3d(0, -14px, 0) scale(.97); filter: blur(3px); }
}
@keyframes story-viz-in-down-v8 {
  0% { opacity: 0; transform: translate3d(14px, 20px, 0) scale(.96); filter: blur(4px); }
  65% { opacity: 1; transform: translate3d(-1px, -1px, 0) scale(1.004); filter: blur(0); }
  100% { opacity: 1; transform: translate3d(0, 0, 0) scale(1); filter: none; }
}
@keyframes story-viz-out-up-v8 {
  to { opacity: 0; transform: translate3d(0, 14px, 0) scale(.97); filter: blur(3px); }
}
@keyframes story-viz-in-up-v8 {
  0% { opacity: 0; transform: translate3d(-14px, -20px, 0) scale(.96); filter: blur(4px); }
  65% { opacity: 1; transform: translate3d(1px, 1px, 0) scale(1.004); filter: blur(0); }
  100% { opacity: 1; transform: translate3d(0, 0, 0) scale(1); filter: none; }
}"""

    new_crossfade = """/* Cross-type transition container: CSS Grid Single-Coordinate Space */
.scroll-story-visual-content.is-crossfading {
  display: grid !important;
  grid-template-areas: "stage-layer" !important;
  position: relative !important;
  overflow: hidden !important;
  isolation: isolate !important;
  will-change: height;
  transition: height .52s cubic-bezier(.16, 1, .3, 1) !important;
}
.scroll-story-visual-content .story-visual-layer {
  grid-area: stage-layer !important;
  width: 100% !important;
  align-self: start !important;
  justify-self: stretch !important;
}
.scroll-story-visual-content .story-visual-out {
  pointer-events: none !important;
  z-index: 1 !important;
  animation: story-viz-out-down-v8 .46s cubic-bezier(.4, 0, .7, .2) forwards !important;
}
.scroll-story-visual-content .story-visual-in {
  z-index: 2 !important;
  animation: story-viz-in-down-v8 .68s cubic-bezier(.16, 1, .3, 1) forwards !important;
  will-change: opacity, transform, filter !important;
}
.scroll-story-visual-content[data-entry-direction="up"] .story-visual-out {
  animation-name: story-viz-out-up-v8 !important;
}
.scroll-story-visual-content[data-entry-direction="up"] .story-visual-in {
  animation-name: story-viz-in-up-v8 !important;
}

@keyframes story-viz-out-down-v8 {
  0% { opacity: 1; transform: translate3d(0, 0, 0) scale(1); filter: blur(0); }
  100% { opacity: 0; transform: translate3d(0, -16px, 0) scale(.975); filter: blur(4px); }
}
@keyframes story-viz-in-down-v8 {
  0% { opacity: 0; transform: translate3d(0, 20px, 0) scale(.975); filter: blur(5px); }
  65% { opacity: 1; transform: translate3d(0, -1px, 0) scale(1.004); filter: blur(0); }
  100% { opacity: 1; transform: translate3d(0, 0, 0) scale(1); filter: none; }
}
@keyframes story-viz-out-up-v8 {
  0% { opacity: 1; transform: translate3d(0, 0, 0) scale(1); filter: blur(0); }
  100% { opacity: 0; transform: translate3d(0, 16px, 0) scale(.975); filter: blur(4px); }
}
@keyframes story-viz-in-up-v8 {
  0% { opacity: 0; transform: translate3d(0, -20px, 0) scale(.975); filter: blur(5px); }
  65% { opacity: 1; transform: translate3d(0, 1px, 0) scale(1.004); filter: blur(0); }
  100% { opacity: 1; transform: translate3d(0, 0, 0) scale(1); filter: none; }
}"""

    if old_crossfade in content:
        content = content.replace(old_crossfade, new_crossfade)
        print("Updated crossfading in scroll-story-v8-overrides.css")
    else:
        old_norm = old_crossfade.replace('\r\n', '\n')
        content_norm = content.replace('\r\n', '\n')
        if old_norm in content_norm:
            content = content_norm.replace(old_norm, new_crossfade)
            print("Updated crossfading (normalized) in scroll-story-v8-overrides.css")
        else:
            print("Could not match old_crossfade in scroll-story-v8-overrides.css!")

    # 2. Add Inter-Topic Graph Transition & Continuous Marks Animation at end of v8-overrides
    extra_transitions = """
/* ==========================================================================
   8. INTER-TOPIC GRAPH CONTINUITY & SEAMLESS TRANSITIONS
   ========================================================================== */
.tu-graph-stage {
  transition: opacity .65s cubic-bezier(.16, 1, .3, 1),
              transform .65s cubic-bezier(.16, 1, .3, 1),
              filter .65s cubic-bezier(.16, 1, .3, 1),
              box-shadow .55s ease,
              border-color .45s ease !important;
  will-change: transform, opacity;
}

.tu-graph-stage:not(.is-in-view) {
  opacity: .84;
  transform: translate3d(0, 14px, 0) scale(.988);
  filter: blur(1.5px);
}

.tu-graph-stage.is-in-view {
  opacity: 1 !important;
  transform: translate3d(0, 0, 0) scale(1) !important;
  filter: blur(0) !important;
}

/* Topic 07 (Triple Crown & Rankings) Stage Smoothness */
#topic-07 .scroll-story-stage {
  background: rgba(15, 23, 42, 0.88) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35) !important;
}
#topic-07 .scroll-story-stage-title {
  color: #ffffff !important;
}
#topic-07 .story-pair-card {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
}
#topic-07 .story-pair-card-label {
  color: #94a3b8 !important;
}
#topic-07 .story-pair-card-value {
  color: #38bdf8 !important;
}
#topic-07 .story-pair-card-note {
  color: #cbd5e1 !important;
}
#topic-07 .story-badge {
  background: rgba(255, 255, 255, 0.07) !important;
  border: 1px solid rgba(255, 255, 255, 0.16) !important;
  color: #ffffff !important;
}
#topic-07 .story-badge strong {
  color: #ffffff !important;
}
#topic-07 .story-badge small {
  color: #cbd5e1 !important;
}

/* Topic 08 (Green Campus) Stage Marks Animation */
#topic-08 .scroll-story-stage {
  border-left: 4px solid #10b981 !important;
  box-shadow: 0 12px 36px rgba(16, 185, 129, 0.08) !important;
}
#topic-08 .story-bar-fill {
  transition: width .82s cubic-bezier(.16, 1, .3, 1), background-color .4s ease !important;
}

/* Topic 09 (Hospital & Health) Stage Marks Animation */
#topic-09 .scroll-story-stage {
  border-left: 4px solid #0284c7 !important;
  box-shadow: 0 12px 36px rgba(2, 132, 199, 0.08) !important;
}

/* Smooth Arrow Pulse on Narrative Bridges */
.narrative-connector-bridge i {
  animation: bridge-arrow-glide 2.4s ease-in-out infinite alternate;
}
@keyframes bridge-arrow-glide {
  0% { transform: translateX(0); }
  100% { transform: translateX(5px); }
}

@media (prefers-reduced-motion: reduce) {
  .tu-graph-stage {
    transition: none !important;
    transform: none !important;
    filter: none !important;
  }
  .narrative-connector-bridge i {
    animation: none !important;
  }
}
"""

    if "/* ==========================================================================\n   8. INTER-TOPIC GRAPH CONTINUITY" not in content:
        content += "\n" + extra_transitions
        print("Added Inter-Topic Graph Continuity styles to scroll-story-v8-overrides.css")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Saved scroll-story-v8-overrides.css successfully.")

def update_editorial_refinement():
    path = r'assets/css/editorial-refinement.css'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    ambient_blends = """
/* ── Cinematic Atmospheric Gradients (Topics 07 → 08 → 09 → 10) ── */
#topic-07 {
  position: relative;
}
#topic-07::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 140px;
  background: linear-gradient(180deg, rgba(11, 22, 59, 0) 0%, rgba(11, 22, 59, 0.72) 45%, rgba(6, 36, 25, 0.95) 100%);
  pointer-events: none;
  z-index: 1;
}

#topic-08 {
  position: relative;
}
#topic-08::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120px;
  background: linear-gradient(180deg, rgba(6, 36, 25, 0.40) 0%, rgba(244, 248, 245, 0.82) 65%, var(--edit-green-paper) 100%);
  pointer-events: none;
  z-index: 1;
}
#topic-08::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 90px;
  background: linear-gradient(180deg, transparent 0%, rgba(255, 255, 255, 0.85) 100%);
  pointer-events: none;
  z-index: 1;
}

#topic-09 {
  position: relative;
}
#topic-09::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 85px;
  background: linear-gradient(180deg, transparent 0%, rgba(248, 250, 252, 0.9) 100%);
  pointer-events: none;
  z-index: 1;
}
"""

    if "/* ── Cinematic Atmospheric Gradients" not in content:
        content += "\n" + ambient_blends
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Added Cinematic Atmospheric Gradients to editorial-refinement.css")
    else:
        print("Cinematic Atmospheric Gradients already present in editorial-refinement.css")

if __name__ == '__main__':
    update_v8_overrides()
    update_editorial_refinement()
