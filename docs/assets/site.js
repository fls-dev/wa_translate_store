/* WA Translate site — no trackers, no external requests. */
(function(){
  var d=document.documentElement,ls=window.localStorage;
  function get(k){try{return ls.getItem(k)}catch(e){return null}}
  function set(k,v){try{ls.setItem(k,v)}catch(e){}}
  var q=(location.search.match(/[?&]lang=(en|ru)/)||[])[1];
  var lang=q||get('wat-lang')||(/^ru|^uk|^be|^kk/i.test(navigator.language||'')?'ru':'en');
  function setLang(l){d.setAttribute('data-lang',l);d.lang=l;set('wat-lang',l);
    document.querySelectorAll('[data-setlang]').forEach(function(b){b.classList.toggle('on',b.dataset.setlang===l)});
    var t=document.documentElement.dataset['title'+l.toUpperCase()];if(t)document.title=t;}
  var theme=get('wat-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
  d.setAttribute('data-theme',theme);
  setLang(lang);
  document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});
  var tb=document.getElementById('theme');
  if(tb)tb.addEventListener('click',function(){var n=d.getAttribute('data-theme')==='dark'?'light':'dark';d.setAttribute('data-theme',n);set('wat-theme',n)});
  /* gallery tabs */
  var tabs=document.querySelectorAll('.tab');
  tabs.forEach(function(t){t.addEventListener('click',function(){
    tabs.forEach(function(x){x.classList.remove('on')});t.classList.add('on');
    document.querySelectorAll('.shots figure').forEach(function(f){f.classList.toggle('on',f.dataset.k===t.dataset.k)});})});
  /* lightbox */
  var lb=document.getElementById('lb');
  if(lb){document.querySelectorAll('.shots img').forEach(function(i){i.addEventListener('click',function(){lb.querySelector('img').src=i.src;lb.classList.add('on')})});
    lb.addEventListener('click',function(){lb.classList.remove('on')});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on')});}
  /* Chrome Web Store link: set STORE_URL when the extension is published */
  var STORE_URL='';
  var cws=document.querySelectorAll('[data-cws]');
  cws.forEach(function(a){
    if(STORE_URL){a.href=STORE_URL;a.target='_blank';a.rel='noopener';a.removeAttribute('aria-disabled');a.classList.remove('soon');}
    else{a.setAttribute('aria-disabled','true');a.addEventListener('click',function(e){e.preventDefault()});}
  });
  document.querySelectorAll('[data-soon]').forEach(function(n){n.style.display=STORE_URL?'none':''});
})();
