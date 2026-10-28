const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const SCREENSHOT_DIR = path.join(__dirname, 'screenshots');
if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function runTests() {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
  });

  const page = await browser.newPage();
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });
  page.on('pageerror', err => {
    consoleErrors.push(err.toString());
  });

  console.log('=== STEP 1: LOAD PAGE & CHECK CONSOLE ERRORS ===');
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });
  console.log(`Page loaded. Console errors: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    consoleErrors.forEach(e => console.log('  [Console Error]:', e));
  }

  console.log('\n=== STEP 2: HORIZONTAL OVERFLOW ACROSS VIEWPORTS ===');
  const viewports = [
    { name: 'Desktop 1440', w: 1440, h: 900 },
    { name: 'Laptop 1280', w: 1280, h: 800 },
    { name: 'Laptop 1024', w: 1024, h: 768 },
    { name: 'Mobile 390', w: 390, h: 844 }
  ];

  for (const vp of viewports) {
    await page.setViewport({ width: vp.w, height: vp.h });
    await page.evaluate(() => window.scrollTo(0, 0));
    await new Promise(r => setTimeout(r, 200));

    const overflowInfo = await page.evaluate(() => {
      const docW = document.documentElement.clientWidth;
      const scrollW = document.documentElement.scrollWidth;
      const bodyScrollW = document.body.scrollWidth;
      const offenders = [];
      document.querySelectorAll('*').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.right > docW + 2) {
          const id = el.id ? `#${el.id}` : '';
          const cls = el.className && typeof el.className === 'string' ? `.${el.className.trim().split(/\s+/).slice(0, 2).join('.')}` : '';
          offenders.push({ tag: el.tagName, sel: `${id}${cls}`, right: Math.round(r.right), excess: Math.round(r.right - docW) });
        }
      });
      return { docW, scrollW, bodyScrollW, hasOverflow: scrollW > docW, offenders: offenders.slice(0, 5) };
    });

    console.log(`Viewport ${vp.name} (${vp.w}px): docW=${overflowInfo.docW}, scrollW=${overflowInfo.scrollW}, hasOverflow=${overflowInfo.hasOverflow}`);
    if (overflowInfo.offenders.length > 0) {
      console.log('  Offenders:', overflowInfo.offenders);
    }
  }

  console.log('\n=== STEP 3: TOPIC 10 POSITION STICKY & STACKING VERIFICATION ===');
  await page.setViewport({ width: 1440, height: 900 });
  await page.evaluate(() => {
    document.documentElement.style.scrollBehavior = 'auto';
  });

  const stickyStyles = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('#topic-10 .tu-pillar-card'));
    const mapCol = document.querySelector('#topic-10 .tu-route-map-col');
    return {
      cardCount: cards.length,
      mapColSticky: getComputedStyle(mapCol).position,
      cards: cards.map((c, i) => {
        const cs = getComputedStyle(c);
        return {
          idx: i,
          position: cs.position,
          top: cs.top,
          zIndex: cs.zIndex
        };
      })
    };
  });
  console.log('Sticky Styles in Topic 10:');
  console.log(`  Map Column position: ${stickyStyles.mapColSticky}`);
  stickyStyles.cards.forEach(c => {
    console.log(`  Card ${c.idx}: position=${c.position}, top=${c.top}, zIndex=${c.zIndex}`);
  });

  console.log('\n=== STEP 4: SCROLL SIMULATION & STACKING BEHAVIOR ===');
  // Scroll to topic 10
  const topic10Pos = await page.evaluate(() => {
    const el = document.getElementById('topic-10');
    return el ? el.offsetTop : 0;
  });
  console.log(`Topic 10 offsetTop: ${topic10Pos}px`);

  // Scroll into the middle of the stack
  await page.evaluate((y) => {
    window.scrollTo(0, y + 600);
  }, topic10Pos);
  await new Promise(r => setTimeout(r, 400));

  const stackRects = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('#topic-10 .tu-pillar-card'));
    return cards.map((c, i) => {
      const r = c.getBoundingClientRect();
      return {
        idx: i,
        top: Math.round(r.top),
        bottom: Math.round(r.bottom),
        height: Math.round(r.height),
        isActive: c.classList.contains('is-active')
      };
    });
  });
  console.log('Stack Card positions when scrolled into topic 10 (+600px):');
  stackRects.forEach(c => {
    console.log(`  Card ${c.idx}: viewport top=${c.top}px, bottom=${c.bottom}px, isActive=${c.isActive}`);
  });

  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic10_desktop_stacked.png') });
  console.log('  Saved screenshot: qa/screenshots/topic10_desktop_stacked.png');

  console.log('\n=== STEP 5: DESTINATION NODE CLICK & ROUTE ANIMATION ===');
  for (let nodeIdx = 0; nodeIdx < 4; nodeIdx++) {
    const result = await page.evaluate((idx) => {
      const btn = document.querySelectorAll('.tu-route-node')[idx];
      if (btn) btn.click();
      return { clicked: !!btn };
    }, nodeIdx);

    // Wait for the route animation (920ms + buffer)
    await new Promise(r => setTimeout(r, 1100));

    const state = await page.evaluate((idx) => {
      const active = document.getElementById('tuRouteActive');
      const walker = document.getElementById('tuRouteWalker');
      const cards = Array.from(document.querySelectorAll('#topic-10 .tu-pillar-card'));
      const nodes = Array.from(document.querySelectorAll('.tu-route-node'));
      const activeCard = cards[idx];
      return {
        idx,
        nodeActive: nodes[idx]?.classList.contains('active'),
        cardActive: activeCard?.classList.contains('is-active'),
        cardRevealedBars: activeCard?.classList.contains('is-revealed-bars'),
        strokeOffset: active?.style.strokeDashoffset,
        walkerTransform: walker?.getAttribute('transform'),
        scrollY: Math.round(window.scrollY)
      };
    }, nodeIdx);

    console.log(`Destination Node ${nodeIdx}: nodeActive=${state.nodeActive}, cardActive=${state.cardActive}, walkerTransform=${state.walkerTransform}`);
  }

  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic10_node3_active.png') });
  console.log('  Saved screenshot: qa/screenshots/topic10_node3_active.png');

  console.log('\n=== STEP 6: CARD HEADER CLICK & KEYBOARD NAVIGATION ===');
  // Click card header 1 (index 0) to ensure clicking cards works
  const cardClickResult = await page.evaluate(() => {
    const head1 = document.querySelectorAll('#topic-10 .tu-pillar-head')[0];
    if (head1) head1.click();
    return { clicked: !!head1 };
  });
  await new Promise(r => setTimeout(r, 1100));

  const afterCardClick = await page.evaluate(() => {
    const nodes = Array.from(document.querySelectorAll('.tu-route-node'));
    const cards = Array.from(document.querySelectorAll('#topic-10 .tu-pillar-card'));
    return {
      node0Active: nodes[0]?.classList.contains('active'),
      card0Active: cards[0]?.classList.contains('is-active'),
      head0Expanded: cards[0]?.querySelector('.tu-pillar-head')?.getAttribute('aria-expanded')
    };
  });
  console.log('After Card Header 0 Click:');
  console.log(`  node0Active=${afterCardClick.node0Active}, card0Active=${afterCardClick.card0Active}, head0Expanded=${afterCardClick.head0Expanded}`);

  // Test Keyboard Navigation on Card Header 2 (index 1)
  const keyNavResult = await page.evaluate(() => {
    const head2 = document.querySelectorAll('#topic-10 .tu-pillar-head')[1];
    if (head2) {
      head2.focus();
      const event = new KeyboardEvent('keydown', { key: 'Enter', bubbles: true });
      head2.dispatchEvent(event);
      return { focused: true };
    }
    return { focused: false };
  });
  await new Promise(r => setTimeout(r, 1100));

  const afterKeyNav = await page.evaluate(() => {
    const nodes = Array.from(document.querySelectorAll('.tu-route-node'));
    const cards = Array.from(document.querySelectorAll('#topic-10 .tu-pillar-card'));
    return {
      node1Active: nodes[1]?.classList.contains('active'),
      card1Active: cards[1]?.classList.contains('is-active'),
      head1Expanded: cards[1]?.querySelector('.tu-pillar-head')?.getAttribute('aria-expanded')
    };
  });
  console.log('After Card Header 1 Enter Key:');
  console.log(`  node1Active=${afterKeyNav.node1Active}, card1Active=${afterKeyNav.card1Active}, head1Expanded=${afterKeyNav.head1Expanded}`);

  console.log('\n=== STEP 7: MOBILE RESPONSIVENESS & TOPIC 02 CHECKS ===');
  await page.setViewport({ width: 390, height: 844 });
  await page.evaluate(() => {
    const t10 = document.getElementById('topic-10');
    if (t10) window.scrollTo(0, t10.offsetTop);
  });
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic10_mobile.png') });
  console.log('  Saved screenshot: qa/screenshots/topic10_mobile.png');

  // Check Topic 02 at 1024px laptop
  await page.setViewport({ width: 1024, height: 768 });
  await page.evaluate(() => {
    const t2 = document.getElementById('topic-02');
    if (t2) window.scrollTo(0, t2.offsetTop);
  });
  await new Promise(r => setTimeout(r, 400));

  const t2Layout = await page.evaluate(() => {
    const t2 = document.getElementById('topic-02');
    const layout = t2?.querySelector('.cluster-map-layout');
    const pillbox = t2?.querySelector('.cluster-selector-pillbox');
    const canvasCard = t2?.querySelector('.cluster-map-canvas-card');
    return {
      t2ScrollW: t2?.scrollWidth,
      t2ClientW: t2?.clientWidth,
      layoutW: layout?.offsetWidth,
      pillboxW: pillbox?.offsetWidth,
      canvasCardW: canvasCard?.offsetWidth
    };
  });
  console.log('Topic 02 at 1024px Laptop:');
  console.log(`  scrollWidth=${t2Layout.t2ScrollW}, clientWidth=${t2Layout.t2ClientW}, layoutW=${t2Layout.layoutW}`);

  await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'topic02_laptop1024.png') });
  console.log('  Saved screenshot: qa/screenshots/topic02_laptop1024.png');

  await browser.close();
  console.log('\n=== ALL TESTS COMPLETED SUCCESSFULLY ===');
}

runTests().catch(err => {
  console.error('Test Failed:', err);
  process.exit(1);
});
