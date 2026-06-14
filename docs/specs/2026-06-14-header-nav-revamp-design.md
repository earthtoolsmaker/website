# Header nav bar revamp

**Date:** 2026-06-14
**Status:** Designed

## Goal

Make the site header tighter, better aligned, and more responsive — without
changing the navigation content or the brand button language. Three problems
drive this:

1. **Spacing** — the resting header is heavy: 32px vertical padding, a 54px
   logo, and a 64px gap below it eat ~182px before any page content. It should
   sit leaner by default.
2. **Nav element polish** — the active-page indicator is a tiny teal dot that
   floats above the word and reads as a rendering glitch; the logo wordmark and
   nav links are box-centered but not optically aligned; the "Work ⌄" chevron
   sits slightly low.
3. **Responsiveness** — the full nav collapses to a hamburger at ≤1024px, which
   is far too early. At 1025–1200px there is plenty of room the nav could use,
   so tablet-landscape / small-laptop users get a hamburger they don't need.

The redesign also turns the existing `etm` ↔ `earthtoolsmaker` brandmark into a
**responsive spacing lever**: show the compact `etm` mark on narrower widths to
buy room and keep the full inline nav alive longer.

## Compact resting header

Reduce the default (non-scrolled) header density:

| | Current | New |
|---|---|---|
| Vertical padding | 32px | **16px** |
| Logo height | 54px (desktop) | **~44px** |
| Gap below header (`margin-bottom`) | 64px | **~32px** |

Net: ~182px → ~108px before content, roughly **40% less** vertical space, with
the existing responsive logo step-downs (54/48/44) shifted down proportionally.

The grid stays `1fr auto 1fr` (logo left, nav centered, Support right) at wide
widths.

## Sticky + condense on scroll

The header becomes **sticky** (pinned to the top on scroll) and **condenses**:

- At the top of the page: the compact resting header above, transparent
  background (as today).
- After scrolling down: padding shrinks (~16px → ~10px), the logo steps down,
  and a **blurred, semi-opaque background** (`var(--background-color)` at ~82%
  opacity + `backdrop-filter: blur(10px)`) fades in with a **hairline bottom
  border** (`var(--border)`, `#ede0d4`) and a soft shadow, so the bar reads as
  floating above the content. Dark mode uses the dark background equivalent.

A small scroll listener toggles a `.is-scrolled` class on `.header`; all visual
change is CSS. Reduced-motion users still get the background (no size
animation).

## Nav element polish

- **Active / hover state** — replace the floating dot with a **2px underline**
  in `--secondary-color` (`#006d77`) that sits just under the link. Active = solid
  underline + the link text in `--secondary-color`; hover = the underline wipes
  in left→right. This applies to top-level links; the dropdown keeps its current
  panel styling. Removes the `::before` dot entirely.
- **Optical alignment** — align the serif logo wordmark and the sans nav links
  on a shared optical centerline (not just box-centered), so the two type
  styles read as one row. The Support button is already centered and keeps its
  brand style.
- **"Work ⌄" chevron** — nudge the chevron to the text's optical middle and
  size it consistently with the label.

The Support button keeps the **site-wide brand button** look (rounded 6px,
`4px 4px` hard shadow, tertiary background) — unchanged, for consistency with
the hero/CTA buttons.

## Responsive ladder

| Band | Width | Logo | Nav | Notes |
|---|---|---|---|---|
| Wide | ≥1100px | full `earthtoolsmaker` | full inline | brand prominent |
| Mid | 900–1100px | compact `etm` | **full inline** | etm frees ~150px so no hamburger here (today it would already be collapsed) |
| Narrow | <900px | compact `etm` | hamburger | nav folds into the panel |
| Mobile | ≤576px | compact `etm` | hamburger | tighter padding/logo |

The hamburger threshold moves from **≤1024px → <900px**. The existing mobile
dropdown panel mechanics (JS toggle, outside-click + Escape to close) are
unchanged — only the breakpoint and the resting bar move.

## Logo: etm vs earthtoolsmaker

The same rule applies on **every page, including home** (today home is a
special case that always shows the full wordmark). The resting word is
**viewport-driven**:

- **≥1100px:** full `earthtoolsmaker` at rest.
- **<1100px:** compact `etm` at rest.

### Animation reconciliation

The current `--unroll` hover animation (pangolin rolls 360°; word swaps
`etm` → `earthtoolsmaker`) is **preserved**, with one deliberate change in where
the *word swap* lives:

- **Pangolin roll on hover** — kept at **all** widths.
- **Word unroll (`etm`→`earthtoolsmaker`)** — happens in the **mid band
  (900–1100px)**, where `etm` is the resting word: hovering reveals the full
  name. In this band the full word is allowed to **overlay** on hover rather
  than reserving its width in-flow, so the compaction actually saves space (the
  resting logo column is `etm`-width, not full-width).
- **≥1100px** the full word is already shown at rest, so there is no word swap —
  only the pangolin roll on hover.

This means the full `earthtoolsmaker` wordmark is the resting brand on wide
screens (prominent), and the playful word-reveal becomes a mid-width touch.
Home gains the responsive behavior it doesn't have today.

> **Flag for review:** this is the one place the spec changes the *feel* of the
> recent animated-brandmark feature (the word swap no longer fires at desktop
> width because the full word is already shown). If you'd rather keep `etm`-at-rest
> + hover-to-reveal at *all* widths (so the animation fires on desktop too, at the
> cost of the full name not being visible by default), say so and we'll flip it.

## Files touched

- `layouts/partials/header.html` — unify the logo block so every page (incl.
  home) renders the same responsive brandmark (drop the `.IsHome` special
  case); keep the baked-lockup fallback.
- `assets/sass/3-modules/_header.scss` — compact resting spacing; sticky +
  condense (`.is-scrolled`); underline active/hover state (remove the dot);
  optical alignment; chevron tweak; move the collapse breakpoint to 900px;
  responsive `etm`/full word visibility + mid-band hover overlay.
- `assets/js/common.js` — add the scroll listener that toggles `.is-scrolled`
  (small addition alongside the existing menu toggle).
- `assets/sass/0-settings/_variables.scss` — only if a new `$nav-collapse`
  breakpoint variable is warranted (the existing `$desktop`/`$tablet`/`$mobile`
  in `_grid.scss` may suffice).

## Out of scope

- Nav content / menu structure (items stay as configured in `config.toml`).
- The mobile dropdown panel's visual design (positioning/animation unchanged).
- Dark-mode logo variant (still unset).
- The footer brandmark (`--slide`) — untouched.

## Verification

- `hugo` builds cleanly.
- Screenshot ladder at 1440 / 1100 / 1000 / 900 / 768 / 390px: full wordmark
  ≥1100, `etm` below, full inline nav down to 900, hamburger below 900.
- Resting header measurably leaner (~108px vs ~182px before content).
- Scroll past the fold: background/blur/border fade in, header stays pinned and
  condensed; scroll back to top restores the transparent resting bar.
- Active page shows the underline (no floating dot); logo + nav read as one
  optically aligned row.
- Hover at mid width reveals `earthtoolsmaker`; pangolin rolls at all widths;
  keyboard `:focus-visible` triggers the same.
- Dark mode: condensed background and border render correctly.
