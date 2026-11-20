const isSpanish = document.documentElement.lang === 'es';
const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.navigation');
const desktopMenu = window.matchMedia('(min-width: 821px)');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const setMenu = (open) => {
  menu.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
  if (open && window.gsap && motionIsEnabled()) {
    gsap.fromTo(navigation, { opacity: .45, y: -9 }, { opacity: 1, y: 0, duration: .3, clearProps: 'opacity,transform' });
  }
};
menu?.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') === 'false'));
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    menu.focus();
  }
});

const navLinks = Array.from(navigation.querySelectorAll('a'));
const currentPage = navigation.querySelector('[aria-current="page"]');
const moveMarker = (link) => {
  if (!desktopMenu.matches || !link) return;
  navigation.style.setProperty('--marker-left', link.offsetLeft + 'px');
  navigation.style.setProperty('--marker-width', link.offsetWidth + 'px');
  navigation.classList.add('has-marker');
};
const resetMarker = () => moveMarker(currentPage);
navLinks.forEach((link) => {
  link.addEventListener('pointerenter', () => moveMarker(link));
  link.addEventListener('focus', () => moveMarker(link));
});
navigation.addEventListener('pointerleave', resetMarker);
navigation.addEventListener('focusout', (event) => {
  if (!navigation.contains(event.relatedTarget)) resetMarker();
});
desktopMenu.addEventListener('change', () => {
  if (desktopMenu.matches) setMenu(false);
  resetMarker();
});
document.fonts?.ready.then(resetMarker);
resetMarker();

const filters = document.querySelectorAll('.filter');
const cards = document.querySelectorAll('.archive-card');
const resultCount = document.querySelector('#result-count');
filters.forEach((button) => {
  button.addEventListener('click', () => {
    filters.forEach((filter) => filter.setAttribute('aria-pressed', String(filter === button)));
    const matching = Array.from(cards).filter((card) => {
      card.hidden = button.dataset.filter !== 'all' && card.dataset.category !== button.dataset.filter;
      return !card.hidden;
    });
    if (window.gsap && motionIsEnabled()) {
      gsap.fromTo(matching.slice(0, 6), { y: 10, opacity: .72 },
        { y: 0, opacity: 1, duration: .34, stagger: .045, overwrite: true, clearProps: 'transform,opacity' });
    }
    const noun = isSpanish ? 'proyecto' : 'project';
    resultCount.textContent = matching.length + ' ' + noun + (matching.length === 1 ? '' : 's');
    window.ScrollTrigger?.refresh();
  });
});

const url = new URL(window.location.href);
const requested = url.searchParams.get('project');
const projectInterest = document.querySelector('#project-interest');
if (requested && projectInterest) {
  const option = Array.from(projectInterest.options).find((item) => item.value === requested);
  if (option) {
    projectInterest.value = option.value;
    document.querySelectorAll('.language-list a').forEach((link) => {
      const alternate = new URL(link.href);
      alternate.searchParams.set('project', option.value);
      link.href = alternate.href;
    });
  }
}
const inquiryForm = document.querySelector('#project-inquiry');
inquiryForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  const fields = new FormData(inquiryForm);
  const service = projectInterest.selectedOptions[0].textContent.trim();
  const labels = isSpanish
    ? { subject: 'Consulta de proyecto', hello: 'Hola, Laura:', name: 'Nombre', email: 'Correo electrónico', service: 'Servicio', website: 'Sitio web actual' }
    : { subject: 'Project inquiry', hello: 'Hi Laura,', name: 'Name', email: 'Email', service: 'Service', website: 'Current website' };
  const subject = labels.subject + ' · ' + service;
  const lines = [
    labels.hello,
    '',
    labels.name + ': ' + fields.get('Name'),
    labels.email + ': ' + fields.get('Email'),
    labels.service + ': ' + service,
  ];
  if (fields.get('Website')) lines.push(labels.website + ': ' + fields.get('Website'));
  lines.push('', fields.get('Project details'));
  window.location.href = inquiryForm.getAttribute('action') + '?subject=' + encodeURIComponent(subject) +
    '&body=' + encodeURIComponent(lines.join('\n'));
});

