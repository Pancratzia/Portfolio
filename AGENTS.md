# Pancratzia publishing

The production origin is https://www.pancratzia.com. Keep the Site public.

## GitHub Pages publication

The user selected `Pancratzia/Portfolio`, branch `main`, as the website's
GitHub repository. Every completed website change must be committed and pushed
there so `.github/workflows/pages.yml` can publish it. Publishing in ChatGPT
Sites alone is not completion of a request to update the GitHub Pages website.
Use `python scripts/build-pages.py --base-path /Portfolio` to validate the
preview URL, or no base path for the custom domain. Preserve existing GitHub
repository files outside the current `dist/`, scripts and deployment config.
Never publish secrets, repository credentials or generated `_site` output.

Before EVERY source packaging/publication, run `python scripts/prepare-site.py`
after page edits or generation. Pass it as an ordered command to the Sites
source workflow helper: `["python", "scripts/prepare-site.py"]`.
It installs GTM-MJ25B2CM and GA4 G-8PBFVMNNQS once per page, updates URLs to
the custom domain, and regenerates sitemap.xml and robots.txt from actual
HTML pages. It includes English and Spanish pages and omits noindex pages.
The tracked .openai/sitemap-state.json preserves lastmod for unchanged pages.
Never publish a hand-maintained sitemap or omit this preparation command.
Preparation also rebuilds localized 404.html pages from the latest shared
navigation/footer and generates browser-language routing in locale.js.
The explicit language selector preference always overrides browser detection.

The checked-in dist/ tree is the current deployable website. For small edits,
edit dist directly and update matching source templates where applicable.
Do not regenerate all pages with legacy build.py for unrelated small changes.
