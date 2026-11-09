from core import t, u, write_page, star, ARR
from pages_home import PROJECTS, work_cards


def hero(eyebrow, h1, lead, extra=''):
    return f'''<section class="sec"><div class="wrap pad g2" style="gap: 56px; align-items: end; padding-bottom: 72px">
<div><p class="eyebrow up d1">{eyebrow}</p><h1 class="h1 up d2">{h1}</h1></div>
<div class="up d3" style="display: flex; flex-direction: column; gap: 24px"><p class="lead">{lead}</p>{extra}</div>
</div></section>'''


def payments():
    items = [('PayPal', t('Project payments through PayPal.', 'Pagos del proyecto por PayPal.')),
             ('AirTM', t('AirTM-to-AirTM transfers or my AirTM virtual US account.', 'Transferencias AirTM a AirTM o mi cuenta virtual de EE. UU. en AirTM.')),
             ('Binance International', t('Binance International only, not Binance.US.', 'Solo Binance International, no Binance.US.')),
             ('USDT', t('To my wallet. Network and details confirmed before transfer.', 'A mi wallet. Red y datos se confirman antes de transferir.'))]
    cells = ''.join(f'<div class="cell{" br" if i < 3 else ""}"><p class="num" style="font-size: 18px; margin: 0">0{i+1}</p><h3 class="h4">{n}</h3><p class="txt" style="font-size: 15px">{d}</p></div>' for i, (n, d) in enumerate(items))
    return f'''<section class="sec"><div class="wrap pad" style="padding-top: 80px">
<p class="eyebrow">{t('Payment methods', 'Métodos de pago')}</p>
<h2 class="h2" style="margin-bottom: 48px">{t('Ways to pay for your project.', 'Formas de pagar tu proyecto.')}</h2>
<div class="g4 box reveal">{cells}</div>
<p class="sm" style="margin-top: 16px">{t('Payment details are shared directly when we agree on your project.', 'Los datos de pago se comparten directamente cuando acordamos el proyecto.')}</p>
</div></section>'''


def maint_table():
    k, m = t('1,000', '1.000'), t('1,500', '1.500')
    rows = [('200', '200', '1'), ('600', '600', '3'), (k, k, '5'), (m, m, '7')]
    trs = ''.join(f'<tr><td>USD {a}</td><td><strong>USD {b}</strong></td><td>{c}</td></tr>' for a, b, c in rows)
    return f'<table class="t box"><thead><tr><th>{t("Website package", "Paquete web")}</th><th>{t("3 months of care", "3 meses de mantenimiento")}</th><th>{t("AI images / month", "Imágenes IA / mes")}</th></tr></thead><tbody>{trs}</tbody></table>'


def loc_box():
    return f'''<div class="dark" style="padding: 32px; border: 1.5px solid #251b33">
<p class="eyebrow pu">{t('Localization / add-on', 'Localización / extra')}</p>
<h3 class="h3">{t('Localization plugin setup &amp; care', 'Instalación y mantenimiento del plugin de localización')}</h3>
<div class="g2" style="gap: 24px; margin: 24px 0"><div><p style="margin: 0; font: 700 44px/1 'Space Grotesk'">USD 100</p><p class="txt" style="margin-top: 6px; font-size: 14px">{t('one-time installation', 'instalación única')}</p></div><div><p style="margin: 0; font: 700 44px/1 'Space Grotesk'">USD 50</p><p class="txt" style="margin-top: 6px; font-size: 14px">{t('per month for maintenance', 'al mes de mantenimiento')}</p></div></div>
<p class="txt" style="font-size: 14px">{t('You pay the plugin subscription or license directly. Plugin fees are not included. We confirm the plugin and platform before setup.', 'Tú pagas directamente la suscripción o licencia del plugin; no está incluida. Confirmamos plugin y plataforma antes de instalar.')}</p>
</div>'''


def work():
    body = hero(t('Selected work / 04', 'Proyectos seleccionados / 04'), t("Websites I've built. <span class=\"pu\">Different kinds of magic.</span>", 'Sitios que he construido. <span class="pu">Distintos tipos de magia.</span>'),
                t('Law firms, healthcare and community directories. Each one designed and built with care, structure and on-page SEO.', 'Firmas legales, salud y directorios comunitarios. Cada uno diseñado y construido con cuidado, estructura y SEO on-page.'))
    body += f'''<section class="sec"><div class="wrap pad" style="padding-top: 72px">{work_cards()}
<div class="row" style="justify-content: center; margin-top: 72px"><a class="btn btn-g" href="https://webflow.com/@pancratzia">{t('More on my Webflow portfolio', 'Más en mi portafolio de Webflow')} ↗</a></div></div></section>'''
    write_page('/work/', t('Web Design & Development Portfolio | Pancratzia', 'Portafolio de diseño y desarrollo web | Pancratzia'),
               t("Explore Laura Ortega's Webflow and WordPress portfolio: Joumana Kayrouz, Mungo Law, Hire Warriors and Her Vitality Clinic.", 'Explora el portafolio Webflow y WordPress de Laura Ortega: Joumana Kayrouz, Mungo Law, Hire Warriors y Her Vitality Clinic.'), body, active='/work/')


