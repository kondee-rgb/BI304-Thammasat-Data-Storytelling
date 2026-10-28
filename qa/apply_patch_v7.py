import os

with open('assets/js/tu-interactive.js', 'r', encoding='utf-8') as f:
    text = f.read()

quiz_idx = text.find('  /* ====================== 2) Quiz ====================== */')
if quiz_idx == -1:
    print('Error: Quiz section not found')
    exit(1)

new_head = '''/*!
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

'''

rest = text[quiz_idx:]
# In rest, remove the [data-tu-guess] init line
guess_init_str = "[].forEach.call(document.querySelectorAll('[data-tu-guess]'), function (el) { if (!el.__tui) el.__tui = new Guess(el); });"
rest = rest.replace('    ' + guess_init_str + '\r\n', '')
rest = rest.replace('    ' + guess_init_str + '\n', '')
rest = rest.replace(guess_init_str, '')

updated = new_head + rest
with open('assets/js/tu-interactive.js', 'w', encoding='utf-8', newline='') as f:
    f.write(updated)

print('Updated tu-interactive.js successfully')
