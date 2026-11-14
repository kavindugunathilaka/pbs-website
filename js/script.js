(() => {
  'use strict';

  /* ------------------------------------------------------------------
     Edit these once you have the real page links. Empty = icon hidden.
     ------------------------------------------------------------------ */
  const SOCIAL = {
    facebook: 'https://www.facebook.com/PBSolutionsSL/',
    linkedin: 'https://www.linkedin.com/in/deepani-panambara-6a226b141',
    tiktok:   '',
    youtube:  'https://www.youtube.com/channel/UCYsc7NPU5trLjidRzrCPwHA'
  };

  const WHATSAPP = '94716664111';
  const EMAIL = 'info@panambara.lk';
  const SLIDE_MS = 7000;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => Array.from(el.querySelectorAll(s));

  /* ---------- socials ---------- */
  const LABELS = { facebook: 'Facebook', linkedin: 'LinkedIn', tiktok: 'TikTok', youtube: 'YouTube' };
  $$('[data-socials]').forEach(list => {
    Object.entries(SOCIAL).forEach(([name, url]) => {
      if (!url) return;
      const li = document.createElement('li');
      li.innerHTML = `<a href="${url}" target="_blank" rel="noopener" aria-label="${LABELS[name]}"><svg aria-hidden="true"><use href="#i-${name}"/></svg></a>`;
      list.appendChild(li);
    });
  });
  $$('[data-social]').forEach(a => {
    const url = SOCIAL[a.dataset.social];
    if (url) a.href = url; else a.hidden = true;
  });

  /* ---------- nav: scrolled state + hero image parallax ---------- */
  const nav = $('#nav');
  const hero = $('#home');
  const heroImgs = $$('.slide-media img');
  let ticking = false;
  const onScroll = () => {
    const y = window.scrollY;
    nav.classList.toggle('is-scrolled', y > 40);
    if (!reduceMotion && heroImgs.length && hero && window.innerWidth > 760 && y < hero.offsetHeight) {
      heroImgs.forEach(img => { img.style.transform = `translate3d(0, ${y * 0.12}px, 0) scale(1.06)`; });
    }
    ticking = false;
  };
  window.addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  /* ---------- services dropdown (desktop) ---------- */
  const menuBtn = $('#menuBtn');
  const mega = $('#svcMenu');
  if (menuBtn && mega) {
    let closeTimer;
    const setMega = (open) => {
      mega.classList.toggle('is-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
    };
    const canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    menuBtn.addEventListener('click', () => setMega(menuBtn.getAttribute('aria-expanded') !== 'true'));
    if (canHover) {
      const wrap = menuBtn.parentElement;
      wrap.addEventListener('pointerenter', () => { clearTimeout(closeTimer); setMega(true); });
      wrap.addEventListener('pointerleave', () => { closeTimer = setTimeout(() => setMega(false), 180); });
    }
    document.addEventListener('click', (e) => { if (!e.target.closest('.has-menu')) setMega(false); });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mega.classList.contains('is-open')) { setMega(false); menuBtn.focus(); }
    });
    mega.addEventListener('focusout', (e) => { if (!mega.contains(e.relatedTarget) && e.relatedTarget !== menuBtn) setMega(false); });
  }

  /* ---------- mobile menu ---------- */
  const burger = $('#burger');
  const sheet = $('#sheet');
  const setMenu = (open) => {
    document.body.classList.toggle('nav-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    sheet.setAttribute('aria-hidden', String(!open));
    if (open) { const first = $('a', sheet); first && setTimeout(() => first.focus({ preventScroll: true }), 300); }
  };
  burger.addEventListener('click', () => setMenu(!document.body.classList.contains('nav-open')));
  $$('a', sheet).forEach(a => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && document.body.classList.contains('nav-open')) { setMenu(false); burger.focus(); }
  });
  window.addEventListener('resize', () => { if (window.innerWidth > 960) setMenu(false); });

  const subBtn = $('.sheet-sub-btn');
  const sub = $('#sheetSub');
  if (subBtn && sub) {
    subBtn.addEventListener('click', () => {
      const open = subBtn.getAttribute('aria-expanded') !== 'true';
      subBtn.setAttribute('aria-expanded', String(open));
      sub.classList.toggle('is-open', open);
    });
  }

  /* ---------- same-page anchors: land with a little air above the heading ---------- */
  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = $(id);
      if (!target) return;
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 10;
      window.scrollTo({ top, behavior: reduceMotion ? 'auto' : 'smooth' });
      history.replaceState(null, '', id);
    });
  });

  /* ---------- reveal on scroll ---------- */
  const reveals = $$('.reveal');
  reveals.forEach(el => {
    const siblings = Array.from(el.parentElement.children).filter(c => c.classList.contains('reveal'));
    el.style.setProperty('--d', `${Math.min(siblings.indexOf(el), 5) * 0.08}s`);
  });
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(el => io.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('is-in'));
  }

  /* ---------- stat counters ---------- */
  const counters = $$('.stat-num[data-count], .stat-num[data-since]');
  if (counters.length && 'IntersectionObserver' in window) {
    const year = new Date().getFullYear();
    const run = (el) => {
      const target = el.dataset.since ? year - parseInt(el.dataset.since, 10) : parseInt(el.dataset.count, 10);
      const show = (n) => n.toLocaleString('en-US') + (el.dataset.suffix || '');
      el.textContent = show(target);                           // correct value even if animation never runs
      if (reduceMotion) return;
      const start = performance.now(), dur = 1200;
      const step = (now) => {
        const p = Math.min((now - start) / dur, 1);
        el.textContent = show(Math.round((1 - Math.pow(1 - p, 3)) * target));
        if (p < 1) requestAnimationFrame(step); else el.textContent = show(target);
      };
      el.textContent = show(0);
      requestAnimationFrame(step);
      setTimeout(() => { el.textContent = show(target); }, dur + 300);
    };
    const co = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { run(e.target); co.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counters.forEach(el => co.observe(el));
  }

  /* ---------- hero slider ---------- */
  const slides = $$('.slide');
  if (hero && slides.length > 1) {
    const pgs = $$('.pg', hero);
    const toggle = $('#pgToggle');
    let index = 0;
    let playing = !reduceMotion;
    hero.style.setProperty('--slide-ms', `${SLIDE_MS}ms`);

    const render = () => {
      slides.forEach((s, i) => {
        const on = i === index;
        s.classList.toggle('is-active', on);
        s.setAttribute('aria-hidden', String(!on));
        on ? s.removeAttribute('inert') : s.setAttribute('inert', '');
      });
      pgs.forEach((p, i) => {
        p.classList.toggle('is-active', i === index);
        i === index ? p.setAttribute('aria-current', 'true') : p.removeAttribute('aria-current');
      });
      // restart the progress animation, which also drives the auto-advance
      hero.classList.remove('is-running');
      void hero.offsetWidth;
      if (playing) hero.classList.add('is-running');
    };
    const go = (n) => { index = (n + slides.length) % slides.length; render(); };

    pgs.forEach((p, i) => p.addEventListener('click', () => go(i)));
    // each time the active progress bar finishes, move on
    hero.addEventListener('animationend', (e) => {
      if (e.animationName === 'fill' && playing) go(index + 1);
    });

    const setPlaying = (on, byUser) => {
      playing = on;
      hero.classList.toggle('is-running', on);
      if (on) { hero.classList.remove('is-paused'); render(); }
      toggle.setAttribute('aria-label', on ? 'Pause slideshow' : 'Play slideshow');
      toggle.innerHTML = `<svg class="i" aria-hidden="true"><use href="#i-${on ? 'pause' : 'play'}"/></svg>`;
      if (byUser) hero.dataset.userPaused = on ? '' : '1';
    };
    toggle.addEventListener('click', () => setPlaying(!playing, true));

    // pause while pointer is over the hero or focus is inside it
    const hold = (on) => { if (playing) hero.classList.toggle('is-paused', on); };
    hero.addEventListener('pointerenter', () => hold(true));
    hero.addEventListener('pointerleave', () => hold(false));
    hero.addEventListener('focusin', () => hold(true));
    hero.addEventListener('focusout', () => hold(false));
    document.addEventListener('visibilitychange', () => hold(document.hidden));

    hero.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') go(index + 1);
      if (e.key === 'ArrowLeft') go(index - 1);
    });

    // swipe on touch screens
    let x0 = null;
    hero.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener('touchend', (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) go(index + (dx < 0 ? 1 : -1));
      x0 = null;
    }, { passive: true });

    if (!playing) toggle.innerHTML = '<svg class="i" aria-hidden="true"><use href="#i-play"/></svg>', toggle.setAttribute('aria-label', 'Play slideshow');
    render();
  }

  /* ---------- video reels: thumbnail first, player loads on tap ----------
     The reel cards and their captions are in the page itself (built from tools/content.py);
     this only adds the thumbnails, the player and the arrows. */
  const rail = $('#rail');
  const reels = rail ? $$('.reel', rail) : [];
  if (reels.length) {
    const pad = (n) => String(n).padStart(2, '0');
    const thumb = (id, q) => `https://i.ytimg.com/vi/${id}/${q}.jpg`;
    const frameOf = (li) => $('.reel-frame', li);
    const titleOf = (li) => (($('h3', li) || {}).textContent || `reel ${Number(li.dataset.index) + 1}`);

    const renderThumb = (li) => {
      const id = li.dataset.id, i = Number(li.dataset.index), frame = frameOf(li);
      frame.innerHTML = '';
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'reel-btn';
      btn.setAttribute('aria-label', `Play video: ${titleOf(li)}`);
      const img = document.createElement('img');
      img.alt = '';
      img.loading = 'lazy';
      img.decoding = 'async';
      img.src = thumb(id, 'maxresdefault');
      img.addEventListener('error', () => { if (!img.dataset.fb) { img.dataset.fb = '1'; img.src = thumb(id, 'hqdefault'); } });
      img.addEventListener('load', () => { if (img.naturalWidth <= 120 && !img.dataset.fb) { img.dataset.fb = '1'; img.src = thumb(id, 'hqdefault'); } });
      const no = document.createElement('span');
      no.className = 'reel-no tnum';
      no.textContent = pad(i + 1);
      const play = document.createElement('span');
      play.className = 'reel-play';
      play.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M8 5.5v13l11-6.5z"/></svg>';
      btn.append(img, no, play);
      btn.addEventListener('click', () => playReel(li));
      frame.appendChild(btn);
    };

    const playReel = (li) => {
      // only one reel plays at a time: put any other card back to its thumbnail
      $$('.reel.is-playing', rail).forEach(other => {
        if (other === li) return;
        other.classList.remove('is-playing');
        renderThumb(other);
      });
      li.classList.add('is-playing');
      const frame = frameOf(li);
      frame.innerHTML = '';
      const player = document.createElement('iframe');
      player.src = `https://www.youtube-nocookie.com/embed/${li.dataset.id}?autoplay=1&rel=0&playsinline=1&modestbranding=1`;
      player.title = `PBS video: ${titleOf(li)}`;
      player.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      player.allowFullscreen = true;
      player.referrerPolicy = 'strict-origin-when-cross-origin';
      frame.appendChild(player);
      player.focus();
    };

    reels.forEach(renderThumb);

    const prev = $('#railPrev'), next = $('#railNext'), count = $('#railCount');
    const step = () => reels[0].getBoundingClientRect().width + 18;
    const updateRail = () => {
      const max = rail.scrollWidth - rail.clientWidth;
      prev.disabled = rail.scrollLeft <= 4;
      next.disabled = rail.scrollLeft >= max - 4;
      const first = Math.min(reels.length, Math.round(rail.scrollLeft / step()) + 1);
      count.textContent = `${pad(first)} / ${pad(reels.length)}`;
    };
    prev.addEventListener('click', () => rail.scrollBy({ left: -step() * 2, behavior: reduceMotion ? 'auto' : 'smooth' }));
    next.addEventListener('click', () => rail.scrollBy({ left: step() * 2, behavior: reduceMotion ? 'auto' : 'smooth' }));
    rail.addEventListener('scroll', updateRail, { passive: true });
    window.addEventListener('resize', updateRail);
    updateRail();
  }

  /* ---------- open / closed status (Sri Lanka time) ---------- */
  // [opens, closes] in minutes from midnight, index 0 = Sunday
  const HOURS = [null, [540, 1020], [540, 1020], [540, 1020], [540, 1020], [540, 1020], [540, 780]];
  const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const fmt = (m) => {
    const h = Math.floor(m / 60), mm = String(m % 60).padStart(2, '0');
    return `${((h + 11) % 12) + 1}:${mm} ${h < 12 ? 'am' : 'pm'}`;
  };
  const colomboNow = () => {
    const parts = new Intl.DateTimeFormat('en-GB', {
      timeZone: 'Asia/Colombo', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false
    }).formatToParts(new Date());
    const get = (t) => parts.find(p => p.type === t).value;
    return { day: DAYS.indexOf(get('weekday')), mins: (parseInt(get('hour'), 10) % 24) * 60 + parseInt(get('minute'), 10) };
  };
  const statusText = () => {
    const { day, mins } = colomboNow();
    const today = HOURS[day];
    if (today && mins >= today[0] && mins < today[1]) return { open: true, text: `Open now · closes ${fmt(today[1])}` };
    if (today && mins < today[0]) return { open: false, text: `Closed · opens today ${fmt(today[0])}` };
    for (let i = 1; i <= 7; i++) {
      const d = (day + i) % 7;
      if (HOURS[d]) return { open: false, text: `Closed · opens ${i === 1 ? 'tomorrow' : DAYS[d]} ${fmt(HOURS[d][0])}` };
    }
    return { open: false, text: 'Closed' };
  };
  const renderStatus = () => {
    const s = statusText();
    $$('[data-open-status]').forEach(el => {
      el.classList.toggle('is-open', s.open);
      const span = $('span', el);
      if (span) span.textContent = s.text;
    });
  };
  renderStatus();
  setInterval(renderStatus, 60000);

  /* ---------- contact form: WhatsApp or email ---------- */
  const form = $('#form');
  if (form && form.tagName === 'FORM') {
    const err = $('#formError');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const channel = (e.submitter && e.submitter.dataset.channel) || 'whatsapp';
      const data = new FormData(form);
      const name = String(data.get('name') || '').trim();
      const phone = String(data.get('phone') || '').trim();
      const service = String(data.get('service') || '').trim();
      const message = String(data.get('message') || '').trim();

      const nameEl = form.elements.name, phoneEl = form.elements.phone;
      nameEl.setAttribute('aria-invalid', String(!name));
      phoneEl.setAttribute('aria-invalid', String(!phone));
      if (!name || !phone) {
        err.hidden = false;
        (name ? phoneEl : nameEl).focus();
        return;
      }
      err.hidden = true;

      const lines = [
        'Hello Panambara Business Solutions,',
        `I'm ${name} (${phone}).`,
        `I need help with: ${service}.`,
        message ? `\n${message}` : ''
      ].filter(Boolean).join('\n');

      if (channel === 'email') {
        window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent('Website enquiry: ' + service)}&body=${encodeURIComponent(lines)}`;
      } else {
        window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(lines)}`, '_blank', 'noopener');
      }
    });
  }

  /* ---------- year ---------- */
  const y = $('#year');
  if (y) y.textContent = new Date().getFullYear();
})();