CASES = {
    'joumana-kayrouz': dict(tags=['Webflow', 'Redesign|Rediseño', 'SEO'], live='https://www.yourrights.com', role=('Design + Webflow development', 'Diseño + desarrollo Webflow'),
        over=('A complete rebuild of an outdated website into a responsive Webflow experience. Clear practice areas, reusable components and on-page SEO give the firm a stronger, maintainable foundation.', 'Reconstrucción completa de un sitio desactualizado en una experiencia Webflow responsive. Áreas de práctica claras, componentes reutilizables y SEO on-page le dan a la firma una base más sólida y fácil de mantener.'),
        start=('An outdated site needed a full rethink, with a structure the team could continue to extend.', 'Un sitio desactualizado necesitaba replantearse por completo, con una estructura que el equipo pudiera seguir ampliando.'),
        appr=('I designed and built the new experience in Webflow, rebuilding the page structure around practice areas, results, FAQs and contact. Responsive layouts and a reusable component system support ongoing updates.', 'Diseñé y construí la nueva experiencia en Webflow, reorganizando la estructura alrededor de áreas de práctica, resultados, preguntas frecuentes y contacto. Layouts responsive y un sistema de componentes reutilizables facilitan las actualizaciones.')),
    'mungo-law': dict(tags=['Webflow', 'Multi-page|Multipágina', 'SEO'], live='https://www.mungolawpc.com', role=('Webflow development + SEO structure', 'Desarrollo Webflow + estructura SEO'),
        over=('A single landing page became a full Webflow website, connecting practice areas, resources, guides, FAQs and contact with a consistent visual language and SEO-minded structure.', 'Una sola landing se convirtió en un sitio Webflow completo, conectando áreas de práctica, recursos, guías, preguntas frecuentes y contacto con un lenguaje visual coherente y una estructura pensada para SEO.'),
        start=('A single page limited how the firm could explain its services and help visitors find relevant information.', 'Una sola página limitaba cómo la firma podía explicar sus servicios y ayudar a los visitantes a encontrar información relevante.'),
        appr=('I expanded the site into interconnected pages for practice areas, results, about, resources, guides, blog, FAQs and contact. The build includes responsive layouts and on-page SEO.', 'Amplié el sitio con páginas conectadas para áreas de práctica, resultados, nosotros, recursos, guías, blog, preguntas frecuentes y contacto, con layouts responsive y SEO on-page.')),
    'hire-warriors': dict(tags=['Webflow CMS', 'Directory|Directorio', 'Jetboost'], live='https://www.hirewarriors.com', role=('Webflow CMS development', 'Desarrollo Webflow CMS'),
        over=('A national veteran-owned business directory built in Webflow for Honorable Marketing. Structured CMS content, Jetboost search and filtering, and owner listing flows bring a complex directory together.', 'Un directorio nacional de negocios de veteranos construido en Webflow para Honorable Marketing. Contenido CMS estructurado, búsqueda y filtros con Jetboost y flujos de publicación para dueños unen un directorio complejo.'),
        start=('A national directory needed organized listings and practical ways for visitors to find businesses by category and location.', 'Un directorio nacional necesitaba fichas organizadas y formas prácticas de encontrar negocios por categoría y ubicación.'),
        appr=('I built the Webflow CMS structure, live search and location filters with Jetboost, the owner listing flow and Enhanced Profiles. Structured data supports discovery, while the team can manage listings without a developer.', 'Construí la estructura CMS, la búsqueda en vivo y los filtros por ubicación con Jetboost, el flujo para publicar negocios y los perfiles mejorados. Los datos estructurados ayudan a descubrir negocios y el equipo gestiona las fichas sin un desarrollador.')),
    'her-vitality-clinic': dict(tags=['WordPress', 'Healthcare|Salud', 'Web design|Diseño web'], live='https://hervitality.clinic', role=('Web design + WordPress development', 'Diseño web + desarrollo WordPress'),
        over=("A women's health and longevity clinic website, with an editorial visual direction and clear paths to services, memberships and consultations.", 'El sitio de una clínica de salud y longevidad femenina, con una dirección visual editorial y caminos claros hacia servicios, membresías y consultas.'),
        start=('Present a broad range of services with a calm, approachable visual identity.', 'Presentar una amplia gama de servicios con una identidad visual serena y cercana.'),
        appr=('A project that brings together service discovery, editorial imagery and consultation pathways. Explore the live site to see the complete experience.', 'Un proyecto que une descubrimiento de servicios, imágenes editoriales y rutas de consulta. Visita el sitio en vivo para ver la experiencia completa.')),
}


def cases():
    for i, (slug, name, img, meta, sub) in enumerate(PROJECTS):
        c = CASES[slug]
        nslug, nname = PROJECTS[(i + 1) % 4][0], PROJECTS[(i + 1) % 4][1]
        tags = ''.join(f'<span class="tag">{t(*x.split("|")) if "|" in x else x}</span>' for x in c['tags'])
        body = f'''<section class="sec"><div class="wrap pad" style="padding-bottom: 56px">
<p class="crumb"><a href="{u('/work/')}">{t('Work', 'Proyectos')}</a> / {name}</p>
<div class="row up d1" style="gap: 8px; margin-bottom: 24px">{tags}</div>
<h1 class="h1 up d2">{name}</h1>
<p class="lead up d3" style="margin-top: 24px; font-size: 24px">{t(*sub)}</p>
</div></section>
<section class="sec"><div class="wrap" style="padding-top: 56px; padding-bottom: 56px"><div class="shot up d4" style="aspect-ratio: 4 / 3; max-width: 1100px; margin: 0 auto; box-shadow: 12px 12px 0 #251b33"><img src="{img}" alt="{t(name + ' website shown in a browser', 'Sitio web de ' + name + ' en un navegador')}" width="1000" height="750"></div></div></section>
<section class="sec"><div class="wrap pad g3" style="gap: 48px">
<div class="reveal" style="display: flex; flex-direction: column; gap: 16px"><p class="eyebrow" style="margin: 0">{t('Overview', 'Resumen')}</p><p class="txt" style="font-size: 18px">{t(*c['over'])}</p><div class="box" style="padding: 20px; margin-top: 8px"><p class="sm" style="margin: 0">{t('Role', 'Rol')}</p><p style="margin: 4px 0 0; font: 600 18px 'Space Grotesk'">{t(*c['role'])}</p></div></div>
<div class="reveal" style="display: flex; flex-direction: column; gap: 16px"><p class="num" style="margin: 0">01</p><h2 class="h3">{t('The starting point', 'El punto de partida')}</h2><p class="txt">{t(*c['start'])}</p></div>
<div class="reveal" style="display: flex; flex-direction: column; gap: 16px"><p class="num" style="margin: 0">02</p><h2 class="h3">{t('My approach', 'Mi enfoque')}</h2><p class="txt">{t(*c['appr'])}</p></div>
</div></section>
<section class="sec dark"><div class="wrap row" style="justify-content: space-between; padding-top: 56px; padding-bottom: 56px; gap: 24px">
<a class="btn btn-w" href="{c['live']}">{t('Visit live website', 'Ver sitio en vivo')} ↗</a>
<a href="{u('/work/' + nslug + '/')}" style="color: #f5f2ec; text-decoration: none; text-align: right"><span class="sm" style="color: #b3a8bd">{t('Next project', 'Siguiente proyecto')}</span><br><span class="h3" style="font-size: 36px">{nname} →</span></a>
</div></section>'''
        write_page('/work/' + slug + '/', t(f'{name} Website Project | Pancratzia', f'Proyecto web {name} | Pancratzia'), t(*sub) + ' ' + t("Explore Laura Ortega's role, approach and the live website.", 'Conoce el rol de Laura Ortega, su enfoque y el sitio en vivo.'), body, active='/work/', image=img)


