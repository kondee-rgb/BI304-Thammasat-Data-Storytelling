const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const SCREENSHOT_DIR = path.join(__dirname, 'screenshots');
if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function testV5Transitions() {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', err => errors.push(err.toString()));

  console.log('=== STEP 1: INITIAL LOAD & SYNCHRONIZATION ===');
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  await page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; });

  console.log('\n=== STEP 2: TEST SAME-TYPE IN-PLACE MORPHS ===');
  
  // Test Topic 01 (Vertical bars in-place update)
  const topic01Morph = await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-01"]');
    const content = mod.querySelector('.scroll-story-visual-content');
    const layerBefore = content.querySelector('.story-viz-layer');
    const barsBefore = layerBefore.querySelector('.story-vertical-bars');
    const bar0Before = barsBefore.children[0].querySelector('.story-vertical-fill').style.getPropertyValue('--bar-height');

    // Click step 2 (index 1)
    mod.querySelectorAll('.scroll-story-step')[1].click();
    await new Promise(r => setTimeout(r, 400));

    const layerAfter = content.querySelector('.story-viz-layer');
    const barsAfter = layerAfter.querySelector('.story-vertical-bars');
    const bar0After = barsAfter.children[0].querySelector('.story-vertical-fill').style.getPropertyValue('--bar-height');
    const sameElement = (layerBefore === layerAfter);

    return { sameElement, bar0Before, bar0After, activeIndex: mod.querySelector('.scroll-story-stage').dataset.activeIndex };
  });
  console.log('Topic 01 Vertical Bars In-Place Morph:', topic01Morph);

  // Test Topic 04 (Demographics: 100 person icons in-place update with transitionDelay)
  const topic04People = await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-04"]');
    const grid = mod.querySelector('.story-people-grid');
    const iconsBefore = Array.from(grid.querySelectorAll('.story-person'));
    const femaleCount0 = iconsBefore.filter(i => i.classList.contains('female')).length;

    // Click step 2 (Health: 71.5% female)
    mod.querySelectorAll('.scroll-story-step')[1].click();
    await new Promise(r => setTimeout(r, 200));

    const femaleCount1 = Array.from(grid.querySelectorAll('.story-person.female')).length;
    const sameGrid = (grid === mod.querySelector('.story-people-grid'));
    const metricText = mod.querySelector('.scroll-story-metric').textContent.trim();

    return { sameGrid, femaleCount0, femaleCount1, metricText };
  });
  console.log('Topic 04 Person Icons In-Place Update:', topic04People);

  // Test Topic 05 (Stacked segmented bar in-place width morph)
  const topic05Stacked = await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-05"]');
    const track = mod.querySelector('.story-stacked-track');
    const seg0Before = track.children[0].style.getPropertyValue('--segment-width');

    // Click step 3 (BE 2545: 26% Tha Prachan, 70% Rangsit)
    mod.querySelectorAll('.scroll-story-step')[2].click();
    await new Promise(r => setTimeout(r, 400));

    const seg0After = track.children[0].style.getPropertyValue('--segment-width');
    const seg1After = track.children[1].style.getPropertyValue('--segment-width');
    const sameTrack = (track === mod.querySelector('.story-stacked-track'));

    return { sameTrack, seg0Before, seg0After, seg1After };
  });
  console.log('Topic 05 Stacked Segments In-Place Morph:', topic05Stacked);

  console.log('\n=== STEP 3: TEST CROSS-TYPE SCENE TRANSITIONS ===');

  // Test Topic 03 (Horizontal bars -> Pairs)
  const topic03Cross = await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-03"]');
    const content = mod.querySelector('.scroll-story-visual-content');

    // Click step 1 (horizontal bars)
    mod.querySelectorAll('.scroll-story-step')[0].click();
    await new Promise(r => setTimeout(r, 200));
    const type0 = content.querySelector('.story-viz-layer')?.dataset.visualType;

    // Click step 2 (pairs)
    mod.querySelectorAll('.scroll-story-step')[1].click();
    // Check during transition
    const isTransitioning = content.classList.contains('is-scene-transition') || !!content.querySelector('.story-viz-layer--leaving');
    await new Promise(r => setTimeout(r, 850)); // Wait for transition to complete
    const type1 = content.querySelector('.story-viz-layer')?.dataset.visualType;
    const isTransitionDone = !content.classList.contains('is-scene-transition');

    return { type0, type1, isTransitioning, isTransitionDone };
  });
  console.log('Topic 03 Cross-Type Transition (horizontal -> pairs):', topic03Cross);

  // Test Topic 07 (Badges -> Vertical Bars -> Pairs)
  const topic07Cross = await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-07"]');
    const content = mod.querySelector('.scroll-story-visual-content');

    mod.querySelectorAll('.scroll-story-step')[0].click();
    await new Promise(r => setTimeout(r, 100));
    const type0 = content.querySelector('.story-viz-layer')?.dataset.visualType;

    mod.querySelectorAll('.scroll-story-step')[1].click();
    await new Promise(r => setTimeout(r, 850));
    const type1 = content.querySelector('.story-viz-layer')?.dataset.visualType;

    mod.querySelectorAll('.scroll-story-step')[2].click();
    await new Promise(r => setTimeout(r, 850));
    const type2 = content.querySelector('.story-viz-layer')?.dataset.visualType;

    return { type0, type1, type2 };
  });
  console.log('Topic 07 Multi-Type Transition (badges -> vertical -> pairs):', topic07Cross);

  console.log('\n=== STEP 4: RAPID STEP SWITCHING & REVERSE SCROLL TEST ===');
  const rapidTest = await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-01"]');
    const steps = mod.querySelectorAll('.scroll-story-step');

    // Rapid clicking 0 -> 2 -> 1 -> 0 -> 2 in quick succession
    steps[0].click();
    await new Promise(r => setTimeout(r, 60));
    steps[2].click();
    await new Promise(r => setTimeout(r, 60));
    steps[1].click();
    await new Promise(r => setTimeout(r, 60));
    steps[0].click();
    await new Promise(r => setTimeout(r, 60));
    steps[2].click();
    await new Promise(r => setTimeout(r, 850)); // Allow final state to settle

    const stage = mod.querySelector('.scroll-story-stage');
    const metric = stage.querySelector('.scroll-story-metric').textContent.trim();
    const activeStep = Array.from(steps).findIndex(s => s.classList.contains('is-active'));
    const leavingLayers = stage.querySelectorAll('.story-viz-layer--leaving').length;

    return { metric, activeStep, leavingLayers };
  });
  console.log('Rapid Switching Settle Result:', rapidTest);

  console.log('\n=== STEP 5: CAPTURE VERIFICATION SCREENSHOTS ===');
  // Topic 01 morph
  await page.evaluate(() => {
    const t1 = document.getElementById('topic-01');
    if (t1) window.scrollTo(0, t1.offsetTop + 140);
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'v5_topic01_morph.png') });
  console.log('  Saved: v5_topic01_morph.png');

  // Topic 04 people transition
  await page.evaluate(() => {
    const t4 = document.getElementById('topic-04');
    if (t4) window.scrollTo(0, t4.offsetTop + 140);
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'v5_topic04_people_transition.png') });
  console.log('  Saved: v5_topic04_people_transition.png');

  // Mobile 390px test
  await page.setViewport({ width: 390, height: 844 });
  await page.evaluate(() => {
    const t5 = document.getElementById('topic-05');
    if (t5) window.scrollTo(0, t5.offsetTop + 100);
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'v5_mobile_v5_transition.png') });
  console.log('  Saved: v5_mobile_v5_transition.png');

  console.log('\nConsole Errors during test:', errors.length);
  if (errors.length > 0) {
    errors.forEach(e => console.log('  [Console Error]:', e));
  } else {
    console.log('  SUCCESS: 0 console errors during v5 transition testing!');
  }

  await browser.close();
}

testV5Transitions().catch(console.error);
