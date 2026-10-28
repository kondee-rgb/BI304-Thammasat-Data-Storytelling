/*!
 * TU Interactive — Quiz component for the "90 ปีธรรมศาสตร์" website
 *   [data-tu-quiz] quiz: answer choices, sourced feedback, and score summary
 * Data is stored as JSON inside the component. No additional library required.
 */
(function () {
  'use strict';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function h(tag, attrs, kids) {
    var el = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      if (k === 'class') el.className = attrs[k];
      else if (k === 'text') el.textContent = attrs[k];
      else if (k.slice(0, 2) === 'on') el.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] !== null && attrs[k] !== undefined) el.setAttribute(k, attrs[k]);
    }
    (kids || []).forEach(function (c) { if (c) el.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return el;
  }
  function readData(root) {
    var s = root.querySelector('script[type="application/json"]');
    try { return JSON.parse(s.textContent); } catch (e) { return null; }
  }
  function sourceLink(src) {
    if (!src || !src.url) return null;
    return h('a', { class: 'tui-src', href: src.url, target: '_blank', rel: 'noopener noreferrer', text: 'แหล่งที่มา: ' + (src.label || src.url) });
  }
  function live(root, msg) {
    var l = root.querySelector('.tui-live'); if (!l) return;
    l.textContent = ''; setTimeout(function () { l.textContent = msg; }, 30);
  }

  /* ====================== 2) Quiz ====================== */
  function Quiz(root) {
    var d = readData(root); if (!d || !d.questions || !d.questions.length) return;
    this.root = root; this.d = d; this.i = 0; this.score = 0; this.wrong = [];
    this.count = Math.min(d.count || 5, d.questions.length); this.lastIds = [];
    root.classList.add('tui', 'tui-quiz');
    root.setAttribute('role', 'group');
    root.setAttribute('aria-label', d.title || 'Quiz');
    this.intro();
  }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  Quiz.prototype.draw = function () {
    var pool = this.d.questions.map(function (q, k) { return { q: q, id: k }; }), last = this.lastIds;
    var fresh = shuffle(pool.filter(function (x) { return last.indexOf(x.id) < 0; }));
    var old = shuffle(pool.filter(function (x) { return last.indexOf(x.id) >= 0; }));
    var picked = fresh.concat(old).slice(0, this.count);
    this.lastIds = picked.map(function (x) { return x.id; });
    return shuffle(picked).map(function (x) {
      var idx = shuffle(x.q.options.map(function (_, k) { return k; }));
      var c = {}; for (var k in x.q) c[k] = x.q[k];
      c.options = idx.map(function (k) { return x.q.options[k]; });
      c.correct = idx.indexOf(x.q.correct);
      return c;
    });
  };
  Quiz.prototype.intro = function () {
    var z = this, d = this.d, root = this.root;
    root.classList.add('tui-quiz--intro');
    root.innerHTML = ''; root.appendChild(h('script', { type: 'application/json', text: JSON.stringify(d) }));
    root.appendChild(h('div', { class: 'tui-intro' }, [
      h('div', { class: 'tui-intro__txt' }, [
        h('span', { class: 'tui-kicker', text: d.kicker || 'Quiz' }),
        h('h3', { class: 'tui-q', text: d.introTitle || ('ลองทำ Quiz ' + this.count + ' ข้อ') }),
        h('p', { class: 'tui-note', text: d.introText || ('สุ่มใหม่ทุกครั้งจากคลังคำถาม ' + d.questions.length + ' ข้อ') })
      ]),
      h('button', { type: 'button', class: 'tui-btn', text: d.startLabel || 'เริ่ม Quiz', onclick: function () { z.start(); } })
    ]));
    root.appendChild(h('div', { class: 'tui-live', 'aria-live': 'polite' }));
  };
  Quiz.prototype.start = function () {
    this.qs = this.draw(); this.i = 0; this.score = 0; this.wrong = [];
    this.root.classList.remove('tui-quiz--intro');
    this.render();
    var f = this.root.querySelector('.tui-opt'); if (f) f.focus({ preventScroll: true });
    this.root.scrollIntoView({ block: 'nearest', behavior: reduce ? 'auto' : 'smooth' });
  };
  Quiz.prototype.render = function () {
    var z = this, d = this.d, qd = this.qs[this.i], root = this.root, answered = false;
    root.innerHTML = ''; root.appendChild(h('script', { type: 'application/json', text: JSON.stringify(d) }));
    var dots = h('div', { class: 'tui-dots', 'aria-hidden': 'true' }, this.qs.map(function (_, k) {
      return h('i', { class: k < z.i ? 'is-done' : k === z.i ? 'is-now' : '' });
    }));
    root.appendChild(h('div', { class: 'tui-head' }, [
      h('span', { class: 'tui-kicker', text: d.kicker || 'Quiz' }),
      h('span', { class: 'tui-step', text: 'ข้อ ' + (this.i + 1) + ' / ' + this.qs.length }), dots
    ]));
    root.appendChild(h('h3', { class: 'tui-q', text: qd.q }));
    var opts = h('div', { class: 'tui-opts', role: 'group', 'aria-label': 'ตัวเลือกคำตอบ' });
    var fb = h('div', { class: 'tui-fb', hidden: '' });
    var btns = qd.options.map(function (o, k) {
      var b = h('button', { type: 'button', class: 'tui-opt' }, [h('span', { class: 'tui-key', 'aria-hidden': 'true', text: String(k + 1) }), h('span', { class: 'tui-txt', text: o }), h('span', { class: 'tui-mark', 'aria-hidden': 'true' })]);
      b.addEventListener('click', function () { choose(k); });
      opts.appendChild(b); return b;
    });
    function choose(k) {
      if (answered) return; answered = true;
      var ok = k === qd.correct;
      if (ok) z.score++; else z.wrong.push({ q: qd.q, correct: qd.options[qd.correct], ref: qd.ref });
      btns.forEach(function (b, j) {
        b.disabled = true;
        if (j === qd.correct) { b.classList.add('is-correct'); b.querySelector('.tui-mark').textContent = '✓ ถูก'; }
        else if (j === k) { b.classList.add('is-wrong'); b.querySelector('.tui-mark').textContent = '✗ ผิด'; }
      });
      fb.hidden = false;
      fb.appendChild(h('div', { class: 'tui-verdict ' + (ok ? 'tui-ok' : 'tui-far'), text: ok ? 'ถูกต้อง!' : 'ยังไม่ใช่ — คำตอบคือ “' + qd.options[qd.correct] + '”' }));
      fb.appendChild(h('p', { class: 'tui-note', text: qd.explain }));
      var s = sourceLink(qd.source); if (s) fb.appendChild(s);
      var last = z.i === z.qs.length - 1;
      var next = h('button', { type: 'button', class: 'tui-btn', text: last ? 'ดูคะแนน' : 'ข้อถัดไป →', onclick: function () { if (last) z.finish(); else { z.i++; z.render(); var f = root.querySelector('.tui-opt'); if (f) f.focus({ preventScroll: true }); } } });
      fb.appendChild(next); next.focus();
      live(root, ok ? 'ถูกต้อง' : 'ผิด คำตอบคือ ' + qd.options[qd.correct]);
    }
    root.addEventListener('keydown', root.__qk = function (e) {
      var n = parseInt(e.key, 10); if (n >= 1 && n <= btns.length && !answered && e.target.closest && e.target.closest('.tui-quiz')) choose(n - 1);
    });
    root.appendChild(opts); root.appendChild(fb);
    root.appendChild(h('div', { class: 'tui-live', 'aria-live': 'polite' }));
  };
  Quiz.prototype.finish = function () {
    var z = this, root = this.root, n = this.qs.length, sc = this.score;
    root.removeEventListener('keydown', root.__qk);
    root.innerHTML = ''; root.appendChild(h('script', { type: 'application/json', text: JSON.stringify(this.d) }));
    var msg = sc === n ? 'เยี่ยมมาก! คุณรู้จักธรรมศาสตร์ดีทีเดียว' : sc >= n - 1 ? 'เกือบเต็ม!' : sc >= Math.ceil(n / 2) ? 'ทำได้ดี — ลองดูข้อที่พลาดอีกครั้ง' : 'ไม่เป็นไร — กลับไปอ่านแล้วลองใหม่ได้';
    root.appendChild(h('div', { class: 'tui-head' }, [h('span', { class: 'tui-kicker', text: 'ผลคะแนน' })]));
    root.appendChild(h('div', { class: 'tui-score' }, [h('b', { text: String(sc) }), h('span', { text: ' / ' + n })]));
    root.appendChild(h('p', { class: 'tui-q', text: msg }));
    if (this.wrong.length) {
      root.appendChild(h('p', { class: 'tui-note', text: 'ข้อที่พลาด:' }));
      root.appendChild(h('ul', { class: 'tui-list' }, this.wrong.map(function (w) {
        var kids = [h('span', { text: w.q }), h('b', { text: ' → ' + w.correct })];
        if (w.ref) kids.push(h('a', { class: 'tui-src', href: w.ref.href, text: ' อ่านที่: ' + w.ref.label }));
        return h('li', null, kids);
      })));
    }
    root.appendChild(h('button', { type: 'button', class: 'tui-btn tui-btn--ghost', text: 'เล่นอีกครั้ง (สุ่มชุดใหม่)', onclick: function () { z.start(); } }));
    root.appendChild(h('div', { class: 'tui-live', 'aria-live': 'polite' }));
    live(root, 'ได้ ' + sc + ' จาก ' + n + ' คะแนน');
    if (sc === n && !reduce && typeof window.confetti === 'function') {
      try { window.confetti({ particleCount: 120, spread: 70, origin: { y: 0.7 }, colors: ['#c51944', '#ffc72c', '#0b163b'] }); } catch (e) {}
    }
  };

  function init() {
    [].forEach.call(document.querySelectorAll('[data-tu-quiz]'), function (el) { if (!el.__tui) el.__tui = new Quiz(el); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  window.TUInteractive = { init: init };
})();