SERVICES = [
    ('web-design', ('Web design', 'Diseño web'), ('A clear visual direction before development.', 'Una dirección visual clara antes del desarrollo.'), [], '<rect x="3" y="8" width="46" height="34"></rect><path d="M3 16h46M10 24h18M10 30h12"></path><rect x="32" y="22" width="11" height="13" fill="#ddd0ef"></rect>'),
    ('webflow-development', ('Webflow development', 'Desarrollo Webflow'), ('Custom builds, landing pages and approved designs brought to life.', 'Desarrollos a medida, landings y diseños aprobados hechos realidad.'), [('figma-to-webflow', ('Figma to Webflow', 'Figma a Webflow')), ('landing-pages', ('Landing pages', 'Landing pages'))], '<path d="M17 16L7 26l10 10M35 16l10 10-10 10M30 10L22 42"></path>'),
    ('webflow-cms', ('CMS &amp; dynamic content', 'CMS y contenido dinámico'), ('Content structures, templates and directories your team can manage.', 'Estructuras de contenido, plantillas y directorios que tu equipo puede gestionar.'), [('directories', ('CMS directories', 'Directorios CMS'))], '<rect x="6" y="6" width="18" height="18"></rect><rect x="28" y="6" width="18" height="18" fill="#ddd0ef"></rect><rect x="6" y="28" width="18" height="18" fill="#ddd0ef"></rect><rect x="28" y="28" width="18" height="18"></rect>'),
    ('localization', ('English + Spanish', 'Español + inglés'), ('A complete experience for both audiences.', 'Una experiencia completa para ambas audiencias.'), [], '<rect x="3" y="8" width="26" height="20"></rect><rect x="23" y="24" width="26" height="20" fill="#ddd0ef"></rect><path d="M9 22l5-10 5 10M11 19h6M30 30h12M36 30v8"></path>'),
    ('seo-migrations', ('SEO &amp; migrations', 'SEO y migraciones'), ('Plan content, URLs and the move to your next platform.', 'Planifica contenido, URLs y la mudanza a tu próxima plataforma.'), [('wordpress-to-webflow', ('WordPress to Webflow', 'WordPress a Webflow'))], '<rect x="3" y="12" width="18" height="24"></rect><rect x="31" y="12" width="18" height="24" fill="#ddd0ef"></rect><path d="M22 24h8M26 20l4 4-4 4"></path>'),
    ('website-rebuilds', ('Website rebuilds', 'Reconstrucción de sitios'), ('Give your current website a better structure and implementation.', 'Dale a tu sitio actual una mejor estructura e implementación.'), [], '<path d="M10 26a16 16 0 0 1 28-10.5M42 26a16 16 0 0 1-28 10.5"></path><path d="M38 8v8h-8M14 44v-8h8"></path>'),
    ('wordpress-oxygen', ('WordPress + Oxygen', 'WordPress + Oxygen'), ('A flexible WordPress build when it fits your project.', 'Un desarrollo flexible en WordPress cuando encaja con tu proyecto.'), [], '<circle cx="26" cy="26" r="20"></circle><path d="M12 18l8 22 6-16 6 16 8-22"></path>'),
    ('maintenance', ('Website care', 'Mantenimiento web'), ('Keep your content, images and pages up to date.', 'Mantén al día tu contenido, imágenes y páginas.'), [('webflow', ('Webflow maintenance', 'Mantenimiento Webflow'))], '<path d="M26 4l18 7v12c0 12-8 20-18 25C16 43 8 35 8 23V11Z" fill="#ddd0ef"></path><path d="M17 26l6 6 12-12"></path>'),
    ('ai-images', ('AI images for websites', 'Imágenes IA para sitios web'), ('Visual assets with a consistent direction for your website.', 'Recursos visuales con una dirección coherente para tu sitio.'), [], '<rect x="4" y="8" width="44" height="36"></rect><path d="M4 36l12-12 10 10 6-6 16 14"></path>'),
]


def services_hub():
    cells = []
    for i, (slug, name, desc, subs, icon) in enumerate(SERVICES):
        cls = 'cell card' + (' br' if i % 3 != 2 else '') + (' bb' if i < 6 else '')
        sub = ' · '.join(t(*n) for _, n in subs)
        cells.append(f'''<a href="{u('/services/' + slug + '/')}" class="{cls}" style="text-decoration: none; color: inherit">
<p class="num" style="font-size: 18px; margin: 0">0{i+1}</p>
<svg width="48" height="48" viewBox="0 0 52 52" fill="none" stroke="#7136d0" stroke-width="2" aria-hidden="true">{icon}</svg>
<h2 class="h3">{t(*name)}</h2><p class="txt">{t(*desc)}</p>{f'<p class="sm" style="margin: 0">{sub}</p>' if sub else ''}<p class="pu" style="margin: auto 0 0; font-weight: 500">{t('Explore service', 'Ver servicio')} ↗</p></a>''')
    body = hero(t('Services / from idea to website', 'Servicios / de la idea al sitio web'), t('What does your next chapter <span class="pu">need?</span>', '¿Qué necesita tu <span class="pu">próximo capítulo?</span>'),
                t('Design, development and ongoing care. Find the area and the specific service that fit your next project.', 'Diseño, desarrollo y cuidado continuo. Encuentra el área y el servicio que encajan con tu próximo proyecto.'),
                f'<div class="row"><a class="btn btn-p" href="{u("/contact/")}">{t("Discuss your project", "Hablemos de tu proyecto")} {ARR}</a><a class="btn btn-g" href="{u("/pricing/")}">{t("See starting prices", "Ver precios de partida")}</a></div>')
    body += f'<section class="sec"><div class="wrap pad" style="padding-top: 72px"><div class="g3 box reveal">{"".join(cells)}</div></div></section>'
    body += f'''<section class="sec lilac"><div class="wrap pad g2" style="gap: 56px; align-items: center">
<div><p class="eyebrow" style="color: #5a26ad">{t('Not sure where to start?', '¿No sabes por dónde empezar?')}</p><h2 class="h2">{t('Tell me what you want to improve.', 'Cuéntame qué quieres mejorar.')}</h2></div>
<div style="display: flex; flex-direction: column; gap: 24px"><p class="lead" style="color: #3d3347">{t('You do not need to choose a tool before we talk. Share your website or idea and we can define the scope together.', 'No necesitas elegir una herramienta antes de hablar. Comparte tu sitio o tu idea y definimos el alcance juntas.')}</p>
<div class="row"><a class="btn btn-p" href="{u('/contact/')}">{t("Let's discuss the project", 'Hablemos del proyecto')} {ARR}</a><a class="btn btn-g" href="{u('/pricing/')}">{t('Packages + prices', 'Paquetes y precios')}</a></div></div>
</div></section>'''
    write_page('/services/', t('Webflow Design & Development Services | Pancratzia', 'Servicios de diseño y desarrollo Webflow | Pancratzia'),
               t('Custom Webflow and WordPress development, CMS, localization, SEO and migrations. Explore services, starting prices and website maintenance.', 'Desarrollo Webflow y WordPress a medida, CMS, localización, SEO y migraciones. Explora servicios, precios de partida y mantenimiento.'), body, active='/services/')


