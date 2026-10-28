const puppeteer = require('puppeteer');

async function audit() {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', err => errors.push(err.toString()));

  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  const summary = await page.evaluate(() => {
    const modules = Array.from(document.querySelectorAll('.scroll-story-module'));
    return modules.map(m => {
      const id = m.dataset.storyFor;
      const title = m.querySelector('.scroll-story-title')?.textContent?.trim();
      const steps = Array.from(m.querySelectorAll('.scroll-story-step')).map(s => ({
        idx: s.dataset.stepIndex,
        title: s.querySelector('h4')?.textContent?.trim(),
        metric: s.querySelector('.scroll-story-step-period')?.textContent?.trim()
      }));
      const stage = m.querySelector('.scroll-story-stage');
      const cs = stage ? getComputedStyle(stage) : {};
      const visualContent = stage?.querySelector('.scroll-story-visual-content');
      return {
        id,
        title,
        stepsCount: steps.length,
        steps,
        stagePosition: cs.position,
        visualType: visualContent?.firstElementChild?.className || 'none'
      };
    });
  });

  console.log('Audited Scrollytelling Modules:', summary.length);
  summary.forEach(s => {
    console.log(`[${s.id}] "${s.title}" — ${s.stepsCount} steps, visual: ${s.visualType}, stage pos: ${s.stagePosition}`);
  });

  console.log('\nPage Errors during audit:', errors.length);
  if (errors.length > 0) console.log(errors);

  await browser.close();
}

audit().catch(console.error);
