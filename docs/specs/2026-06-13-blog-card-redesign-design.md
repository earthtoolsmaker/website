# Blog Card Redesign

**Date:** 2026-06-13
**Status:** Approved

## Problem

The blog post cards (homepage blog section and `/posts` listing) feel dark and
overpacked. Each card overlays the date, read time, and a row of tag pills
directly on the cover image, which requires two dark gradient overlays plus a
50% grayscale filter on the photo to keep the white text legible. The result is
muddy, dim imagery and a card crowded with competing information.

## Goal

A lighter, calmer, more editorial card: a clean full-color photo and a clear
text block beneath it. Less information per card, better visual hierarchy.

## Decisions

- **Image:** clean and full color. Remove both dark gradient overlays and the
  grayscale filter. Keep the current landscape aspect ratio and rounded corners.
- **Removed entirely:** read time (`· N min read`), tags, and the
  date/tags-on-image overlays.
- **Moved below the image:** the date, shown as quiet muted text.
- **Layout direction:** white/light bordered card panel wrapping image + text
  (the "minimal + accent" direction), with a thin terracotta accent rule on the
  title.

## Design

### Card structure (top to bottom), all inside one bordered panel

1. **Cover image** — full color, no overlays, no grayscale. Rounded corners,
   current landscape ratio preserved.
2. **Title** — Newsreader serif, weight 600, **18px**, line-height ~1.2, with a
   **3px terracotta left accent rule** (`--tertiary-color`), ~12px left padding.
3. **Excerpt** — Mulish, ~14.5px, muted gray, clamped to **2 lines**.
4. **Date** — ~12.5px, weight 600, muted gray (e.g. `12 Jun, 2026`).

### Panel styling

- Surface, border, and text colors map to existing brand CSS variables so the
  card adapts to the site's dark-mode toggle:

  | Element        | Light (value)      | Dark (value) | Variable                  |
  |----------------|--------------------|--------------|---------------------------|
  | Card surface   | near-white `#fbf6f6` | `#1a1a1f`  | `--background-alt-color`  |
  | Border (1px)   | sand `#ede0d4`     | `#252629`    | `--border-color`          |
  | Title          | `#161616`          | `#f0f0f0`    | `--heading-font-color`    |
  | Excerpt / date | `#60626a`          | `#9e9e9e`    | `--text-alt-color`        |
  | Accent rule    | terracotta `#e29578` | (same)     | `--tertiary-color`        |

- Soft shadow `0 6px 26px rgba(0, 0, 0, .05)`, border-radius 16px, padding 14px.

### Hover

- Keep the existing lift (`transform: translateY(...)`).
- Whole card remains clickable via the title link's full-card `::after` overlay.

## Files touched

- `layouts/partials/article.html` — restructure markup: wrap image + text in one
  panel; drop the `article__meta` (date/read-time) overlay, the
  `article-tags__box` overlay, and the read-time span; render the date beneath
  the title/excerpt instead.
- `layouts/partials/related-posts.html` — the "You may also like" cards on post
  pages reuse the same `article__` classes, so apply the identical markup
  restructure here for visual consistency (and to avoid emitting now-unstyled
  overlay/tag markup).
- `assets/sass/3-modules/_article.scss` — restyle per above; remove the image
  gradient `::before` overlay and the grayscale filter rules; remove now-unused
  overlay/tag styles.

Grid columns (`col-4 col-w-6 col-t-12` for the blog grid, `col-6 col-t-12` for
related posts) and the blog section partial are unchanged.

## Out of scope

- Tag/category display on cards (tags remain accessible on the post page itself).
- Project cards (`project-card.html`) and other card types.