def pricing():
    pk = [
        ('01', t('Landing', 'Landing'), t('The first spark', 'La primera chispa'), '200', t('A focused page for one clear offer or campaign.', 'Una página enfocada en una oferta o campaña clara.'), [t('1 landing page', '1 landing page'), t('No CMS collections', 'Sin colecciones CMS')]),
        ('02', t('Website', 'Sitio web'), t('A new chapter', 'Un nuevo capítulo'), '600', t('A complete presence with room for dynamic content.', 'Una presencia completa con espacio para contenido dinámico.'), [t('8 to 10 static pages', '8 a 10 páginas estáticas'), t('1 or 2 CMS collections', '1 o 2 colecciones CMS')]),
        ('03', t('Website', 'Sitio web'), t('The full story', 'La historia completa'), t('1,000', '1.000'), t('A larger website with a more connected CMS structure.', 'Un sitio más grande con una estructura CMS más conectada.'), [t('10 to 16 static pages', '10 a 16 páginas estáticas'), t('3 to 5 CMS collections', '3 a 5 colecciones CMS')]),
        ('04', t('Website', 'Sitio web'), t('A bigger universe', 'Un universo más grande'), t('1,500', '1.500'), t('An expanded website with a defined scope and clear limits.', 'Un sitio amplio con alcance definido y límites claros.'), [t('17 to 25 static pages', '17 a 25 páginas estáticas'), t('6 to 8 CMS collections', '6 a 8 colecciones CMS')]),
    ]
    common = [t('Responsive development', 'Desarrollo responsive'), t('Up to 2 revision rounds per stage', 'Hasta 2 rondas de revisión por etapa'), t('Up to 10 AI-generated images', 'Hasta 10 imágenes generadas con IA'), t('Up to 3 image revisions', 'Hasta 3 revisiones de imagen')]
    cards = []
    for i, (n, kind, name, price, d, items) in enumerate(pk):
        hi = i == 2
        lis = ''.join(f'<li>{x}</li>' for x in items + common)
        badge = f'<span style="position: absolute; top: -14px; left: 30px; background: #251b33; color: #fff; font-size: 12px; letter-spacing: .1em; text-transform: uppercase; padding: 6px 10px">{t("Most complete", "La más completa")}</span>' if hi else ''
        cards.append(f'''<article class="cell{' purple' if hi else ' card'}{' br' if i < 3 else ''}" style="position: relative">{badge}
<p class="eyebrow" style="margin: 0{'; color: #ddd0ef' if hi else ''}">{n} / {kind}</p><h2 class="h3">{name}</h2>
<p style="margin: 0"><span class="sm"{' style="color: #ddd0ef"' if hi else ''}>{t('From', 'Desde')}</span><br><span class="price">${price}</span> <span class="sm"{' style="color: #ddd0ef"' if hi else ''}>USD</span></p>
<p class="txt"{' style="color: #ece4fb"' if hi else ''}>{d}</p><ul class="list"{' style="color: #fff"' if hi else ''}>{lis}</ul>
<a class="btn {'btn-w' if hi else 'btn-g'}" href="mailto:me@pancratzia.com?subject={name.replace(' ', '%20')}%20(USD%20{price})" style="margin-top: auto; justify-content: center">{t('Ask about this', 'Consultar este paquete')} {ARR}</a></article>''')
    body = hero(t('The investment', 'La inversión'), t('Big ideas. <span class="pu">Clear starting points.</span>', 'Grandes ideas. <span class="pu">Puntos de partida claros.</span>'),
                t('Starting prices in USD. The final quote depends on your content, functionality and project needs.', 'Precios de partida en USD. La cotización final depende de tu contenido, funcionalidades y necesidades del proyecto.'))
    info = [
        (star(40), t('A little visual magic, included', 'Un poco de magia visual, incluida'), t("Every package includes up to 10 AI-generated images and up to 3 image revisions in total. Each revision applies to one image. I don't offer photo editing, though some adjustments can be explored with AI.", 'Cada paquete incluye hasta 10 imágenes con IA y hasta 3 revisiones de imagen en total. Cada revisión aplica a una imagen. No ofrezco edición fotográfica, aunque algunos ajustes pueden explorarse con IA.')),
        ('<svg width="40" height="40" viewBox="0 0 52 52" fill="none" stroke="#7136d0" stroke-width="2.5" aria-hidden="true"><rect x="6" y="6" width="18" height="18"></rect><rect x="28" y="6" width="18" height="18" fill="#ddd0ef"></rect><rect x="6" y="28" width="18" height="18" fill="#ddd0ef"></rect><rect x="28" y="28" width="18" height="18"></rect></svg>', t('What counts as CMS?', '¿Qué cuenta como CMS?'), t('One content collection and its template, like a blog, projects or team members. Individual entries are not static pages. Content entry and migration volume are confirmed in your quote.', 'Una colección de contenido y su plantilla, como blog, proyectos o equipo. Las entradas individuales no son páginas estáticas. La carga de contenido y el volumen de migración se confirman en tu cotización.')),
        ('<svg width="40" height="40" viewBox="0 0 52 52" fill="none" stroke="#7136d0" stroke-width="2.5" aria-hidden="true"><rect x="8" y="14" width="36" height="30"></rect><path d="M18 14V8h16v6M8 24h36"></path></svg>', t('What should you bring?', '¿Qué debes traer?'), t('Your branding direction, copy and assets. Branding is not included. Hosting, platform subscriptions, paid tools and extra language versions are scoped separately.', 'Tu dirección de marca, textos y recursos. El branding no está incluido. Hosting, suscripciones, herramientas pagas e idiomas adicionales se cotizan aparte.')),
    ]
    info_html = ''.join(f'<div class="reveal" style="display: flex; flex-direction: column; gap: 12px">{ic}<h3 class="h4">{h}</h3><p class="txt">{p}</p></div>' for ic, h, p in info)
    body += f'''<section class="sec"><div class="wrap pad" style="padding-top: 64px"><div class="g4 box">{''.join(cards)}</div><div class="g3" style="gap: 40px; margin-top: 72px">{info_html}</div></div></section>
<section class="sec lilac"><div class="wrap pad g2" style="gap: 56px; align-items: center; padding-top: 80px; padding-bottom: 80px">
<div><p class="eyebrow" style="color: #5a26ad">{t('Custom scope', 'Alcance a medida')}</p><h2 class="h2">{t('More pages? A different mix?', '¿Más páginas? ¿Otra combinación?')}</h2></div>
<div style="display: flex; flex-direction: column; gap: 24px"><p class="lead" style="color: #3d3347">{t('Need more than 25 static pages, more than 8 CMS collections, or a different combination? Write to me for a custom quote. Projects with 2 to 7 static pages can also be quoted individually.', '¿Necesitas más de 25 páginas estáticas, más de 8 colecciones CMS u otra combinación? Escríbeme para una cotización a medida. Los proyectos de 2 a 7 páginas también se cotizan individualmente.')}</p>
<div class="row"><a class="btn btn-p" href="mailto:me@pancratzia.com?subject=Custom%20quote">{t('Request a custom quote', 'Pedir una cotización a medida')} {ARR}</a></div></div>
</div></section>
<section class="sec"><div class="wrap pad g2" style="gap: 64px">
<div><p class="eyebrow">{t('Website maintenance', 'Mantenimiento web')}</p><h2 class="h2">{t('One quarter, the same price as your website.', 'Un trimestre, el mismo precio que tu sitio.')}</h2>
<p class="lead" style="margin-top: 24px">{t('Three months of maintenance cost the same as the agreed price of your website. If your build has a custom price, the quarterly price follows that amount.', 'Tres meses de mantenimiento cuestan lo mismo que el precio acordado de tu sitio. Si tu proyecto tiene un precio a medida, el trimestre sigue ese monto.')}</p>
<div class="g2" style="gap: 32px; margin-top: 40px"><div><h3 class="h4" style="margin-bottom: 12px">{t("What's included", 'Qué incluye')}</h3><ul class="list"><li>{t('Updates to supplied content', 'Actualización del contenido que envías')}</li><li>{t('Image updates + monthly AI allowance', 'Actualización de imágenes + cupo mensual de IA')}</li><li>{t('Adding supplied content to CMS', 'Carga de contenido en el CMS')}</li></ul></div>
<div><h3 class="h4" style="margin-bottom: 12px">{t('Content comes from you', 'El contenido viene de ti')}</h3><p class="txt" style="font-size: 15px">{t("I'm not a content writer. You supply the copy; I organize, format and improve how it's presented.", 'No soy redactora. Tú envías los textos; yo los organizo, les doy formato y mejoro su presentación.')}</p></div></div></div>
<div style="display: flex; flex-direction: column; gap: 32px">{maint_table()}{loc_box()}</div>
</div></section>''' + payments()
    write_page('/pricing/', t('Website Pricing & Maintenance Plans | Pancratzia', 'Precios web y planes de mantenimiento | Pancratzia'),
               t('Website packages start at USD 200, with Webflow and WordPress scopes, CMS limits, AI images and quarterly maintenance.', 'Paquetes web desde USD 200, con alcances Webflow y WordPress, límites CMS, imágenes IA y mantenimiento trimestral.'), body, active='/pricing/')


