# Pancratzia website

The current website lives in `dist/`. It is static HTML, CSS, JavaScript and
local images. `scripts/prepare-site.py` prepares analytics, language detection,
localized error pages, sitemap and robots.txt. It keeps unchanged sitemap dates.

## GitHub Pages

The production repository is `Pancratzia/Portfolio`, branch `main`.
Choose **Settings → Pages → Build and deployment → Source: GitHub Actions**.
Every push to `main` runs `.github/workflows/pages.yml` and publishes `_site`.
The workflow supports the default `/Portfolio/` URL and a custom domain.
The older React/Vite files are retained for history and are not part of this
workflow's build. Do not run their npm build to regenerate the current website.

For a local check:

```sh
python -m pip install -r requirements-pages.txt
python scripts/build-pages.py --base-path /Portfolio
```

## Future changes from ChatGPT

Edit the current `dist/` pages and matching scripts. Run preparation and checks,
then commit and push those changes to `Pancratzia/Portfolio:main`. GitHub Actions
handles the website deployment. A publication to ChatGPT Sites alone does not
update GitHub; the source must also be pushed to this repository.

The public origin in SEO metadata is `https://www.pancratzia.com`.
Configure the custom domain in GitHub Pages after checking the preview, then
replace the website DNS records in Spaceship. Preserve email MX/TXT records.
