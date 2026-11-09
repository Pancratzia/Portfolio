from core import t, u, write_page, star, CHECK, ARR

PROJECTS = [
    ('joumana-kayrouz', 'Joumana Kayrouz', '/assets/joumana.png', ('Law firm · Redesign + SEO', 'Firma legal · Rediseño + SEO'),
     ('A fresh chapter for an established law firm.', 'Un nuevo capítulo para una firma consolidada.')),
    ('mungo-law', 'Mungo Law', '/assets/mungo-upwork.webp', ('Law firm · Multi-page site', 'Firma legal · Sitio multipágina'),
     ('From one landing page to a connected website.', 'De una landing a un sitio completo y conectado.')),
    ('hire-warriors', 'Hire Warriors', '/assets/hire-upwork.webp', ('Directory · Webflow CMS', 'Directorio · Webflow CMS'),
     ('A national directory of veteran-owned businesses: 102 categories in 50 states.', 'Un directorio nacional de negocios de veteranos: 102 categorías en 50 estados.')),
    ('her-vitality-clinic', 'Her Vitality Clinic', '/assets/her-vitality-upwork.webp', ('Healthcare · WordPress', 'Salud · WordPress'),
     ("A considered digital presence for women's wellness.", 'Una presencia digital cuidada para el bienestar femenino.')),
]


def work_cards(cols='g2'):
    out = []
    for slug, name, img, meta, desc in PROJECTS:
        out.append(f'''<a class="work reveal" href="{u('/work/' + slug + '/')}">
<div class="shot" style="aspect-ratio: 4 / 3"><img src="{img}" alt="{t(name + ' website', 'Sitio web de ' + name)}" loading="lazy" width="1000" height="750"></div>
<p class="sm" style="margin: 0; letter-spacing: .06em; text-transform: uppercase">{t(*meta)}</p>
<h3 class="h3" style="font-size: 30px; transition: color .2s">{name} ↗</h3>
<p class="txt">{t(*desc)}</p>
</a>''')
    return f'<div class="{cols}" style="gap: 56px 40px">' + ''.join(out) + '</div>'


def service_card(n, icon, title, body, items, price_label, price, dark=False, href='/services/'):
    cls = 'cell' + (' dark' if dark else ' card br')
    lis = ''.join(f'<li>{i}</li>' for i in items)
    border = '#4a3f55' if dark else '#d9d1df'
    return f'''<a class="{cls}" href="{u(href)}" style="text-decoration: none; color: {'#f5f2ec' if dark else '#251b33'}">
{icon}
<h3 class="h3">{title}</h3>
<p class="txt" style="font-size: 15px">{body}</p>
<ul class="list" style="font-size: 14px">{lis}</ul>
<div style="margin-top: auto; padding-top: 20px; border-top: 1px solid {border}"><p class="sm" style="margin: 0{'; color: #b3a8bd' if dark else ''}">{price_label}</p><p style="margin: 4px 0 0; font: 700 28px/1 'Space Grotesk', sans-serif">{price}</p></div>
</a>'''


ICON_NEW = '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="#7136d0" stroke-width="2" aria-hidden="true"><rect x="3" y="8" width="46" height="34"></rect><path d="M3 16h46M10 24h18M10 30h12"></path><rect x="32" y="22" width="11" height="13" fill="#ddd0ef"></rect><path d="M40 4l1 3 3 1-3 1-1 3-1-3-3-1 3-1Z" fill="#7136d0" stroke="none"></path></svg>'
ICON_MIG = '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="#7136d0" stroke-width="2" aria-hidden="true"><rect x="3" y="12" width="18" height="24"></rect><rect x="31" y="12" width="18" height="24" fill="#ddd0ef"></rect><path d="M7 19h10M7 24h8M35 19h10M35 24h8M22 30h8M26 26l4 4-4 4"></path></svg>'
ICON_CODE = '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="#7136d0" stroke-width="2" aria-hidden="true"><path d="M17 16L7 26l10 10M35 16l10 10-10 10"></path><path d="M30 10L22 42"></path></svg>'
ICON_CARE = '<svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="#b994f5" stroke-width="2" aria-hidden="true"><path d="M26 4l18 7v12c0 12-8 20-18 25C16 43 8 35 8 23V11Z"></path><path d="M17 26l6 6 12-12"></path></svg>'