def process():
    steps = [
        (t('Discovery call', 'Llamada inicial'), '', t('We talk about your goals, audience, current website and what the new site needs to do.', 'Hablamos de tus objetivos, tu audiencia, tu sitio actual y lo que debe lograr el nuevo.')),
        (t('Your content &amp; assets', 'Tu contenido y recursos'), '', t('You send your copy, logo, brand guidelines, images and other assets. A defined branding direction is needed before the homepage exploration begins.', 'Me envías textos, logo, manual de marca, imágenes y demás recursos. Se necesita una dirección de marca definida antes de explorar la home.')),
        (t('2 or 3 homepage drafts', '2 o 3 propuestas de home'), '', t('I prepare two or three homepage drafts to explore visual directions. We choose a main direction and can bring in elements from the other drafts or your references.', 'Preparo dos o tres propuestas de home para explorar direcciones visuales. Elegimos una principal y podemos sumar elementos de las otras o de tus referencias.')),
        (t('Homepage refinement', 'Refinamiento de la home'), 'r', t('We bring your feedback together to refine the selected homepage before moving into the rest of the website.', 'Reunimos tu feedback para refinar la home elegida antes de pasar al resto del sitio.')),
        (t('Static pages', 'Páginas estáticas'), 'r', t('I build the agreed static pages using the approved direction. The two rounds cover the full set, not each page.', 'Construyo las páginas estáticas acordadas con la dirección aprobada. Las dos rondas cubren el conjunto completo, no cada página.')),
        (t('CMS pages, when needed', 'Páginas CMS, si aplica'), 'r', t('I build the agreed CMS collections and templates. The two rounds cover the complete CMS set.', 'Construyo las colecciones y plantillas CMS acordadas. Las dos rondas cubren todo el CMS.')),
        (t('Final checks &amp; handover', 'Revisión final y entrega'), '', t('We review the finished website, confirm the agreed scope and prepare for launch. The Webflow project is transferred to your account.', 'Revisamos el sitio terminado, confirmamos el alcance y preparamos el lanzamiento. El proyecto de Webflow se transfiere a tu cuenta.')),
    ]
    tag = f'<span class="tag" style="align-self: flex-start; color: #7136d0; border-color: #7136d0">{t("Up to 2 revision rounds", "Hasta 2 rondas de revisión")}</span>'
    lis = ''.join(f'<li class="g4 reveal{" bb" if i < 6 else ""}" style="padding: 36px 0; gap: 32px; align-items: start"><p class="num" style="margin: 0">0{i+1}</p><div style="display: flex; flex-direction: column; gap: 10px"><h2 class="h3">{a}</h2>{tag if r else ""}</div><p class="txt" style="grid-column: span 2">{b}</p></li>' for i, (a, r, b) in enumerate(steps))
    body = hero(t('The process', 'El proceso'), t('A clear path. <span class="pu">A little magic.</span>', 'Un camino claro. <span class="pu">Un poco de magia.</span>'),
                t('From our first conversation to your finished website, here is how we work together.', 'Desde nuestra primera conversación hasta tu sitio terminado, así trabajamos juntas.'))
    body += f'''<section class="sec dark"><div class="wrap g2" style="gap: 48px; align-items: center; padding-top: 64px; padding-bottom: 64px">
<div><p class="eyebrow pu">{t('Branding / first', 'Primero / la marca')}</p><h2 class="h2" style="font-size: 44px">{t('I build websites. Branding comes first.', 'Construyo sitios web. La marca va primero.')}</h2></div>
<div style="display: flex; flex-direction: column; gap: 20px"><p class="txt" style="font-size: 18px">{t("I don't offer branding services, so you'll need an existing brand identity and visual direction. If you need help with branding, I can introduce you to people who specialize in it.", 'No ofrezco servicios de branding, así que necesitas una identidad de marca y una dirección visual. Si necesitas ayuda, puedo presentarte a especialistas.')}</p><a class="btn btn-w" href="{u('/contact/')}" style="align-self: flex-start">{t("Let's talk", 'Hablemos')} {ARR}</a></div>
</div></section>
<section class="sec"><div class="wrap pad"><ol style="margin: 0; padding: 0; list-style: none">{lis}</ol></div></section>
<section class="sec lilac"><div class="wrap g2" style="gap: 48px; align-items: center; padding-top: 72px; padding-bottom: 72px">
<div><p class="eyebrow" style="color: #5a26ad">{t('Good to know', 'Bueno saberlo')}</p><h2 class="h2" style="font-size: 44px">{t('What is a revision round?', '¿Qué es una ronda de revisión?')}</h2></div>
<div style="display: flex; flex-direction: column; gap: 20px"><p class="txt" style="font-size: 18px; color: #3d3347">{t('One consolidated set of feedback on the current stage. New pages, a new scope or a change of direction after approval are discussed separately, so the project stays clear for both of us.', 'Un conjunto consolidado de comentarios sobre la etapa actual. Páginas nuevas, otro alcance o un cambio de dirección después de aprobar se conversan aparte, para que el proyecto siga claro para ambas partes.')}</p><a class="btn btn-g" href="{u('/pricing/')}" style="align-self: flex-start">{t('Explore pricing', 'Ver precios')} {ARR}</a></div>
</div></section>''' + payments()
    write_page('/process/', t('Website Design & Development Process | Pancratzia', 'Proceso de diseño y desarrollo web | Pancratzia'),
               t('See how Laura Ortega works: discovery, assets, homepage drafts, revisions, static pages, CMS and handover.', 'Conoce cómo trabaja Laura Ortega: descubrimiento, recursos, propuestas de home, revisiones, páginas, CMS y entrega.'), body)


