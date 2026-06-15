# Technical SEO — Design Spec

**Date:** 2026-06-15
**Status:** Approved (design)
**Scope:** Technical SEO only, implemented this engagement. No keyword research, no
content rewriting, no analytics/tracking, no performance refactor.

## Goal

Help conservation NGOs and funders discover EarthToolsMaker through organic search.
The single highest-leverage lever for this is **structured data that establishes
EarthToolsMaker as a recognizable entity** (Organization) plus clean, non-redirecting
canonical URLs and rich SERP metadata for projects and blog posts.

## Context (current state)

Hugo static site, deployed on Netlify. SEO basics already present in
`layouts/partials/head.html`:

- ✅ `<title>`, meta description, Open Graph, Twitter cards, favicon, manifest, RSS
- ✅ Hugo auto-generates `/sitemap.xml`
- ✅ 13 blog posts, 14 projects — real content to mark up
- ❌ No `<link rel="canonical">`
- ❌ No JSON-LD structured data (Organization / WebSite / Article / BreadcrumbList)
- ❌ No `robots.txt`
- ❌ Meta description in the `<title>`-adjacent tag has no fallback — pages without an
  explicit `description` emit an empty `<meta name="description">`
- ❌ Missing `og:type`, `og:url`, `og:site_name`, `og:locale`; no `article:*` tags on posts
- ❌ OG/Twitter image has no default fallback for pages with no `image`
- ⚠️ **Canonical domain mismatch:** `config.toml` `baseURL` is `https://earthtoolsmaker.org`,
  but the live site 301-redirects that to `https://www.earthtoolsmaker.org`. Hugo therefore
  emits canonicals, sitemap entries, and OG URLs that all get redirected.

## Decisions

- **Canonical domain: `https://www.earthtoolsmaker.org/`** (verified: non-www 301s to www).
  Fix `baseURL` in `config.toml` accordingly.
- **Implementation approach: dedicated SEO partials.** Extract SEO concerns out of
  `head.html` into focused partials rather than inlining everything. Each partial has one
  clear purpose and can be reasoned about in isolation.

## Architecture

```
layouts/partials/head.html          # slimmed: calls the two SEO partials
layouts/partials/seo/meta.html      # title, description, canonical, OG, Twitter, article:*
layouts/partials/seo/schema.html    # JSON-LD: Organization, WebSite, Article, BreadcrumbList
layouts/robots.txt                  # robots.txt template (enabled via config)
config.toml                         # baseURL fix + Organization sameAs params
```

`head.html` keeps ownership of non-SEO concerns (favicons, fonts, CSS pipeline, theme
script, math). It delegates all SEO output to `seo/meta.html` and `seo/schema.html` via
`{{ partial "seo/meta.html" . }}` and `{{ partial "seo/schema.html" . }}`.

### Unit responsibilities

| Unit | Does | Depends on |
|------|------|-----------|
| `seo/meta.html` | Emits `<title>`, description, canonical, all OG + Twitter tags, `article:*` on posts | `.Permalink`, `.Description`/`.Summary`, `.Params.image`, site params |
| `seo/schema.html` | Emits one or more `<script type="application/ld+json">` blocks, type-aware | page kind, site Organization params |
| `robots.txt` | Allows all, points to sitemap | `.Site.Home.Permalink` |

## Detailed behavior

### 1. JSON-LD structured data (`seo/schema.html`)

- **Organization** — emitted sitewide. Fields: `name`, `url`, `logo` (absolute), `description`,
  `sameAs` array (GitHub, LinkedIn, HuggingFace org URLs). Driven by new
  `[params.organization]` config so links live in one place.
- **WebSite** — emitted on the homepage only. Fields: `name`, `url`.
- **Article** — emitted on blog posts (`content/posts/`). Fields: `headline`, `image`,
  `datePublished`, `dateModified`, `author` (Organization), `mainEntityOfPage`.
- **BreadcrumbList** — emitted on nested pages (posts, projects, tools, spaces) reflecting
  the section → page hierarchy, for richer SERP breadcrumbs.

All URLs absolute (`absURL`/`.Permalink`). JSON built with Hugo's `jsonify`/`dict` so output
is always valid JSON (no hand-built string interpolation).

### 2. Canonical & robots

- `seo/meta.html` emits `<link rel="canonical" href="{{ .Permalink }}">` on every page.
- `layouts/robots.txt` (with `enableRobotsTXT = true` in config) outputs:
  ```
  User-agent: *
  Allow: /
  Sitemap: https://www.earthtoolsmaker.org/sitemap.xml
  ```

### 3. Meta-tag hardening (`seo/meta.html`)

Centralize the description expression with a single fallback chain used by the description
meta, `og:description`, and `twitter:description`:

```
description = .Description | default .Summary | default .Site.Params.description
```

- Add `og:type` = `article` on posts, `website` elsewhere.
- Add `og:url` (= canonical), `og:site_name` (= site title), `og:locale` (from `languageCode`).
- Add `article:published_time`, `article:modified_time`, `article:author` on posts.
- OG/Twitter image: use page `image` when present, else a site-wide default share image
  (`params.hero.hero__image` / a designated default), always `absURL`.

### 4. Config changes (`config.toml`)

- `baseURL = "https://www.earthtoolsmaker.org/"`
- `enableRobotsTXT = true`
- New `[params.organization]` block: `sameAs` URLs + default share image reference.

## Out of scope (explicitly)

- Keyword research, content/title/description rewriting per page
- Analytics, Google Search Console, or any tracking
- Performance / Core Web Vitals refactor (render-blocking fonts, etc.) — possible later phase
- Image `alt`-text audit (content task)

## Verification

Build-based, no live deploy needed:

1. `hugo` builds cleanly (no template errors).
2. Inspect generated `public/`:
   - Homepage `index.html` contains Organization + WebSite JSON-LD, canonical = www URL.
   - A blog post contains Article + BreadcrumbList JSON-LD, `og:type=article`, `article:*` tags.
   - A page with no `description` now emits a non-empty description meta (fallback works).
   - `public/robots.txt` exists and references the www sitemap.
   - `public/sitemap.xml` URLs are all `https://www.earthtoolsmaker.org/...`.
3. Validate one homepage + one post JSON-LD blob parses as valid JSON.

## Success criteria

- All four schema types emit on the correct page kinds with valid JSON.
- Canonical, OG `url`, and sitemap all use the www domain — zero redirected canonicals.
- No page emits an empty description meta.
- `head.html` no longer contains inline SEO logic beyond the two partial calls.
