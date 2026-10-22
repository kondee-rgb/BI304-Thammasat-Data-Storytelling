const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const breakpoints = [
  { name: '360', width: 360, height: 740 },
  { name: '390', width: 390, height: 844 },
  { name: '768', width: 768, height: 1024 },
  { name: '1024', width: 1024, height: 768 },
  { name: '1440', width: 1440, height: 900 }
];

const sections = [
  'hero',
  'key-findings',
  'topic-01',
  'topic-02',
  'topic-03',
  'topic-04',
  'topic-05',
  'topic-06',
  'topic-07',
  'topic-08',
  'topic-09',
  'topic-10',
  'methodology',
  'finish'
];

(async () => {
  const outputDir = path.join(__dirname, 'phase6_screens');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();

  for (const bp of breakpoints) {
    console.log(`Capturing breakpoint ${bp.name}px (${bp.width}x${bp.height})...`);
    await page.setViewport({ width: bp.width, height: bp.height, deviceScaleFactor: 1 });
    await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });

    // Wait 1.5s for charts and map tiles to stabilize
    await new Promise(r => setTimeout(r, 1500));

    // Capture each section
    for (const sec of sections) {
      const el = await page.$(`#${sec}`);
      if (el) {
        // Scroll element into view
        await page.evaluate((s) => {
          const target = document.getElementById(s);
          if (target) target.scrollIntoView({ behavior: 'instant', block: 'start' });
        }, sec);

        await new Promise(r => setTimeout(r, 400));
        const filename = path.join(outputDir, `${sec}_${bp.name}px.png`);
        await page.screenshot({ path: filename, fullPage: false });
      }
    }
  }

  await browser.close();
  console.log('All Phase 6 screenshots captured successfully!');
})();
