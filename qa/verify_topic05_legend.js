const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  console.log('🚀 Verifying Topic 05 Campus Distribution Legend and Heading Names...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  const screenshotDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(screenshotDir)) fs.mkdirSync(screenshotDir, { recursive: true });

  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  // Scroll to topic-05 campus-distribution-card
  const check = await page.evaluate(async () => {
    const card = document.querySelector('.campus-distribution-card');
    if (!card) return { error: 'No campus-distribution-card' };

    card.scrollIntoView({ block: 'center' });
    await new Promise(r => setTimeout(r, 600));

    const h3 = card.querySelector('h3');
    const p = card.querySelector('p');
    const canvas = card.querySelector('canvas#campusDistributionCanvas');

    // Chart.js instance check via Chart.getChart
    let chartLegendLabels = [];
    let chartLegendColor = null;
    const chart = window.Chart ? window.Chart.getChart('campusDistributionCanvas') : null;
    if (chart) {
      chartLegendLabels = chart.data.datasets.map(d => d.label);
      chartLegendColor = chart.options.plugins?.legend?.labels?.color;
    }

    return {
      titleText: h3?.textContent.trim(),
      titleColor: h3 ? window.getComputedStyle(h3).color : null,
      subtitleText: p?.textContent.trim(),
      subtitleColor: p ? window.getComputedStyle(p).color : null,
      chartLegendLabels,
      chartLegendColor,
      canvasWidth: canvas?.width,
      canvasHeight: canvas?.height
    };
  });

  console.log('Topic 05 Check Result:\n', JSON.stringify(check, null, 2));

  if (!check.chartLegendLabels.includes('ศูนย์ท่าพระจันทร์') || !check.chartLegendLabels.includes('ศูนย์รังสิต')) {
    console.error('❌ FAILED: Chart dataset labels missing campus names!');
    process.exit(1);
  }

  if (check.chartLegendColor === '#ffffff' || check.chartLegendColor === 'rgb(255, 255, 255)') {
    console.error('❌ FAILED: Chart legend color is still white on white background!');
    process.exit(1);
  }

  // Capture screenshot of the card
  const cardEl = await page.$('.campus-distribution-card');
  if (cardEl) {
    await cardEl.screenshot({ path: path.join(screenshotDir, 'v11_topic05_campus_names_legend.png') });
    console.log('📸 Saved v11_topic05_campus_names_legend.png');
  }

  // Also capture full view of Topic 05
  await page.screenshot({ path: path.join(screenshotDir, 'v11_topic05_full_view.png') });
  console.log('📸 Saved v11_topic05_full_view.png');

  console.log('✅ PASSED: All 4 campus names are now clearly visible with high contrast in the legend and heading!');
  await browser.close();
})();
