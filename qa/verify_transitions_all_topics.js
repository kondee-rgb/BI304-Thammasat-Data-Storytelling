const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', err => errors.push(err.message));

  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  console.log('1. Checking graph stages in DOM:');
  const graphCount = await page.evaluate(() => {
    return document.querySelectorAll('.tu-graph-stage').length;
  });
  console.log(`Found ${graphCount} .tu-graph-stage elements across topics.`);

  console.log('2. Testing crossfade grid layout in Topic 07:');
  // Scroll to topic-07 and step 2
  await page.evaluate(() => {
    const el = document.getElementById('topic-07');
    if (el) el.scrollIntoView({ behavior: 'instant' });
  });
  await new Promise(r => setTimeout(r, 600));

  // Trigger step 2 (crossfade from badges to vertical)
  await page.evaluate(() => {
    const steps = document.querySelectorAll('#topic-07 .scroll-story-step');
    if (steps[1]) steps[1].scrollIntoView({ behavior: 'instant', block: 'center' });
  });

  // Check immediately while crossfading
  await new Promise(r => setTimeout(r, 120));
  const crossfadeInfo = await page.evaluate(() => {
    const content = document.querySelector('#topic-07 .scroll-story-visual-content');
    if (!content) return null;
    const computed = window.getComputedStyle(content);
    const layers = Array.from(content.children).map(c => ({
      className: c.className,
      top: c.getBoundingClientRect().top,
      gridArea: window.getComputedStyle(c).gridArea
    }));
    return {
      display: computed.display,
      isCrossfading: content.classList.contains('is-crossfading'),
      layers
    };
  });
  console.log('Topic 07 crossfade layout:', JSON.stringify(crossfadeInfo, null, 2));

  // Wait for it to settle and screenshot
  await new Promise(r => setTimeout(r, 800));
  const stage07 = await page.$('#topic-07 .scroll-story-stage');
  if (stage07) {
    await stage07.screenshot({ path: 'qa/screenshots/v13_topic07_step2_vertical.png' });
    console.log('Saved qa/screenshots/v13_topic07_step2_vertical.png');
  }

  // 3. Test atmospheric transition between Topic 07 and Topic 08
  console.log('3. Capturing Topic 07 to 08 transition bridge:');
  await page.evaluate(() => {
    const bridge = document.querySelector('#topic-07 .narrative-connector-bridge');
    if (bridge) bridge.scrollIntoView({ behavior: 'instant', block: 'center' });
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'qa/screenshots/v13_transition_07_to_08.png' });
  console.log('Saved qa/screenshots/v13_transition_07_to_08.png');

  // 4. Test Topic 08 green stage
  console.log('4. Testing Topic 08 green stage:');
  await page.evaluate(() => {
    const el = document.getElementById('topic-08');
    if (el) el.scrollIntoView({ behavior: 'instant' });
  });
  await new Promise(r => setTimeout(r, 600));
  const stage08 = await page.$('#topic-08 .scroll-story-stage');
  if (stage08) {
    await stage08.screenshot({ path: 'qa/screenshots/v13_topic08_stage.png' });
    console.log('Saved qa/screenshots/v13_topic08_stage.png');
  }

  // 5. Test Topic 09 hospital stage
  console.log('5. Testing Topic 09 hospital stage:');
  await page.evaluate(() => {
    const el = document.getElementById('topic-09');
    if (el) el.scrollIntoView({ behavior: 'instant' });
  });
  await new Promise(r => setTimeout(r, 600));
  const stage09 = await page.$('#topic-09 .scroll-story-stage');
  if (stage09) {
    await stage09.screenshot({ path: 'qa/screenshots/v13_topic09_stage.png' });
    console.log('Saved qa/screenshots/v13_topic09_stage.png');
  }

  // 6. Test full page console errors
  console.log(`6. Total console errors: ${errors.length}`);
  if (errors.length > 0) {
    console.log('Errors:', errors);
  }

  await browser.close();
  console.log('All transition tests completed!');
})();
