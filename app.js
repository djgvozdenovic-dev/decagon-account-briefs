(function () {
  // ---- Access gate. Obfuscation, not security: see README. ----
  var KEY = 'dcg-briefs-ok', H = 1358338935;
  function hash(s){ var x = 5381; for (var i=0;i<s.length;i++){ x = ((x*33) ^ s.charCodeAt(i)) >>> 0; } return x; }
  function unlock(){
    document.documentElement.classList.remove('gated');
    var g = document.getElementById('gate'); if (g) g.remove();
  }
  try { if (sessionStorage.getItem(KEY) === String(H)) { unlock(); return; } } catch (e) {}
  document.documentElement.classList.add('gated');
  document.addEventListener('DOMContentLoaded', function () {
    var pw = document.getElementById('gatePw'),
        go = document.getElementById('gateGo'),
        err = document.getElementById('gateErr');
    if (!pw) return;
    pw.focus();
    function submit(){
      if (hash(pw.value.trim().toLowerCase()) === H) {
        try { sessionStorage.setItem(KEY, String(H)); } catch (e) {}
        unlock();
      } else {
        err.textContent = 'Not quite. Try again.';
        pw.value = ''; pw.focus();
      }
    }
    go.addEventListener('click', submit);
    pw.addEventListener('keydown', function (e) { if (e.key === 'Enter') submit(); });
  });
})();

(function () {

  // ---- Theme toggle: honour OS default, allow override ----
  var root = document.documentElement;
  var btn = document.getElementById('themeBtn');
  var lbl = document.getElementById('themeLbl');
  var icon = document.getElementById('themeIcon');
  var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

  function apply(mode) {
    root.setAttribute('data-theme', mode);
    lbl.textContent = mode === 'dark' ? 'Light mode' : 'Dark mode';
    icon.textContent = mode === 'dark' ? '◑' : '◐';
  }
  apply(prefersDark ? 'dark' : 'light');
  btn.addEventListener('click', function () {
    apply(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  });


  // ---- Mobile drawer nav ----
  var root = document.documentElement,
      navBtn = document.getElementById('navBtn'),
      scrim = document.getElementById('navScrim');
  function setNav(open) {
    root.classList.toggle('nav-open', open);
    if (navBtn) navBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (navBtn) navBtn.addEventListener('click', function () { setNav(!root.classList.contains('nav-open')); });
  if (scrim) scrim.addEventListener('click', function () { setNav(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setNav(false); });
  // close the drawer after tapping any nav link
  Array.prototype.forEach.call(document.querySelectorAll('aside a'), function (a) {
    a.addEventListener('click', function () { setNav(false); });
  });
  // reset when resizing back to desktop
  window.addEventListener('resize', function () { if (window.innerWidth > 860) setNav(false); });

  // ---- Accordions: bulk toggle, deep-link, jump-link auto-open ----
  var accs = function () { return document.querySelectorAll('details.acc'); };
  document.getElementById('expAll').addEventListener('click', function () {
    Array.prototype.forEach.call(accs(), function (d) { d.open = true; });
  });
  document.getElementById('colAll').addEventListener('click', function () {
    Array.prototype.forEach.call(accs(), function (d) { d.open = false; });
  });

  function openTarget(id) {
    var d = document.getElementById(id);
    if (!d || d.tagName.toLowerCase() !== 'details') return false;
    d.open = true;
    d.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return true;
  }
  Array.prototype.forEach.call(document.querySelectorAll('.jump a'), function (a) {
    a.addEventListener('click', function (e) {
      if (openTarget(this.getAttribute('href').slice(1))) e.preventDefault();
    });
  });
  if (location.hash.length > 1) { openTarget(location.hash.slice(1)); }
})();
