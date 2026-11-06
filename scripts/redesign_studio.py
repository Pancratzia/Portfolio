"""Bilingual Pancratzia studio redesign; preserve existing content routes."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

COPY = {
 'en': {
  'nav':['Work','Services','About','Journal'], 'start':'Start a project',
  'eyebrow':'LAURA ORTEGA · WEBFLOW DESIGNER & DEVELOPER',
  'headline':'A little magic.<br><span>A lot of Webflow.</span>',
  'intro':'Distinctive websites for brands with something to say. I design and build in Webflow, so your next big idea feels right—and works beautifully.',
  'chips':['Web design + development','CMS + migrations','English + Spanish'],
  'secondary':'Explore my work', 'note':'For brands, founders & creative agencies.',
  'drag':'Drag to explore', 'gallery':'A few things I’ve brought to life',
  'proof':['Designed with intention.','Built for real people.','Ready for your next chapter.'],
  'worktag':'01 / SELECTED WORK', 'worktitle':'Real projects.<br><em>Different kinds of magic.</em>',
  'workintro':'A closer look at the design, structure and care behind each build.', 'allwork':'All projects',
  'serviceTag':'02 / WHAT I CAN HELP WITH', 'serviceTitle':'Your idea.<br><em>My design + dev brain.</em>',
  'serviceIntro':'From a fresh start to a better version of what you already have. One person who connects the design with the details.',
  'serviceNames':['Webflow design + development','CMS, content + migrations','English + Spanish websites','WordPress + ongoing care'],
  'serviceDesc':['A custom website or thoughtful redesign, with responsive layouts, purposeful interactions and reusable components.','Collections your team can manage. Content that lands in the right place. Redirects planned before the move.','An experience that makes sense in both languages, from navigation to the smallest call to action.','Oxygen builds when WordPress is the right fit, plus updates and maintenance after launch.'],
  'serviceLinks':['See Webflow services','Organize your content','Explore localization','Explore WordPress'],
  'agencyTag':'FOR BRANDS. AND THE PEOPLE BEHIND THEM.', 'agencyTitle':'A creative partner.<br><em>Not another handoff.</em>',
  'agencyText':'Bring me your idea, your Figma file or the website you’ve outgrown. I’ll help connect the visual direction, content and development into a website that’s ready to use.',
  'agencyPoints':['Design + development in one conversation','Direct collaboration with Laura','Clear stages, feedback and handover'],
  'about':'Meet your developer', 'aboutTag':'HUMAN BEHIND THE PIXELS',
  'aboutTitle':'Hi, I’m Laura.<br><em>Builder. Designer.<br>Detail person.</em>',
  'aboutText':'I’m the person behind Pancratzia. My background in telematics engineering meets a creative eye for layout, motion and all the little details that make a website feel considered.',
  'aboutText2':'Based in Venezuela, working remotely with brands and agencies in English and Spanish. Usually with a few poodles nearby.',
  'processTag':'03 / HOW WE GET THERE','processTitle':'Good work.<br><em>Clear next steps.</em>',
  'steps':[('Tell me the idea','We talk about your goals, your current website and what needs to change.'),('Find the direction','We explore the homepage and agree on the look before building the rest.'),('Build + refine','I develop the site, organize the content and work through your feedback.'),('Launch with clarity','We check the details, publish and hand over a website you can work with.')],
  'processLink':'The full process', 'faqTag':'A FEW THINGS YOU MIGHT BE WONDERING',
  'faqTitle':'Before we say <em>hello.</em>',
  'faqs':[('Can you work from my existing design?','Yes. I can develop a supplied design, rebuild an existing website or help shape a new visual direction. Share what you have and we can define the right scope.'),('Do you work with agencies?','Yes. I collaborate with agencies as a Webflow development partner, as well as working directly with brands and founders.'),('What do you need to give me a quote?','Your current website, what you want to build or improve, the content and functionality involved, and your preferred timeline. Pricing follows the scope.'),('Can my website be bilingual?','Yes. I work in English and Spanish and can plan both language experiences, including content structure, navigation and localization setup.')],
  'journalTag':'FROM MY DESK', 'journalTitle':'A little clarity<br><em>before you build.</em>', 'journalLink':'Read the journal',
  'endTag':'YOUR NEXT CHAPTER STARTS HERE', 'endTitle':'Have an idea?<br><em>Let’s make it real.</em>',
  'endText':'A new website, a fresh direction, or an extra pair of Webflow hands. Tell me what you have in mind.',
  'emailCopy':'Copy email', 'emailCopied':'Email copied', 'footerline':'Thoughtfully designed. Carefully built.',
  'contactTitle':'Let’s turn that<br><em>idea into a website.</em>', 'contactIntro':'Tell me what you’re imagining. A few details are enough to start a useful conversation.',
  'choose':'What are you working on?', 'contactTypes':['A new Webflow website','A redesign or migration','CMS or bilingual content','Agency collaboration','Something else'],
  'contactNext':'A good first message', 'contactItems':['Your business and current website, if you have one.','What you want to create or improve.','The scope and dates you have in mind.'],
  'emailButton':'Email Laura', 'emailNote':'Opens your email app. Prefer your usual inbox? Copy the address below.',
  'seoTitle':'Webflow Designer & Developer — Laura Ortega | Pancratzia', 'seoDesc':'Custom Webflow design and development by Laura Ortega. Distinctive websites, CMS, migrations and English–Spanish localization for brands and agencies.'
 },
 'es': {
  'nav':['Proyectos','Servicios','Sobre mí','Blog'], 'start':'Empezar un proyecto',
  'eyebrow':'LAURA ORTEGA · DISEÑO Y DESARROLLO WEBFLOW',
  'headline':'Un poco de magia.<br><span>Mucho Webflow.</span>',
  'intro':'Sitios con personalidad para marcas que tienen algo que decir. Diseño y desarrollo en Webflow para que tu próxima gran idea se vea bien y funcione mejor.',
  'chips':['Diseño + desarrollo web','CMS + migraciones','Inglés + español'],
  'secondary':'Explorar mis proyectos', 'note':'Para marcas, emprendedores y agencias creativas.',
  'drag':'Arrastra para explorar', 'gallery':'Ideas que ya se hicieron realidad',
  'proof':['Diseño con intención.','Pensado para personas.','Listo para tu próximo capítulo.'],
  'worktag':'01 / PROYECTOS DESTACADOS', 'worktitle':'Proyectos reales.<br><em>Distintas formas de hacer magia.</em>',
  'workintro':'El diseño, la estructura y los detalles detrás de cada sitio.', 'allwork':'Todos los proyectos',
  'serviceTag':'02 / EN QUÉ PUEDO AYUDARTE', 'serviceTitle':'Tu idea.<br><em>Mi lado creativo + técnico.</em>',
  'serviceIntro':'Desde un nuevo comienzo hasta una mejor versión de lo que ya tienes. Una persona que conecta el diseño con los detalles.',
  'serviceNames':['Diseño + desarrollo Webflow','CMS, contenido + migraciones','Sitios en inglés + español','WordPress + mantenimiento'],
  'serviceDesc':['Un sitio a medida o un rediseño bien pensado, con layouts responsive, interacciones con intención y componentes reutilizables.','Colecciones que tu equipo puede gestionar. Contenido en su lugar. Redirecciones planificadas antes de migrar.','Una experiencia coherente en ambos idiomas, desde la navegación hasta el último llamado a la acción.','Desarrollo con Oxygen cuando WordPress sea la mejor opción, y soporte para cuidar el sitio después de publicarlo.'],
  'serviceLinks':['Ver servicios Webflow','Organizar tu contenido','Explorar localización','Explorar WordPress'],
  'agencyTag':'PARA MARCAS. Y QUIENES LAS HACEN CRECER.', 'agencyTitle':'Una aliada creativa.<br><em>Menos vueltas, más conexión.</em>',
  'agencyText':'Trae tu idea, tu archivo de Figma o ese sitio que ya se quedó pequeño. Te ayudo a conectar la dirección visual, el contenido y el desarrollo en una web lista para usar.',
  'agencyPoints':['Diseño y desarrollo en una misma conversación','Colaboración directa conmigo','Etapas, feedback y entrega claros'],
  'about':'Conoce a tu desarrolladora', 'aboutTag':'LA PERSONA DETRÁS DE LOS PÍXELES',
  'aboutTitle':'Hola, soy Laura.<br><em>Creativa. Técnica.<br>De los detalles.</em>',
  'aboutText':'Soy la persona detrás de Pancratzia. Mi formación en ingeniería telemática se combina con una mirada creativa para el diseño, el movimiento y esos detalles que hacen que una web se sienta bien pensada.',
  'aboutText2':'Desde Venezuela, trabajo de forma remota con marcas y agencias en inglés y español. Casi siempre con unos poodles cerca.',
  'processTag':'03 / CÓMO LO HACEMOS','processTitle':'Buen trabajo.<br><em>Próximos pasos claros.</em>',
  'steps':[('Cuéntame la idea','Conversamos sobre tus objetivos, tu sitio actual y lo que quieres mejorar.'),('Definimos la dirección','Exploramos el homepage y acordamos el estilo antes de desarrollar el resto.'),('Desarrollamos + ajustamos','Construyo el sitio, organizo el contenido y trabajamos tus comentarios.'),('Publicamos con claridad','Revisamos los detalles, publicamos y te entrego una web que puedes gestionar.')],
  'processLink':'El proceso completo', 'faqTag':'ALGUNAS DUDAS ANTES DE EMPEZAR',
  'faqTitle':'Antes de decir <em>hola.</em>',
  'faqs':[('¿Puedes trabajar con un diseño que ya tengo?','Sí. Puedo desarrollar un diseño aprobado, reconstruir un sitio existente o ayudarte a encontrar una nueva dirección visual. Comparte lo que tienes y definimos el alcance.'),('¿Trabajas con agencias?','Sí. Colaboro con agencias como desarrolladora Webflow y también trabajo directamente con marcas y emprendedores.'),('¿Qué necesitas para preparar un presupuesto?','Tu sitio actual, qué quieres crear o mejorar, el contenido y las funciones necesarias, y las fechas que tienes en mente. El presupuesto depende del alcance.'),('¿Mi sitio puede estar en dos idiomas?','Sí. Trabajo en inglés y español y puedo planificar ambas experiencias, incluyendo contenido, navegación y configuración de localización.')],
  'journalTag':'DESDE MI ESCRITORIO', 'journalTitle':'Un poco de claridad<br><em>antes de construir.</em>', 'journalLink':'Visitar el blog',
  'endTag':'TU PRÓXIMO CAPÍTULO EMPIEZA AQUÍ', 'endTitle':'¿Tienes una idea?<br><em>Hagámosla realidad.</em>',
  'endText':'Un sitio nuevo, otra dirección o apoyo para tu equipo Webflow. Cuéntame qué tienes en mente.',
  'emailCopy':'Copiar correo', 'emailCopied':'Correo copiado', 'footerline':'Diseño con intención. Desarrollo con cuidado.',
  'contactTitle':'Hagamos de tu idea<br><em>un buen sitio web.</em>', 'contactIntro':'Cuéntame qué tienes en mente. Con unos pocos detalles podemos iniciar una conversación útil.',
  'choose':'¿En qué estás trabajando?', 'contactTypes':['Un sitio nuevo en Webflow','Un rediseño o migración','CMS o contenido bilingüe','Colaboración con agencia','Algo diferente'],
  'contactNext':'Un buen primer mensaje', 'contactItems':['Tu negocio y sitio actual, si tienes uno.','Qué quieres crear o mejorar.','El alcance y las fechas que tienes en mente.'],
  'emailButton':'Escribirle a Laura', 'emailNote':'Abre tu aplicación de correo. ¿Prefieres tu bandeja habitual? Copia la dirección de abajo.',
  'seoTitle':'Diseño y Desarrollo Webflow — Laura Ortega | Pancratzia', 'seoDesc':'Diseño y desarrollo Webflow a medida con Laura Ortega. Sitios con personalidad, CMS, migraciones y localización inglés–español para marcas y agencias.'
 }
}

PROJECTS = [
 ('joumana-kayrouz','Joumana Kayrouz','joumana.png','Webflow · Redesign · SEO','Webflow · Rediseño · SEO'),
 ('mungo-law','Mungo Law','mungo-upwork.webp','Webflow · Multi-page website','Webflow · Sitio multipágina'),
 ('hire-warriors','Hire Warriors','hire-upwork.webp','Webflow CMS · Directory','Webflow CMS · Directorio'),
 ('her-vitality-clinic','Her Vitality Clinic','her-vitality-upwork.webp','WordPress · Healthcare','WordPress · Salud'),
]

def arrow(): return '<span aria-hidden="true">↗</span>'
def button(url,label,secondary=False): return f'<a class="s-button{" s-button-ghost" if secondary else ""}" href="{url}">{label}{arrow()}</a>'

def header(lang,other):
 c=COPY[lang]; p='/es' if lang=='es' else ''
 links=''.join(f'<a href="{p}/{route}/">{label}</a>' for route,label in zip(['work','services','about','blog'],c['nav']))
 return f'''<header><div class="s-nav s-container"><a class="s-brand" href="{p}/" aria-label="Pancratzia — {'Inicio' if lang=='es' else 'Home'}"><span class="s-brand-mark" aria-hidden="true">[p*]</span>pancratzia<span class="s-brand-period">.</span></a><nav id="studio-navigation" aria-label="{'Principal' if lang=='es' else 'Main navigation'}">{links}</nav><div class="s-nav-actions"><a class="language" href="{other}" lang="{'en' if lang=='es' else 'es'}" aria-label="{'Switch to English' if lang=='es' else 'Cambiar a español'}">{'EN' if lang=='es' else 'ES'}</a>{button(p+'/contact/',c['start'])}<button class="s-menu" type="button" aria-controls="studio-navigation" aria-expanded="false" aria-label="{'Abrir menú' if lang=='es' else 'Open menu'}"><span></span><span></span></button></div></div></header>'''

def footer(lang):
 c=COPY[lang];p='/es' if lang=='es' else ''
 pages=[('work',c['nav'][0]),('services',c['nav'][1]),('process','Proceso' if lang=='es' else 'Process'),('pricing','Precios' if lang=='es' else 'Pricing'),('about',c['nav'][2]),('blog',c['nav'][3]),('faq','FAQ')]
 legal=[('privacy','Privacidad' if lang=='es' else 'Privacy'),('terms','Términos' if lang=='es' else 'Terms'),('storage','Navegador' if lang=='es' else 'Browser storage')]
 return f'''<footer><div class="s-footer s-container"><div class="s-footer-top"><div><a class="s-brand" href="{p}/"><span class="s-brand-mark" aria-hidden="true">[p*]</span>pancratzia.</a><p>{c['footerline']}</p><a class="s-email" href="mailto:me@pancratzia.com">me@pancratzia.com {arrow()}</a></div><div class="s-footer-links">{''.join(f'<a href="{p}/{route}/">{label}</a>' for route,label in pages)}</div><div class="s-footer-links"><span class="s-mono">ELSEWHERE / EN OTRAS PARTES</span><a href="https://webflow.com/@pancratzia" target="_blank" rel="noopener">Webflow ↗</a><a href="https://www.upwork.com/freelancers/~016a6410dfa02febf5?mp_source=share" target="_blank" rel="noopener">Upwork ↗</a></div></div><div class="s-footer-bottom"><span>© 2026 Laura Ortega · Pancratzia</span><span>REMOTE, WORLDWIDE · EN / ES</span><div>{''.join(f'<a href="{p}/{route}/">{label}</a>' for route,label in legal)}<button id="motion-toggle" type="button" aria-pressed="false">{'Reducir movimiento' if lang=='es' else 'Reduce motion'}</button></div></div></div></footer>'''

def home(lang):
 c=COPY[lang];p='/es' if lang=='es' else '';es=lang=='es'
 chiproutes=['webflow-development','webflow-cms','localization']
 chips=''.join(f'<a href="{p}/services/{route}/">{label}{arrow()}</a>' for label,route in zip(c['chips'],chiproutes))
 cards=''
 for i in range(8):
  if i == 4:
   art='\n'.join(''.join('+' if (abs(x-20)+abs(y-18)<13 and (abs(x-20)<3 or abs(y-18)<3)) else ':' if x in (3,37) and 3<y<33 else '-' if y in (3,33) and 3<x<37 else '.' if (x*7+y*13)%71==0 else ' ' for x in range(42)) for y in range(38))
   label='Tu próximo sitio' if es else 'Your next website'
   cards+=f'<a class="s-reel s-reel-ascii" href="{p}/contact/" aria-label="{label}"><pre aria-hidden="true">{art}</pre><span class="s-reel-ascii-note">[ DESIGN + CODE + YOU ]</span><span class="s-reel-caption"><span>{label}</span>{arrow()}</span></a>'
   continue
  slug,name,image,tag,estag=PROJECTS[i%4]
  cards+=f'<a class="s-reel" href="{p}/work/{slug}/" aria-label="{name}"><img src="/assets/{image}" alt="{name} — {estag if es else tag}" width="540" height="360" loading="eager" draggable="false"><div class="s-reel-cover"></div><span class="s-reel-caption"><span>{name}</span>{arrow()}</span></a>'
 reel=f'''<div class="s-gallery"><div class="s-gallery-top s-container"><span class="s-mono">{c['gallery']}</span><span class="s-mono">[ {c['drag']} ↔ ]</span></div><div class="s-reel-stage" aria-label="{'Galería de proyectos, arrastra o usa las flechas' if es else 'Project gallery, drag or use arrow controls'}">{cards}</div><div class="s-gallery-bottom s-container"><span class="s-mono">DESIGN / DEVELOP / MAKE IT FEEL RIGHT</span><div><button type="button" data-reel="prev" aria-label="{'Proyecto anterior' if es else 'Previous project'}">←</button><button type="button" data-reel="pause" aria-label="{'Pausar galería' if es else 'Pause gallery'}" aria-pressed="false">Ⅱ</button><button type="button" data-reel="next" aria-label="{'Siguiente proyecto' if es else 'Next project'}">→</button></div></div></div>'''
 main=f'''<main id="main" class="s-home"><section class="s-hero"><div class="s-hero-copy s-container"><p class="s-eyebrow"><span class="s-dot" aria-hidden="true"></span>{c['eyebrow']}</p><h1>{c['headline']}</h1><p class="s-hero-intro">{c['intro']}</p><div class="s-service-chips">{chips}</div><div class="s-hero-actions">{button(p+'/contact/',c['start'])}{button('#selected-work',c['secondary'],True)}</div><p class="s-hero-note">{c['note']}</p><span class="s-hero-spark" aria-hidden="true">+<br>+++<br>+++++++<br>+++<br>+</span><span class="s-handnote" aria-hidden="true">{'tu próxima gran idea' if es else 'your next big thing'}<svg viewBox="0 0 110 95" fill="none"><path d="M4 2C90 5 99 36 72 77M56 70l16 9 17-10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span></div>{reel}</section>'''
 main+='<div class="s-proof"><div class="s-container">'+''.join('<span><b aria-hidden="true">✳</b>'+item+'</span>' for item in c['proof'])+'</div></div>'
 main+=f'<section class="s-work s-section s-container" id="selected-work"><div class="s-section-heading"><div><p class="s-eyebrow">{c["worktag"]}</p><h2>{c["worktitle"]}</h2></div><div><p>{c["workintro"]}</p><a class="s-text-link" href="{p}/work/">{c["allwork"]} {arrow()}</a></div></div><div class="s-work-grid">'
 for i,(slug,name,image,tag,estag) in enumerate(PROJECTS[:3]):
  desc=[('A new chapter for an established law firm.','Un nuevo capítulo para una firma consolidada.'),('From a landing page to a connected website.','De una landing a un sitio completo.'),('A directory built to connect a community.','Un directorio que conecta a una comunidad.')][i][int(es)]
  main+=f'<a class="s-work-card" href="{p}/work/{slug}/"><div class="s-work-image"><span class="s-work-index s-mono">0{i+1} / {"VER PROYECTO" if es else "VIEW PROJECT"} {arrow()}</span><img src="/assets/{image}" alt="{name} website" width="540" height="360" loading="lazy"></div><div class="s-work-caption"><div><span class="s-mono">{estag if es else tag}</span><h3>{name}</h3><p>{desc}</p></div><span class="s-round-arrow" aria-hidden="true">↗</span></div></a>'
 main+='</div></section>'
 main+=f'<section class="s-services s-section" id="services"><div class="s-container"><div class="s-section-heading"><div><p class="s-eyebrow">{c["serviceTag"]}</p><h2>{c["serviceTitle"]}</h2></div><p>{c["serviceIntro"]}</p></div><div class="s-services-grid">'
 icons=['< / >','{ : }','EN/ES','[ + ]'];routes=['webflow-development','webflow-cms','localization','wordpress-oxygen']
 for i in range(4):
  main+=f'<a class="s-service" href="{p}/services/{routes[i]}/"><span class="s-service-icon" aria-hidden="true">{escape(icons[i])}</span><span class="s-mono">0{i+1}</span><h3>{c["serviceNames"][i]}</h3><p>{c["serviceDesc"][i]}</p><span class="s-text-link">{c["serviceLinks"][i]} {arrow()}</span></a>'
 main+=f'</div><div class="s-agency"><div><p class="s-eyebrow">{c["agencyTag"]}</p><h3>{c["agencyTitle"]}</h3><p>{c["agencyText"]}</p>{button(p+"/contact/?service=agency",c["start"])}</div><ul>'+''.join(f'<li><span aria-hidden="true">[✓]</span>{t}</li>' for t in c['agencyPoints'])+'</ul></div></div></section>'
 main+=f'''<section class="s-about s-section s-container" id="about"><div class="s-about-art"><div class="s-ascii-label s-mono">PANCRATZIA / HUMAN.EXE</div><pre class="s-ascii" data-ascii aria-hidden="true"></pre><img class="s-ascii-source" src="/assets/laura-cutout.webp" alt="" hidden><span class="s-ascii-bottom s-mono">DESIGNER + DEVELOPER + A LITTLE MAGIC</span></div><div class="s-about-copy"><p class="s-eyebrow">{c['aboutTag']}</p><h2>{c['aboutTitle']}</h2><p>{c['aboutText']}</p><p>{c['aboutText2']}</p><a class="s-text-link" href="{p}/about/">{c['about']} {arrow()}</a></div></section>'''
 main+=f'<section class="s-process s-section" id="process"><div class="s-container"><div class="s-section-heading"><div><p class="s-eyebrow">{c["processTag"]}</p><h2>{c["processTitle"]}</h2></div><a class="s-text-link" href="{p}/process/">{c["processLink"]} {arrow()}</a></div><div class="s-steps">'
 for i,(title,desc) in enumerate(c['steps']): main+=f'<article><span class="s-mono">[ 0{i+1} ]</span><h3>{title}</h3><p>{desc}</p></article>'
 main+='</div></div></section>'
 main+=f'<section class="s-faq s-section s-container" id="questions"><div><p class="s-eyebrow">{c["faqTag"]}</p><h2>{c["faqTitle"]}</h2><a class="s-text-link" href="{p}/faq/">{"Más respuestas" if es else "More answers"} {arrow()}</a></div><div class="faq-list">'
 for q,a in c['faqs']: main+=f'<details name="studio-faq"><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>'
 main+='</div></section>'
 main+=f'<section class="s-journal s-section"><div class="s-container"><div class="s-section-heading"><div><p class="s-eyebrow">{c["journalTag"]}</p><h2>{c["journalTitle"]}</h2></div><a class="s-text-link" href="{p}/blog/">{c["journalLink"]} {arrow()}</a></div><div class="s-journal-grid">'
 posts=[('wordpress-to-webflow-migration','wordpress-webflow-migration.webp','¿Conviene migrar de WordPress a Webflow?' if es else 'Should you migrate from WordPress to Webflow?'),('website-migration-checklist','migration-hero.webp','Qué revisar antes de migrar tu sitio web.' if es else 'What to check before you move your website.')]
 for slug,image,title in posts: main+=f'<a href="{p}/blog/{slug}/"><img src="/assets/{image}" alt="" width="1672" height="941" loading="lazy"><span class="s-mono">WORDPRESS / WEBFLOW / MIGRATIONS</span><h3>{title}</h3><span class="s-text-link">{"Leer artículo" if es else "Read article"} {arrow()}</span></a>'
 main+='</div></div></section>'
 main+=f'<section class="s-closing" id="contact"><div class="s-container"><p class="s-eyebrow">{c["endTag"]}</p><h2>{c["endTitle"]}</h2><p>{c["endText"]}</p>{button(p+"/contact/",c["start"])}<div class="s-close-email"><a href="mailto:me@pancratzia.com">me@pancratzia.com</a><button type="button" data-copy-email>{c["emailCopy"]}</button><span role="status" class="s-copy-status"></span></div><span class="s-close-star" aria-hidden="true">*</span></div></section></main>'
 return main

def contact(lang):
 c=COPY[lang];p='/es' if lang=='es' else '';es=lang=='es'
 opts=''.join(f'<button type="button" class="s-project-choice" aria-pressed="false" data-brief="{escape(t,quote=True)}">{t}{arrow()}</button>' for t in c['contactTypes'])
 return f'''<main id="main" class="s-contact s-container"><div class="s-contact-heading"><p class="s-eyebrow">LET’S MAKE SOMETHING GOOD / HAGAMOS ALGO BUENO</p><h1>{c['contactTitle']}</h1><p>{c['contactIntro']}</p><div class="s-contact-social"><a href="https://webflow.com/@pancratzia" target="_blank" rel="noopener">Webflow ↗</a><a href="https://www.upwork.com/freelancers/~016a6410dfa02febf5?mp_source=share" target="_blank" rel="noopener">Upwork ↗</a><span>EN / ES · REMOTE</span></div></div><div class="s-brief"><h2>{c['choose']}</h2><div class="s-brief-options">{opts}</div><h3>{c['contactNext']}</h3><ul>{''.join('<li>'+item+'</li>' for item in c['contactItems'])}</ul><a class="s-button s-compose" href="mailto:me@pancratzia.com?subject=Let%E2%80%99s%20build%20a%20website">{c['emailButton']}{arrow()}</a><p class="s-contact-note">{c['emailNote']}</p><div class="s-close-email"><a href="mailto:me@pancratzia.com">me@pancratzia.com</a><button type="button" data-copy-email>{c['emailCopy']}</button><span role="status" class="s-copy-status"></span></div></div></main>'''

def main():
 for f in DIST.rglob('*.html'):
  if f.name=='sitemap.html':continue
  text=f.read_text();es=f.relative_to(DIST).parts[0]=='es';lang='es' if es else 'en';c=COPY[lang]
  relative=f.relative_to(DIST).as_posix();route='/'+(relative[:-10] if relative.endswith('index.html') else relative)
  other=route[3:] if es else '/es'+route
  text=re.sub(r'<header>.*?</header>',lambda m:header(lang,other),text,count=1,flags=re.S)
  text=re.sub(r'<footer>.*?</footer>',lambda m:footer(lang),text,count=1,flags=re.S)
  text=re.sub(r'<body\b[^>]*>','<body class="studio-site">',text,count=1)
  if relative in ('index.html','es/index.html'):
   text=re.sub(r'<main\b.*?</main>',lambda m:home(lang),text,count=1,flags=re.S)
   text=text.replace('class="studio-site"','class="studio-site studio-home"',1)
   text=re.sub(r'<title>.*?</title>','<title>'+escape(c['seoTitle'])+'</title>',text)
   for attr in ['name="description"','property="og:description"','name="twitter:description"']:
    text=re.sub(r'<meta '+attr+r' content="[^"]*">','<meta '+attr+' content="'+escape(c['seoDesc'],quote=True)+'">',text)
   for attr in ['property="og:title"','name="twitter:title"']:
    text=re.sub(r'<meta '+attr+r' content="[^"]*">','<meta '+attr+' content="'+escape(c['seoTitle'],quote=True)+'">',text)
  elif relative in ('contact/index.html','es/contact/index.html'):
   text=re.sub(r'<main\b.*?</main>',lambda m:contact(lang),text,count=1,flags=re.S)
  if '/studio.css' not in text:text=text.replace('</head>','<link rel="stylesheet" href="/studio.css"><script src="/studio.js" defer></script></head>')
  f.write_text(text)

if __name__=='__main__':main()
