# 404 page: sticky footer + animated pangolin

Date: 2026-06-15

## Problem

1. On short pages (the 404 page being the clearest case), the footer is not pinned
   to the bottom of the viewport — it floats up directly under the sparse content,
   leaving empty space below it.
2. The 404 page is plain. Adding the site's pangolin mascot (the brandmark logo),
   animated, makes the dead-end page feel intentional and on-brand.

## Part 1 — Sticky footer (all short pages)

`layouts/_default/baseof.html` lays the body out as
`header → main.content → subscribe → footer` with no mechanism to push the footer
down when content is short.

**Fix** (`assets/sass/2-base/_base.scss`):

```scss
body { display: flex; flex-direction: column; min-height: 100vh; }
.content { flex: 1 0 auto; } // <main class="content"> absorbs the slack
```

Safe because the two non-flow siblings are unaffected by flex layout:
- `.hero__image` is `position: absolute; z-index: -1` (home-only, out of flow).
- The body load curtain (`body::after`) is `position: fixed`.

Footer and subscribe remain natural last children; the growing `main` pushes the
footer to the bottom on short pages and behaves normally on tall ones.

## Part 2 — Animated pangolin on the 404 page

The pangolin mascot stands in for the middle **0** of "404", reusing the existing
brandmark asset `assets/images/logos/etm-logo.png` (its round earth-globe reads
naturally as a zero). No new asset, no JS.

**Markup** (`layouts/404.html`) — the title is `4` + pangolin + `4`:

```
.error
  h2.error__title  "4" <span.error__zero><img etm-logo.png alt="0"></span> "4"
  p.error__text
  a.button "Back to home"
```

The image carries `alt="0"` so the heading still reads "404" to assistive tech. A
Hugo `{{ with }}`/`{{ else }}` falls back to a literal `0` if the asset is missing.

**Styles** (extend the existing `.error` block in
`assets/sass/4-layouts/_post.scss`):

- `.error__title` becomes a centered flex row (`4`, pangolin, `4`) with a small gap.
- `.error__zero img` height `0.82em` — sized in `em` so it tracks the responsive
  title font-size and matches the digits' visual height on every breakpoint (no
  separate mobile size rule needed).
- **Roll-in entrance** `@keyframes error-pangolin-rollin`: on load, translateX from
  the left + `rotate(360deg)` → settles in place (it *is* a rolling ball). ~0.9s
  ease-out, runs once.
- **Gentle bob** `@keyframes error-pangolin-bob`: subtle `translateY` with a tiny
  rotate, ~3s ease-in-out, infinite. Chained after the roll-in via the `animation`
  shorthand list with a 0.9s delay so the bob starts once the entrance ends.
- **Reduced motion**: inside `@media (prefers-reduced-motion: reduce)`, set
  `animation: none` and show the pangolin static — matching the existing guard in
  `common.js` and the header brandmark.

The existing `bm-roll` keyframe (header/footer logo) is untouched; the 404
keyframes are uniquely named to avoid collision.

## Out of scope (YAGNI)

- No changes to header/footer brandmark behavior.
- No new JavaScript.
- No new image assets.

## Success criteria

- `hugo` builds clean.
- On the built `404.html`, the footer sits at the bottom of the viewport with the
  short error content (no footer floating mid-page).
- The pangolin stands in for the middle 0 of "404", rolls in on load, then bobs
  gently; static under `prefers-reduced-motion: reduce`. Heading reads "404" to
  assistive tech via `alt="0"`.
- Tall pages (home, a blog post) are visually unchanged.
