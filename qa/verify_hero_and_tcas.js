const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  // 1. Desktop Test (1440x900)
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  
  // Wait for doorway entrance animation to complete
  await new Promise(r => setTimeout(r, 2200));

  // Screenshot Hero on desktop
  const hero = await page.$('#hero');
  if (hero) {
    await hero.screenshot({ path: 'qa/screenshots/v12_hero_doorway_desktop.png' });
    console.log('Saved qa/screenshots/v12_hero_doorway_desktop.png');
  }

  const stage = await page.$('.central-track-stage');
  if (stage) {
    await stage.screenshot({ path: 'qa/screenshots/v12_doorway_stage_detail.png' });
    console.log('Saved qa/screenshots/v12_doorway_stage_detail.png');
  }

  // Scroll to Topic 03 to test TCAS KPI
  await page.evaluate(() => {
    const el = document.getElementById('topic-03');
    if (el) el.scrollIntoView({ behavior: 'instant' });
  });

  // Wait for counter animation to finish
  await new Promise(r => setTimeout(r, 2500));

  const tcasCard = await page.$('#topic-03 .faculties-white-card');
  if (tcasCard) {
    await tcasCard.screenshot({ path: 'qa/screenshots/v12_topic03_tcas_kpi.png' });
    console.log('Saved qa/screenshots/v12_topic03_tcas_kpi.png');
  }

  // Check text content of the 3rd KPI item in Topic 03
  const tcasKpiInfo = await page.evaluate(() => {
    const item = document.querySelector('.fac-kpi-item.tu-stagger-3');
    if (!item) return null;
    return {
      numText: item.querySelector('.kpi-num') ? item.querySelector('.kpi-num').innerText : null,
      lblText: item.querySelector('.kpi-lbl') ? item.querySelector('.kpi-lbl').innerText : null,
      title: item.getAttribute('title')
    };
  });
  console.log('Topic 03 KPI evaluated:', JSON.stringify(tcasKpiInfo, null, 2));

  // 2. Mobile Test (390x844 iPhone 12/13/14)
  await page.setViewport({ width: 390, height: 844, isMobile: true });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  const heroMobile = await page.$('#hero');
  if (heroMobile) {
    await heroMobile.screenshot({ path: 'qa/screenshots/v12_hero_doorway_mobile.png' });
    console.log('Saved qa/screenshots/v12_hero_doorway_mobile.png');
  }

  await browser.close();
  console.log('All tests completed successfully!');
})();
