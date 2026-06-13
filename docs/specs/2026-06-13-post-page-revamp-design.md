# Post Page Revamp — Design

**Date:** 2026-06-13
**Status:** Approved
**Scope:** Individual blog post pages (`content/posts/*`), rendered by the post branch of `layouts/_default/single.html`.

## Goal

Revamp the individual post reading experience: restyle tags, add a table-of-contents outline, and refresh the overall UI into a left-aligned editorial layout. Keep the clean single-column reading column (780px).

Only the **post branch** of `_default/single.html` changes (the `eq .Section "post"/"posts"` block). The non-post page branch is left untouched.

## Decisions (validated via visual brainstorming)

- **Layout:** Single centered 780px column, left-aligned editorial header. Outline is an inline collapsible box at the top of the article (not a sticky sidebar).
- **Tags:** Kicker line — uppercase, letter-spaced, dot-separated clickable links above the title.
- **No reading-progress bar.**

## Components

### 1. Tags — kicker line

Replace the current top pill chips (`.post-tags` / `.post__tag`) with an uppercase, letter-spaced, dot-separated row of links rendered **above** the title.

- Brand purple (`--primary-color`).
- Each tag links to its term page, using the existing `$.GetTerms "tags"` iteration (`.Permalink` / `.LinkTitle`).
- Dot (`·`) separators between tags, rendered via CSS (e.g. `::after` on items) so markup stays clean.
- `text-transform: uppercase`, small `letter-spacing`, bold weight.
- Hidden entirely when the post has no tags.

### 2. Meta row

Left-aligned `date · author · reading time`.

- Replace the literal `/` separators with dot separators (`·`), matching the kicker style.
- Keep the author link to `/about/` and `.ReadingTime` "min read".
- Rendered below the title (title → description → meta), left-aligned.

### 3. Outline box — "On this page"

New partial `layouts/partials/post-toc.html`, included after the cover image and before `.post__content`.

- Source: Hugo's built-in table of contents (`.TableOfContents`), configured for `##`–`###` only.
- Container: boxed, rounded, light background, **purple left-border** accent. Heading label "On this page" in uppercase.
- Built on native `<details>`/`<summary>` so it is collapsible:
  - **Open by default on desktop.**
  - **Collapsed by default on mobile** — a small inline `matchMedia` script removes the `open` attribute below the mobile breakpoint on load.
- `##` items flush, `###` items indented; styling overrides Hugo's default `#TableOfContents ul/li` markup.
- **Render guard:** only show when the post has ≥2 headings (check `.TableOfContents` is non-empty / fragment count). Posts with no/one heading show nothing.
- Anchor navigation uses Goldmark's auto-generated heading IDs. Smooth scrolling via CSS `scroll-behavior: smooth` (scoped, with a `scroll-margin-top` on headings so anchors aren't hidden under any fixed header).

### 4. Cover & header

- Header text block left-aligned (currently centered max-width block).
- Cover image keeps its rounded treatment (`.post-image`) and optional caption.
- Header order: kicker tags → title → description → meta → cover → outline.

### 5. Body typography (`.post__content` only)

Polish the reading experience without changing markup the content authors write:

- Heading rhythm/spacing (`h2`, `h3`, `h4`) for clearer section breaks.
- Links, blockquotes (note the `<cite>` convention used in posts), inline `code` and fenced code blocks, list spacing.
- Scoped strictly to `.post__content`; the `.page__content` branch is not affected.

### 6. Footer — share + prev/next

- Restyle `layouts/partials/share-buttons.html` (`.post__share`) and `layouts/partials/post-navigation.html` (`.post__navigation`) to match the editorial look.
- Functionality (links, share targets) unchanged.

### 7. Related posts

- Restyle the "You may also like" cards (`layouts/partials/related-posts.html`) to match.
- **Constraint:** `.article__*` styles are shared by three templates (`article.html`, `related-posts.html`, and the `article_card` shortcode). Any change to shared `.article__*` rules must be verified against all three; prefer a wrapper-scoped override (e.g. under `.related-posts`) over editing shared classes.

## Files touched

- `layouts/_default/single.html` — post-branch header markup (kicker tags, meta separators, left alignment), include the outline partial.
- `layouts/partials/post-toc.html` — **new** outline box partial.
- `assets/sass/4-layouts/_post.scss` — all post styling (kicker, meta, outline, header alignment, body typography, share/nav refresh).
- `layouts/partials/post-navigation.html`, `layouts/partials/share-buttons.html` — light markup tweaks if needed for restyle.
- `layouts/partials/related-posts.html` — restyle, respecting the shared-class constraint.
- `config.toml` — verify/add `markup.tableOfContents` (`startLevel = 2`, `endLevel = 3`); verify Goldmark heading-ID generation.

## Non-goals

- No sticky sidebar / scroll-spy outline.
- No reading-progress bar.
- No changes to the non-post page layout, post list page, or post front matter.
- No heavy JS — native `<details>` plus a few lines for mobile default and (optional) smooth scroll.

## Verification

- `hugo` builds with no errors/warnings.
- Spot-check rendered output (static build is ground truth — local `hugo server` can serve stale pages) on several posts: one with many headings (e.g. `how-to-analyze-elephant-rumbles-at-scale`), one with tags, and one short post to confirm the outline render-guard.
- Confirm desktop (outline open) vs. mobile (outline collapsed) behavior.
- Confirm related-posts restyle did not regress the other two `.article__*` consumers.
