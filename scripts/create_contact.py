"""Keep contact pages focused on direct email, without a submission backend."""
from pathlib import Path
import re

DIST = Path(__file__).resolve().parents[1] / 'dist'


def contact_card(es=False):
    eyebrow = 'DIRECTO A MI CORREO' if es else 'STRAIGHT TO MY INBOX'
    title = 'Cuéntame tu<br><em>idea.</em>' if es else 'Tell me about<br><em>your idea.</em>'
    copy = 'Escríbeme con los detalles de tu proyecto. Para empezar, puedes incluir:' if es else 'Email me with your project details. A good starting point is:'
    items = ['Tu negocio y sitio actual, si tienes uno.', 'Qué necesitas crear o mejorar.', 'Plataforma, alcance y fechas que tienes en mente.'] if es else ['Your business and current website, if you have one.', 'What you want to build or improve.', 'Your preferred platform, scope and timeline.']
    write = 'Escribirme por correo' if es else 'Send me an email'
    note = 'Este enlace abre tu aplicación de correo. También puedes copiar la dirección y escribir desde tu correo habitual.' if es else 'This link opens your email app. You can also copy the address and write from your usual inbox.'
    return f'''<aside class="direct-contact" id="contact-options"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2><p>{copy}</p><ul>{''.join('<li>'+item+'</li>' for item in items)}</ul><a class="button contact-email" href="mailto:me@pancratzia.com">{write} <span>↗</span></a><a class="direct-contact-address" href="mailto:me@pancratzia.com">me@pancratzia.com</a><p class="direct-contact-note">{note}</p></aside>'''


def remove_forms():
    for es, path in [(False, DIST/'contact/index.html'), (True, DIST/'es/contact/index.html')]:
        text = path.read_text()
        text = re.sub(r'<form\b.*?</form>', lambda m: contact_card(es), text, flags=re.S)
        path.write_text(text)


if __name__ == '__main__':
    remove_forms()
