const puppeteer = require('puppeteer');

(async () => {
  console.log('🚀 Testing Hero Timeline 90-Year Runner Fixes...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', err => errors.push(err.message));

  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });

  // Test 1: Check Scroll 0 (First Fold)
  console.log('\n--- 1. Testing Scroll 0 (First Screen) ---');
  await page.evaluate(() => window.scrollTo(0, 0));
  await new Promise(r => setTimeout(r, 200));

  const scroll0Data = await page.evaluate(() => {
    const p = el => el ? { top: Math.round(el.getBoundingClientRect().top), bottom: Math.round(el.getBoundingClientRect().bottom) } : null;
    const desc = p(document.querySelector('.hero-lead-desc'));
    const btn = p(document.querySelector('.hero-scroll-pill-btn'));
    const pole = p(document.querySelector('.grid-box-pole'));
    const leader = p(document.getElementById('studentLeader'));
    const scholar = p(document.getElementById('studentScholar'));
    return { desc, btn, pole, leader, scholar };
  });
  console.log('Scroll 0 Data:', JSON.stringify(scroll0Data, null, 2));

  // Verify that pole (2477) and students do NOT collide with hero lead desc or CTA button
  const poleBelowBtn = scroll0Data.pole.top >= scroll0Data.btn.bottom;
  console.log(`✅ 2477 Pin is cleanly below Hero CTA button: ${poleBelowBtn} (Pole top: ${scroll0Data.pole.top}, Btn bottom: ${scroll0Data.btn.bottom})`);
  await page.screenshot({ path: 'qa/screenshots/fixed_scroll_0.png' });

  // Test 2: Check Scroll 600 (Runway in view)
  console.log('\n--- 2. Testing Scroll 600 (Timeline in View) ---');
  await page.evaluate(() => window.scrollTo(0, 600));
  await new Promise(r => setTimeout(r, 200));

  const scroll600Data = await page.evaluate(() => {
    const p = el => el ? { top: Math.round(el.getBoundingClientRect().top), bottom: Math.round(el.getBoundingClientRect().bottom) } : null;
    const header = p(document.getElementById('mainHeader'));
    const pole = p(document.querySelector('.grid-box-pole'));
    return { header, pole };
  });
  console.log('Scroll 600 Data:', JSON.stringify(scroll600Data, null, 2));
  const poleClearOfHeader = scroll600Data.pole.top >= scroll600Data.header.bottom + 20;
  console.log(`✅ 2477 Pin has generous clearance from top header: ${poleClearOfHeader} (Pole top: ${scroll600Data.pole.top}, Header bottom: ${scroll600Data.header.bottom})`);
  await page.screenshot({ path: 'qa/screenshots/fixed_scroll_600.png' });

  // Test 3: Check Scroll 1500 & End of Runway
  console.log('\n--- 3. Testing Scroll at End of Runway & Deep Scroll ---');
  const scrollTests = [1200, 1600, 2000, 2500];
  for (const sy of scrollTests) {
    await page.evaluate(y => window.scrollTo(0, y), sy);
    await new Promise(r => setTimeout(r, 200));

    const check = await page.evaluate(() => {
      const p = el => el ? { top: Math.round(el.getBoundingClientRect().top), bottom: Math.round(el.getBoundingClientRect().bottom) } : null;
      const slot2 = p(document.querySelector('.grid-box-slot2'));
      const leader = p(document.getElementById('studentLeader'));
      const scholar = p(document.getElementById('studentScholar'));
      const kfTitle = p(document.querySelector('#key-findings .summary-main-title'));
      return { slot2, leader, scholar, kfTitle };
    });

    console.log(`\nAt ScrollY ${sy}:`);
    console.log(`- 2567 Pin bottom: ${check.slot2.bottom}`);
    console.log(`- Student Scholar bottom: ${check.scholar.bottom} (Diff from Pin: ${check.scholar.bottom - check.slot2.bottom}px)`);
    console.log(`- Student Leader bottom: ${check.leader.bottom} (Diff from Pin: ${check.leader.bottom - check.slot2.bottom}px)`);
    console.log(`- Next Section Header top: ${check.kfTitle.top} (Whitespace to Scholar: ${check.kfTitle.top - check.scholar.bottom}px)`);

    const scholarNeverExceedsPin = check.scholar.bottom <= check.slot2.bottom + 5;
    const leaderNeverExceedsPin = check.leader.bottom <= check.slot2.bottom + 5;
    const safeGapToNextHeader = check.kfTitle.top >= check.scholar.bottom + 60;

    console.log(`  * Scholar clamped at/above Pin: ${scholarNeverExceedsPin}`);
    console.log(`  * Leader clamped at/above Pin: ${leaderNeverExceedsPin}`);
    console.log(`  * Safe Whitespace to Next Section: ${safeGapToNextHeader}`);

    await page.screenshot({ path: `qa/screenshots/fixed_scroll_${sy}.png` });
  }

  // Also test clicking the CTA button
  console.log('\n--- 4. Testing CTA button click ---');
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.click('.hero-scroll-pill-btn');
  await new Promise(r => setTimeout(r, 600));
  const scrolledYAfterClick = await page.evaluate(() => window.pageYOffset);
  console.log(`- Scroll position after clicking CTA: ${scrolledYAfterClick}px`);

  console.log('\n--- Console Errors ---');
  console.log(errors.length === 0 ? '🎉 0 Errors!' : `❌ Errors: ${errors.join(', ')}`);

  await browser.close();
  process.exit(errors.length === 0 ? 0 : 1);
})();
