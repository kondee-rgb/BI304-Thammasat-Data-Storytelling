import os, sys

def update_scroll_story():
    path = r'assets/js/scroll-story.js'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    target = "{ rootMargin: '-38% 0px -38% 0px', threshold: 0.01 }"
    replacement = "{ rootMargin: '-24% 0px -24% 0px', threshold: 0.01 }"

    if target in content:
        content = content.replace(target, replacement)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated rootMargin in scroll-story.js")
    else:
        print("Could not find target in scroll-story.js")

def update_app_js():
    path = r'assets/js/app.js'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    fn_code = """
    // ==========================================================================
    // INTER-CHAPTER GRAPH & CHART SEAMLESS TRANSITIONS
    // ==========================================================================
    function initInterTopicGraphTransitions() {
      const graphSelectors = [
        '#topic-01 .milestone-event-card',
        '#topic-02 #campusLeafletMap',
        '#topic-02 .campus-cluster-cards-grid',
        '#topic-03 .faculties-white-card',
        '#topic-04 .demographic-white-card',
        '#topic-05 .campus-distribution-card',
        '#topic-06 .cost-cap-white-card',
        '#topic-07 .triple-crown-badges-stage',
        '#topic-07 .tbs-benchmark-card',
        '#topic-08 .green-highlight-box',
        '#topic-08 .green-visual-card',
        '#topic-09 .hospital-kpi-row',
        '#topic-09 .hospital-chart-card',
        '#topic-10 .tu-route-layout'
      ];

      const elements = [];
      graphSelectors.forEach(sel => {
        const el = document.querySelector(sel);
        if (el) {
          el.classList.add('tu-graph-stage');
          elements.push(el);
        }
      });

      if (!elements.length || !('IntersectionObserver' in window)) return;
      const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (prefersReduced) {
        elements.forEach(el => el.classList.add('is-in-view'));
        return;
      }

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          const el = entry.target;
          if (entry.isIntersecting) {
            el.classList.add('is-in-view');
            // If it contains a canvas with Chart.js, refresh animation smoothly once
            const canvas = el.querySelector('canvas') || (el.tagName === 'CANVAS' ? el : null);
            if (canvas && typeof Chart !== 'undefined' && Chart.getChart) {
              const chart = Chart.getChart(canvas);
              if (chart && !el.dataset.graphHasRendered) {
                el.dataset.graphHasRendered = 'true';
                chart.update();
              }
            }
            if (el.id === 'campusLeafletMap' || el.querySelector('#campusLeafletMap')) {
              if (window.tuMap && typeof window.tuMap.invalidateSize === 'function') {
                window.tuMap.invalidateSize();
              }
            }
          } else {
            // Keep subtle softening when out of reading line
            el.classList.remove('is-in-view');
          }
        });
      }, {
        rootMargin: '-6% 0px -6% 0px',
        threshold: 0.12
      });

      elements.forEach(el => observer.observe(el));
    }
"""

    if "function initInterTopicGraphTransitions" not in content:
        # Insert fn_code right before line 2915 (before narrative connector bridges handler)
        target_marker = "      // Smooth Inter-Chapter Navigation via Narrative Connector Bridges"
        if target_marker in content:
            content = content.replace(target_marker, fn_code + "\n" + target_marker)
            print("Added initInterTopicGraphTransitions function to app.js")
        else:
            print("Could not find target_marker in app.js!")

        # Also add invocation right after initBidwellsScrollMotions();
        init_call_target = "      initBidwellsScrollMotions();"
        if init_call_target in content:
            content = content.replace(init_call_target, init_call_target + "\n      initInterTopicGraphTransitions();")
            print("Added initInterTopicGraphTransitions() invocation to app.js")
        else:
            print("Could not find init_call_target in app.js!")

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Saved app.js successfully.")
    else:
        print("initInterTopicGraphTransitions already in app.js")

if __name__ == '__main__':
    update_scroll_story()
    update_app_js()