def about():
    exp = [
        ('2020 / NOW', '2020 / HOY', t('Freelance Web Developer', 'Desarrolladora web freelance'), t("Webflow and WordPress projects for direct clients and through Upwork. Recent work includes JuryBall Vegas, Her Vitality Clinic and Men's Vitality Clinic.", "Proyectos Webflow y WordPress para clientes directos y por Upwork. Trabajos recientes: JuryBall Vegas, Her Vitality Clinic y Men's Vitality Clinic.")),
        ('2024 / NOW', '2024 / HOY', 'Honorable Marketing', t("Contract Webflow work from July 2024, then Web Developer &amp; Designer from October 2024. Builds, redesigns, CMS, localization and migrations for the agency's clients.", 'Trabajo Webflow por contrato desde julio de 2024 y luego Web Developer &amp; Designer desde octubre de 2024. Desarrollos, rediseños, CMS, localización y migraciones para los clientes de la agencia.')),
        ('JUN / OCT 2024', 'JUN / OCT 2024', t('Web Development Intern, UCLA', 'Pasante de desarrollo web, UCLA'), t("University website migration to the Arty template, custom Web Components and front-end work with the university's IT department.", 'Migración del sitio universitario a la plantilla Arty, Web Components a medida y front-end con el departamento de TI.')),
        ('2023', '2023', t('University technical &amp; team roles', 'Roles técnicos y de equipo en la universidad'), t('Scrum Master for RocketNet, coordinating an 11-student team, plus technical support for university computer labs.', 'Scrum Master de RocketNet, coordinando un equipo de 11 estudiantes, y soporte técnico en laboratorios de computación.')),
        ('2018 / JAN 2025', '2018 / ENE 2025', t('Telematics Engineering', 'Ingeniería en Telemática'), t('Engineering degree at Universidad Centro Occidental Lisandro Alvarado.', 'Título de ingeniera en la Universidad Centro Occidental Lisandro Alvarado.')),
    ]
    rows = ''.join(f'<div class="g4 bb reveal" style="padding: 32px 0; gap: 32px"><p class="pu" style="margin: 0; font: 600 16px \'Space Grotesk\'">{t(a, b)}</p><h3 class="h3" style="font-size: 22px">{c}</h3><p class="txt" style="grid-column: span 2">{d}</p></div>' for a, b, c, d in exp)
    body = f'''<section class="sec"><div class="hero" style="max-width: 1360px; margin: 0 auto; grid-template-columns: 1.2fr 1fr">
<div class="hero-copy" style="gap: 22px">
<p class="eyebrow up d1" style="margin: 0">{t('About Laura', 'Sobre Laura')}</p>
<h1 class="h1 up d2">{t('Developer. Designer.', 'Desarrolladora. Diseñadora.')} <span class="pu">Laura.</span></h1>
<p class="txt up d3" style="font-size: 18px">{t("I'm Laura Ortega, a web developer and designer based in Barquisimeto, Venezuela. I build websites for clients directly, through Upwork and as part of the team at Honorable Marketing.", 'Soy Laura Ortega, desarrolladora y diseñadora web en Barquisimeto, Venezuela. Construyo sitios para clientes directos, por Upwork y como parte del equipo de Honorable Marketing.')}</p>
<p class="txt up d4" style="font-size: 18px">{t('Most of my recent work is in Webflow: full builds, CMS structure, English and Spanish localization, on-page SEO and platform migrations. I also develop WordPress websites with Oxygen and Elementor when the project calls for it.', 'La mayor parte de mi trabajo reciente es en Webflow: desarrollos completos, estructura CMS, localización español-inglés, SEO on-page y migraciones. También desarrollo en WordPress con Oxygen y Elementor cuando el proyecto lo pide.')}</p>
<p class="txt up d5" style="font-size: 18px">{t('My background in telematics engineering helps me think beyond the layout. I care about site structure, performance, accessibility, and making content manageable for the people who own the website.', 'Mi formación en ingeniería telemática me ayuda a pensar más allá del layout. Me importan la estructura, el rendimiento, la accesibilidad y que el contenido sea fácil de gestionar para quienes son dueños del sitio.')}</p>
<div class="row" style="margin-top: 8px"><a class="btn btn-p" href="{u('/contact/')}">{t('Tell me about your project', 'Cuéntame de tu proyecto')} {ARR}</a><a class="btn btn-g" href="https://www.linkedin.com/in/leortegaperez/">LinkedIn ↗</a></div>
</div>
<div style="display: flex; flex-direction: column"><img src="/assets/laura-portrait.webp" alt="{t('Portrait of Laura Ortega', 'Retrato de Laura Ortega')}" width="900" height="900" style="width: 100%; flex: 1; min-height: 520px; object-fit: cover; display: block"><p class="dark" style="margin: 0; padding: 20px 28px; font: 500 14px/1.4 'Space Grotesk'; letter-spacing: .08em; text-transform: uppercase">Laura Ortega / Pancratzia</p></div>
</div></section>
<section class="sec"><div class="wrap pad"><p class="eyebrow">{t('Experience &amp; education', 'Experiencia y formación')}</p><h2 class="h2" style="margin-bottom: 48px">{t('How I got here.', 'Cómo llegué hasta aquí.')}</h2><div style="border-top: 1.5px solid #251b33">{rows}</div></div></section>
<section class="sec"><div class="g3" style="max-width: 1360px; margin: 0 auto">
<div class="cell br" style="padding: 56px 40px"><h3 class="h4">{t('Languages', 'Idiomas')}</h3><p class="txt">{t('Spanish and English.', 'Español e inglés.')}</p></div>
<div class="cell br" style="padding: 56px 40px"><h3 class="h4">{t('Webflow certifications', 'Certificaciones Webflow')}</h3><ul class="list"><li>Webflow Layouts Certification: Level 1</li><li>The Webflow Way</li></ul></div>
<div class="cell" style="padding: 56px 40px"><h3 class="h4">{t('Outside the browser', 'Fuera del navegador')}</h3><p class="txt">{t('Poodles, fantasy worlds and the visual language of playing cards. Those interests are part of the personality of Pancratzia.', 'Poodles, mundos de fantasía y el lenguaje visual de los naipes. Esos intereses son parte de la personalidad de Pancratzia.')}</p></div>
</div></section>
<section class="sec"><div class="g2" style="max-width: 1360px; margin: 0 auto">
<img class="br" src="/assets/office.webp" alt="{t("Laura's workspace", 'El espacio de trabajo de Laura')}" loading="lazy" style="width: 100%; height: 100%; min-height: 440px; object-fit: cover; display: block">
<div class="cell" style="padding: 80px 40px 80px 56px; gap: 20px; justify-content: center">
<svg width="44" height="44" viewBox="0 0 52 52" fill="none" stroke="#7136d0" stroke-width="2.5" aria-hidden="true"><rect x="10" y="22" width="32" height="24"></rect><path d="M17 22v-7a9 9 0 0 1 18 0v7"></path><circle cx="26" cy="34" r="3" fill="#7136d0"></circle></svg>
<h2 class="h2" style="font-size: 48px">{t('Your website stays yours.', 'Tu sitio sigue siendo tuyo.')}</h2>
<p class="txt" style="font-size: 18px">{t('Hosting and domains stay in your name. At handover, the Webflow project is transferred to your account.', 'El hosting y los dominios quedan a tu nombre. En la entrega, el proyecto de Webflow se transfiere a tu cuenta.')}</p>
</div></div></section>'''
    write_page('/about/', t('Laura Ortega, Web Developer & Designer | Pancratzia', 'Laura Ortega, desarrolladora y diseñadora web | Pancratzia'),
               t('Meet Laura Ortega, a telematics engineer and web developer specializing in Webflow and WordPress.', 'Conoce a Laura Ortega, ingeniera en telemática y desarrolladora web especializada en Webflow y WordPress.'), body, active='/about/')


