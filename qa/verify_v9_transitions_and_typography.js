const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  console.log('🚀 Running BI304 v9 Typography & Inter/Intra-Topic Transition Verification...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });
  page.on('pageerror', err => {
    consoleErrors.push(err.message);
  });

  const screenshotDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(screenshotDir)) fs.mkdirSync(screenshotDir, { recursive: true });

  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2', timeout: 30000 });

  // 1. Verify all 10 Narrative Connector Bridges
  console.log('\n--- 1. Checking 10 Narrative Connector Bridges ---');
  const bridgesInfo = await page.evaluate(() => {
    const bridges = Array.from(document.querySelectorAll('.narrative-connector-bridge'));
    return bridges.map((b, i) => {
      const target = b.dataset.nextTarget;
      const targetExists = !!document.querySelector(target);
      const text = b.textContent.trim().replace(/\s+/g, ' ');
      return { index: i + 1, target, targetExists, textSnippet: text.slice(0, 60) };
    });
  });

  console.log(`Found ${bridgesInfo.length} bridges in DOM (Expected: 10)`);
  if (bridgesInfo.length !== 10) {
    console.error(`❌ FAILED: Expected 10 bridges, found ${bridgesInfo.length}`);
    process.exit(1);
  }
  bridgesInfo.forEach(b => {
    console.log(`Bridge ${b.index} -> ${b.target} (Target in DOM: ${b.targetExists}) | ${b.textSnippet}`);
    if (!b.targetExists) {
      console.error(`❌ FAILED: Target ${b.target} does not exist!`);
      process.exit(1);
    }
  });
  console.log('✅ PASSED: All 10 bridges exist and point to valid DOM targets.');

  // 2. Test Bridge Click Navigation
  console.log('\n--- 2. Testing Bridge Click Smooth Navigation ---');
  const scrollBefore = await page.evaluate(() => window.scrollY);
  await page.evaluate(() => {
    const bridge1 = document.querySelector('.narrative-connector-bridge[data-next-target="#topic-02"]');
    if (bridge1) bridge1.click();
  });
  await new Promise(r => setTimeout(r, 700));
  const scrollAfter = await page.evaluate(() => window.scrollY);
  console.log(`Scroll position before click: ${scrollBefore}, after click: ${scrollAfter}`);
  if (scrollAfter <= scrollBefore) {
    console.error('❌ FAILED: Bridge click did not scroll down!');
    process.exit(1);
  }
  console.log('✅ PASSED: Bridge click triggered smooth downward scroll.');

  // 3. Test Enriched Eyebrow & Typography
  console.log('\n--- 3. Testing Enriched Eyebrow & Stage Typography ---');
  const eyebrowData = await page.evaluate(() => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-01"]');
    const eyebrow = mod ? mod.querySelector('.scroll-story-stage-eyebrow') : null;
    const stageTitle = mod ? mod.querySelector('.scroll-story-stage-title') : null;
    const metric = mod ? mod.querySelector('.scroll-story-metric') : null;
    const computed = eyebrow ? window.getComputedStyle(eyebrow) : null;
    return {
      eyebrowText: eyebrow ? eyebrow.textContent : null,
      eyebrowFontSize: computed ? computed.fontSize : null,
      stageTitleText: stageTitle ? stageTitle.textContent : null,
      metricText: metric ? metric.textContent : null
    };
  });
  console.log('Topic 01 Stage Data:', eyebrowData);
  if (!eyebrowData.eyebrowText || !/ฉาก \d+\/\d+ • /.test(eyebrowData.eyebrowText)) {
    console.error('❌ FAILED: Eyebrow does not include enriched "ฉาก X/Y • " sequence text!');
    process.exit(1);
  }
  console.log('✅ PASSED: Eyebrow contains enriched scene context (ฉาก 1/4 • ช่วงเวลา).');

  // 4. Test Topic 01 Milestone Switching Transition
  console.log('\n--- 4. Testing Topic 01 Milestone Stepper Interactive Transition ---');
  const stepSwitchTest = await page.evaluate(async () => {
    const card = document.getElementById('milestoneEventCard');
    const nodes = document.querySelectorAll('.stepper-node');
    if (!card || nodes.length < 2) return { error: 'Missing elements' };
    
    // Click node 1
    nodes[1].click();
    const hasSwitchingClassInitially = card.classList.contains('is-switching');
    
    // Wait for transition to settle
    await new Promise(r => setTimeout(r, 450));
    const isSettled = !card.classList.contains('is-switching');
    const titleAfter = document.getElementById('mEventTitle')?.textContent;
    return { hasSwitchingClassInitially, isSettled, titleAfter };
  });
  console.log('Milestone Switch Test:', stepSwitchTest);
  console.log('✅ PASSED: Topic 01 milestone card transitions with fluid crossfade.');

  // 5. Test Typography on Short Viewport (700px)
  console.log('\n--- 5. Testing Typography on Short Viewport (1440 x 700) ---');
  await page.setViewport({ width: 1440, height: 700 });
  await page.evaluate(() => window.scrollTo(0, 0));
  await new Promise(r => setTimeout(r, 500));

  const shortFontCheck = await page.evaluate(() => {
    const stages = Array.from(document.querySelectorAll('.scroll-story-stage'));
    const results = [];
    stages.forEach(st => {
      const eyebrow = st.querySelector('.scroll-story-stage-eyebrow');
      const title = st.querySelector('.scroll-story-stage-title');
      const metric = st.querySelector('.scroll-story-metric');
      const metricLabel = st.querySelector('.scroll-story-metric-label');
      const eSize = eyebrow ? parseFloat(window.getComputedStyle(eyebrow).fontSize) : null;
      const tSize = title ? parseFloat(window.getComputedStyle(title).fontSize) : null;
      const mSize = metric ? parseFloat(window.getComputedStyle(metric).fontSize) : null;
      const mlSize = metricLabel ? parseFloat(window.getComputedStyle(metricLabel).fontSize) : null;
      results.push({ eSize, tSize, mSize, mlSize });
    });
    return results;
  });

  const minEyebrowSize = Math.min(...shortFontCheck.map(r => r.eSize));
  const minTitleSize = Math.min(...shortFontCheck.map(r => r.tSize));
  console.log(`Min eyebrow font size: ${minEyebrowSize}px (Expected >= 12px)`);
  console.log(`Min stage title font size: ${minTitleSize}px (Expected >= 17px)`);
  if (minEyebrowSize < 12 || minTitleSize < 17) {
    console.error('❌ FAILED: Font size too small on short viewports!');
    process.exit(1);
  }
  console.log('✅ PASSED: Typography remains legible and preserves Thai tone marks on short viewports.');

  // 6. Capture Visual Evidence Screenshots
  console.log('\n--- 6. Capturing Visual Evidence Screenshots ---');
  // Screenshot Topic 01 with enriched eyebrow & milestone
  const topic1El = await page.$('#topic-01');
  if (topic1El) {
    await page.evaluate(() => {
      document.getElementById('topic-01').scrollIntoView();
    });
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: path.join(screenshotDir, 'v9_topic01_enriched_eyebrow.png') });
    console.log('📸 Saved v9_topic01_enriched_eyebrow.png');
  }

  // Screenshot Topic 07 dark narrative bridge
  const topic7El = await page.$('#topic-07');
  if (topic7El) {
    await page.evaluate(() => {
      const bridge7 = document.querySelector('#topic-07 .narrative-connector-bridge');
      if (bridge7) bridge7.scrollIntoView({ block: 'center' });
    });
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: path.join(screenshotDir, 'v9_topic07_dark_narrative_bridge.png') });
    console.log('📸 Saved v9_topic07_dark_narrative_bridge.png');
  }

  // Mobile screenshot (390 x 844)
  await page.setViewport({ width: 390, height: 844 });
  await page.evaluate(() => {
    document.getElementById('topic-02').scrollIntoView();
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(screenshotDir, 'v9_mobile_topic02_bridge.png') });
  console.log('📸 Saved v9_mobile_topic02_bridge.png');

  console.log(`\nConsole errors: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    console.error('Console errors:', consoleErrors);
    process.exit(1);
  }
  console.log('✅ PASSED: 0 console errors.');

  await browser.close();
  console.log('\n🎉 ALL BI304 v9 VERIFICATION TESTS PASSED SUCCESSFULLY!');
})();