const motionToggle = document.querySelector('.motion-toggle');
let motionPaused = false;
try {
  motionPaused = sessionStorage.getItem('pancratzia-motion') === 'paused';
} catch {
  // The preference stays available for this page if storage is disabled.
}
const motionIsEnabled = () => !motionPaused && !reducedMotion.matches;
const setupPointerAccent = () => {
  const accent = document.querySelector('.pointer-accent');
  const caption = accent.querySelector('span');
  const moveX = gsap.quickTo(accent, 'x', { duration: .25, ease: 'power3.out' });
  const moveY = gsap.quickTo(accent, 'y', { duration: .25, ease: 'power3.out' });
  const fade = gsap.quickTo(accent, 'opacity', { duration: .18 });
  let current = null;
  const hide = () => {
    if (!current) return;
    current = null;
    fade(0);
  };
  const move = (event) => {
    if (event.pointerType !== 'mouse') return;
    const target = event.target.closest('[data-cursor]');
    if (!target || document.querySelector('dialog[open]')) {
      hide();
      return;
    }
    const label = target.dataset.cursor;
    const offsetX = event.clientX > window.innerWidth - 120 ? -88 : 17;
    const offsetY = event.clientY > window.innerHeight - 55 ? -47 : 17;
    const x = event.clientX + offsetX;
    const y = event.clientY + offsetY;
    if (target !== current) {
      if (!current) {
        moveX(x, x);
        moveY(y, y);
      }
      current = target;
      caption.textContent = label;
      fade(1);
    }
    moveX(x);
    moveY(y);
  };
  const leave = (event) => {
    if (!event.relatedTarget) hide();
  };
  document.addEventListener('pointermove', move);
  document.addEventListener('pointerout', leave);
  window.addEventListener('blur', hide);
  window.addEventListener('scroll', hide, { passive: true });
  return () => {
    document.removeEventListener('pointermove', move);
    document.removeEventListener('pointerout', leave);
    window.removeEventListener('blur', hide);
    window.removeEventListener('scroll', hide);
    caption.textContent = '';
  };
};

