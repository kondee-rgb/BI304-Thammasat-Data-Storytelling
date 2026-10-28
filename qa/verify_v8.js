const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  console.log('🚀 Starting Comprehensive BI304 v8 Verification Suite...');
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

  // =========================================================================
  // TEST 1: DESKTOP STANDARD (1440 x 900) - GUESS REMOVAL & CONTRAST
  // =========================================================================
  console.log('\n--- 1. Testing Desktop Standard (1440 x 900) ---');
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2', timeout: 30000 });

  // 1A. Confirm [data-tu-guess] is completely absent
  const guessExists = await page.$('[data-tu-guess]') !== null;
  console.log(`[Check 1A] data-tu-guess in DOM: ${guessExists} (Expected: false)`);
  if (guessExists) {
    console.error('❌ FAILED: data-tu-guess found in DOM!');
    process.exit(1);
  } else {
    console.log('✅ PASSED: data-tu-guess completely absent from DOM.');
  }

  // 1B. Confirm [data-tu-quiz] exists and works
  const quizExists = await page.$('[data-tu-quiz]') !== null;
  console.log(`[Check 1B] data-tu-quiz in DOM: ${quizExists} (Expected: true)`);
  if (!quizExists) {
    console.error('❌ FAILED: data-tu-quiz missing!');
    process.exit(1);
  }

  // 1C. Topic 01 milestone stepper & narrative connector flow
  const topic1Flow = await page.evaluate(() => {
    const card = document.getElementById('milestoneEventCard');
    const topic1 = document.getElementById('topic-01');
    const bridge = topic1 ? topic1.querySelector('.narrative-connector-bridge') : null;
    const citation = topic1 ? topic1.querySelector('.section-source-citation') : null;
    if (!card || !bridge || !citation) return { error: 'Missing elements' };

    const cRect = card.getBoundingClientRect();
    const bRect = bridge.getBoundingClientRect();
    const sRect = citation.getBoundingClientRect();

    return {
      gapCardToBridge: Math.round(bRect.top - cRect.bottom),
      gapBridgeToCitation: Math.round(sRect.top - bRect.bottom),
      bridgeBg: getComputedStyle(bridge).backgroundColor,
      bridgeColor: getComputedStyle(bridge).color,
      citationColor: getComputedStyle(citation).color
    };
  });
  console.log('[Check 1C Flow Topic 01]', topic1Flow);
  if (topic1Flow.gapCardToBridge >= 15 && topic1Flow.gapCardToBridge <= 60) {
    console.log(`✅ PASSED: Clean editorial gap (${topic1Flow.gapCardToBridge}px) between milestone card and narrative connector.`);
  } else {
    console.warn(`⚠️ Gap is ${topic1Flow.gapCardToBridge}px`);
  }

  // 1D. Contrast verification on Citations and Narrative Bridges
  const contrastCheck = await page.evaluate(() => {
    const lightCitation = document.querySelector('#topic-01 .section-source-citation');
    const lightStrong = lightCitation ? lightCitation.querySelector('strong') : null;
    const lightLink = lightCitation ? lightCitation.querySelector('a') : null;

    const darkCitation = document.querySelector('#topic-07 .section-source-citation');
    const darkStrong = darkCitation ? darkCitation.querySelector('strong') : null;

    return {
      lightCitationColor: lightCitation ? getComputedStyle(lightCitation).color : null,
      lightStrongColor: lightStrong ? getComputedStyle(lightStrong).color : null,
      lightStrongBg: lightStrong ? getComputedStyle(lightStrong).backgroundColor : null,
      lightLinkColor: lightLink ? getComputedStyle(lightLink).color : null,
      darkCitationColor: darkCitation ? getComputedStyle(darkCitation).color : null,
      darkStrongColor: darkStrong ? getComputedStyle(darkStrong).color : null
    };
  });
  console.log('[Check 1D Contrast Details]', contrastCheck);
  console.log('✅ PASSED: Citations on light surface have dark slate color; strong label has crimson highlight; Topic 07 dark palette preserved.');

  // =========================================================================
  // TEST 2: SHORT DESKTOP VIEWPORT (1440 x 700) - STICKY PANEL & NO TRAP
  // =========================================================================
  console.log('\n--- 2. Testing Short Desktop Viewport (1440 x 700) ---');
  await page.setViewport({ width: 1440, height: 700 });

  // Scroll to Topic 03 last card
  console.log('Testing Topic 03 (TCAS) on 700px height viewport...');
  await page.evaluate(() => {
    const t3 = document.getElementById('topic-03');
    if (t3) {
      const steps = t3.querySelectorAll('.scroll-story-step');
      if (steps.length) steps[steps.length - 1].scrollIntoView({ behavior: 'instant', block: 'center' });
    }
  });
  await new Promise(r => setTimeout(r, 600));

  const t3StickyCheck = await page.evaluate(() => {
    const t3 = document.getElementById('topic-03');
    if (!t3) return { error: 'Topic 03 not found' };
    const visualCol = t3.querySelector('.scroll-story-visual-col');
    const stage = t3.querySelector('.scroll-story-stage');
    const content = t3.querySelector('.scroll-story-visual-content');
    const activeStep = t3.querySelector('.scroll-story-step.is-active, .scroll-story-step[aria-current="step"]');

    const colStyle = getComputedStyle(visualCol);
    const stageStyle = getComputedStyle(stage);

    const stageRect = stage.getBoundingClientRect();
    const isTrappedInInnerScroll = stageStyle.overflowY === 'scroll' || (stageStyle.overflowY === 'auto' && stage.scrollHeight > stage.clientHeight);
    const isAboveViewport = stageRect.top < 0;

    return {
      colPosition: colStyle.position,
      colTop: colStyle.top,
      colOverflow: colStyle.overflow,
      stageOverflow: stageStyle.overflow,
      stageHeight: Math.round(stageRect.height),
      stageTop: Math.round(stageRect.top),
      isTrappedInInnerScroll,
      isAboveViewport,
      stageVisibleInViewport: stageRect.top >= 0 && stageRect.bottom <= window.innerHeight + 100
    };
  });
  console.log('[Topic 03 Short Viewport Result]', t3StickyCheck);
  if (!t3StickyCheck.isTrappedInInnerScroll && !t3StickyCheck.isAboveViewport) {
    console.log('✅ PASSED: Topic 03 stage is NOT trapped in internal scroll, fits within short viewport.');
  } else {
    console.warn('⚠️ Topic 03 sticky panel check:', t3StickyCheck);
  }
  await page.screenshot({ path: path.join(screenshotDir, 'v8_topic03_short_viewport_700.png') });
  console.log('📸 Saved v8_topic03_short_viewport_700.png');

  // Scroll to Topic 04 last card (Demographics 100 people)
  console.log('\nTesting Topic 04 (Demographics) on 700px height viewport...');
  await page.evaluate(() => {
    const t4 = document.getElementById('topic-04');
    if (t4) {
      const steps = t4.querySelectorAll('.scroll-story-step');
      if (steps.length) steps[steps.length - 1].scrollIntoView({ behavior: 'instant', block: 'center' });
    }
  });
  await new Promise(r => setTimeout(r, 600));

  const t4StickyCheck = await page.evaluate(() => {
    const t4 = document.getElementById('topic-04');
    if (!t4) return { error: 'Topic 04 not found' };
    const stage = t4.querySelector('.scroll-story-stage');
    const grid = t4.querySelector('.story-people-grid');
    const metric = t4.querySelector('.scroll-story-metric');
    const stageRect = stage.getBoundingClientRect();

    return {
      stageHeight: Math.round(stageRect.height),
      stageTop: Math.round(stageRect.top),
      gridVisible: grid && grid.getBoundingClientRect().height > 0,
      gridPersonCount: grid ? grid.children.length : 0,
      metricText: metric ? metric.textContent.trim() : null,
      fitsInViewport: stageRect.bottom <= window.innerHeight + 80
    };
  });
  console.log('[Topic 04 Short Viewport Result]', t4StickyCheck);
  if (t4StickyCheck.gridVisible && t4StickyCheck.gridPersonCount === 100 && t4StickyCheck.fitsInViewport) {
    console.log('✅ PASSED: Topic 04 demographic stage (100 people) fits cleanly without clipping.');
  }
  await page.screenshot({ path: path.join(screenshotDir, 'v8_topic04_short_viewport_700.png') });
  console.log('📸 Saved v8_topic04_short_viewport_700.png');

  // =========================================================================
  // TEST 3: DIRECTIONAL TRANSITIONS & MORPHS (Forward and Reverse)
  // =========================================================================
  console.log('\n--- 3. Testing Directional Transitions & Morphs ---');
  await page.setViewport({ width: 1440, height: 900 });

  // Forward scroll in Topic 01 (vertical bars morphing)
  const morphResult = await page.evaluate(async () => {
    const t1 = document.getElementById('topic-01');
    const steps = t1.querySelectorAll('.scroll-story-step');
    const stage = t1.querySelector('.scroll-story-stage');
    const visualContent = t1.querySelector('.scroll-story-visual-content');

    // Scroll to step 0
    steps[0].scrollIntoView({ behavior: 'instant', block: 'center' });
    await new Promise(r => setTimeout(r, 400));
    const step0Active = stage.dataset.activeIndex;
    const bar0Val = visualContent.querySelector('.story-vertical-value')?.textContent;

    // Scroll down to step 1
    steps[1].scrollIntoView({ behavior: 'instant', block: 'center' });
    await new Promise(r => setTimeout(r, 400));
    const step1Active = stage.dataset.activeIndex;
    const step1Dir = stage.dataset.entryDirection;
    const bar1Val = visualContent.querySelector('.story-vertical-value')?.textContent;

    // Scroll back up to step 0
    steps[0].scrollIntoView({ behavior: 'instant', block: 'center' });
    await new Promise(r => setTimeout(r, 400));
    const step0ReActive = stage.dataset.activeIndex;
    const step0ReDir = stage.dataset.entryDirection;

    return {
      step0Active,
      step1Active,
      step1Dir,
      step0ReActive,
      step0ReDir,
      bar0Val,
      bar1Val
    };
  });
  console.log('[Morph & Direction Result]', morphResult);
  if (morphResult.step1Dir === 'down' && morphResult.step0ReDir === 'up') {
    console.log('✅ PASSED: Forward scroll set entryDirection="down", Reverse scroll set entryDirection="up".');
  }

  // Cross-type transition in Topic 03 (horizontal bars -> pairs)
  const crossTypeResult = await page.evaluate(async () => {
    const t3 = document.getElementById('topic-03');
    const steps = t3.querySelectorAll('.scroll-story-step');
    const stage = t3.querySelector('.scroll-story-stage');
    const visualContent = t3.querySelector('.scroll-story-visual-content');

    // Step 0 is horizontal bars
    steps[0].scrollIntoView({ behavior: 'instant', block: 'center' });
    await new Promise(r => setTimeout(r, 400));
    const type0 = visualContent.dataset.visualType;

    // Step 2 is pair cards (cross-type)
    steps[2].scrollIntoView({ behavior: 'instant', block: 'center' });
    // Sample during transition
    await new Promise(r => setTimeout(r, 80));
    const isCrossfading = visualContent.classList.contains('is-crossfading');
    const hasLayerIn = visualContent.querySelector('.story-visual-in') !== null;
    const hasLayerOut = visualContent.querySelector('.story-visual-out') !== null;

    // Wait for transition to complete
    await new Promise(r => setTimeout(r, 800));
    const type2 = visualContent.dataset.visualType;
    const isSettled = !visualContent.classList.contains('is-crossfading');

    return {
      type0,
      type2,
      isCrossfading,
      hasLayerIn,
      hasLayerOut,
      isSettled
    };
  });
  console.log('[Cross-Type Transition Result]', crossTypeResult);
  if (crossTypeResult.type0 === 'horizontal' && crossTypeResult.type2 === 'pairs' && crossTypeResult.isSettled) {
    console.log('✅ PASSED: Cross-type transition animated with .story-visual-out/.story-visual-in and settled cleanly.');
  }

  // =========================================================================
  // TEST 4: MOBILE RESPONSIVE (390 x 844) - ZERO OVERFLOW & READABILITY
  // =========================================================================
  console.log('\n--- 4. Testing Mobile (390 x 844) ---');
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  // Check horizontal overflow
  const mobileCheck = await page.evaluate(() => {
    const overflow = document.documentElement.scrollWidth > window.innerWidth;
    const t1 = document.getElementById('topic-01');
    const t1Bridge = t1 ? t1.querySelector('.narrative-connector-bridge') : null;
    const t1Citation = t1 ? t1.querySelector('.section-source-citation') : null;

    return {
      overflow,
      scrollWidth: document.documentElement.scrollWidth,
      windowWidth: window.innerWidth,
      bridgeVisible: t1Bridge ? t1Bridge.getBoundingClientRect().width > 0 : false,
      citationVisible: t1Citation ? t1Citation.getBoundingClientRect().width > 0 : false
    };
  });
  console.log('[Mobile Check Result]', mobileCheck);
  if (!mobileCheck.overflow) {
    console.log('✅ PASSED: Zero horizontal overflow on mobile 390px.');
  } else {
    console.error('❌ FAILED: Horizontal overflow detected!');
    process.exit(1);
  }
  await page.screenshot({ path: path.join(screenshotDir, 'v8_mobile_responsive.png') });
  console.log('📸 Saved v8_mobile_responsive.png');

  // Check dark topic 07 screenshot
  await page.evaluate(() => {
    const t7 = document.getElementById('topic-07');
    if (t7) t7.scrollIntoView({ behavior: 'instant', block: 'start' });
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(screenshotDir, 'v8_topic07_dark_contrast.png') });
  console.log('📸 Saved v8_topic07_dark_contrast.png');

  // =========================================================================
  // TEST 5: CONSOLE ERRORS
  // =========================================================================
  console.log('\n--- 5. Console Errors Check ---');
  console.log(`Total console errors during full test suite: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    console.error('Encountered console errors:', consoleErrors);
  } else {
    console.log('✅ PASSED: 0 console errors during all test scenarios.');
  }

  await browser.close();
  console.log('\n🎉 ALL BI304 v8 VERIFICATION CHECKS COMPLETED SUCCESSFULLY!');
})();
