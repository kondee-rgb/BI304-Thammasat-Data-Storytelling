const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  async function auditTopicSteps(topicId) {
    console.log(`\n========================================`);
    console.log(`Auditing ${topicId}`);
    console.log(`========================================`);

    const stepCount = await page.evaluate((id) => {
      return document.querySelectorAll(`#${id} .scroll-story-step`).length;
    }, topicId);

    for (let i = 0; i < stepCount; i++) {
      // Scroll smoothly to simulate user reading
      await page.evaluate((args) => {
        const { id, idx } = args;
        const steps = document.querySelectorAll(`#${id} .scroll-story-step`);
        if (steps[idx]) {
          const rect = steps[idx].getBoundingClientRect();
          const targetY = window.scrollY + rect.top - (window.innerHeight * 0.40);
          window.scrollTo({ top: targetY, behavior: 'instant' });
        }
      }, { id: topicId, idx: i });

      // Wait 900ms for transition and animation to settle
      await new Promise(r => setTimeout(r, 900));

      const stepState = await page.evaluate((args) => {
        const { id, idx } = args;
        const module = document.querySelector(`#${id} .scroll-story-module`);
        const stage = module ? module.querySelector('.scroll-story-stage') : null;
        const content = stage ? stage.querySelector('.scroll-story-visual-content') : null;
        const title = stage ? stage.querySelector('.scroll-story-stage-title')?.innerText : '';
        const eyebrow = stage ? stage.querySelector('.scroll-story-stage-eyebrow')?.innerText : '';
        const stepEl = document.querySelectorAll(`#${id} .scroll-story-step`)[idx];
        const isActive = stepEl ? stepEl.classList.contains('is-active') : false;

        return {
          stepIdx: idx + 1,
          isActive,
          eyebrow,
          title,
          visualType: content ? content.dataset.visualType : null,
          contentHeight: content ? content.getBoundingClientRect().height : null,
          innerHTMLPreview: content ? content.firstElementChild?.className : null
        };
      }, { id: topicId, idx: i });

      console.log(`Step ${i + 1}:`, stepState);

      // Screenshot the stage
      const stage = await page.$(`#${topicId} .scroll-story-stage`);
      if (stage) {
        await stage.screenshot({ path: `qa/screenshots/${topicId}_step_${i+1}_settled.png` });
      }
    }
  }

  await auditTopicSteps('topic-07');
  await auditTopicSteps('topic-08');
  await auditTopicSteps('topic-09');

  await browser.close();
  console.log('\nThorough step audit completed!');
})();