def faq():
    qa = [
        (t('Which platforms do you work with?', '¿Con qué plataformas trabajas?'), t('I specialize in Webflow and Webflow CMS. I also build in WordPress with Oxygen and Elementor when the project calls for it.', 'Me especializo en Webflow y Webflow CMS. También construyo en WordPress con Oxygen y Elementor cuando el proyecto lo pide.')),
        (t('Do I need branding before we start?', '¿Necesito tener marca antes de empezar?'), t("Yes. You provide the brand direction, logo, copy and assets. I don't offer branding, but I can introduce you to professionals who do.", 'Sí. Tú aportas la dirección de marca, logo, textos y recursos. No ofrezco branding, pero puedo presentarte a profesionales que sí.')),
        (t('How do homepage drafts and revisions work?', '¿Cómo funcionan las propuestas de home y las revisiones?'), t('I prepare two or three homepage drafts and we choose one main direction. The homepage includes up to two revision rounds. Static pages have up to two rounds for the whole set; CMS pages have up to two rounds for the CMS stage.', 'Preparo dos o tres propuestas de home y elegimos una dirección. La home incluye hasta dos rondas de revisión. Las páginas estáticas tienen hasta dos rondas para todo el conjunto y el CMS hasta dos rondas para su etapa.')),
        (t('What does a CMS collection mean in your packages?', '¿Qué significa una colección CMS en tus paquetes?'), t('A collection is a content type and its template, such as articles, projects or team members. Individual entries are not static pages. Content entry and migration volume are confirmed in your quote.', 'Una colección es un tipo de contenido y su plantilla, como artículos, proyectos o equipo. Las entradas no son páginas estáticas. La carga de contenido y el volumen de migración se confirman en tu cotización.')),
        (t('Are AI images included?', '¿Las imágenes con IA están incluidas?'), t("Each website package includes up to 10 AI-generated images, with up to three image revisions in total. I don't offer photo editing, although some adjustments may be possible with AI.", 'Cada paquete incluye hasta 10 imágenes con IA y hasta tres revisiones de imagen en total. No ofrezco edición fotográfica, aunque algunos ajustes pueden hacerse con IA.')),
        (t('Do you write the content?', '¿Escribes el contenido?'), t('Partially, yes. You provide the complete information about your business, services and project in a document. I then restructure and adapt it into clear, organized website content.', 'En parte, sí. Tú entregas la información completa de tu negocio, servicios y proyecto en un documento, y yo la reestructuro y adapto en contenido web claro y organizado.')),
        (t('Can you migrate an existing website?', '¿Puedes migrar un sitio existente?'), t('Yes. We review the current platform, content, URLs, CMS and integrations before defining the migration scope. Redirects and launch checks are part of the plan.', 'Sí. Revisamos plataforma, contenido, URLs, CMS e integraciones antes de definir el alcance. Las redirecciones y revisiones de lanzamiento son parte del plan.')),
        (t('Do you offer maintenance?', '¿Ofreces mantenimiento?'), t('Yes. Three months of maintenance cost the same as the agreed website price. Monthly AI image allowances are 1, 3, 5 or 7 for the USD 200, 600, 1,000 or 1,500 packages.', 'Sí. Tres meses de mantenimiento cuestan lo mismo que el precio acordado del sitio. El cupo mensual de imágenes IA es 1, 3, 5 o 7 para los paquetes de USD 200, 600, 1.000 o 1.500.')),
        (t('What does localization plugin support cost?', '¿Cuánto cuesta el soporte del plugin de localización?'), t('Installation is USD 100 once and plugin maintenance is USD 50 per month. You pay the plugin subscription or license separately.', 'La instalación cuesta USD 100 una vez y el mantenimiento USD 50 al mes. La suscripción o licencia del plugin se paga aparte.')),
        (t('Which payment methods do you accept?', '¿Qué métodos de pago aceptas?'), t("PayPal, AirTM-to-AirTM transfers, my AirTM virtual US account, Binance International and USDT to my wallet. I don't use Binance.US.", 'PayPal, transferencias AirTM a AirTM, mi cuenta virtual de EE. UU. en AirTM, Binance International y USDT a mi wallet. No uso Binance.US.')),
        (t('Will I own the website?', '¿El sitio será mío?'), t('Yes. Hosting and domains stay in your name. At delivery, the Webflow project is transferred to your account.', 'Sí. El hosting y los dominios quedan a tu nombre. En la entrega, el proyecto de Webflow se transfiere a tu cuenta.')),
        (t('How long will my project take?', '¿Cuánto tardará mi proyecto?'), t('It depends on scope, content readiness, migration volume and feedback. We agree on a schedule after reviewing the project.', 'Depende del alcance, del contenido listo, del volumen de migración y del feedback. Acordamos un calendario después de revisar el proyecto.')),
    ]
    det = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q} <span class="pm" aria-hidden="true">+</span></summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))
    body = f'''<section class="sec"><div class="wrap pad g2" style="gap: 64px; align-items: start">
<div style="position: sticky; top: 120px; display: flex; flex-direction: column; gap: 24px">
<p class="eyebrow up d1" style="margin: 0">FAQ</p><h1 class="h1 up d2">{t('Questions before <span class="pu">we begin?</span>', '¿Preguntas antes <span class="pu">de empezar?</span>')}</h1>
<p class="lead up d3">{t('A few practical answers about scope, revisions, maintenance and working together.', 'Respuestas prácticas sobre alcance, revisiones, mantenimiento y cómo trabajamos juntas.')}</p>
<div class="row up d4"><a class="btn btn-g" href="{u('/process/')}">{t('Full process', 'Proceso completo')}</a><a class="btn btn-g" href="{u('/pricing/')}">{t('Pricing', 'Precios')}</a></div>
</div>
<div style="border-top: 1.5px solid #251b33">{det}</div>
</div></section>'''
    write_page('/faq/', t('Website Project FAQs: Scope, Costs & Revisions | Pancratzia', 'Preguntas frecuentes: alcance, costos y revisiones | Pancratzia'),
               t('Answers about Webflow and WordPress projects, branding, revisions, CMS, AI images, maintenance, localization and payment methods.', 'Respuestas sobre proyectos Webflow y WordPress, marca, revisiones, CMS, imágenes IA, mantenimiento, localización y pagos.'), body)


