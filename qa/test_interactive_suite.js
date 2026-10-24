const puppeteer = require('puppeteer');

(async () => {
  console.log('🚀 Starting Comprehensive Interactive Test Suite...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push(`Console Error: ${msg.text()}`);
    }
  });
  page.on('pageerror', err => {
    errors.push(`Page Error: ${err.message}`);
  });

  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2', timeout: 30000 });
  console.log('✅ Page loaded successfully');

  // Test 1: Check Data Guessing Widget
  console.log('\n🔍 Testing Data Guessing Widget ([data-tu-guess])...');
  const guessExists = await page.$('[data-tu-guess]') !== null;
  console.log(`- Guess widget in DOM: ${guessExists}`);

  const guessQuestion = await page.$eval('.tui-guess .tui-q', el => el.textContent.trim());
  console.log(`- First guess question: "${guessQuestion}"`);

  // Interact with slider and submit guess
  const initialBigNum = await page.$eval('.tui-guess .tui-bignum', el => el.textContent.trim());
  console.log(`- Slider initial value: ${initialBigNum}`);

  await page.click('.tui-guess .tui-btn');
  await new Promise(r => setTimeout(r, 1200)); // wait for bar animation

  const verdictText = await page.$eval('.tui-guess .tui-verdict', el => el.textContent.trim());
  console.log(`- Guess verdict: "${verdictText}"`);

  // Click next question
  await page.click('.tui-guess .tui-reveal .tui-btn');
  const secondQ = await page.$eval('.tui-guess .tui-q', el => el.textContent.trim());
  console.log(`- Second question loaded: "${secondQ}"`);

  // Test 2: Check Quiz Widget
  console.log('\n🔍 Testing Quiz Widget ([data-tu-quiz])...');
  const quizExists = await page.$('[data-tu-quiz]') !== null;
  console.log(`- Quiz widget in DOM: ${quizExists}`);

  const introTitle = await page.$eval('.tui-quiz .tui-q', el => el.textContent.trim());
  console.log(`- Quiz intro title: "${introTitle}"`);

  // Start quiz
  await page.click('.tui-quiz .tui-intro .tui-btn');
  await new Promise(r => setTimeout(r, 300));

  const q1Text = await page.$eval('.tui-quiz .tui-q', el => el.textContent.trim());
  console.log(`- Q1 active: "${q1Text}"`);

  const optCount = await page.$$eval('.tui-quiz .tui-opt', els => els.length);
  console.log(`- Options count: ${optCount}`);

  // Select first option
  await page.click('.tui-quiz .tui-opt');
  await new Promise(r => setTimeout(r, 300));

  const fbVerdict = await page.$eval('.tui-quiz .tui-verdict', el => el.textContent.trim());
  console.log(`- Q1 Feedback verdict: "${fbVerdict}"`);

  // Test 3: Check TU Runner Mini-Game
  console.log('\n🔍 Testing TU Runner Mini-Game ([data-tu-runner])...');
  const runnerExists = await page.$('[data-tu-runner]') !== null;
  console.log(`- Runner widget in DOM: ${runnerExists}`);

  const runnerPlayBtn = await page.$('.tu-runner [data-play]');
  console.log(`- Play button present: ${runnerPlayBtn !== null}`);

  const runnerCanvas = await page.$('.tu-runner canvas.tu-runner__canvas');
  console.log(`- Canvas present: ${runnerCanvas !== null}`);

  const jumpTouchBtn = await page.$('.tu-runner [data-jump]');
  console.log(`- Mobile Jump Touch button present: ${jumpTouchBtn !== null}`);

  const duckTouchBtn = await page.$('.tu-runner [data-duck]');
  console.log(`- Mobile Duck Touch button present: ${duckTouchBtn !== null}`);

  // Test 4: Check Cockpit Sliders & Readiness Score
  console.log('\n🔍 Testing Strategy Cockpit Score...');
  const initialScore = await page.$eval('#cockpitCompositeScore', el => el.textContent.trim());
  console.log(`- Cockpit initial composite score: ${initialScore}`);

  // Test 5: Check Flourish Hub Modal
  console.log('\n🔍 Testing Flourish Hub Modal...');
  await page.evaluate(() => window.openFlourishHubModal());
  await new Promise(r => setTimeout(r, 500));

  const modalDisplay = await page.$eval('#flourishHubModal', el => window.getComputedStyle(el).display);
  console.log(`- Modal display style after open: ${modalDisplay}`);

  const activeSceneTitle = await page.$eval('#flourishDetailPane .flourish-detail-title', el => el.textContent.trim());
  console.log(`- Active Flourish scene title: "${activeSceneTitle}"`);

  const csvDownloadHref = await page.$eval('#flourishDetailPane .flourish-btn-primary', el => el.getAttribute('href'));
  console.log(`- CSV download button href: "${csvDownloadHref}"`);

  await page.evaluate(() => window.closeFlourishHubModal());
  await new Promise(r => setTimeout(r, 300));
  const modalDisplayAfterClose = await page.$eval('#flourishHubModal', el => window.getComputedStyle(el).display);
  console.log(`- Modal display style after close: ${modalDisplayAfterClose}`);

  // Final Console Error Check
  console.log('\n📋 Console Error Summary:');
  if (errors.length === 0) {
    console.log('🎉 0 CONSOLE ERRORS! All tests passed with flying colors.');
  } else {
    console.log(`❌ Found ${errors.length} error(s):`);
    errors.forEach(e => console.log('  -', e));
  }

  await browser.close();
  process.exit(errors.length === 0 ? 0 : 1);
})();
