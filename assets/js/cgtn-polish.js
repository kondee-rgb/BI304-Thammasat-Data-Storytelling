/*
 * Scroll storytelling enhancements for the BI304 Thammasat site.
 * No data is changed and no visualization dependency is added.
 * v=20261026c
 */
(() => {
  'use strict';
  if (window.__cgtnPolishLoaded) return;
  window.__cgtnPolishLoaded = true;

  const root = document.documentElement;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('cgtn-polish-enabled');

  const main = document.querySelector('#main');
  if (!main) return;

  const allSections = Array.from(main.querySelectorAll('section[id]'));
  const trackSecs = ['hero', 'key-findings', 'topic-01', 'topic-02', 'topic-03', 'topic-04', 'topic-05', 'topic-06', 'topic-07', 'topic-08', 'topic-09', 'topic-10', 'finish'];
  const storySections = allSections.filter(section => trackSecs.includes(section.id));
  const topics = storySections.filter(section => /^topic-\d{2}$/.test(section.id));

  const plainText = (element) => (element?.textContent || '').replace(/\s+/g, ' ').trim();
  const titleFor = (section) => {
    const heading = section.querySelector('.section-headline, .statement-main-text, h1, h2, h3');
    if (heading) return plainText(heading).replace(/^[“”"']+|[“”"']+$/g, '');
    if (section.id === 'hero') return '90 ปี มหาวิทยาลัยธรรมศาสตร์';
    if (section.id === 'key-findings') return 'สรุป 3 มิติสำคัญแห่งทศวรรษ';
    if (section.id === 'finish') return 'บทสรุป 90 ปี';
    return section.getAttribute('aria-label') || section.id;
  };

  /* Build live chapter capsule marker (bottom-left) */
  const chapter = document.createElement('aside');
  chapter.className = 'cgtn-chapter-marker cgtn-chapter-hidden';
  chapter.setAttribute('aria-live', 'polite');
  chapter.setAttribute('aria-atomic', 'true');
  chapter.innerHTML = '<span class="cgtn-chapter-count">01 <i>/ 10</i></span><span class="cgtn-chapter-divider" aria-hidden="true"></span><span class="cgtn-chapter-title">90 ปี มหาวิทยาลัยธรรมศาสตร์</span>';
  document.body.appendChild(chapter);

  const chapterCount = chapter.querySelector('.cgtn-chapter-count');
  const chapterTitle = chapter.querySelector('.cgtn-chapter-title');
  const numberById = (id) => (id.match(/topic-(\d{2})/) || [,'01'])[1];
  let activeSectionId = '';

  function setActiveSection(section) {
    if (!section || activeSectionId === section.id) return;
    activeSectionId = section.id;
    storySections.forEach(item => item.classList.toggle('cgtn-scene-active', item.id === section.id));

    const isTopic = /^topic-\d{2}$/.test(section.id);
    if (isTopic) {
      chapterCount.innerHTML = `${numberById(section.id)} <i>/ 10</i>`;
      chapterTitle.textContent = titleFor(section);
      chapter.classList.remove('cgtn-chapter-hidden');
    } else {
      chapter.classList.add('cgtn-chapter-hidden');
    }

    /* Keep the three existing navigation systems in sync */
    document.querySelectorAll('.desktop-dot-nav a[href^="#"], .header-nav a[href^="#"], .mobile-nav-links a[href^="#"]').forEach(link => {
      const href = link.getAttribute('href');
      const isActive = href === `#${section.id}` || (section.id === 'key-findings' && href === '#hero');
      link.classList.toggle('active', isActive);
      if (isActive) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }

  window.__cgtnSetActiveSection = setActiveSection;

  /* Reveal section introductions and visualization frames gently as they enter view */
  const revealCandidates = [];
  topics.forEach((section) => {
    const candidates = [
      section.querySelector('.section-headline'),
      section.querySelector('.statement-main-text'),
      section.querySelector('.section-lead'),
      section.querySelector('.cluster-map-layout'),
      section.querySelector('.milestones-strip-section'),
      section.querySelector('.faculty-chart-wrap'),
      section.querySelector('.demographic-chips-row'),
      section.querySelector('.shift-metrics-grid'),
      section.querySelector('.cost-cap-white-card'),
      section.querySelector('.curved-track-content > div'),
      section.querySelector('.green-cards-grid'),
      section.querySelector('.hospital-kpi-row'),
      section.querySelector('.circuit-layout-grid')
    ].filter(Boolean);

    candidates.forEach((element) => {
      if (element.matches('.tu-reveal-slide-up, .tu-reveal-slide-left, .tu-reveal-slide-right, .tu-reveal-scale')) return;
      if (element.closest('.tu-reveal-slide-up, .tu-reveal-slide-left, .tu-reveal-slide-right, .tu-reveal-scale')) return;
      if (element.dataset.cgtnRevealAttached) return;
      element.dataset.cgtnRevealAttached = '1';
      element.classList.add('cgtn-reveal');
      revealCandidates.push(element);
    });
  });

  if (!reducedMotion && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('cgtn-in-view');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -7% 0px' });
    revealCandidates.forEach(element => revealObserver.observe(element));

    const sceneObserver = new IntersectionObserver((entries) => {
      const visible = entries.filter(entry => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (visible[0]) setActiveSection(visible[0].target);
    }, { threshold: [0.15, 0.3, 0.5, 0.7], rootMargin: '-15% 0px -35% 0px' });
    storySections.forEach(section => sceneObserver.observe(section));
  } else {
    revealCandidates.forEach(element => element.classList.add('cgtn-in-view'));
    setActiveSection(storySections[0]);
  }

  /* Scroll progress and active section fallback */
  const progress = document.getElementById('topReadingProgress');
  let ticking = false;

  const updateProgress = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const percent = scrollable > 0 ? Math.min(100, Math.max(0, (window.scrollY / scrollable) * 100)) : 0;
    if (progress) {
      progress.style.width = `${percent}%`;
      progress.setAttribute('aria-valuenow', String(Math.round(percent)));
    }
    document.body.classList.toggle('cgtn-has-scrolled', window.scrollY > 32);

    /* Instant active-section fallback tracking on scroll */
    let candidate = null;
    for (let i = 0; i < storySections.length; i++) {
      const sec = storySections[i];
      const rect = sec.getBoundingClientRect();
      if (rect.top <= window.innerHeight * 0.45 && rect.bottom >= window.innerHeight * 0.15) {
        candidate = sec;
      }
    }
    if (candidate) setActiveSection(candidate);

    ticking = false;
  };

  window.__cgtnUpdateProgress = updateProgress;

  const onScroll = () => {
    updateProgress();
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  updateProgress();

  /* Refined Editorial Chart.js Tooltip Defaults */
  if (typeof Chart !== 'undefined' && Chart.defaults && Chart.defaults.plugins) {
    // Give the original charts a shared editorial baseline without altering datasets.
    Chart.defaults.color = '#626978';
    Chart.defaults.borderColor = 'rgba(16, 26, 53, .11)';
    Chart.defaults.font.family = "'Sarabun', 'Prompt', sans-serif";
    Chart.defaults.font.size = 12;
    if (Chart.defaults.plugins.legend && Chart.defaults.plugins.legend.labels) {
      Chart.defaults.plugins.legend.labels.usePointStyle = true;
      Chart.defaults.plugins.legend.labels.boxWidth = 9;
      Chart.defaults.plugins.legend.labels.padding = 16;
    }
    const t = Chart.defaults.plugins.tooltip;
    if (t) {
      t.backgroundColor = 'rgba(26, 29, 36, 0.94)';
      t.borderColor = 'rgba(255, 255, 255, 0.14)';
      t.borderWidth = 1;
      t.cornerRadius = 8;
      t.padding = 12;
      t.boxPadding = 6;
      t.usePointStyle = true;
      t.titleColor = '#ffffff';
      t.bodyColor = '#f1f5f9';
    }
  }

  /* Keyboard support for the clickable div controls */
  const makeKeyboardButton = (element, label) => {
    if (!element || element.dataset.cgtnKeyboardReady) return;
    element.dataset.cgtnKeyboardReady = '1';
    element.setAttribute('role', 'button');
    if (!element.hasAttribute('tabindex')) element.setAttribute('tabindex', '0');
    if (label && !element.hasAttribute('aria-label')) element.setAttribute('aria-label', label);
    element.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        element.click();
      }
    });
  };
  makeKeyboardButton(document.querySelector('.header-logo-group'), 'กลับไปหน้าแรก');
  document.querySelectorAll('.stepper-node, .circuit-milestone-node').forEach((element) => {
    makeKeyboardButton(element, plainText(element));
  });

  /* Modal accessibility enhancements */
  [document.getElementById('facultyModal'), document.getElementById('flourishHubModal')].filter(Boolean).forEach((modal) => {
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    if (!modal.hasAttribute('aria-label') && !modal.hasAttribute('aria-labelledby')) {
      const title = modal.querySelector('h1, h2, h3, .modal-title, #flourishHubModalTitle, #mFacTitle');
      if (title) {
        if (!title.id) title.id = `${modal.id}-accessible-title`;
        modal.setAttribute('aria-labelledby', title.id);
      } else {
        modal.setAttribute('aria-label', modal.id === 'facultyModal' ? 'รายละเอียดคณะวิชา' : 'คลังภาพข้อมูล Flourish');
      }
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    const visibleModal = [document.getElementById('facultyModal'), document.getElementById('flourishHubModal')]
      .filter(Boolean)
      .find(modal => {
        return modal.classList.contains('active') ||
               modal.classList.contains('show') ||
               modal.getAttribute('aria-hidden') === 'false' ||
               modal.style.display === 'flex' ||
               window.getComputedStyle(modal).display === 'flex';
      });
    if (!visibleModal) return;
    if (visibleModal.id === 'facultyModal' && typeof window.closeFacultyModal === 'function') window.closeFacultyModal();
    if (visibleModal.id === 'flourishHubModal' && typeof window.closeFlourishHubModal === 'function') window.closeFlourishHubModal();
  });
})();
