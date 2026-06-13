# Project cards match blog cards — design

**Date:** 2026-06-13
**Status:** Approved

## Goal

Make project cards visually identical to blog post cards (`.article__*`). Today
the two card systems diverge: blog cards are a unified bordered/shadowed
container with a left-accent 18px title, a 2-line clamped excerpt, and a small
date footer; project cards have no outer container, a tan `#ede0d4` box around a
grayscaled image, a gradient subtitle, a 32px title, a 3-line excerpt, and no
date.

The user chose a **full match** (project cards become structurally the same as
blog cards) implemented via **reuse** of the existing blog card markup.

## Approach: reuse the blog card

Project card templates emit the existing `.article__*` markup instead of
`.project__*`. The now-unused `.project__*` card SCSS is deleted. This gives a
single source of truth — projects can never drift from blog cards — and fits the
existing pattern where `.article__*` is already shared across three templates
(`article.html`, `related-posts.html`, and the `article_card` shortcode);
project cards become the fourth consumer.

## Changes

1. **`layouts/partials/project-card.html`** — rewrite to mirror
   `layouts/partials/article.html`, emitting `.article__*` markup, with project
   field mappings:
   - image ← `.Params.Image`
   - title / link ← `.Title` / `.RelPermalink`
   - excerpt ← `.Params.summary` (blog cards use `.Params.description`)
   - **no date block, no subtitle** — full match drops both, so there is no
     footer line.
   - Note: the desktop grayscale / color-on-hover image effect is already shared
     by both card types in `_lazy-images.scss` (it targets `.article__image` and
     `.project__image` together), so reusing `.article__*` inherits the exact
     blog-card image treatment — the tan box is dropped, the grayscale stays and
     matches blog cards.

2. **`layouts/shortcodes/project_card.html`** — rewrite to mirror
   `layouts/shortcodes/article_card.html`, emitting `.article__*`:
   - excerpt ← `.Get "excerpt"`
   - keep the in-prose link reset (`border-bottom: none; font-weight: inherit`)
     since the shortcode renders inside tool/prose content
   - no date.

3. **`layouts/projects/list.html`** (the `/projects` index) — this third surface
   renders cards inline with `.project__*` markup. Replace the inline
   `<article class="project …">…</article>` block with
   `{{ partial "project-card.html" . }}` so it shares the same (now blog-styled)
   card.

4. **`assets/sass/3-modules/_projects.scss`** — delete the unused `.project__*`
   card styles and remove its `@import` from the SASS entrypoint
   (`assets/sass/main.scss`). The single-project page uses `.project-*`
   (hyphenated) which is separate and untouched.

5. **`assets/sass/3-modules/_lazy-images.scss`** — remove the now-dead
   `.project__image` / `.project__content` selectors (orphaned once no card emits
   `.project__*`); the parallel `.article__*` selectors remain and cover the
   converted cards.

## Out of scope / deliberately unchanged

- **Section wrappers** (`section-projects.html`, `support.html`) — they already
  drop cards into a `.row` with no project-specific assumptions, and each card
  brings its own column classes. Blog uses `row grid`; section layout is not
  touched, only the cards.
- **Single-project page layout** (`assets/sass/4-layouts/_project.scss`,
  `.project-*`).

## Verification

1. Static `hugo` build succeeds.
2. Chromium screenshot of the homepage projects section and the support page,
   confirming cards match the blog cards (static build is ground truth per the
   local-preview workflow).
