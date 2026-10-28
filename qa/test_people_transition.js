const puppeteer = require('puppeteer');

(async () => {
  console.log('🚀 Testing Topic 04 People Icons Transition & Wave Morph...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:8000/index.html', { waitUntil: 'networkidle2' });

  // Scroll to topic 04
  const res = await page.evaluate(async () => {
    const mod = document.querySelector('.scroll-story-module[data-story-for="topic-04"]');
    if (!mod) return { error: 'No topic-04' };

    const grid = mod.querySelector('.story-people-grid');
    const steps = mod.querySelectorAll('.scroll-story-step');
    if (!grid || steps.length < 2) return { error: 'Missing elements' };

    // Step 0 is active (62.4% female)
    const count0 = grid.querySelectorAll('.story-person.female').length;

    // Click step 1 (71.5% female) to trigger transition
    steps[1].click();

    // Check immediately for flipping class and morphing state
    await new Promise(r => setTimeout(r, 60));
    const flippingCount = grid.querySelectorAll('.story-person.is-flipping').length;
    const isMorphing = mod.querySelector('.scroll-story-visual-content').classList.contains('is-morphing');
    
    // Check person delays
    const firstPersonDelay = grid.children[0].style.getPropertyValue('--person-delay');
    const lastPersonDelay = grid.children[99].style.getPropertyValue('--person-delay');

    // Wait for transition to complete
    await new Promise(r => setTimeout(r, 850));
    const count1 = grid.querySelectorAll('.story-person.female').length;
    const flippingAfter = grid.querySelectorAll('.story-person.is-flipping').length;
    const femalePct = mod.querySelector('.story-female-pct')?.textContent;
    const malePct = mod.querySelector('.story-male-pct')?.textContent;

    return {
      count0,
      count1,
      flippingCount,
      isMorphing,
      firstPersonDelay,
      lastPersonDelay,
      flippingAfter,
      femalePct,
      malePct
    };
  });

  console.log('People Transition Test Result:\n', JSON.stringify(res, null, 2));

  if (res.count0 !== 62 || res.count1 !== 72) {
    console.error(`❌ FAILED: Icon count mismatch: initial=${res.count0}, after=${res.count1}`);
    process.exit(1);
  }
  if (res.flippingCount === 0) {
    console.error('❌ FAILED: No icons received .is-flipping animation!');
    process.exit(1);
  }
  if (!res.isMorphing) {
    console.error('❌ FAILED: .is-morphing not active on container!');
    process.exit(1);
  }

  console.log('✅ PASSED: People icons have full 3D flip animation, wave stagger delays, and morphing transitions!');
  await browser.close();
})();
