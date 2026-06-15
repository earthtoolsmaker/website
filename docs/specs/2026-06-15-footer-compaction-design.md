# Footer Compaction — Design

**Date:** 2026-06-15
**Status:** Approved

## Problem

The site footer feels too big. It is a three-column widget block (info, recent
posts, navigation) followed by a bottom info bar, with generous spacing that
stacks up — especially tall on mobile where the columns stack vertically.

## Goal

Reduce footer height by roughly 30% while keeping all existing content and the
overall three-widget layout. The only structural change is laying the
navigation links out in two columns instead of one tall list.

## Non-goals

- No removal of widgets (info, recent posts, navigation all stay).
- No change to recent-post thumbnail size (kept as-is).
- No color, theme-toggle, back-to-top, or social-icon changes.
- No HTML/partial restructuring beyond what the nav 2-column needs (CSS-only).

## Changes

All changes are in `assets/sass/3-modules/_footer.scss`.

### 1. Spacing / size reductions (current → proposed)

| Selector | Property | Current | Proposed |
|----------|----------|---------|----------|
| `.footer__inner` | padding | `40px 0` | `28px 0` |
| `.widget-title` | margin-bottom | `28px` | `16px` |
| `.widget-title` | font-size | `24px` | `18px` |
| `.logo-footer__link` | margin-bottom | `28px` | `16px` |
| `.widget-footer__desc` | margin-bottom | `20px` | `14px` |
| `.recent-posts` | margin-bottom | `20px` | `14px` |
| `.footer__info` | padding | `32px 0` | `20px 0` |
| `.widget-footer` (@media `$desktop`) | margin-bottom | `60px` | `36px` |
| `.widget-footer` (@media `$mobile`) | margin-bottom | `48px` | `32px` |

### 2. Navigation → two columns

`.footer__nav-list` becomes a CSS multi-column list:

```scss
.footer__nav-list {
  line-height: 1;
  column-count: 2;
  column-gap: 32px;
}
```

- The 10 links flow 5 + 5 instead of a single tall column.
- Existing per-item `margin-bottom: 12px` provides row spacing within columns.
- `text-align: right` (desktop) / `left` (mobile) and the active-dot
  `::before` indicator are unchanged and continue to work per item.
- Two columns are kept at all breakpoints for the height saving.

## Verification

1. `hugo` build succeeds with no template/SASS errors.
2. Screenshot the contact page footer (identical site-wide) at 1440px and
   390px widths, before and after, and confirm:
   - Footer is visibly shorter (~30% less vertical space).
   - All content still present: logo, description, social icons, 3 recent
     posts with thumbnails, all 10 nav links (now 2 columns), copyright,
     back-to-top.
   - No overlap, clipping, or misalignment at either width.
