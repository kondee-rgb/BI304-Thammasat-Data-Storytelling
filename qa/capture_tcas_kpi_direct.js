const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  
  await page.evaluate(() => {
    const kpi = document.querySelector('.faculties-kpi-row');
    if (kpi) kpi.scrollIntoView({ block: 'center' });
  });

  // Wait 3.5s for counter to finish counting up to 14.0
  await new Promise(r => setTimeout(r, 3500));

  const kpiRow = await page.$('.faculties-kpi-row');
  if (kpiRow) {
    await kpiRow.screenshot({ path: 'qa/screenshots/v12_tcas_kpi_row_clean.png' });
    console.log('Saved qa/screenshots/v12_tcas_kpi_row_clean.png');
  }

  await browser.close();
})();
