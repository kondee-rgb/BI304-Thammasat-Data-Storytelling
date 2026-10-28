const puppeteer = require('puppeteer');

async function runContrastAudit() {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();

  const viewports = [
    { name: 'Desktop 1440', w: 1440, h: 900 },
    { name: 'Mobile 390', w: 390, h: 844 }
  ];

  for (const vp of viewports) {
    await page.setViewport({ width: vp.w, height: vp.h });
    await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

    const issues = await page.evaluate(() => {
      function parseRgbStr(s) {
        const m = s.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);
        if (!m) return null;
        return { r: +m[1], g: +m[2], b: +m[3], a: m[4] !== undefined ? +m[4] : 1 };
      }

      function getEffectiveBg(el) {
        let cur = el;
        while (cur && cur !== document.documentElement) {
          const cs = getComputedStyle(cur);
          const bg = cs.backgroundColor;
          const parsed = parseRgbStr(bg);
          if (parsed && parsed.a > 0.5) return parsed;
          if (cs.backgroundImage && cs.backgroundImage !== 'none') {
            if (cur.classList.contains('scroll-story-stage') || cur.classList.contains('scroll-story-step')) {
              return { r: 255, g: 255, b: 255, a: 1 };
            }
          }
          cur = cur.parentElement;
        }
        return { r: 255, g: 255, b: 255, a: 1 };
      }

      function lum(c) {
        const a = [c.r, c.g, c.b].map(v => {
          v /= 255;
          return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
        });
        return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
      }

      function contrast(c1, c2) {
        const l1 = lum(c1);
        const l2 = lum(c2);
        return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
      }

      const lowContrast = [];
      const textEls = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, a, th, td, figcaption, label, button, .lbl, .val');

      textEls.forEach(el => {
        const text = el.textContent.trim();
        if (!text || text.length < 2) return;
        const rect = el.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) return;
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) < 0.1) return;

        const fg = parseRgbStr(cs.color);
        if (!fg) return;
        const bg = getEffectiveBg(el);
        const cr = contrast(fg, bg);

        const fontSize = parseFloat(cs.fontSize) || 16;
        const fontWeight = cs.fontWeight;
        const isLarge = fontSize >= 24 || (fontSize >= 18.5 && (fontWeight === 'bold' || parseInt(fontWeight) >= 600));
        const required = isLarge ? 3.0 : 4.5;

        if (cr < required && !el.closest('#dinoGameModal')) {
          lowContrast.push({
            tag: el.tagName,
            cls: el.className,
            text: text.slice(0, 30),
            ratio: +cr.toFixed(2),
            required,
            fg: cs.color,
            bg: `rgb(${bg.r},${bg.g},${bg.b})`
          });
        }
      });

      return lowContrast;
    });

    console.log(`[${vp.name}] Potential low contrast elements: ${issues.length}`);
    if (issues.length > 0) {
      issues.slice(0, 5).forEach(it => console.log('  ', it));
    }
  }

  await browser.close();
}

runContrastAudit().catch(console.error);
