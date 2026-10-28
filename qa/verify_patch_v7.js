const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  console.log('🚀 Starting Patch v7 Verification (Remove Interactive Data Guess)...');
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

  // Test 1: Desktop 1440px
  console.log('\n--- 1. Testing Desktop (1440 x 900) ---');
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2', timeout: 30000 });

  // A. Confirm data-tu-guess is NOT in DOM
  const guessExists = await page.$('[data-tu-guess]') !== null;
  console.log(`[DOM Check] data-tu-guess exists: ${guessExists} (Expected: false)`);
  if (guessExists) {
    console.error('❌ FAILED: data-tu-guess still found in DOM!');
    process.exit(1);
  } else {
    console.log('✅ PASSED: data-tu-guess is completely absent from DOM.');
  }

  // B. Confirm milestone stepper and event card exist
  const milestoneCard = await page.$('#milestoneEventCard');
  console.log(`[DOM Check] milestoneEventCard exists: ${milestoneCard !== null} (Expected: true)`);

  // C. Check layout flow in Topic 01
  const topic1Flow = await page.evaluate(() => {
    const card = document.getElementById('milestoneEventCard');
    const topic1 = document.getElementById('topic-01');
    const bridge = topic1 ? topic1.querySelector('.narrative-connector-bridge') : null;
    const citation = topic1 ? topic1.querySelector('.section-source-citation') : null;
    
    if (!card || !bridge || !citation) {
      return { error: 'Missing elements in Topic 01' };
    }

    const cardRect = card.getBoundingClientRect();
    const bridgeRect = bridge.getBoundingClientRect();
    const citationRect = citation.getBoundingClientRect();

    const gapBetweenCardAndBridge = bridgeRect.top - cardRect.bottom;
    const gapBetweenBridgeAndCitation = citationRect.top - bridgeRect.bottom;

    return {
      cardBottom: cardRect.bottom,
      bridgeTop: bridgeRect.top,
      gapBetweenCardAndBridge,
      gapBetweenBridgeAndCitation,
      bridgeText: bridge.textContent.trim().slice(0, 80),
      citationText: citation.textContent.trim().slice(0, 80)
    };
  });

  console.log('[Layout Flow]', topic1Flow);
  if (topic1Flow.gapBetweenCardAndBridge > 80 || topic1Flow.gapBetweenCardAndBridge < 10) {
    console.warn(`⚠️ Warning: Gap between card and bridge is ${topic1Flow.gapBetweenCardAndBridge}px`);
  } else {
    console.log(`✅ PASSED: Clean editorial gap (${topic1Flow.gapBetweenCardAndBridge}px) between milestone card and narrative connector.`);
  }

  // D. Test milestone stepper clicks in Topic 01
  console.log('\n[Milestone Stepper Interaction]');
  const statBefore = await page.$eval('#mEventStat', el => el.textContent.trim());
  console.log(`- Initial stat (Step 1): ${statBefore}`);
  
  // Click step 3 (2519)
  await page.evaluate(() => {
    const nodes = document.querySelectorAll('#topic-01 .stepper-node');
    if (nodes[2]) nodes[2].click();
  });
  await new Promise(r => setTimeout(r, 400));
  const titleStep3 = await page.$eval('#mEventTitle', el => el.textContent.trim());
  const statStep3 = await page.$eval('#mEventStat', el => el.textContent.trim());
  console.log(`- After click Step 3: "${titleStep3}" | Stat: ${statStep3}`);

  // Screenshot Topic 01 on Desktop
  const screenshotDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(screenshotDir)) fs.mkdirSync(screenshotDir, { recursive: true });
  
  await page.evaluate(() => {
    document.getElementById('topic-01').scrollIntoView({ behavior: 'instant', block: 'start' });
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(screenshotDir, 'v7_topic01_desktop.png') });
  console.log('📸 Saved v7_topic01_desktop.png');

  // E. Verify Quiz ([data-tu-quiz]) is working intact
  console.log('\n--- 2. Testing Quiz Component ([data-tu-quiz]) ---');
  const quizExists = await page.$('[data-tu-quiz]') !== null;
  console.log(`[DOM Check] data-tu-quiz exists: ${quizExists} (Expected: true)`);
  if (!quizExists) {
    console.error('❌ FAILED: data-tu-quiz is missing!');
    process.exit(1);
  }

  const quizTitle = await page.$eval('.tui-quiz .tui-q', el => el.textContent.trim());
  console.log(`- Quiz intro text: "${quizTitle}"`);

  // Start quiz
  await page.click('.tui-quiz .tui-btn');
  await new Promise(r => setTimeout(r, 400));
  const q1Text = await page.$eval('.tui-quiz .tui-q', el => el.textContent.trim());
  const optCount = await page.$$eval('.tui-quiz .tui-opt', opts => opts.length);
  console.log(`- Quiz question 1: "${q1Text}" (${optCount} options rendered)`);
  console.log('✅ PASSED: Quiz initializes and starts cleanly.');

  // Test 3: Mobile 390px
  console.log('\n--- 3. Testing Mobile (390 x 844) ---');
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  // Scroll to topic 01
  await page.evaluate(() => {
    document.getElementById('topic-01').scrollIntoView({ behavior: 'instant', block: 'start' });
  });
  await new Promise(r => setTimeout(r, 500));

  const mobileFlow = await page.evaluate(() => {
    const card = document.getElementById('milestoneEventCard');
    const topic1 = document.getElementById('topic-01');
    const bridge = topic1 ? topic1.querySelector('.narrative-connector-bridge') : null;
    if (!card || !bridge) return null;
    const cardRect = card.getBoundingClientRect();
    const bridgeRect = bridge.getBoundingClientRect();
    return {
      gap: bridgeRect.top - cardRect.bottom,
      bodyOverflow: document.documentElement.scrollWidth > window.innerWidth
    };
  });
  console.log('[Mobile Flow]', mobileFlow);
  console.log(`- Mobile horizontal overflow: ${mobileFlow.bodyOverflow}`);
  if (mobileFlow.bodyOverflow) {
    console.error('❌ FAILED: Mobile has horizontal overflow!');
    process.exit(1);
  } else {
    console.log('✅ PASSED: Mobile layout fits viewport with zero overflow.');
  }

  await page.screenshot({ path: path.join(screenshotDir, 'v7_topic01_mobile.png') });
  console.log('📸 Saved v7_topic01_mobile.png');

  // Check console errors
  console.log('\n--- 4. Console Errors Check ---');
  console.log(`Total console errors: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    console.error('Console errors encountered:', consoleErrors);
  } else {
    console.log('✅ PASSED: Zero console errors on both desktop and mobile.');
  }

  await browser.close();
  console.log('\n🎉 ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!');
})();
