<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9" exclude-result-prefixes="s">
  <xsl:output method="html" encoding="UTF-8" doctype-system="about:legacy-compat"/>
  <xsl:template match="/">
    <html lang="es">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <meta name="robots" content="noindex,follow"/>
        <title>Sitemap | Pancratzia</title>
        <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"/>
        <style>
          *{box-sizing:border-box}body{margin:0;background:#faf7fd;color:#493753;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.6}main{max-width:1120px;margin:0 auto;padding:60px 32px 48px}a{color:#7548ad;text-underline-offset:4px}a:focus-visible{outline:3px solid #7548ad;outline-offset:5px;border-radius:3px}.brand{font-size:21px;font-weight:750;text-decoration:none;letter-spacing:-.6px}.intro{margin:38px 0 30px}.eyebrow{color:#846294;font-size:12px;letter-spacing:2px;text-transform:uppercase}h1{font-size:clamp(36px,6vw,56px);line-height:1.15;letter-spacing:-2px;margin:10px 0 18px;font-weight:650}.intro p{max-width:640px;margin:0;font-size:16px;color:#786582}.summary{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;margin:30px 0 18px}.count{display:inline-flex;align-items:center;gap:9px;font-size:14px}.count b{font-size:24px;color:#7548ad}.domain{font-size:14px}.table-wrap{overflow-x:auto;background:#fff;border:1px solid #e7d9ef;border-radius:16px;box-shadow:0 12px 36px #60378408}table{border-collapse:collapse;width:100%;min-width:620px;text-align:left}th{padding:18px 24px;background:#f1e8f8;color:#6c467f;font-size:12px;font-weight:650;letter-spacing:1px;text-transform:uppercase}td{padding:18px 24px;border-top:1px solid #f0e7f5;font-size:14px;vertical-align:middle}tbody tr:hover{background:#fcf9ff}td:first-child{width:65%}.url{display:block;color:#664285;font-weight:550;overflow-wrap:anywhere;text-decoration:none}.url:hover{text-decoration:underline}.url small{display:block;color:#9a89a4;font-size:11px;font-weight:400;margin-top:3px}.language{display:inline-block;background:#f1e8f8;color:#7548ad;border-radius:30px;padding:4px 11px;font-size:11px;font-weight:650;letter-spacing:.7px}time{white-space:nowrap;color:#80688d;font-variant-numeric:tabular-nums}.foot{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;margin-top:26px;color:#8b7797;font-size:13px}.foot p{margin:0;max-width:610px}.foot a{white-space:nowrap}@media(max-width:600px){main{padding:32px 18px}.intro{margin-top:28px}h1{letter-spacing:-1.4px}.summary{align-items:flex-start;flex-direction:column;gap:8px}th,td{padding:16px 20px}.foot{gap:16px}}
        </style>
      </head>
      <body>
        <main>
          <a class="brand" href="https://www.pancratzia.com/">pancratzia.</a>
          <div class="intro">
            <span class="eyebrow">Mapa del sitio</span>
            <h1>Todo en un lugar.</h1>
            <p>Páginas públicas de Pancratzia, organizadas por dirección, idioma y última actualización.</p>
          </div>
          <div class="summary">
            <span class="count"><b><xsl:value-of select="count(s:urlset/s:url)"/></b> páginas indexables</span>
            <a class="domain" href="https://www.pancratzia.com/">www.pancratzia.com</a>
          </div>
          <div class="table-wrap">
            <table>
              <thead><tr><th scope="col">Página</th><th scope="col">Idioma</th><th scope="col">Actualización</th></tr></thead>
              <tbody>
                <xsl:for-each select="s:urlset/s:url">
                  <tr>
                    <td><a class="url" href="{s:loc}"><xsl:value-of select="substring-after(s:loc, 'https://www.pancratzia.com')"/><small>www.pancratzia.com</small></a></td>
                    <td><span class="language"><xsl:choose><xsl:when test="starts-with(s:loc, 'https://www.pancratzia.com/es/')">ES</xsl:when><xsl:otherwise>EN</xsl:otherwise></xsl:choose></span></td>
                    <td><time datetime="{s:lastmod}"><xsl:value-of select="s:lastmod"/></time></td>
                  </tr>
                </xsl:for-each>
              </tbody>
            </table>
          </div>
          <div class="foot">
            <p>Este mapa se actualiza con cada publicación del sitio. Las páginas de confirmación se excluyen de la indexación.</p>
            <a href="/sitemap.html">Ver versión HTML ↗</a>
            <a href="/sitemap.xml">Archivo XML ↗</a>
          </div>
        </main>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