def contact():
    opts = [(t('A new Webflow website', 'Un sitio nuevo en Webflow'), 'A%20new%20Webflow%20website'), (t('A redesign or migration', 'Un rediseño o migración'), 'A%20redesign%20or%20migration'),
            (t('CMS or bilingual content', 'CMS o contenido bilingüe'), 'CMS%20or%20bilingual%20content'), (t('Agency collaboration', 'Colaboración con agencia'), 'Agency%20collaboration'), (t('Something else', 'Otra cosa'), 'Something%20else')]
    picks = ''.join(f'<a class="pick" href="mailto:me@pancratzia.com?subject={s}">{l} <span class="pu" aria-hidden="true">↗</span></a>' for l, s in opts)
    body = f'''<section class="sec purple" style="position: relative">
<span class="hide-m" style="position: absolute; right: 8%; top: 72px">{star(80, '#ddd0ef')}</span>
<div class="wrap pad g2" style="gap: 64px">
<div style="display: flex; flex-direction: column; gap: 28px">
<p class="eyebrow up d1" style="margin: 0; color: #ddd0ef">{t("Let's make something good", 'Hagamos algo bueno')}</p>
<h1 class="h1 up d2">{t("Let's turn that idea into a website.", 'Convirtamos esa idea en un sitio web.')}</h1>
<p class="lead up d3" style="color: #ece4fb">{t("Tell me what you're imagining. A few details are enough to start a useful conversation.", 'Cuéntame lo que imaginas. Con unos pocos detalles basta para empezar una buena conversación.')}</p>
<a class="btn btn-w up d4" href="mailto:me@pancratzia.com" style="align-self: flex-start; font-size: 22px; min-height: 68px; padding: 0 30px">me@pancratzia.com {ARR}</a>
<p class="up d5" style="margin: 0; font-size: 14px; color: #ddd0ef">{t('Opens your email app. Prefer your usual inbox? Copy the address above.', 'Abre tu app de correo. ¿Prefieres tu bandeja habitual? Copia la dirección de arriba.')}</p>
<div class="row up d5" style="gap: 24px; font-size: 15px"><a href="https://webflow.com/@pancratzia" style="color: #fff">Webflow ↗</a><a href="https://www.upwork.com/freelancers/~016a6410dfa02febf5" style="color: #fff">Upwork ↗</a><span style="color: #ddd0ef">EN / ES · {t('Remote', 'Remoto')}</span></div>
</div>
<div class="box" style="color: #251b33; box-shadow: 10px 10px 0 #251b33">
<p class="h4" style="padding: 24px 20px; margin: 0; border-bottom: 1.5px solid #251b33">{t('What are you working on?', '¿En qué estás trabajando?')}</p>
{picks}
<div style="padding: 24px 20px; background: #f5f2ec"><p class="h4" style="margin: 0 0 12px; font-size: 17px">{t('A good first message includes', 'Un buen primer mensaje incluye')}</p>
<ul class="list" style="font-size: 15px"><li>{t('Your business and current website, if you have one', 'Tu negocio y tu sitio actual, si tienes uno')}</li><li>{t('What you want to create or improve', 'Qué quieres crear o mejorar')}</li><li>{t('The scope and dates you have in mind', 'El alcance y las fechas que tienes en mente')}</li></ul></div>
</div>
</div></section>'''
    write_page('/contact/', t('Contact Laura Ortega for Your Website | Pancratzia', 'Contacta a Laura Ortega para tu sitio web | Pancratzia'),
               t('Discuss a Webflow or WordPress build, redesign, CMS or migration with Laura Ortega. Email me@pancratzia.com.', 'Conversa con Laura Ortega sobre un sitio Webflow o WordPress, rediseño, CMS o migración. Escribe a me@pancratzia.com.'), body, with_cta=False)


def blog_index():
    posts = [('wordpress-to-webflow-migration', '/assets/wordpress-webflow-migration.webp', t('14 October 2026 · WordPress / Webflow', '14 de octubre de 2026 · WordPress / Webflow'), t('Should you migrate from WordPress to Webflow?', '¿Deberías migrar de WordPress a Webflow?'), t('A migration should improve how your website works, how your team publishes and how you serve your customers. Here are the questions to answer before changing platforms.', 'Una migración debe mejorar cómo funciona tu sitio, cómo publica tu equipo y cómo atiendes a tus clientes. Estas son las preguntas que conviene responder antes de cambiar de plataforma.')),
             ('website-migration-checklist', '/assets/migration-hero.webp', t('Migrations · Practical guide', 'Migraciones · Guía práctica'), t('Planning a website migration? Check these things before you move.', '¿Planeas migrar tu sitio? Revisa esto antes de mudarte.'), t("A new design is only part of the move. Here's how to prepare your content, URLs, CMS and forms so the new website has a solid starting point.", 'Un nuevo diseño es solo parte de la mudanza. Así puedes preparar contenido, URLs, CMS y formularios para que el nuevo sitio arranque con una base sólida.'))]
    cards = ''.join(f'''<a class="work reveal" href="{u('/blog/' + s + '/')}"><div class="shot" style="aspect-ratio: 16 / 9"><img src="{img}" alt="" loading="lazy" width="1672" height="941"></div><p class="sm" style="margin: 0; letter-spacing: .08em; text-transform: uppercase">{m}</p><h2 class="h3" style="font-size: 30px">{h}</h2><p class="txt">{d}</p><p class="pu" style="margin: 0; font-weight: 500">{t('Read the article', 'Leer el artículo')} ↗</p></a>''' for s, img, m, h, d in posts)
    body = hero(t('Journal', 'Blog'), t('Notes from <span class="pu">my desk.</span>', 'Notas desde <span class="pu">mi escritorio.</span>'), t('Practical guides to planning and maintaining a website.', 'Guías prácticas para planificar y mantener un sitio web.'))
    body += f'<section class="sec"><div class="wrap pad" style="padding-top: 64px"><div class="g2" style="gap: 48px 40px">{cards}</div></div></section>'
    write_page('/blog/', t('Website Planning & Migration Blog | Pancratzia', 'Blog de planificación y migración web | Pancratzia'),
               t('Practical guides by Laura Ortega on website migrations, WordPress, Webflow, content and CMS.', 'Guías prácticas de Laura Ortega sobre migraciones, WordPress, Webflow, contenido y CMS.'), body, active='/blog/')
