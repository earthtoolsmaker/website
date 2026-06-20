# Click-to-expand blog images (desktop) — Design

**Date:** 2026-06-20
**Status:** Approved, ready for implementation plan

## Summary

Let readers click any content image in a blog post to view it fullscreen, on
desktop only. Carousels already have a custom fullscreen lightbox; this feature
extracts that lightbox into a single shared, page-level component and reuses it
for standalone (non-carousel) content images.

## Goals

- Click any standalone content image in a post body → open it fullscreen.
- Desktop only — no expand behavior on mobile / touch.
- Reuse the existing carousel lightbox look, keyboard model, and CSS. One
  pattern, not two.
- Zero edits required to the 161 existing post images.

## Non-goals

- No zoom/pan inside the fullscreen view (just a large image + caption).
- No change to carousel UX (arrows, counter, captions stay as they are).
- No new image-processing pipeline; we display the already-rendered `src`.
- Not targeting the post hero image (`post-image` / `page-image`) — it lives
  outside `.post__content` and already carries `no-lightense`.

## Decisions

| Decision | Choice |
|----------|--------|
| Scope | All standalone content images in the post body, automatic |
| Overlay | Reuse the carousel lightbox via a shared page-level extraction |
| Desktop gate | `(min-width: 768px) and (pointer: fine)` |
| Caption source | Image `alt` text |
| Opt-out | New `.no-zoom` class on an image |
| Refactor | Extract one shared lightbox; carousels re-point to it |

### Why alt text for captions

Survey of all post Markdown: 161 images, **0 with empty alt**, only **2 with a
title string**. Alt text is universally present and frequently descriptive
(full sentences describing diagrams and plots). It matches what the carousel
lightbox already uses (`img.alt`). Titles/figure captions are effectively
unused, so a separate caption code path is not worth it.

### Why a shared lightbox

Today the lightbox markup is emitted **per carousel** inside
`layouts/shortcodes/image_carousel.html`, and its JS lives **inside the
`.image-carousel` forEach loop** in `assets/js/common.js`. A page with no
carousel has no lightbox at all. To reuse it for single images without
duplicating it or enabling a second (Lightense) pattern, we extract one shared
lightbox rendered once per page that both carousels and single images feed.

## Architecture

### Components

**a. Shared lightbox partial** — `layouts/partials/image-lightbox.html`
The lightbox markup currently inline in `image_carousel.html` moves here, with a
single fixed id (`#page-lightbox`). Rendered once in the post layout
(`layouts/_default/single.html`), inside the post branch. Prev/next/counter
elements remain in the markup but are hidden in single-image mode (see CSS).

**b. Refactored carousel shortcode** — `layouts/shortcodes/image_carousel.html`
Stops emitting its own `image-lightbox` div. Carousel container markup is
otherwise unchanged.

**c. Generalized lightbox JS** — `assets/js/common.js`
Refactor so opening the lightbox is a reusable function parameterized by an
image list + starting index + mode (`gallery` vs `single`), rather than a
closure bound to one carousel. Carousels call it with their image list and
`gallery` mode (arrows + counter). Single images call it with a one-item list
and `single` mode (no arrows, no counter).

**d. Single-image wiring** — `assets/js/common.js`
After carousels initialize:
1. Evaluate the desktop gate:
   `window.matchMedia('(min-width: 768px) and (pointer: fine)').matches`.
   If false → attach no handlers and stop (mobile/touch get nothing).
2. Select `.post__content img`, excluding:
   - images inside `.image-carousel` (handled by carousel path),
   - images with `.no-zoom`,
   - images with `.no-lightense` (existing opt-out convention).
3. Attach a click handler to each remaining image that opens `#page-lightbox`
   in `single` mode using the image's resolved `src` and `alt` (caption).

**e. CSS affordance** — `assets/sass/3-modules/_image-carousel.scss` (or a small
companion module)
- Under `@media (min-width: 768px) and (pointer: fine)`, expandable content
  images get `cursor: zoom-in`.
- `single` mode hides `.image-lightbox__prev`, `.image-lightbox__next`, and
  `.image-lightbox__counter` (e.g. via a `is-single` modifier on the lightbox).
- The `lightbox-open` body class and existing overlay/backdrop styles are
  reused unchanged.

### Data flow

1. Page loads → shared `#page-lightbox` partial is in the DOM, hidden.
2. JS checks the desktop media query. Mobile/touch → no handlers, no zoom
   cursor, done.
3. Carousels init as today but feed the shared lightbox (gallery mode).
4. Standalone content images (minus carousel/opt-out images) get click handlers
   → open shared lightbox in single mode.
5. Open = set `src`/`alt`/caption, add `is-active` (+ `is-single` when single),
   add body `lightbox-open`. Esc / overlay click / close button dismiss.

## Edge cases

- **`#noround` / fragment-marked images** — normal `<img>`; expand fine, show
  full-res source.
- **SVG diagrams** (pipelines, system diagrams) — expand and scale cleanly; a
  genuine win for fullscreen.
- **Lazy-loaded images** — loaded by click time; we use the resolved `src`.
- **Post hero image** — outside `.post__content`, already `no-lightense`; not
  targeted.
- **Images wrapped in links** — if any content image is inside an `<a>`, the
  link takes precedence; do not attach expand there (avoid hijacking
  navigation). Verify during implementation whether any exist.

## Testing

Manual, on the running site:
- **Desktop wide:** click a standalone image in an image-heavy post (e.g.
  forest-fire or trout post) → opens fullscreen, no prev/next/counter; Esc,
  overlay click, and close button all dismiss.
- **Carousel unchanged:** a post with a carousel still opens the gallery
  lightbox with arrows + counter, sharing the same overlay.
- **Opt-out:** an image tagged `.no-zoom` does not expand and shows no zoom
  cursor.
- **Mobile/touch:** emulate touch or narrow the viewport below 768px → clicking
  a content image does nothing; no zoom cursor.

Build:
- `hugo` builds clean.
- Run locally and verify one image-heavy post and one carousel post.

## Files touched

- `layouts/partials/image-lightbox.html` (new)
- `layouts/_default/single.html` (render shared lightbox in post branch)
- `layouts/shortcodes/image_carousel.html` (drop inline lightbox div)
- `assets/js/common.js` (generalize lightbox fn; wire single images + desktop
  gate)
- `assets/sass/3-modules/_image-carousel.scss` (zoom-in cursor, single-mode
  hiding)
- Documentation note for authors on the `.no-zoom` opt-out.
