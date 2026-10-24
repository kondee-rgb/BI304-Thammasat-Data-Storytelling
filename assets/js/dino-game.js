/*!
 * TU Runner — เกมวิ่งกระโดดแบบ Chrome Dino ธีมธรรมศาสตร์
 * ไม่พึ่งไลบรารี ไม่ใช้รูปภายนอก (วาดด้วย canvas ทั้งหมด)
 * ใช้งาน: ใส่ <div data-tu-runner></div> แล้วโหลดไฟล์นี้ (defer) + dino-game.css
 *
 * ค่าฟิสิกส์อ้างอิงซอร์สจริงของ Chromium (components/neterror/resources/offline.js):
 *   SPEED เริ่ม 6, ACCELERATION 0.001/เฟรม, MAX_SPEED 13, GAP_COEFFICIENT 0.6,
 *   INITIAL_JUMP_VELOCITY -10, GRAVITY 0.6, DROP_VELOCITY -5, SPEED_DROP_COEFFICIENT 3,
 *   CLEAR_TIME 3000ms, MAX_OBSTACLE_LENGTH 3, คะแนน = ระยะ x 0.025, นกเริ่มโผล่ที่ speed >= 8.5
 */
(function () {
  'use strict';

  var W = 600, H = 150;           // พิกัดตรรกะของ canvas
  var GROUND = 130;               // ระดับพื้น (y)
  var FPS_MS = 1000 / 60;
  var CFG = {
    speed: 6, accel: 0.001, maxSpeed: 13,
    gravity: 0.6, jumpV: 10, dropV: -5, speedDrop: 3, minJumpH: 30,
    gapCoef: 0.6, maxGapCoef: 1.5, clearTime: 3000,
    maxLen: 3, scoreCoef: 0.025, achieveEvery: 100, nightEvery: 700, birdMinSpeed: 8.5
  };
  var STAND = { w: 40, h: 46 }, DUCK = { w: 46, h: 28 };

  var TYPES = {
    cone:  { w: 18, h: 32, minGap: 120, minSpeed: 0,   multiSpeed: 4,   y: GROUND - 32 },
    books: { w: 30, h: 40, minGap: 120, minSpeed: 0,   multiSpeed: 7,   y: GROUND - 40 },
    bird:  { w: 42, h: 30, minGap: 150, minSpeed: CFG.birdMinSpeed, multiSpeed: 999, ys: [98, 70, 40] }
  };

  function rnd(a, b) { return Math.floor(Math.random() * (b - a + 1)) + a; }
  function store(k, v) {
    try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; }
  }
  function pad(n, len) { var s = String(Math.max(0, Math.floor(n))); while (s.length < len) s = '0' + s; return s; }

  /* ---------- เสียง (WebAudio, สร้างหลังผู้ใช้กดเล่นเท่านั้น) ---------- */
  function Sound() {
    this.ctx = null; this.muted = store('tu-runner-muted') === '1';
  }
  Sound.prototype.init = function () {
    if (this.ctx) return;
    try { var AC = window.AudioContext || window.webkitAudioContext; if (AC) this.ctx = new AC(); } catch (e) {}
  };
  Sound.prototype.beep = function (freqs, dur, type, vol) {
    if (this.muted || !this.ctx) return;
    try {
      var c = this.ctx, t = c.currentTime, o = c.createOscillator(), g = c.createGain();
      o.type = type || 'square';
      for (var i = 0; i < freqs.length; i++) o.frequency.setValueAtTime(freqs[i], t + i * dur / freqs.length);
      g.gain.setValueAtTime(vol || 0.06, t);
      g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
      o.connect(g); g.connect(c.destination); o.start(t); o.stop(t + dur);
    } catch (e) {}
  };

  /* ---------- วาดตัวละคร / สิ่งกีดขวาง ---------- */
  function R(ctx, c, x, y, w, h) { ctx.fillStyle = c; ctx.fillRect(Math.round(x), Math.round(y), w, h); }

  // ขาหรือแขน 2 ท่อน (ต้นขา/แขนท่อนบน + หน้าแข้ง/แขนท่อนล่าง) มุมเป็นองศาจากแนวดิ่ง (+ = ไปข้างหน้า/ขวา)
  function limb(ctx, x, y, a1, a2, l1, l2, w, color, endColor, endW, endH) {
    var r1 = a1 * Math.PI / 180, r2 = a2 * Math.PI / 180;
    var kx = x + Math.sin(r1) * l1, ky = y + Math.cos(r1) * l1;
    var ex = kx + Math.sin(r2) * l2, ey = ky + Math.cos(r2) * l2;
    ctx.strokeStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(kx, ky); ctx.lineTo(ex, ey); ctx.stroke();
    if (endColor) { ctx.fillStyle = endColor; ctx.fillRect(Math.round(ex - 3), Math.round(ey - endH / 2), endW, endH); }
  }

  // ท่าวิ่ง 4 เฟรม: ก้าวยาว → สลับขาผ่านใต้ลำตัว → ก้าวยาวอีกข้าง → สลับขา (แขนแกว่งสวนขา)
  var RUN_POSE = [
    { a: [38, 12], b: [-34, -78], bob: 1 },
    { a: [12, -22], b: [-8, -55], bob: -1 },
    { a: [-34, -78], b: [38, 12], bob: 1 },
    { a: [-8, -55], b: [12, -22], bob: -1 }
  ];

  function drawStudent(ctx, x, y, state, frame) {
    // state: 'run' | 'duck' | 'dead' | 'idle' | 'jump'
    var skin = '#f1c6a0', hair = '#1b1b2f', shirt = '#f8fafc', line = '#94a3b8',
        pants = '#14234f', pantsBack = '#0b163b', shoe = '#ffffff', bag = '#0b163b', crimson = '#c51944', gold = '#ffc72c';
    ctx.save(); ctx.translate(x, y);
    if (state === 'duck') {
      var st = frame % 2;
      R(ctx, bag, 2, 6, 8, 12);                                  // กระเป๋า
      R(ctx, line, 7, 6, 28, 16); R(ctx, shirt, 8, 7, 26, 14);   // ลำตัวเอนไปข้างหน้า
      R(ctx, crimson, 28, 9, 2, 8);                              // สายคล้องบัตร
      R(ctx, hair, 31, 0, 13, 5); R(ctx, skin, 33, 4, 12, 9);    // หัว
      R(ctx, '#0f172a', 40, 7, 2, 2);                            // ตา
      limb(ctx, 14, 20, st ? 30 : -25, st ? 5 : -60, 4, 4, 5, st ? pantsBack : pants, shoe, 9, 3);
      limb(ctx, 26, 20, st ? -25 : 30, st ? -60 : 5, 4, 4, 5, st ? pants : pantsBack, shoe, 9, 3);
      ctx.restore();
      return;
    }

    var pose;
    if (state === 'run') pose = RUN_POSE[frame % 4];
    else if (state === 'jump') pose = { a: [45, -15], b: [-20, -70], bob: 0 };   // ขาหน้ายกพับ ขาหลังเหยียดดันตัว
    else pose = { a: [6, 0], b: [-6, 0], bob: 0 };                                // idle / dead ยืนตรง
    var by = pose.bob;                                                            // ตัวขึ้นลงตามจังหวะก้าว
    var armA = -pose.a[0] * 0.9, armB = -pose.b[0] * 0.9;                          // แขนแกว่งสวนกับขาข้างเดียวกัน

    // ด้านหลัง (ไกลตา): ขา B + แขน B สีเข้มกว่า
    limb(ctx, 21, 30 + by, pose.b[0], pose.b[1], 8, 8, 6, pantsBack, shoe, 9, 4);
    limb(ctx, 21, 17 + by, armB, armB + 70, 6, 6, 3.5, '#d9a882');

    R(ctx, bag, 8, 16 + by, 7, 13);                                // กระเป๋าสะพายหลัง
    R(ctx, line, 14, 14 + by, 16, 18); R(ctx, shirt, 15, 15 + by, 14, 16); // เสื้อ
    R(ctx, pants, 15, 29 + by, 14, 4);                             // เข็มขัด/สะโพก
    R(ctx, crimson, 23, 15 + by, 2, 9); R(ctx, gold, 22, 24 + by, 4, 5);   // สายคล้อง + บัตร
    R(ctx, hair, 15, 0 + by, 14, 5); R(ctx, skin, 17, 4 + by, 12, 10);     // หัว
    R(ctx, hair, 15, 4 + by, 3, 4);                                // ผมด้านหลัง
    if (state === 'dead') {
      ctx.strokeStyle = '#0f172a'; ctx.lineWidth = 1.5; ctx.beginPath();
      ctx.moveTo(23, 6 + by); ctx.lineTo(27, 10 + by); ctx.moveTo(27, 6 + by); ctx.lineTo(23, 10 + by); ctx.stroke();
    } else R(ctx, '#0f172a', 25, 7 + by, 2, 2);

    // ด้านหน้า (ใกล้ตา): ขา A + แขน A
    limb(ctx, 23, 30 + by, pose.a[0], pose.a[1], 8, 8, 6, pants, shoe, 9, 4);
    limb(ctx, 23, 17 + by, armA, armA + 70, 6, 6, 3.5, skin);
    ctx.restore();
  }

  function drawCone(ctx, x, y) {
    ctx.save(); ctx.translate(x, y);
    ctx.fillStyle = '#c51944'; ctx.beginPath(); ctx.moveTo(9, 0); ctx.lineTo(16, 28); ctx.lineTo(2, 28); ctx.closePath(); ctx.fill();
    ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.moveTo(7, 10); ctx.lineTo(11, 10); ctx.lineTo(12.5, 17); ctx.lineTo(5.5, 17); ctx.closePath(); ctx.fill();
    R(ctx, '#7f1230', 0, 28, 18, 4);
    ctx.restore();
  }
  function drawBooks(ctx, x, y) {
    R(ctx, '#0b163b', x, y + 28, 30, 12);  R(ctx, '#ffc72c', x + 2, y + 31, 26, 2);
    R(ctx, '#c51944', x + 3, y + 16, 26, 12); R(ctx, '#fff', x + 5, y + 20, 14, 2);
    R(ctx, '#00857c', x + 1, y + 6, 24, 10);  R(ctx, '#ffc72c', x + 4, y + 10, 10, 2);
    R(ctx, '#0b163b', x + 5, y, 18, 6);
  }
  function drawBird(ctx, x, y, flap) {
    ctx.save(); ctx.translate(x, y);
    ctx.fillStyle = '#64748b'; ctx.beginPath(); ctx.ellipse(21, 17, 15, 8, 0, 0, 7); ctx.fill();   // ลำตัว
    ctx.fillStyle = '#94a3b8'; ctx.beginPath(); ctx.arc(8, 13, 6, 0, 7); ctx.fill();               // หัว
    R(ctx, '#ffc72c', 0, 13, 5, 3);                                                                  // จะงอย
    R(ctx, '#0f172a', 7, 11, 2, 2);                                                                  // ตา
    ctx.fillStyle = '#475569'; ctx.beginPath();                                                      // ปีก
    if (flap) { ctx.moveTo(18, 14); ctx.lineTo(30, 0); ctx.lineTo(34, 14); }
    else      { ctx.moveTo(18, 18); ctx.lineTo(30, 30); ctx.lineTo(34, 18); }
    ctx.closePath(); ctx.fill();
    ctx.fillStyle = '#64748b'; ctx.beginPath(); ctx.moveTo(34, 15); ctx.lineTo(42, 12); ctx.lineTo(40, 20); ctx.closePath(); ctx.fill();
    ctx.restore();
  }

  /* ---------- ตัวเกม ---------- */
  function Game(root) {
    this.root = root;
    this.sound = new Sound();
    this.state = 'idle';           // idle | running | paused | over
    this.hi = parseInt(store('tu-runner-hi') || '0', 10) || 0;
    this.reduceMotion = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.inView = true;
    this.build();
    this.reset();
    this.bind();
    this.draw();
  }

  Game.prototype.build = function () {
    var r = this.root;
    r.classList.add('tu-runner');
    r.setAttribute('role', 'group');
    r.setAttribute('aria-label', 'มินิเกมวิ่งกระโดดหลบสิ่งกีดขวาง');
    r.tabIndex = 0;
    r.innerHTML =
      '<div class="tu-runner__stage">' +
        '<canvas class="tu-runner__canvas" aria-hidden="true"></canvas>' +
        '<div class="tu-runner__score" aria-hidden="true"><span class="tu-runner__hi">HI 00000</span> <span class="tu-runner__cur">00000</span></div>' +
        '<div class="tu-runner__overlay" data-overlay>' +
          '<div class="tu-runner__title" data-title>มินิเกม: วิ่งสู่เส้นชัย 90 ปี</div>' +
          '<div class="tu-runner__sub" data-sub>กระโดดข้ามกรวยและกองหนังสือ ก้มหลบนกพิราบ ยิ่งไกลยิ่งเร็วขึ้น</div>' +
          '<button type="button" class="tu-runner__btn" data-play><span aria-hidden="true">▶</span> <span data-playlabel>เริ่มเล่น</span></button>' +
        '</div>' +
        '<button type="button" class="tu-runner__mute" data-mute aria-pressed="false" aria-label="ปิดเสียงเกม"></button>' +
      '</div>' +
      '<div class="tu-runner__controls">' +
        '<p class="tu-runner__help"><kbd>Space</kbd>/<kbd>W</kbd>/<kbd>↑</kbd> กระโดด · <kbd>S</kbd>/<kbd>↓</kbd> ก้ม</p>' +
        '<div class="tu-runner__touch-bar">' +
          '<button type="button" class="tu-runner__touch-btn tu-runner__touch-btn--jump" data-jump aria-label="กระโดด (กดค้างเพื่อกระโดดสูง)"><span aria-hidden="true">▲</span> กระโดด</button>' +
          '<button type="button" class="tu-runner__touch-btn tu-runner__touch-btn--duck" data-duck aria-label="ก้ม (กดค้างเพื่อหมอบ)"><span aria-hidden="true">▼</span> ก้ม</button>' +
        '</div>' +
      '</div>' +
      '<div class="tu-runner__sr" aria-live="polite" data-live></div>';
    this.canvas = r.querySelector('canvas');
    this.ctx = this.canvas.getContext('2d');
    this.el = {
      overlay: r.querySelector('[data-overlay]'), title: r.querySelector('[data-title]'),
      sub: r.querySelector('[data-sub]'), play: r.querySelector('[data-play]'),
      playLabel: r.querySelector('[data-playlabel]'), mute: r.querySelector('[data-mute]'),
      duck: r.querySelector('[data-duck]'), jump: r.querySelector('[data-jump]'), live: r.querySelector('[data-live]'),
      hi: r.querySelector('.tu-runner__hi'), cur: r.querySelector('.tu-runner__cur'),
      stage: r.querySelector('.tu-runner__stage')
    };
    this.updateMuteUI();
    this.resize();
  };

  Game.prototype.reset = function () {
    this.speed = CFG.speed; this.distance = 0; this.score = 0; this.runTime = 0;
    this.obstacles = []; this.lastTypes = [];
    this.clouds = [{ x: 380, y: 30 }, { x: 150, y: 50 }];
    this.groundX = 0; this.frame = 0; this.frameT = 0;
    this.px = 30; this.py = GROUND - STAND.h; this.vy = 0; this.jumping = false; this.ducking = false;
    this.fastFall = false; this.holdJump = false;
    this.flashT = 0; this.night = false; this.nextAchieve = CFG.achieveEvery; this.nextNight = CFG.nightEvery;
    this.root.classList.remove('is-night');
    this.setScoreUI();
  };

  Game.prototype.resize = function () {
    var w = this.el.stage.clientWidth || 600, dpr = Math.min(window.devicePixelRatio || 1, 2);
    this.canvas.width = Math.round(w * dpr); this.canvas.height = Math.round(w * dpr * H / W);
    this.scale = this.canvas.width / W;
    if (this.ctx && this.obstacles) this.draw();
  };

  Game.prototype.say = function (t) { this.el.live.textContent = ''; var el = this.el.live; setTimeout(function () { el.textContent = t; }, 40); };

  Game.prototype.updateMuteUI = function () {
    var m = this.sound.muted;
    this.el.mute.textContent = m ? '🔇' : '🔊';
    this.el.mute.setAttribute('aria-pressed', m ? 'true' : 'false');
    this.el.mute.setAttribute('aria-label', m ? 'เปิดเสียงเกม' : 'ปิดเสียงเกม');
  };

  Game.prototype.bind = function () {
    var g = this, r = this.root;

    this.el.play.addEventListener('click', function () {
      if (g.state === 'paused') g.resume(); else g.start();
      g.root.focus({ preventScroll: true });
    });
    this.el.mute.addEventListener('click', function () {
      g.sound.muted = !g.sound.muted; store('tu-runner-muted', g.sound.muted ? '1' : '0'); g.updateMuteUI();
      if (g.state !== 'running') g.root.focus({ preventScroll: true });
    });

    function isJumpKey(e) {
      var c = e.code || '', k = e.key || '';
      return (
        c === 'KeyW' || c === 'Space' || c === 'ArrowUp' ||
        k === ' ' || k === 'Spacebar' || k === 'ArrowUp' || k === 'Up' ||
        k === 'w' || k === 'W' || k === 'ไ' || k === 'ำ'
      );
    }

    function isDownKey(e) {
      var c = e.code || '', k = e.key || '';
      return (
        c === 'KeyS' || c === 'ArrowDown' ||
        k === 'ArrowDown' || k === 'Down' ||
        k === 's' || k === 'S' || k === 'ห' || k === 'ฆ'
      );
    }

    function isTypingInput(target) {
      if (!target) return false;
      var tag = target.tagName;
      return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || target.isContentEditable;
    }

    var onKeyDown = function (e) {
      if (isTypingInput(e.target)) return;
      var isJump = isJumpKey(e);
      var isDown = isDownKey(e);
      if (!isJump && !isDown) return;

      var hasRunnerFocus = document.activeElement === r || (document.activeElement && r.contains(document.activeElement));

      // ให้ปุ่ม BUTTON บนหน้าจอทำงานตามปกติ (เช่น กด Space บนปุ่ม) ถ้าเกมไม่ได้กำลังวิ่ง
      if (e.target && e.target.tagName === 'BUTTON' && (e.key === ' ' || e.key === 'Enter') && g.state !== 'running') {
        return;
      }

      if (g.state === 'running') {
        e.preventDefault();
        if (isJump && !e.repeat) {
          g.holdJump = true;
          g.jump();
        }
        if (isDown) {
          g.ducking = true;
          if (g.jumping) g.fastFall = true;
        }
        return;
      }

      if (g.state === 'paused') {
        if (isJump) {
          e.preventDefault();
          g.resume();
          if (!e.repeat) {
            g.holdJump = true;
            g.jump();
          }
          return;
        }
      }

      if (g.state === 'idle' || g.state === 'over') {
        if (isJump && (hasRunnerFocus || (g.inView && (e.target === r || r.contains(e.target))))) {
          e.preventDefault();
          g.start();
          return;
        }
      }
    };

    var onKeyUp = function (e) {
      if (isTypingInput(e.target)) return;
      if (isJumpKey(e)) {
        g.holdJump = false;
        g.endJump();
      }
      if (isDownKey(e)) {
        g.ducking = false;
        g.fastFall = false;
      }
    };

    window.addEventListener('keydown', onKeyDown, { passive: false });
    window.addEventListener('keyup', onKeyUp, { passive: false });

    // แตะ/คลิกบนเวที = กระโดด
    this.canvas.addEventListener('pointerdown', function (e) {
      if (g.state === 'running') { e.preventDefault(); g.holdJump = true; g.jump(); }
      else if (g.state === 'idle' || g.state === 'over') g.start();
      else if (g.state === 'paused') g.resume();
      g.root.focus({ preventScroll: true });
    });
    window.addEventListener('pointerup', function () { g.holdJump = false; g.endJump(); });
    this.canvas.style.touchAction = 'manipulation';

    // ปุ่มกระโดด (สัมผัสบนมือถือ / คลิก)
    var j = this.el.jump;
    if (j) {
      j.addEventListener('pointerdown', function (e) {
        e.preventDefault();
        if (g.state === 'running') { g.holdJump = true; g.jump(); }
        else if (g.state === 'idle' || g.state === 'over') g.start();
        else if (g.state === 'paused') g.resume();
        g.root.focus({ preventScroll: true });
      });
      ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (ev) {
        j.addEventListener(ev, function () { g.holdJump = false; g.endJump(); });
      });
    }

    // ปุ่มก้ม (สัมผัสบนมือถือ / คลิก)
    var d = this.el.duck;
    if (d) {
      d.addEventListener('pointerdown', function (e) {
        e.preventDefault();
        if (g.state === 'running') { g.ducking = true; if (g.jumping) g.fastFall = true; }
        g.root.focus({ preventScroll: true });
      });
      ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (ev) {
        d.addEventListener(ev, function () { g.ducking = false; g.fastFall = false; });
      });
    }

    // หยุดอัตโนมัติ: ซ่อนแท็บ / สลับหน้าต่าง / เลื่อนพ้นจอ
    window.addEventListener('blur', function () {
      if (g.state === 'running') g.pause('หยุดชั่วคราว');
    });
    document.addEventListener('visibilitychange', function () {
      if (document.hidden && g.state === 'running') g.pause('หยุดชั่วคราว');
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        g.inView = es[0].isIntersecting;
        if (!es[0].isIntersecting && g.state === 'running') g.pause('หยุดชั่วคราว');
      }, { threshold: 0.25 }).observe(r);
    }
    window.addEventListener('resize', function () { g.resize(); });
  };

  Game.prototype.showOverlay = function (title, sub, label) {
    this.el.title.textContent = title; this.el.sub.textContent = sub; this.el.playLabel.textContent = label;
    this.el.overlay.hidden = false; this.root.classList.add('is-overlay');
  };
  Game.prototype.hideOverlay = function () { this.el.overlay.hidden = true; this.root.classList.remove('is-overlay'); };

  Game.prototype.start = function () {
    if (this.state === 'over' && performance.now() - this.diedAt < 400) return;  // กันกดรัวเกินตอนตาย
    this.sound.init();
    if (this.sound.ctx && this.sound.ctx.state === 'suspended') this.sound.ctx.resume();
    this.reset();
    this.state = 'running';
    this.hideOverlay();
    this.root.focus({ preventScroll: true });
    this.say('เริ่มเกม');
    this.last = performance.now();
    this.raf = requestAnimationFrame(this.loop.bind(this));
    this.jump();   // ให้ปุ่ม Space ที่ใช้เริ่มเกมกระโดดครั้งแรกเหมือนเกมจริง
  };
  Game.prototype.pause = function (msg) {
    if (this.state !== 'running') return;
    this.state = 'paused'; cancelAnimationFrame(this.raf);
    this.ducking = false; this.holdJump = false; this.fastFall = false;
    this.showOverlay(msg || 'หยุดชั่วคราว', 'คะแนนปัจจุบัน ' + Math.floor(this.score) + ' · กด Space หรือ W เพื่อเล่นต่อ', 'เล่นต่อ');
    this.draw();
  };
  Game.prototype.resume = function () {
    if (this.state !== 'paused') return;
    this.state = 'running'; this.hideOverlay(); this.root.focus({ preventScroll: true });
    this.last = performance.now();
    this.raf = requestAnimationFrame(this.loop.bind(this));
  };

  Game.prototype.jump = function () {
    if (this.jumping || this.state !== 'running') return;
    this.jumping = true; this.vy = -(CFG.jumpV + this.speed / 10);
    this.sound.beep([520, 760], 0.12, 'square', 0.05);
  };
  Game.prototype.endJump = function () {
    // ปล่อยปุ่มกลางอากาศ = กระโดดเตี้ยลง (เหมือนเกมจริง)
    if (this.jumping && this.vy < CFG.dropV && (GROUND - STAND.h) - this.py > CFG.minJumpH) this.vy = CFG.dropV;
  };

  Game.prototype.spawn = function () {
    var names = ['cone', 'books', 'bird'], pool = [], i;
    for (i = 0; i < names.length; i++) {
      var t = TYPES[names[i]];
      if (this.speed < t.minSpeed) continue;
      var n = this.lastTypes.length;
      if (n >= 2 && this.lastTypes[n - 1] === names[i] && this.lastTypes[n - 2] === names[i]) continue; // ไม่ซ้ำเกิน 2 ครั้ง
      pool.push(names[i]);
    }
    var name = pool[rnd(0, pool.length - 1)], t2 = TYPES[name];
    var size = (name !== 'bird' && this.speed >= t2.multiSpeed) ? rnd(1, CFG.maxLen) : 1;
    if (name !== 'bird' && size > 1 && this.speed < t2.multiSpeed) size = 1;
    var w = t2.w * size, y = name === 'bird' ? t2.ys[rnd(0, 2)] : t2.y;
    var minGap = Math.round(w * this.speed + t2.minGap * CFG.gapCoef);
    var gap = rnd(minGap, Math.round(minGap * CFG.maxGapCoef));
    this.obstacles.push({ type: name, size: size, x: W, y: y, w: w, h: t2.h, gap: gap, speedOffset: name === 'bird' ? (Math.random() > 0.5 ? 0.8 : -0.8) : 0 });
    this.lastTypes.push(name); if (this.lastTypes.length > 3) this.lastTypes.shift();
  };

  Game.prototype.hitbox = function () {
    var d = this.ducking && !this.jumping;
    var w = d ? DUCK.w : STAND.w, h = d ? DUCK.h : STAND.h;
    var top = d ? GROUND - DUCK.h : this.py;
    return { x: this.px + 8, y: top + 3, w: w - 16, h: h - 6 };
  };

  Game.prototype.loop = function (now) {
    if (this.state !== 'running') return;
    var dt = Math.min(now - this.last, 50); this.last = now;
    var f = dt / FPS_MS;
    this.update(dt, f);
    this.draw();
    if (this.state === 'running') this.raf = requestAnimationFrame(this.loop.bind(this));
  };

  Game.prototype.update = function (dt, f) {
    var i, o;
    this.runTime += dt;
    // เพิ่มความเร็วเรื่อยๆ จนถึง MAX
    if (this.speed < CFG.maxSpeed) this.speed = Math.min(CFG.maxSpeed, this.speed + CFG.accel * f);
    this.distance += this.speed * f;
    this.score = this.distance * CFG.scoreCoef;

    // ตัวละคร
    this.frameT += dt; if (this.frameT > 80) { this.frameT = 0; this.frame++; }
    if (this.jumping) {
      var g = CFG.gravity * (this.fastFall ? CFG.speedDrop : 1);
      this.py += this.vy * f; this.vy += g * f;
      var ground = GROUND - STAND.h;
      if (this.py >= ground) { this.py = ground; this.vy = 0; this.jumping = false; this.fastFall = false; if (this.holdJump) { /* ค้างปุ่ม = ไม่กระโดดซ้ำอัตโนมัติ */ } }
    }

    // พื้น + เมฆ
    this.groundX = (this.groundX + this.speed * f) % 600;
    for (i = 0; i < this.clouds.length; i++) {
      this.clouds[i].x -= 0.2 * f * 3;
      if (this.clouds[i].x < -50) { this.clouds[i].x = W + rnd(0, 100); this.clouds[i].y = rnd(20, 70); }
    }

    // สิ่งกีดขวาง
    var last = this.obstacles[this.obstacles.length - 1];
    if (!last) { if (this.runTime > CFG.clearTime) this.spawn(); }
    else if (last.x + last.w + last.gap < W) this.spawn();
    for (i = this.obstacles.length - 1; i >= 0; i--) {
      o = this.obstacles[i];
      o.x -= (this.speed + o.speedOffset) * f;
      if (o.x + o.w < -10) this.obstacles.splice(i, 1);
    }

    // ชน?
    var hb = this.hitbox();
    for (i = 0; i < this.obstacles.length; i++) {
      o = this.obstacles[i];
      var ob = { x: o.x + 3, y: o.y + 3, w: o.w - 6, h: o.h - 6 };
      if (hb.x < ob.x + ob.w && hb.x + hb.w > ob.x && hb.y < ob.y + ob.h && hb.y + hb.h > ob.y) { this.die(); return; }
    }

    // คะแนนทุก 100 = กะพริบ+เสียง, ทุก 700 = สลับกลางวัน/กลางคืน
    if (this.score >= this.nextAchieve) {
      this.nextAchieve += CFG.achieveEvery;
      if (!this.reduceMotion) this.flashT = 1200;
      this.sound.beep([880, 1100, 1320], 0.18, 'square', 0.05);
    }
    if (this.score >= this.nextNight) {
      this.nextNight += CFG.nightEvery;
      this.night = !this.night;
      this.root.classList.toggle('is-night', this.night && !this.reduceMotion);
    }
    if (this.flashT > 0) this.flashT -= dt;
    this.setScoreUI();
  };

  Game.prototype.setScoreUI = function () {
    var hiShown = Math.max(this.hi, Math.floor(this.score));
    this.el.hi.textContent = 'HI ' + pad(this.hi, 5);
    var flashOff = this.flashT > 0 && (Math.floor(this.flashT / 150) % 2 === 1);
    this.el.cur.textContent = flashOff ? '     ' : pad(this.score, 5);
    this.el.cur.style.visibility = flashOff ? 'hidden' : 'visible';
    void hiShown;
  };

  Game.prototype.die = function () {
    this.state = 'over'; this.diedAt = performance.now();
    cancelAnimationFrame(this.raf);
    this.ducking = false; this.holdJump = false; this.fastFall = false;
    var s = Math.floor(this.score), newHi = s > this.hi;
    if (newHi) { this.hi = s; store('tu-runner-hi', String(s)); }
    this.sound.beep([300, 200, 120], 0.35, 'sawtooth', 0.07);
    this.flashT = 0; this.setScoreUI(); this.draw();
    var msg = 'จบเกม — คะแนน ' + s + (newHi && s > 0 ? ' (สถิติใหม่!)' : '');
    this.showOverlay('GAME OVER', 'คะแนน ' + s + (newHi && s > 0 ? ' · สถิติใหม่ 🎉' : ' · สถิติสูงสุด ' + this.hi), 'เล่นอีกครั้ง');
    this.say(msg);
    var b = this.el.play; setTimeout(function () { try { b.focus({ preventScroll: true }); } catch (e) {} }, 420);
  };

  Game.prototype.draw = function () {
    var ctx = this.ctx, s = this.scale || 1, i, o;
    ctx.setTransform(s, 0, 0, s, 0, 0);
    ctx.clearRect(0, 0, W, H);

    // เมฆ
    ctx.fillStyle = '#e2e8f0';
    for (i = 0; i < this.clouds.length; i++) {
      var c = this.clouds[i];
      ctx.beginPath(); ctx.ellipse(c.x + 14, c.y + 8, 16, 7, 0, 0, 7); ctx.ellipse(c.x + 28, c.y + 5, 12, 8, 0, 0, 7); ctx.fill();
    }
    // พื้น
    R(ctx, '#475569', 0, GROUND, W, 2);
    ctx.fillStyle = '#94a3b8';
    for (i = 0; i < 24; i++) {
      var gx = ((i * 83 + 17) - this.groundX * 1) % 640; if (gx < -20) gx += 640;
      ctx.fillRect(Math.round(gx), GROUND + 6 + (i % 3) * 4, 3 + (i % 4) * 3, 2);
    }
    // สิ่งกีดขวาง
    for (i = 0; i < this.obstacles.length; i++) {
      o = this.obstacles[i];
      if (o.type === 'cone') for (var k = 0; k < o.size; k++) drawCone(ctx, o.x + k * TYPES.cone.w, o.y);
      else if (o.type === 'books') for (var m = 0; m < o.size; m++) drawBooks(ctx, o.x + m * TYPES.books.w, o.y);
      else drawBird(ctx, o.x, o.y, Math.floor(this.runTime / 160) % 2 === 0);
    }
    // ตัวละคร
    var st = this.state === 'over' ? 'dead' : this.jumping ? 'jump' : (this.ducking ? 'duck' : (this.state === 'running' ? 'run' : 'idle'));
    var y = st === 'duck' ? GROUND - DUCK.h : this.py;
    drawStudent(ctx, this.px, y, st === 'jump' ? 'jump' : st, this.frame);
  };

  function init() {
    var nodes = document.querySelectorAll('[data-tu-runner]');
    for (var i = 0; i < nodes.length; i++) if (!nodes[i].__tuRunner) nodes[i].__tuRunner = new Game(nodes[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  window.TURunner = { init: init };
})();
