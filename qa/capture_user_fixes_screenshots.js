const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  console.log('📸 Capturing verification screenshots for User Request fixes...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  const screenshotDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(screenshotDir)) fs.mkdirSync(screenshotDir, { recursive: true });

  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  // 1. Capture Topic 04 (People icons at Step 2 - Health Sciences 71.5%)
  await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-04"]');
    const steps = mod.querySelectorAll('.scroll-story-step');
    steps[1].click(); // Health sciences 71.5%
    await new Promise(r => setTimeout(r, 600));
  });
  await page.screenshot({ path: path.join(screenshotDir, 'v10_topic04_people_transition_settled.png') });
  console.log('📸 Saved v10_topic04_people_transition_settled.png');

  // 2. Capture Topic 10 when scrolled down to Step 4 (Net-Zero Campus)
  await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-10"]');
    const steps = mod.querySelectorAll('.scroll-story-step');
    steps[3].click(); // Step 4
    await new Promise(r => setTimeout(r, 600));
  });
  await page.screenshot({ path: path.join(screenshotDir, 'v10_topic10_step4_sticky_unclipped.png') });
  console.log('📸 Saved v10_topic10_step4_sticky_unclipped.png');

  // 3. Test on short viewport (1440 x 720) to ensure zero clipping even on laptop screen!
  await page.setViewport({ width: 1440, height: 720 });
  await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-10"]');
    const steps = mod.querySelectorAll('.scroll-story-step');
    steps[3].click();
    await new Promise(r => setTimeout(r, 600));
  });
  await page.screenshot({ path: path.join(screenshotDir, 'v10_topic10_laptop720_unclipped.png') });
  console.log('📸 Saved v10_topic10_laptop720_unclipped.png');

  await browser.close();
  console.log('🎉 Verification screenshots captured successfully!');
})();
