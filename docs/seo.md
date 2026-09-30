# SEO and Social Sharing

What search engines and social scrapers read from the site, where each piece
lives, and how to change it. Read this before touching titles, descriptions,
share images, favicons, structured data or the sitemap.

---

## 1. Where things live

| What | File |
|---|---|
| `<title>`, meta description, canonical, Open Graph, Twitter Card, `article:*` | `layouts/partials/seo/meta.html` |
| JSON-LD (Organization, WebSite, Article) | `layouts/partials/seo/schema.html` |
| Favicon and manifest links | `layouts/partials/head.html` |
| Site description, tagline, default share image, JSON-LD logo | `config.toml` (`params.description`, `params.tagline`, `params.seo`) |
| Default share card | `assets/images/og/og-default.svg` (source) and `og-default.png` (served) |
| Favicons | `static/favicon.ico` and `static/favicon/` |
| Web manifest | `static/favicon/site.webmanifest` |
| robots.txt | `layouts/robots.txt` (`enableRobotsTXT = true`) |
| Sitemap | Hugo built-in, `/sitemap.xml` |
| Old URL redirects | `netlify.toml` `[[redirects]]` (301) |

## 2. Titles

One expression feeds `<title>`, `og:title` and `twitter:title`:

- Home: `earthtoolsmaker | <params.tagline>`
- Every other page: `<Title> | earthtoolsmaker`

Google uses `<title>` as the blue result link. Keep the tagline short (under
about 60 characters with the brand) and in the site's current wording.

## 3. Descriptions

`meta description`, `og:description` and `twitter:description` share one
fallback chain:

1. front matter `description`
2. front matter `hero_description` (HTML stripped)
3. Hugo `.Summary` (first words of the body)
4. `params.description` in `config.toml`

Rules:

- Every section index and top-level page should have a `description` or a
  `hero_description`. Falling through to `.Summary` gives Google a random
  sentence from the body.
- Aim for 120 to 160 characters. Google cuts snippets around 160; the site
  description is longer on purpose and reads fine when cut.
- Follow the voice rules in `docs/design-guidelines.md` (lowercase
  `earthtoolsmaker`, no em-dashes, no emoji).

## 4. Share images

- A page with front matter `image:` shares that image, cropped by Hugo to
  1200x630 (`.Fill "1200x630 jpg q85"`). The path is asset-relative with a
  leading slash, e.g. `/images/posts/<slug>/cover.png`.
- Every other page shares the default card, `params.seo.default_image`.
- `twitter:card` is always `summary_large_image`, so images must read well at
  1.91:1. Never use a wide wordmark or a small square logo as a share image.

### Default card

`assets/images/og/og-default.svg` is the source: the pangolin icon in a white
disc, `earthtoolsmaker`, the tagline with the teal italic accent, and
`earthtoolsmaker.org` in gray, on the white to pale-teal gradient used by blog
covers. Editing the SVG changes nothing on the site until the PNG is
re-rendered.

To re-render, use the blog-cover recipe: inline the SVG in an HTML page (an
`<img>` SVG cannot load web fonts), load Mulish and Newsreader from Google
Fonts with `display=block`, force `svg text{font-variation-settings:"opsz" 16}`,
rewrite the `../logos/etm-logo.png` href to a local copy, then screenshot with
headless chromium at 1200x630 (`--virtual-time-budget=6000`). Snap chromium can
only write under `$HOME`.

## 5. Structured data (JSON-LD)

- **Organization** on every page: name, URL, `params.description`, `sameAs`
  from `params.social`, and `logo` from `params.seo.logo`.
- **WebSite** on the home page: its `name` is the site name Google shows above
  the result.
- **Article** on blog posts, with the square logo as publisher logo.

The logo is the square pangolin (`assets/images/logos/etm-logo.png`), not the
wordmark: Google wants a square logo.

## 6. Favicons and manifest

Google shows the favicon next to the result. It fetches the icons declared in
`<head>` and falls back to `/favicon.ico` at the site root.

- `static/favicon.ico` and `static/favicon/favicon.ico` must be the same file.
  A stale root `.ico` kept the old tree icon in Google results until 2026-09.
- Declared icons: `/favicon.ico` (`sizes="any"`), a 192px PNG (Google wants a
  square icon that is a multiple of 48px), and the 32px and 16px PNGs.
- `site.webmanifest` icon paths are absolute and include `/favicon/`.

When the icon changes, regenerate every file in `static/favicon/`, then copy
the new `favicon.ico` to `static/`.

## 7. Sitemap and indexing

- Every built page is listed in `/sitemap.xml`. Delete theme demo or
  placeholder pages rather than leaving them in the build (e.g. `/elements/`,
  removed in #210).
- When a section moves, add a 301 in `netlify.toml` so old links and old
  sitelinks follow it (e.g. `/spaces/*` to `/demos/:splat`).
- Sitelinks are chosen by Google and cannot be set. The best levers are clear
  menu pages with good descriptions and no stray pages in the sitemap.

## 8. After a deploy

Search results only change after Google recrawls:

| Change | Typical delay |
|---|---|
| Title and description | a few days (1 to 3 with "Request indexing") |
| Removed page | days to a couple of weeks |
| Favicon | several days to a few weeks |
| Sitelinks | weeks |
| LinkedIn / Slack card | about 7 days of cache; LinkedIn Post Inspector refreshes it at once |

To speed it up, in Google Search Console: URL Inspection, then "Request
indexing" for the home page and the main menu pages; resubmit `sitemap.xml`
under Sitemaps.

## 9. Checking changes locally

Build to a fresh directory and grep the tags:

```bash
hugo --quiet --ignoreCache -d ~/etm-shots/site
grep -o '<title>[^<]*</title>\|<meta [^>]*\(og:\|twitter:\|name="description"\)[^>]*>' ~/etm-shots/site/index.html
```

Check a live deploy preview with LinkedIn Post Inspector or opengraph.xyz.
