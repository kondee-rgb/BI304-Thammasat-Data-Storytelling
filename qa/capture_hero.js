const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  const hero = await page.$('#hero');
  if (hero) {
    await hero.screenshot({ path: 'qa/screenshots/current_hero.png' });
    console.log('Saved qa/screenshots/current_hero.png');
  }
  const stage = await page.$('.central-track-stage');
  if (stage) {
    await stage.screenshot({ path: 'qa/screenshots/current_stage.png' });
    console.log('Saved qa/screenshots/current_stage.png');
  }
  await browser.close();
})();
