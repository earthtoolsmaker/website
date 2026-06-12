# Privacy Policy Page — Design

**Date:** 2026-06-12
**Status:** Approved

## Goal

Add a privacy-policy page to the website, in the spirit of
https://www.hack-the-planet.io/privacy-policy/: short, plain-language,
transparent, and accurate to what the site actually does.

## Context: the site's actual data footprint

Audit of the codebase (2026-06-12):

- **Hosting:** Netlify serves the site; standard server logs process visitor
  IP addresses.
- **Contact forms:** Formspree powers the forms on `/contact/` and
  `/sponsor/` (name, email, message), delivered to us by email.
- **Google Fonts:** loaded from `fonts.googleapis.com`
  (`layouts/partials/head.html`); visitor IP is transmitted to Google.
- **jsDelivr CDN:** KaTeX assets for math rendering
  (`layouts/partials/math.html`).
- **Hugging Face Spaces:** the `hf_space` shortcode embeds Gradio apps from
  `*.hf.space` and loads `gradio.js` from AWS S3; the visitor's browser
  contacts those services directly.
- **No analytics** (`googleAnalytics` is empty), **no cookies set by the
  site**, Mailchimp newsletter and Disqus comments are disabled in
  `config.toml`.

## Decisions

- **Responsible party:** the policy names "EarthToolsMaker" informally and
  points readers to the `/contact/` page. No email or postal address is
  published, and no registered legal entity is named.
- **No cookie banner:** the site sets no cookies itself, so none is needed.

## Implementation

### Page

- `content/privacy-policy.md`, front matter `title: Privacy Policy` only.
- Rendered by the existing `layouts/_default/single.html` page branch
  (title + prose). No new layout, no new styles.
- A "Last updated: June 12, 2026" line appears at the top of the body — the page
  layout does not render front-matter dates, so it lives in the prose, as on
  the reference site.

### Navigation

- One new `[[menu.footer]]` entry in `config.toml`: name "Privacy Policy",
  url `/privacy-policy/`, weight 9 (after "Contact").
- Not added to the main navigation, matching the reference site.

### Content sections

1. **Intro** — one or two sentences: this is a static website; we collect no
   personal data ourselves, run no analytics, set no tracking cookies, show
   no ads.
2. **Hosting** — Netlify serves the site and processes IP addresses in
   standard server logs; link to Netlify's privacy policy.
3. **Contact and sponsor forms** — submissions (name, email, message) are
   processed by Formspree and delivered to us by email; used only to reply,
   never for marketing; link to Formspree's privacy policy.
4. **Embedded content and third-party resources** — Hugging Face Spaces
   demos, Google Fonts, and jsDelivr (KaTeX); the visitor's browser contacts
   these services directly, exposing their IP address; link to each
   provider's privacy policy.
5. **Your rights** — readers can ask what we hold about them (realistically:
   only form emails) and ask us to delete it, via the contact page.
6. **Contact** — questions about this policy go through `/contact/`.

## Verification

- `hugo` builds with no errors.
- `/privacy-policy/` renders with the site chrome, title, and all six
  sections.
- The footer of every page shows a "Privacy Policy" link after "Contact".
