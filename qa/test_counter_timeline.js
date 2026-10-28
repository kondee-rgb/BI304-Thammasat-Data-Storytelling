const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  await page.evaluate(() => {
    document.getElementById('topic-03').scrollIntoView({ behavior: 'instant' });
  });
  for (let i = 0; i < 8; i++) {
    await new Promise(r => setTimeout(r, 500));
    const val = await page.evaluate(() => {
      const item = document.querySelector('.fac-kpi-item.tu-stagger-3');
      return item ? item.querySelector('.kpi-num').innerText : null;
    });
    console.log('t = ' + ((i+1)*500) + 'ms: ' + val);
  }
  await browser.close();
})();
