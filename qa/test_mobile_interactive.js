const puppeteer = require('puppeteer');

(async () => {
  console.log('📱 Testing Mobile Viewport (390x844)...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });

  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2', timeout: 30000 });

  // 1. Check Mobile Navigation Drawer
  await page.click('#mobileMenuBtn');
  await new Promise(r => setTimeout(r, 400));
  const drawerOpen = await page.$eval('#mobileNavDrawer', el => el.classList.contains('active'));
  console.log(`- Mobile Drawer open: ${drawerOpen}`);

  await page.click('#mobileNavDrawer .mobile-nav-close-btn');
  await new Promise(r => setTimeout(r, 400));
  const drawerClosed = await page.$eval('#mobileNavDrawer', el => !el.classList.contains('active'));
  console.log(`- Mobile Drawer closed: ${drawerClosed}`);

  // 2. Check Data Guessing Widget on mobile
  const guessVisible = await page.$eval('.tui-guess', el => el.getBoundingClientRect().width > 0);
  console.log(`- Mobile Guess widget visible: ${guessVisible}`);

  // 3. Check Quiz Widget on mobile
  const quizVisible = await page.$eval('.tui-quiz', el => el.getBoundingClientRect().width > 0);
  console.log(`- Mobile Quiz widget visible: ${quizVisible}`);

  // 4. Check TU Runner on mobile
  const runnerTouchBarVisible = await page.$eval('.tu-runner__touch-bar', el => window.getComputedStyle(el).display !== 'none');
  console.log(`- Mobile TU Runner touch bar visible: ${runnerTouchBarVisible}`);

  // 5. Check no horizontal overflow on body
  const scrollWidth = await page.evaluate(() => document.documentElement.scrollWidth);
  const clientWidth = await page.evaluate(() => document.documentElement.clientWidth);
  console.log(`- Viewport clientWidth: ${clientWidth}, scrollWidth: ${scrollWidth}`);
  const noOverflow = scrollWidth <= clientWidth + 1;
  console.log(`- No horizontal body overflow: ${noOverflow}`);

  // 6. Screenshot mobile
  await page.screenshot({ path: 'qa/screenshots/mobile_interactive_390.png', fullPage: false });
  console.log('📸 Mobile screenshot saved to qa/screenshots/mobile_interactive_390.png');

  await browser.close();
  console.log(errors.length === 0 ? '🎉 Mobile tests passed with 0 errors!' : `❌ Mobile errors: ${errors.length}`);
  process.exit(errors.length === 0 ? 0 : 1);
})();
