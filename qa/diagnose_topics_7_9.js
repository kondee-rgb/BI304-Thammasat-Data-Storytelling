const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  // Helper to scroll and check
  async function testTopic(topicId) {
    console.log(`\n=== Testing ${topicId} ===`);
    await page.evaluate((id) => {
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'instant' });
    }, topicId);
    await new Promise(r => setTimeout(r, 600));

    // Get module and steps
    const stepsCount = await page.evaluate((id) => {
      const module = document.querySelector(`#${id} .scroll-story-module`);
      if (!module) return 0;
      return module.querySelectorAll('.scroll-story-step').length;
    }, topicId);

    console.log(`Found ${stepsCount} steps in ${topicId}`);

    for (let i = 0; i < stepsCount; i++) {
      // Scroll each step into reading position
      await page.evaluate((args) => {
        const { id, stepIdx } = args;
        const steps = document.querySelectorAll(`#${id} .scroll-story-step`);
        if (steps[stepIdx]) {
          steps[stepIdx].scrollIntoView({ behavior: 'instant', block: 'center' });
        }
      }, { id: topicId, stepIdx: i });

      // Check immediately (during transition)
      await new Promise(r => setTimeout(r, 120));
      const midTransitionInfo = await page.evaluate((id) => {
        const content = document.querySelector(`#${id} .scroll-story-visual-content`);
        if (!content) return null;
        const layers = Array.from(content.children).map(c => ({
          className: c.className,
          top: c.getBoundingClientRect().top,
          height: c.getBoundingClientRect().height,
          display: window.getComputedStyle(c).display,
          position: window.getComputedStyle(c).position
        }));
        return {
          isCrossfading: content.classList.contains('is-crossfading'),
          isMorphing: content.classList.contains('is-morphing'),
          height: content.getBoundingClientRect().height,
          layers
        };
      }, topicId);

      console.log(`Step ${i+1} mid-transition:`, JSON.stringify(midTransitionInfo, null, 2));

      // Wait for transition to complete
      await new Promise(r => setTimeout(r, 800));
      const settledInfo = await page.evaluate((id) => {
        const content = document.querySelector(`#${id} .scroll-story-visual-content`);
        if (!content) return null;
        return {
          visualType: content.dataset.visualType,
          height: content.getBoundingClientRect().height
        };
      }, topicId);
      console.log(`Step ${i+1} settled:`, settledInfo);

      // Screenshot settled step
      const stage = await page.$(`#${topicId} .scroll-story-stage`);
      if (stage) {
        await stage.screenshot({ path: `qa/screenshots/${topicId}_step${i+1}_settled.png` });
      }
    }
  }

  await testTopic('topic-07');
  await testTopic('topic-08');
  await testTopic('topic-09');

  await browser.close();
  console.log('\nDiagnosis finished!');
})();
