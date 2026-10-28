const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const SCREENSHOT_DIR = path.join(__dirname, 'screenshots');
if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function testFull() {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', err => errors.push(err.toString()));

  console.log('=== TEST 1: DESKTOP 1440PX FULL RUN ===');
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  await page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; });

  // 1. Screenshot Hero
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'hero_editorial_improved.png') });
  console.log('  Saved: hero_editorial_improved.png');

  // 2. Test Scrollytelling Step Activation Across all 10 Topics
  const topicIds = [
    'topic-01', 'topic-02', 'topic-03', 'topic-04', 'topic-05',
    'topic-06', 'topic-07', 'topic-08', 'topic-09', 'topic-10'
  ];

  for (const tid of topicIds) {
    const modInfo = await page.evaluate((id) => {
      const m = document.querySelector(`.scroll-story-module[data-story-for="${id}"]`);
      if (!m) return null;
      const steps = Array.from(m.querySelectorAll('.scroll-story-step')).length;
      return { found: true, steps, top: m.offsetTop };
    }, tid);

    if (!modInfo) {
      console.log(`  [FAIL] Module for ${tid} not found!`);
      continue;
    }

    console.log(`  [${tid}] Found module with ${modInfo.steps} steps. Testing steps...`);

    // Test each step activation by click
    for (let s = 0; s < modInfo.steps; s++) {
      const activeState = await page.evaluate((id, stepIdx) => {
        const m = document.querySelector(`.scroll-story-module[data-story-for="${id}"]`);
        const step = m.querySelectorAll('.scroll-story-step')[stepIdx];
        if (step) step.click();
        const stage = m.querySelector('.scroll-story-stage');
        const metric = stage.querySelector('.scroll-story-metric')?.textContent?.trim();
        const eyebrow = stage.querySelector('.scroll-story-stage-eyebrow')?.textContent?.trim();
        const isCurrent = step.getAttribute('aria-current') === 'step';
        return { metric, eyebrow, isCurrent };
      }, tid, s);

      if (!activeState.isCurrent) {
        console.log(`    Step ${s} in ${tid} failed to activate!`);
      }
    }

    // Test reverse scroll / activation (activate step 0 again)
    await page.evaluate((id) => {
      const m = document.querySelector(`.scroll-story-module[data-story-for="${id}"]`);
      const step0 = m.querySelectorAll('.scroll-story-step')[0];
      if (step0) step0.click();
    }, tid);
  }

  // 3. Capture Screenshots of Specific Stories
  // Topic 04 Demographics (People Icons)
  await page.evaluate(() => {
    const t4 = document.getElementById('topic-04');
    if (t4) window.scrollTo(0, t4.offsetTop + 120);
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic04_demographic_people.png') });
  console.log('  Saved: topic04_demographic_people.png');

  // Topic 06 Financial Architecture
  await page.evaluate(() => {
    const t6 = document.getElementById('topic-06');
    if (t6) window.scrollTo(0, t6.offsetTop + 120);
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic06_financial_story.png') });
  console.log('  Saved: topic06_financial_story.png');

  // Topic 08 Sustainability Story
  await page.evaluate(() => {
    const t8 = document.getElementById('topic-08');
    if (t8) window.scrollTo(0, t8.offsetTop + 120);
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic08_sustainability_story.png') });
  console.log('  Saved: topic08_sustainability_story.png');

  // Topic 10 TU 2034 with Stacking Cards and Route Map
  await page.evaluate(() => {
    const t10 = document.getElementById('topic-10');
    if (t10) {
      const stack = t10.querySelector('.tu-route-layout');
      window.scrollTo(0, (stack ? stack.offsetTop : t10.offsetTop) + 100);
    }
  });
  await new Promise(r => setTimeout(r, 800));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic10_tu2034_final.png') });
  console.log('  Saved: topic10_tu2034_final.png');

  console.log('\n=== TEST 2: MOBILE 390PX VIEWPORT & STICKY HUD CHECK ===');
  await page.setViewport({ width: 390, height: 844 });
  await page.evaluate(() => window.scrollTo(0, 0));
  await new Promise(r => setTimeout(r, 400));

  // Check mobile overflow
  const mobileOverflow = await page.evaluate(() => {
    return {
      docW: document.documentElement.clientWidth,
      scrollW: document.documentElement.scrollWidth,
      hasOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
    };
  });
  console.log(`Mobile 390px Overflow: docW=${mobileOverflow.docW}, scrollW=${mobileOverflow.scrollW}, hasOverflow=${mobileOverflow.hasOverflow}`);

  // Scroll to topic 04 on mobile and capture screenshot
  await page.evaluate(() => {
    const t4 = document.getElementById('topic-04');
    if (t4) window.scrollTo(0, t4.offsetTop + 80);
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'mobile_demographic_390.png') });
  console.log('  Saved: mobile_demographic_390.png');

  // Scroll to topic 10 on mobile
  await page.evaluate(() => {
    const t10 = document.getElementById('topic-10');
    if (t10) window.scrollTo(0, t10.offsetTop + 100);
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'mobile_topic10_390.png') });
  console.log('  Saved: mobile_topic10_390.png');

  console.log(`\nTotal Page Errors Encountered: ${errors.length}`);
  if (errors.length > 0) {
    errors.forEach(e => console.log('  Error:', e));
  } else {
    console.log('  SUCCESS: 0 console errors during full run!');
  }

  await browser.close();
}

testFull().catch(console.error);
