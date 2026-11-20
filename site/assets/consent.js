/* Cookie consent banner. Analytics (GTM + GA4) load only after "Accept". */
(() => {
  const KEY = 'pancratzia-consent';
  const es = document.documentElement.lang === 'es';
  const text = es ? {
    label: 'Aviso de cookies',
    title: 'Cookies de analítica',
    body: 'Uso Google Analytics para saber cómo se usa el sitio y mejorarlo. Solo se activa si lo aceptas.',
    policy: 'Política de cookies', policyHref: '/es/cookies/',
    accept: 'Aceptar', reject: 'Rechazar', settings: 'Preferencias de cookies'
  } : {
    label: 'Cookie notice',
    title: 'Analytics cookies',
    body: 'I use Google Analytics to understand how the site is used and improve it. It only runs if you accept.',
    policy: 'Cookie policy', policyHref: '/cookies/',
    accept: 'Accept', reject: 'Reject', settings: 'Cookie settings'
  };

  const read = () => { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
  const write = (value) => { try { localStorage.setItem(KEY, value); } catch (e) {} };

  const clearAnalyticsCookies = () => {
    const host = location.hostname;
    const domains = ['', host, '.' + host, '.' + host.replace(/^www\./, '')];
    document.cookie.split(';').map((c) => c.split('=')[0].trim())
      .filter((name) => /^_ga|^_gid|^_gat/.test(name))
      .forEach((name) => domains.forEach((d) => {
        document.cookie = name + '=; Max-Age=0; path=/' + (d ? '; domain=' + d : '');
      }));
  };

  let banner;
  const hide = () => { if (banner) banner.hidden = true; };

  const choose = (value) => {
    const previous = read();
    write(value);
    hide();
    if (value === 'granted') {
      window.pancratziaLoadTracking && window.pancratziaLoadTracking();
    } else {
      window.gtag && window.gtag('consent', 'update', { analytics_storage: 'denied' });
      clearAnalyticsCookies();
      // Tags that already loaded keep running until the page reloads.
      if (previous === 'granted') location.reload();
    }
  };

  const show = () => {
    if (!banner) {
      banner = document.createElement('section');
      banner.className = 'cookie-banner';
      banner.setAttribute('role', 'region');
      banner.setAttribute('aria-label', text.label);
      banner.innerHTML =
        '<p class="cookie-title">' + text.title + '</p>' +
        '<p>' + text.body + ' <a href="' + text.policyHref + '">' + text.policy + '</a></p>' +
        '<div class="cookie-actions">' +
        '<button type="button" class="button small ghost" data-consent="denied">' + text.reject + '</button>' +
        '<button type="button" class="button small light" data-consent="granted">' + text.accept + '</button>' +
        '</div>';
      banner.addEventListener('click', (event) => {
        const button = event.target.closest('[data-consent]');
        if (button) choose(button.dataset.consent);
      });
      document.body.appendChild(banner);
    }
    banner.hidden = false;
  };

  const addSettingsLink = () => {
    document.querySelectorAll('.legal-links').forEach((nav) => {
      if (nav.querySelector('.cookie-settings')) return;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'cookie-settings';
      button.textContent = text.settings;
      button.addEventListener('click', show);
      nav.appendChild(button);
    });
  };

  const init = () => {
    addSettingsLink();
    const choice = read();
    if (choice !== 'granted' && choice !== 'denied') show();
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