if (window.gsap && window.ScrollTrigger) {
  gsap.registerPlugin(ScrollTrigger);
  const motionContext = gsap.matchMedia();
  motionContext.add('(prefers-reduced-motion: no-preference)', () => {
    if (motionPaused) return;
    const hero = document.querySelector('.hero, .page-hero');
    const art = hero?.querySelector('.hero-art');
    if (!art) return;

    const intro = gsap.timeline({ defaults: { ease: 'power3.out' } });
    intro.from('.topbar .shell', { y: -13, opacity: .3, duration: .55, clearProps: 'transform,opacity' }, 0)
      .from('[data-headline] > span', {
        yPercent: 19, opacity: .14, clipPath: 'inset(0 0 100% 0)', duration: .93, stagger: .11,
        clearProps: 'transform,opacity,clipPath'
      }, .10)
      .from('[data-enter]', { y: 14, opacity: .15, duration: .65, stagger: .09, clearProps: 'transform,opacity' }, .26)
      .from('.orbital-lines', { y: 31, opacity: .15, duration: 1.9, clearProps: 'transform,opacity' }, 0)
      .fromTo('.orbital-trace', { attr: { 'stroke-dasharray': 1, 'stroke-dashoffset': 1 } },
        { attr: { 'stroke-dashoffset': 0 }, duration: 2.5, ease: 'power2.inOut' }, .11)
      .from('.orbital-node circle:first-child', {
        opacity: .05, scale: .5, transformOrigin: 'center center', stagger: .24, duration: .76, clearProps: 'transform,opacity'
      }, 1.22);

    gsap.to(art, { yPercent: 16, scale: 1.045, ease: 'none',
      scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: .5 } });

    gsap.utils.toArray('[data-reveal]').forEach((section) => {
      const targets = section.matches('.service-items, .grid-prices, .scope-grid, .timeline') ? section.children : section;
      gsap.from(targets, { y: 22, opacity: .7, duration: .65, stagger: .08, ease: 'power2.out', clearProps: 'transform,opacity',
        scrollTrigger: { trigger: section, start: 'top 93%', once: true } });
    });

    document.querySelectorAll('.section-transition').forEach((separator) => {
      gsap.from(separator.querySelectorAll('span'), {
        y: 12, opacity: .35, duration: .55, stagger: .07, ease: 'power2.out',
        clearProps: 'transform,opacity',
        scrollTrigger: { trigger: separator, start: 'top 91%', once: true }
      });
    });

    document.querySelectorAll('[data-next-panel]').forEach((panel) => {
      const trace = panel.querySelector('.next-trace');
      gsap.fromTo(trace, { attr: { 'stroke-dasharray': 1, 'stroke-dashoffset': 1 } },
        { attr: { 'stroke-dashoffset': 0 }, ease: 'none',
          scrollTrigger: { trigger: panel, start: 'top 94%', end: 'center 66%', scrub: .42 } });
      gsap.from(panel.querySelector('.next-actions'), {
        y: 20, opacity: .62, duration: .52, ease: 'power3.out', clearProps: 'transform,opacity',
        scrollTrigger: { trigger: panel, start: 'top 84%', once: true }
      });
      ScrollTrigger.create({ trigger: panel, start: 'top bottom', end: 'bottom top',
        toggleClass: { targets: panel, className: 'is-in-view' } });
    });

    document.querySelectorAll('[data-project-reveal]').forEach((visual) => {
      gsap.from(visual, {
        clipPath: 'inset(9% 0 0 0 round 13px)', y: 12, duration: .58, ease: 'power3.out',
        immediateRender: false, clearProps: 'transform,clipPath',
        scrollTrigger: { trigger: visual, start: 'top 92%', once: true }
      });
    });

    const shapes = art.querySelectorAll('.float-shape');
    const signal = art.querySelector('.orbital-signal');
    const route = art.querySelector('.orbital-trace');
    const progress = { along: 0 };
    const routeLength = route.getTotalLength();
    const loop = gsap.timeline({ paused: true });
    loop.to(shapes, {
      x: (index) => index === 1 ? 22 : -13,
      y: (index) => index === 1 ? -49 : 38,
      rotation: (index) => index === 1 ? -23 : 44,
      scale: 1.15, transformOrigin: '50% 50%',
      duration: 4.4, stagger: .75, yoyo: true, repeat: -1, ease: 'sine.inOut'
    }, 0);
    loop.to(progress, {
      along: 1, duration: 8, repeat: -1, ease: 'none',
      onUpdate: () => {
        const point = route.getPointAtLength(progress.along * routeLength);
        signal.setAttribute('cx', point.x);
        signal.setAttribute('cy', point.y);
      }
    }, 0);
    loop.to(signal, { opacity: .95, duration: .8 }, 0);
    let visibleHero;
    const updateLoop = () => loop.paused(document.hidden || !visibleHero?.isActive);
    visibleHero = ScrollTrigger.create({ trigger: hero, start: 'top bottom', end: 'bottom top', onToggle: updateLoop });
    document.addEventListener('visibilitychange', updateLoop);
    updateLoop();

    const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
    const removeHover = [];
    const removePointer = finePointer.matches ? setupPointerAccent() : null;
    if (finePointer.matches) {
      document.querySelectorAll('[data-hover]').forEach((surface) => {
        const target = surface.querySelector('.screen, svg');
        const shiftX = gsap.quickTo(target, 'x', { duration: .40, ease: 'power3.out' });
        const shiftY = gsap.quickTo(target, 'y', { duration: .40, ease: 'power3.out' });
        const move = (event) => {
          const box = surface.getBoundingClientRect();
          shiftX(((event.clientX - box.left) / box.width - .5) * 14);
          shiftY(((event.clientY - box.top) / box.height - .5) * 14);
        };
        const reset = () => { shiftX(0); shiftY(0); };
        surface.addEventListener('pointermove', move);
        surface.addEventListener('pointerleave', reset);
        removeHover.push(() => {
          surface.removeEventListener('pointermove', move);
          surface.removeEventListener('pointerleave', reset);
        });
      });
    }
    return () => {
      document.removeEventListener('visibilitychange', updateLoop);
      removeHover.forEach((remove) => remove());
      removePointer?.();
      document.querySelectorAll('[data-next-panel]').forEach((panel) => panel.classList.remove('is-in-view'));
      ['cx', 'cy'].forEach((attribute) => signal.removeAttribute(attribute));
    };
  });
  const showMotionState = () => {
    const pauseLabel = isSpanish ? 'Pausar animación' : 'Pause animation';
    const resumeLabel = isSpanish ? 'Reanudar animación' : 'Resume animation';
    const label = motionPaused ? resumeLabel : pauseLabel;
    motionToggle.hidden = reducedMotion.matches;
    motionToggle.setAttribute('aria-label', label);
    motionToggle.setAttribute('title', label);
    motionToggle.classList.toggle('is-paused', motionPaused);
    document.documentElement.classList.toggle('motion-paused', motionPaused);
  };
  motionToggle.addEventListener('click', () => {
    motionPaused = !motionPaused;
    try {
      sessionStorage.setItem('pancratzia-motion', motionPaused ? 'paused' : 'active');
    } catch {
      // Keep the page-level preference when storage is unavailable.
    }
    showMotionState();
    gsap.matchMediaRefresh();
  });
  reducedMotion.addEventListener('change', showMotionState);
  showMotionState();
}

const preview = document.querySelector('#project-preview');
if (preview && typeof preview.showModal === 'function') {
  const previewTitle = preview.querySelector('h2');
  const previewImage = preview.querySelector('img');
  document.querySelectorAll('.project-preview').forEach((link) => {
    link.addEventListener('click', (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      previewTitle.textContent = link.dataset.title;
      previewImage.src = link.href;
      const description = isSpanish ? 'Vista previa completa de ' : 'Complete project preview for ';
      previewImage.alt = description + link.dataset.title;
      preview.showModal();
    });
  });
}

const openFeaturedProject = () => {
  const projectId = window.location.hash.slice(1);
  const project = document.getElementById(projectId);
  const details = project?.querySelector('.case-info');
  if (details) details.open = true;
};
if (cards.length) {
  openFeaturedProject();
  window.addEventListener('hashchange', openFeaturedProject);
}
