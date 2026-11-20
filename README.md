# Pancratzia

Laura Ortega's portfolio: Webflow Certified Partner, web designer and developer.

**Live site:** https://www.pancratzia.com

## About

Pancratzia presents Laura's services, selected client work, pricing and contact details. The site is fully bilingual: English pages live at the root and Spanish pages live under `/es/`, with a language switcher that links each page to its translation. Contact is email-first: the contact form opens a pre-filled draft in the visitor's email app.

## Stack

- Static HTML, CSS and vanilla JavaScript. There is no framework and no build step.
- [GSAP](https://gsap.com) 3.13 with ScrollTrigger for motion, served locally from `site/assets/`.
- Self-hosted Manrope and Instrument Serif fonts (`.woff2`, licenses included).
- WebP images and per-page Open Graph share cards.
- Google Tag Manager and Google Analytics 4, loaded only after the visitor accepts the cookie banner (`site/assets/consent.js`, Google Consent Mode).
- GitHub Pages with a custom domain, deployed through GitHub Actions.

## Run locally

Any static file server works. From the repository root:

```bash
python3 -m http.server 8000 --directory site
```

Then open http://localhost:8000. Pages use root-relative asset paths, so serve the `site/` folder as the web root instead of opening files directly.

## Deployment

Every push to `main` runs `.github/workflows/pages.yml`, which uploads the `site/` folder as-is and publishes it to GitHub Pages. The custom domain `www.pancratzia.com` is set in the repository's Pages settings and in `site/CNAME`. `pancratzia.com` redirects to `www`.

## Structure

```
site/
├── index.html             Home (EN)
├── about/ contact/ pricing/ work/
├── services/              Service hub and one folder per service
├── es/                    Spanish pages (sobre-mi, contacto, precios, proyectos, servicios/…)
├── assets/                CSS, JS, GSAP, fonts, images, share cards
├── 404.html               English 404 (es/404.html for Spanish)
├── sitemap.xml, robots.txt
└── CNAME, .nojekyll
.github/workflows/pages.yml  GitHub Pages deployment
```

## Contact

- Email: [me@pancratzia.com](mailto:me@pancratzia.com)
- LinkedIn: [linkedin.com/in/leortegaperez](https://www.linkedin.com/in/leortegaperez/)
- Webflow Partner profile: [webflow.com/@pancratzia](https://webflow.com/@pancratzia)
