const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 800 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  // Scroll to topic 10 module
  const diag = await page.evaluate(async () => {
    const mod10 = document.querySelector('.scroll-story-module[data-story-for="topic-10"]');
    if (!mod10) return { error: 'No mod 10' };

    const grid = mod10.querySelector('.scroll-story-grid');
    const col = mod10.querySelector('.scroll-story-visual-col');
    const stage = mod10.querySelector('.scroll-story-stage');
    const steps = mod10.querySelectorAll('.scroll-story-step');
    const step4 = steps[3];

    const vh = window.innerHeight;
    // Calculate absolute document offset of step4
    const sRect = step4.getBoundingClientRect();
    const docTop = sRect.top + window.scrollY;
    // Scroll so step4 is at 45% of viewport height (reading line)
    const targetScroll = docTop - vh * 0.45;
    window.scrollTo({ top: targetScroll, behavior: 'instant' });
    await new Promise(r => setTimeout(r, 600));
    const gridRect = grid.getBoundingClientRect();
    const colRect = col.getBoundingClientRect();
    const stageRect = stage.getBoundingClientRect();
    const step4Rect = step4.getBoundingClientRect();

    const colStyle = window.getComputedStyle(col);
    const stageStyle = window.getComputedStyle(stage);

    // Let's also test scrolling 150px and 250px further down!
    const testScrolls = [0, 100, 200, 300];
    const scrollResults = [];
    for (const offset of testScrolls) {
      window.scrollTo({ top: targetScroll + offset, behavior: 'instant' });
      await new Promise(r => setTimeout(r, 100));
      const sR = stage.getBoundingClientRect();
      const stR = step4.getBoundingClientRect();
      scrollResults.push({
        scrollOffset: offset,
        stageTop: sR.top,
        stageBottom: sR.bottom,
        stageHeight: sR.height,
        step4Top: stR.top,
        isStageClipped: sR.top < 60
      });
    }

    return {
      vh,
      scrollY: window.scrollY,
      grid: { top: gridRect.top, bottom: gridRect.bottom, height: gridRect.height },
      col: { top: colRect.top, bottom: colRect.bottom, height: colRect.height, position: colStyle.position, stickyTop: colStyle.top },
      stage: { top: stageRect.top, bottom: stageRect.bottom, height: stageRect.height },
      step4: { top: step4Rect.top, bottom: step4Rect.bottom, height: step4Rect.height },
      scrollProgression: scrollResults
    };
  });

  console.log('Topic 10 Scroll Diagnostics:\n', JSON.stringify(diag, null, 2));
  await browser.close();
})();
