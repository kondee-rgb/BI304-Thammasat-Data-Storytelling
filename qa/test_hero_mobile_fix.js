const puppeteer = require('puppeteer');

(async () => {
  console.log('📱 Testing Mobile (390x844) Hero Timeline Fixes...');
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });

  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', err => errors.push(err.message));

  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });

  // 1. Scroll 0
  await page.evaluate(() => window.scrollTo(0, 0));
  await new Promise(r => setTimeout(r, 200));

  const scroll0 = await page.evaluate(() => {
    const p = el => el ? { top: Math.round(el.getBoundingClientRect().top), bottom: Math.round(el.getBoundingClientRect().bottom) } : null;
    return {
      btn: p(document.querySelector('.hero-scroll-pill-btn')),
      pole: p(document.querySelector('.grid-box-pole')),
      leader: p(document.getElementById('studentLeader')),
      scholar: p(document.getElementById('studentScholar'))
    };
  });
  console.log('Mobile Scroll 0:', JSON.stringify(scroll0, null, 2));
  console.log(`- Pole below btn: ${scroll0.pole.top >= scroll0.btn.bottom}`);
  await page.screenshot({ path: 'qa/screenshots/mobile_fixed_scroll_0.png' });

  // 2. Scroll 500
  await page.evaluate(() => window.scrollTo(0, 500));
  await new Promise(r => setTimeout(r, 200));
  await page.screenshot({ path: 'qa/screenshots/mobile_fixed_scroll_500.png' });

  // 3. Scroll 1200
  await page.evaluate(() => window.scrollTo(0, 1200));
  await new Promise(r => setTimeout(r, 200));

  const scroll1200 = await page.evaluate(() => {
    const p = el => el ? { top: Math.round(el.getBoundingClientRect().top), bottom: Math.round(el.getBoundingClientRect().bottom) } : null;
    return {
      slot2: p(document.querySelector('.grid-box-slot2')),
      scholar: p(document.getElementById('studentScholar')),
      leader: p(document.getElementById('studentLeader')),
      kfTitle: p(document.querySelector('#key-findings .summary-main-title'))
    };
  });
  console.log('Mobile Scroll 1200:', JSON.stringify(scroll1200, null, 2));
  const scholarAbovePin = scroll1200.scholar.bottom <= scroll1200.slot2.bottom + 5;
  const safeGap = scroll1200.kfTitle.top >= scroll1200.scholar.bottom + 40;
  console.log(`- Scholar clamped at/above Pin: ${scholarAbovePin}`);
  console.log(`- Safe gap to next header: ${safeGap}`);

  await page.screenshot({ path: 'qa/screenshots/mobile_fixed_scroll_1200.png' });

  console.log('\nMobile Errors:', errors.length === 0 ? '🎉 0 Errors!' : errors.join(', '));
  await browser.close();
  process.exit(errors.length === 0 ? 0 : 1);
})();