def home():
    marquee_items = [t('Law firms', 'Firmas legales'), t('Health + wellness clinics', 'Clínicas de salud y bienestar'), t('Directories + communities', 'Directorios y comunidades'), t('Creative agencies', 'Agencias creativas'), t('Founders', 'Emprendedores'), t('Veteran-owned businesses', 'Negocios de veteranos')]
    marquee = ''.join(f'{m} <span aria-hidden="true" style="color: #ddd0ef">✦</span> ' for m in marquee_items)
    faq = [
        (t('How much does a website cost?', '¿Cuánto cuesta un sitio web?'), t('Landing pages start at USD 200 and websites at USD 600, 1,000 or 1,500 depending on pages and CMS collections. The final quote depends on your content and functionality.', 'Las landings parten de USD 200 y los sitios de USD 600, 1.000 o 1.500 según páginas y colecciones CMS. La cotización final depende de tu contenido y funcionalidades.')),
        (t('How long does it take?', '¿Cuánto tarda?'), t('It depends on scope, content readiness, migration volume and feedback. We agree on a schedule after reviewing your project.', 'Depende del alcance, del contenido listo, del volumen de migración y del feedback. Acordamos un calendario después de revisar tu proyecto.')),
        (t('Can you build from my existing design?', '¿Puedes construir sobre mi diseño actual?'), t("Yes. Send the Figma file and I'll build it in Webflow, or rebuild your current site with a new direction.", 'Sí. Envíame el archivo de Figma y lo construyo en Webflow, o reconstruyo tu sitio actual con una nueva dirección.')),
        (t('Will I lose my Google rankings if I migrate?', '¿Perderé posicionamiento en Google si migro?'), t('A planned move reduces that risk. I map old URLs to their new pages with permanent redirects before launch.', 'Una migración planificada reduce ese riesgo. Mapeo las URLs antiguas a sus nuevas páginas con redirecciones permanentes antes del lanzamiento.')),
        (t('Can my website be in English and Spanish?', '¿Mi sitio puede estar en inglés y español?'), t("Yes. I'm a native Spanish speaker and build bilingual sites with localized pages, navigation and buttons.", 'Sí. Hablo español como lengua materna y construyo sitios bilingües con páginas, navegación y botones localizados.')),
        (t('Will I own the website?', '¿El sitio será mío?'), t('Yes. Hosting and domains stay in your name, and at delivery the Webflow project is transferred to your account.', 'Sí. El hosting y los dominios quedan a tu nombre, y en la entrega el proyecto de Webflow se transfiere a tu cuenta.')),
    ]
    faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q} <span class="pm" aria-hidden="true">+</span></summary><p>{a}</p></details>' for i, (q, a) in enumerate(faq))
    steps = [
        (t('Discovery call', 'Llamada inicial'), t('We talk about your goals, audience, current website and what the new site needs to do.', 'Hablamos de tus objetivos, tu audiencia, tu sitio actual y lo que debe lograr el nuevo.')),
        (t('2 or 3 homepage drafts', '2 o 3 propuestas de home'), t('You send your brand, copy and assets. I explore directions, you pick one, and we refine it.', 'Me envías tu marca, textos y recursos. Exploro direcciones, eliges una y la refinamos.')),
        (t('Build in Webflow', 'Desarrollo en Webflow'), t('Static pages, then CMS pages, each stage with up to 2 consolidated revision rounds.', 'Páginas estáticas y luego CMS, cada etapa con hasta 2 rondas de revisión consolidadas.')),
        (t('Launch + handover', 'Lanzamiento y entrega'), t("Final checks, launch, and the Webflow project transferred to your account. It's yours.", 'Revisión final, lanzamiento y el proyecto de Webflow transferido a tu cuenta. Es tuyo.')),
    ]
    steps_html = ''.join(f'<li class="reveal" style="padding: 28px 28px 0 0; display: flex; flex-direction: column; gap: 14px"><p class="num" style="margin: 0">0{i+1}</p><h3 class="h4">{a}</h3><p class="txt" style="font-size: 15px">{b}</p></li>' for i, (a, b) in enumerate(steps))
    packages = [
        ('01', t('The first spark', 'La primera chispa'), '$200', t('1 landing page for one clear offer or campaign.', '1 landing para una oferta o campaña clara.'), False),
        ('02', t('A new chapter', 'Un nuevo capítulo'), '$600', t('8 to 10 pages and 1 or 2 CMS collections.', '8 a 10 páginas y 1 o 2 colecciones CMS.'), False),
        ('03', t('The full story', 'La historia completa'), '$1,000', t('10 to 16 pages and 3 to 5 CMS collections.', '10 a 16 páginas y 3 a 5 colecciones CMS.'), True),
        ('04', t('A bigger universe', 'Un universo más grande'), '$1,500', t('17 to 25 pages and 6 to 8 CMS collections.', '17 a 25 páginas y 6 a 8 colecciones CMS.'), False),
    ]
    pk = ''.join(f'''<a class="pricecard" href="{u('/pricing/')}" style="{'background: #7136d0;' if hi else ''}{'' if i == 3 else 'border-right: 1.5px solid #f5f2ec;'}"><p style="margin: 0; font-size: 13px; letter-spacing: .1em; text-transform: uppercase; color: {'#ece4fb' if hi else '#b994f5'}">{n} · {name}</p><p style="margin: 0; font: 700 52px/1 'Space Grotesk', sans-serif; letter-spacing: -0.04em">{price}</p><p style="margin: 0; font-size: 15px; line-height: 1.5; color: {'#ece4fb' if hi else '#d4cbdc'}">{d}</p></a>''' for i, (n, name, price, d, hi) in enumerate(packages))

    body = f'''
<section class="sec">
<div class="hero" style="max-width: 1360px; margin: 0 auto">
<div class="hero-copy">
<svg class="spin hide-m" width="120" height="120" viewBox="0 0 120 120" aria-hidden="true" style="position: absolute; right: 40px; top: 48px"><defs><path id="circ" d="M60 60m-46 0a46 46 0 1 1 92 0a46 46 0 1 1-92 0"></path></defs><text font-family="Space Grotesk" font-size="11.5" letter-spacing="3.2" fill="#7136d0"><textPath href="#circ">{t('AVAILABLE FOR NEW PROJECTS · EN / ES · ', 'DISPONIBLE PARA PROYECTOS · ES / EN · ')}</textPath></text></svg>
<span class="hide-m" style="position: absolute; right: 87px; top: 95px">{star(26)}</span>
<p class="eyebrow up d1" style="margin: 0; display: flex; align-items: center; gap: 12px"><span class="dot"></span>{t('Laura Ortega · Webflow designer + developer', 'Laura Ortega · Diseñadora y desarrolladora Webflow')}</p>
<h1 class="h1 up d2" style="font-size: 88px; max-width: 720px">{t('Webflow websites that turn visitors into', 'Sitios en Webflow que convierten visitas en')} <span class="pu" style="position: relative; white-space: nowrap">{t('clients', 'clientes')}<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; bottom: -10px; width: 100%; height: 18px"><path class="draw" d="M4 14 C 80 2, 200 2, 296 10" fill="none" stroke="#b994f5" stroke-width="6" stroke-linecap="round"></path></svg></span>.</h1>
<p class="lead up d3">{t('I design and build fast, SEO-ready Webflow sites for brands, founders and agencies. One person from first sketch to launch, in English or Spanish.', 'Diseño y desarrollo sitios en Webflow rápidos y listos para SEO para marcas, emprendedores y agencias. Una sola persona del primer boceto al lanzamiento, en español o inglés.')}</p>
<div class="row up d4"><a class="btn btn-p" href="{u('/contact/')}">{t('Start a project', 'Empezar un proyecto')} {ARR}</a><a class="btn btn-g" href="{u('/work/')}">{t('See my work', 'Ver proyectos')}</a></div>
<ul class="up d5" style="margin: 6px 0 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; gap: 10px 28px; font-size: 15px; color: #4a3f55">
<li class="chip"><span class="pu">{CHECK}</span>{t('Webflow Partner', 'Webflow Partner')}</li>
<li class="chip"><span class="pu">{CHECK}</span>{t('Design + dev, no handoffs', 'Diseño + desarrollo, sin intermediarios')}</li>
<li class="chip"><span class="pu">{CHECK}</span>{t('English + Spanish', 'Español + inglés')}</li>
</ul>
</div>
<div style="position: relative; display: flex; flex-direction: column">
<img src="/assets/laura-portrait.webp" alt="{t('Laura Ortega, Webflow designer and developer', 'Laura Ortega, diseñadora y desarrolladora Webflow')}" width="900" height="900" style="width: 100%; flex: 1; min-height: 520px; object-fit: cover; display: block">
<div class="float hide-m" style="position: absolute; left: -44px; top: 64px; background: #fff; border: 1.5px solid #251b33; padding: 14px 18px; display: flex; align-items: center; gap: 12px; box-shadow: 6px 6px 0 #251b33">
<svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" fill="#7136d0"></rect><path d="M8 15.5l4.5 4.5L22 10.5" fill="none" stroke="#fff" stroke-width="2.6"></path></svg>
<div><p style="margin: 0; font: 600 14px/1.2 'Space Grotesk', sans-serif">{t('Site published', 'Sitio publicado')}</p><p style="margin: 2px 0 0; font-size: 12px; color: #6e6478">{t('yourbrand.com · just now', 'tumarca.com · justo ahora')}</p></div>
</div>
<div class="float hide-m" style="position: absolute; right: 28px; bottom: 120px; background: #251b33; color: #f5f2ec; padding: 12px 16px; font: 500 13px/1 'Space Grotesk', monospace; animation-delay: -2.4s">&lt;/&gt; build.webflow<span class="caret" style="color: #b994f5">_</span></div>
<div class="dark" style="padding: 22px 28px; display: flex; justify-content: space-between; align-items: center; gap: 16px">
<p style="margin: 0; font-size: 15px; line-height: 1.4">{t('Built the 3 sites that earned an agency<br><strong style="font-weight: 600">Webflow Certified Partner</strong> status.', 'Construí los 3 sitios con los que una agencia<br>obtuvo el estatus de <strong style="font-weight: 600">Webflow Certified Partner</strong>.')}</p>
<p style="margin: 0; font: 700 40px/1 'Space Grotesk', sans-serif; color: #b994f5">3/3</p>
</div>
</div>
</div>
</section>

<section class="sec purple" aria-label="{t('Industries I work with', 'Industrias con las que trabajo')}" style="overflow: hidden">
<div class="marq" style="padding: 22px 0; font: 500 20px/1 'Space Grotesk', sans-serif">
<span style="display: flex; gap: 40px; align-items: center; padding-right: 40px; white-space: nowrap">{marquee}</span><span aria-hidden="true" style="display: flex; gap: 40px; align-items: center; padding-right: 40px; white-space: nowrap">{marquee}</span>
</div>
</section>

<section class="sec" id="services"><div class="wrap pad">
<div class="row" style="justify-content: space-between; align-items: end; gap: 24px; margin-bottom: 56px">
<div style="max-width: 760px"><p class="eyebrow">{t('Services', 'Servicios')}</p><h2 class="h2" style="font-size: 60px">{t('Pick what you need. I handle the rest.', 'Elige lo que necesitas. Yo me encargo del resto.')}</h2></div>
<p class="txt" style="max-width: 360px; font-size: 17px">{t("Clear scope, clear starting prices, one point of contact. Not sure which one fits? Ask me.", 'Alcance claro, precios de partida claros y una sola persona de contacto. ¿No sabes cuál encaja? Pregúntame.')}</p>
</div>
<div class="g4 box reveal">
{service_card('01', ICON_NEW, t('New Webflow website', 'Sitio nuevo en Webflow'), t('Custom design and development from zero: structure, responsive build, interactions and SEO setup.', 'Diseño y desarrollo a medida desde cero: estructura, desarrollo responsive, interacciones y SEO.'), [t('2 or 3 homepage drafts', '2 o 3 propuestas de home'), t('CMS you can edit', 'CMS que puedes editar'), t('On-page SEO', 'SEO on-page')], t('Websites from', 'Sitios desde'), 'USD 600', href='/services/webflow-development/')}
{service_card('02', ICON_MIG, t('Redesign + migration', 'Rediseño + migración'), t('Move from WordPress, Wix or a static site to Webflow with a planned, careful move.', 'Pasa de WordPress, Wix o un sitio estático a Webflow con una migración planificada y cuidadosa.'), [t('Content + URL inventory', 'Inventario de contenido y URLs'), t('Redirect planning', 'Plan de redirecciones'), t('Post-migration checks', 'Revisión post-migración')], t('Priced by', 'Se cotiza según'), t('Content + scope', 'Contenido + alcance'), href='/services/seo-migrations/')}
{service_card('03', ICON_CODE, t('Figma to Webflow', 'Figma a Webflow'), t('You have the design, I build it carefully. White-label development for agencies and designers.', 'Tú tienes el diseño, yo lo construyo con cuidado. Desarrollo white-label para agencias y diseñadores.'), [t('Responsive adaptation', 'Adaptación responsive'), t('Reusable components', 'Componentes reutilizables'), t('Interactions suited to your content', 'Interacciones acordes a tu contenido')], t('Landing pages from', 'Landings desde'), 'USD 200', href='/services/webflow-development/figma-to-webflow/')}
{service_card('04', ICON_CARE, t('Website care', 'Mantenimiento web'), t('Quarterly maintenance for Webflow and WordPress: content updates, CMS entries and fresh AI images every month.', 'Mantenimiento trimestral para Webflow y WordPress: actualizaciones, entradas CMS e imágenes con IA cada mes.'), [t('Updates to supplied content', 'Actualización del contenido que envías'), t('1 to 7 AI images per month', '1 a 7 imágenes IA al mes'), t('New CMS entries added', 'Nuevas entradas en el CMS')], t('3 months cost', '3 meses cuestan'), t('= your site price', '= el precio de tu sitio'), dark=True, href='/services/maintenance/')}
</div>
<p class="txt" style="margin-top: 24px; font-size: 15px"><strong style="color: #251b33">{t('Add-ons:', 'Extras:')}</strong> {t('English + Spanish localization · Localization plugin setup USD 100 + USD 50/month · WordPress + Oxygen builds', 'Localización español + inglés · Instalación de plugin de localización USD 100 + USD 50/mes · Desarrollo en WordPress + Oxygen')} · <a class="pu" href="{u('/services/')}">{t('All services →', 'Todos los servicios →')}</a></p>
</div></section>

<section class="sec dark"><div class="wrap pad">
<div class="row" style="justify-content: space-between; align-items: end; gap: 24px; margin-bottom: 48px">
<div><p class="eyebrow pu">{t('Pricing', 'Precios')}</p><h2 class="h2" style="font-size: 60px">{t('Big ideas. Clear starting points.', 'Grandes ideas. Puntos de partida claros.')}</h2></div>
<a class="btn btn-w" href="{u('/pricing/')}">{t('See full pricing', 'Ver todos los precios')} {ARR}</a>
</div>
<div class="g4 reveal" style="border: 1.5px solid #f5f2ec">{pk}</div>
<p style="margin: 20px 0 0; font-size: 14px; color: #b3a8bd">{t('Starting prices in USD. Every package includes responsive development, up to 10 AI-generated images and up to 2 revision rounds per stage.', 'Precios de partida en USD. Todos los paquetes incluyen desarrollo responsive, hasta 10 imágenes con IA y hasta 2 rondas de revisión por etapa.')}</p>
</div></section>

<section class="sec"><div class="g3" style="max-width: 1360px; margin: 0 auto">
<div class="cell br" style="padding: 80px 48px 80px 40px; gap: 20px">
<p class="eyebrow" style="margin: 0">{t('For brands + founders', 'Para marcas y emprendedores')}</p>
<h2 class="h3" style="font-size: 34px">{t('A site that explains what you do in 5 seconds and brings you leads.', 'Un sitio que explica lo que haces en 5 segundos y te trae clientes.')}</h2>
<p class="txt" style="font-size: 17px">{t('You talk directly with the person designing and building it. No account managers, no lost messages.', 'Hablas directamente con la persona que lo diseña y lo construye. Sin intermediarios ni mensajes perdidos.')}</p>
<a href="{u('/contact/')}" style="font-weight: 500; margin-top: auto">{t('Start a project →', 'Empezar un proyecto →')}</a>
</div>
<div class="br hide-m"><img src="/assets/hands.webp" alt="{t('Hands sketching website wireframes next to a laptop and phone', 'Manos dibujando wireframes junto a una laptop y un teléfono')}" loading="lazy" style="width: 100%; height: 100%; min-height: 460px; object-fit: cover; display: block"></div>
<div class="cell lilac" style="padding: 80px 40px 80px 48px; gap: 20px">
<p class="eyebrow" style="margin: 0; color: #5a26ad">{t('For agencies', 'Para agencias')}</p>
<h2 class="h3" style="font-size: 34px">{t('Your white-label Webflow developer, minus the overhead.', 'Tu desarrolladora Webflow white-label, sin costos fijos.')}</h2>
<p class="txt" style="font-size: 17px; color: #3d3347">{t('I lead the website department at a digital agency. I can take your Figma files, CMS builds and QA off your plate.', 'Lidero el departamento web de una agencia digital. Puedo encargarme de tus archivos de Figma, builds de CMS y QA.')}</p>
<a href="mailto:me@pancratzia.com?subject=Agency%20collaboration" style="font-weight: 500; margin-top: auto">{t('Talk partnership →', 'Hablemos de colaboración →')}</a>
</div>
</div></section>

<section class="sec" id="work"><div class="wrap pad">
<div class="row" style="justify-content: space-between; align-items: end; gap: 24px; margin-bottom: 56px">
<div><p class="eyebrow">{t('Selected work', 'Proyectos seleccionados')}</p><h2 class="h2" style="font-size: 60px">{t('Real sites. Real businesses.', 'Sitios reales. Negocios reales.')}</h2></div>
<a class="btn btn-g" href="{u('/work/')}">{t('All projects', 'Todos los proyectos')} {ARR}</a>
</div>
{work_cards()}
</div></section>

<section class="sec dark" style="position: relative; overflow: hidden">
<svg class="spin hide-m" width="220" height="220" viewBox="0 0 24 24" aria-hidden="true" style="position: absolute; right: 6%; top: 50%; margin-top: -110px; opacity: .14; animation-duration: 40s"><path fill="#b994f5" d="M12 0l3 9 9 3-9 3-3 9-3-9-9-3 9-3Z"></path></svg>
<figure class="reveal" style="max-width: 1100px; margin: 0 auto; padding: 96px 40px; display: flex; flex-direction: column; gap: 28px; position: relative">
<p style="margin: 0; font: 700 64px/0.6 'Space Grotesk', sans-serif; color: #b994f5" aria-hidden="true">“</p>
<blockquote style="margin: 0; font: 500 38px/1.25 'Space Grotesk', sans-serif; letter-spacing: -0.02em">{t("I'm so happy with the results we achieved together. We went from zero visits and not showing up in any search to <span class=\"q\">ranking in first place</span>, thanks to Laura's SEO work and analysis.", 'Estoy muy feliz con los resultados que logramos juntos. Pasamos de tener cero visitas y no aparecer en ninguna búsqueda a <span style="color: #b994f5">posicionarnos en primer lugar</span>, gracias al trabajo y análisis SEO de Laura.')}</blockquote>
<figcaption style="display: flex; align-items: center; gap: 16px"><span aria-hidden="true" style="width: 52px; height: 52px; background: #7136d0; display: flex; align-items: center; justify-content: center; font: 700 20px/1 'Space Grotesk', sans-serif">SJ</span><span><span style="display: block; font: 600 17px/1.2 'Space Grotesk', sans-serif">Sergio Jiménez</span><span style="display: block; margin-top: 4px; font-size: 14px; color: #b3a8bd">Prosatcomm · Venezuela</span></span></figcaption>
</figure>
</section>

<section class="sec"><div class="wrap pad">
<p class="eyebrow">{t('Process', 'Proceso')}</p>
<h2 class="h2" style="font-size: 60px; margin-bottom: 56px">{t('From idea to launch in 4 steps.', 'De la idea al lanzamiento en 4 pasos.')}</h2>
<svg class="hide-m" viewBox="0 0 1280 24" preserveAspectRatio="none" aria-hidden="true" style="width: 100%; height: 24px; display: block"><path class="draw" d="M0 12H1280" stroke="#7136d0" stroke-width="2"></path><rect x="0" y="4" width="16" height="16" fill="#7136d0"></rect><rect x="320" y="4" width="16" height="16" fill="#7136d0"></rect><rect x="640" y="4" width="16" height="16" fill="#7136d0"></rect><rect x="960" y="4" width="16" height="16" fill="#7136d0"></rect></svg>
<ol class="g4" style="margin: 0; padding: 0; list-style: none">{steps_html}</ol>
<a class="btn btn-g" href="{u('/process/')}" style="margin-top: 48px">{t('The full process', 'El proceso completo')} {ARR}</a>
</div></section>

<section class="sec"><div class="g2" style="max-width: 1360px; margin: 0 auto">
<div class="br" style="position: relative"><img src="/assets/office.webp" alt="{t("Laura's workspace with a website on screen and a poodle asleep nearby", 'El espacio de trabajo de Laura con un sitio web en pantalla y una poodle dormida cerca')}" loading="lazy" style="width: 100%; height: 100%; min-height: 520px; object-fit: cover; display: block"><p style="position: absolute; left: 24px; bottom: 24px; margin: 0; background: #f5f2ec; border: 1.5px solid #251b33; padding: 10px 14px; font-size: 13px">{t('Office manager: a very sleepy poodle', 'Gerente de oficina: una poodle muy dormilona')}</p></div>
<div class="cell" style="padding: 96px 40px 96px 56px; gap: 20px; justify-content: center">
<p class="eyebrow" style="margin: 0">{t('About', 'Sobre mí')}</p>
<h2 class="h2">{t("Hi, I'm Laura. Engineer brain, designer eye.", 'Hola, soy Laura. Mente de ingeniera, ojo de diseñadora.')}</h2>
<p class="txt" style="font-size: 17px">{t("I'm a telematics engineer turned Webflow designer and developer. I lead the website department of a digital marketing agency, working side by side with SEO teams on law firm, clinic and contractor sites.", 'Soy ingeniera en telemática convertida en diseñadora y desarrolladora Webflow. Lidero el departamento web de una agencia de marketing digital, trabajando junto al equipo SEO en sitios de firmas legales, clínicas y contratistas.')}</p>
<p class="txt" style="font-size: 17px">{t('I work remotely from Venezuela with clients in the US and Latin America, in English and Spanish. Usually with a few poodles nearby.', 'Trabajo de forma remota desde Venezuela con clientes en EE. UU. y Latinoamérica, en español e inglés. Normalmente con unas cuantas poodles cerca.')}</p>
<div class="row" style="margin-top: 8px"><a class="btn btn-g" href="{u('/about/')}">{t('Meet your developer', 'Conoce a tu desarrolladora')} {ARR}</a><a class="btn btn-g" href="https://webflow.com/@pancratzia">Webflow ↗</a></div>
</div>
</div></section>

<section class="sec"><div class="wrap pad g2" style="gap: 56px">
<div><p class="eyebrow">FAQ</p><h2 class="h2" style="font-size: 60px">{t('Before you ask.', 'Antes de que preguntes.')}</h2><a class="btn btn-g" href="{u('/faq/')}" style="margin-top: 32px">{t('More answers', 'Más respuestas')} {ARR}</a></div>
<div style="border-top: 1.5px solid #251b33">{faq_html}</div>
</div></section>
'''
    write_page('/', t('Webflow Designer & Developer — Laura Ortega | Pancratzia', 'Diseño y desarrollo Webflow — Laura Ortega | Pancratzia'),
               t('Laura Ortega designs and builds Webflow websites for brands, founders and agencies, in English and Spanish. Landing pages from USD 200, websites from USD 600.', 'Laura Ortega diseña y desarrolla sitios en Webflow para marcas, emprendedores y agencias, en español e inglés. Landings desde USD 200, sitios desde USD 600.'),
               body, active=None)
