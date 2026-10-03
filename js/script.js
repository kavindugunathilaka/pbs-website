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

  /* YouTube Shorts IDs, shown in order in the Videos section. */
  const REELS = [
    'H_6nEMdlAJk',
    'nhGKPW9T97Q',
    'E6R3xKaU7mo',
    '_jB0lTdaYMY',
    'xJ3Rc278e4Y',
    'iuRT9uJsRu4',
    'ojXUzfCtD4A',
    'yX8wqarXu5k'
  ];

  const WHATSAPP = '94716664111';
  const EMAIL = 'info@panambara.lk';
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
  // buttons that point at a social page; hide when no URL is set
  $$('[data-social]').forEach(a => {
    const url = SOCIAL[a.dataset.social];
    if (url) a.href = url; else a.hidden = true;
  });

  /* ---------- video reels: thumbnail first, player loads on tap ---------- */
  const rail = $('#rail');
  if (rail && REELS.length) {
    const pad = (n) => String(n).padStart(2, '0');
    const thumb = (id, q) => `https://i.ytimg.com/vi/${id}/${q}.jpg`;

    const renderCard = (li, id, i) => {
      li.innerHTML = '';
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'reel-btn';
      btn.setAttribute('aria-label', `Play reel ${i + 1} of ${REELS.length}`);
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
      btn.addEventListener('click', () => playReel(li, id, i));
      li.appendChild(btn);
    };

    const playReel = (li, id, i) => {
      // only one reel plays at a time: put any other card back to its thumbnail
      $$('.reel.is-playing', rail).forEach(other => {
        if (other === li) return;
        other.classList.remove('is-playing');
        renderCard(other, other.dataset.id, Number(other.dataset.index));
      });
      li.classList.add('is-playing');
      li.innerHTML = '';
      const frame = document.createElement('iframe');
      frame.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&playsinline=1&modestbranding=1`;
      frame.title = `PBS reel ${i + 1} of ${REELS.length}`;
      frame.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      frame.allowFullscreen = true;
      frame.referrerPolicy = 'strict-origin-when-cross-origin';
      li.appendChild(frame);
      frame.focus();
    };

    REELS.forEach((id, i) => {
      const li = document.createElement('li');
      li.className = 'reel';
      li.dataset.id = id;
      li.dataset.index = i;
      renderCard(li, id, i);
      rail.appendChild(li);
    });

    const prev = $('#railPrev'), next = $('#railNext'), count = $('#railCount');
    const step = () => {
      const card = $('.reel', rail);
      return card ? card.getBoundingClientRect().width + 18 : 280;
    };
    const updateRail = () => {
      const max = rail.scrollWidth - rail.clientWidth;
      prev.disabled = rail.scrollLeft <= 4;
      next.disabled = rail.scrollLeft >= max - 4;
      const first = Math.min(REELS.length, Math.round(rail.scrollLeft / step()) + 1);
      count.textContent = `${pad(first)} / ${pad(REELS.length)}`;
    };
    prev.addEventListener('click', () => rail.scrollBy({ left: -step() * 2, behavior: reduceMotion ? 'auto' : 'smooth' }));
    next.addEventListener('click', () => rail.scrollBy({ left: step() * 2, behavior: reduceMotion ? 'auto' : 'smooth' }));
    rail.addEventListener('scroll', updateRail, { passive: true });
    window.addEventListener('resize', updateRail);
    updateRail();
  }

  /* ---------- nav: scrolled state + scrollspy ---------- */
  const nav = $('#nav');
  const heroImg = $('.hero-media img');
  const hero = $('#home');
  let ticking = false;

  const onScroll = () => {
    const y = window.scrollY;
    nav.classList.toggle('is-scrolled', y > 40);

    if (!reduceMotion && heroImg && window.innerWidth > 760 && y < hero.offsetHeight) {
      heroImg.style.transform = `translate3d(0, ${y * 0.12}px, 0) scale(1.06)`;
    }
    ticking = false;
  };
  window.addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  const links = $$('.nav-links a');
  const spy = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === `#${e.target.id}`));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  links.forEach(a => { const t = $(a.getAttribute('href')); if (t) spy.observe(t); });

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

  /* ---------- in-page anchors: land with a little air above the heading ---------- */
  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = $(id);
      if (!target) return;
      e.preventDefault();
      const top = id === '#home' ? 0 : target.getBoundingClientRect().top + window.scrollY - 10;
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

  /* ---------- services accordion (one open at a time) ---------- */
  const items = $$('.svc');
  items.forEach(item => {
    const btn = $('button', item);
    btn.addEventListener('click', () => {
      const willOpen = !item.classList.contains('is-open');
      items.forEach(i => {
        i.classList.remove('is-open');
        $('button', i).setAttribute('aria-expanded', 'false');
      });
      if (willOpen) {
        item.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

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
  const form = $('#contactForm');
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

  /* ---------- year ---------- */
  const y = $('#year');
  if (y) y.textContent = new Date().getFullYear();
})();
