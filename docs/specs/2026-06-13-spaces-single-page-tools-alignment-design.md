# Spaces Single Page — Alignment with Tools Page — Design

**Date:** 2026-06-13
**Status:** Approved (brainstorm) — ready for implementation plan

## Overview

Bring the individual space pages (`layouts/spaces/single.html`) up to the visual
standard of the recently redesigned tools page (`layouts/tools/single.html`). The
spaces single page is the older design: it links out via an emoji `<ul>`, uses a
heavy emoji "Manual" heading, and ends with a prev/next navigation block padded with
~16 empty `<div>`s. The tools page is clean: centered title, content, then a tidy
"Resources" footer.

Scope is the **single** space page only. This is unrelated to the in-progress spaces
**listing** card refresh (`2026-06-13-spaces-page-refresh-design.md`).

## Approach

Inline replication (not a shared partial). All template changes are scoped to
`layouts/spaces/single.html`, plus one small SCSS tweak in `_space.scss`. The tools
page is **not** modified, so the just-shipped tools redesign is not regressed. The
footer markup/styles mirror the tools `tool-resources` block exactly, under a
`space-resources` class.

## Changes

### 1. Resources footer (core change)

Replace the emoji `<ul>` (🛠️ project / GitHub / 🤗 hosted) with the tools-page
"Resources" footer: a centered uppercase "RESOURCES" label and inline links separated
by `·`, built dynamically from whichever params exist:

| Param | Icon | Label |
|---|---|---|
| `project` | `fa-solid fa-circle-info` | Project overview |
| `github_repo` | `fa-brands fa-github` | Source code |
| `hf_space_code` | `fa-solid fa-arrow-up-right-from-square` | Hosted on Hugging Face |

Render only the rows whose param exists (same `slice`/`append` pattern as tools).
Same inline styles as `tool-resources` for exact visual parity, under class
`space-resources`.

### 2. Reorder content

Match the tools page, where Resources is always last. New order inside
`.space-content`:

```
manual steps  →  Gradio embed  →  .Content  →  Resources footer
```

Today the link list sits mid-page, before `.Content`.

### 3. Restrained "Manual" heading

`🧑🏾‍🏫 Manual 📖` → `📖 Manual` — one emoji per heading, per the house style
(About/Support are the reference).

### 4. Separator

Remove the `<hr class="space-separator">` between the info block and content, to match
the tools page (which has no separator). The centered title+summary block keeps its own
bottom margin.

### 5. Remove prev/next navigation

Delete the entire `.space__navigation` block (the prev/next "Next Space" markup with
the empty `<div>`s). The spaces listing/gallery is how users move between spaces, and
the tools page has no such nav.

## Kept as-is

- Gradio embed (`hf_space`) — the core function of a space page.
- Manual steps list (`manual_steps`).
- Hero image logic (`card_image` illustration / `hero_image` fallback).
- Centered title + summary (`space-info`).

## Dead code (flagged, not removed)

Removing the nav block leaves `.space__nav`, `.space__navigation`, `.space-separator`,
and related rules in `assets/sass/4-layouts/_space.scss` unused. Per the user's
"don't delete pre-existing dead code unless asked" rule, these are left in place and
flagged here. Prune on request.

## Verification / Success Criteria

- `hugo` builds cleanly (static build is ground truth, not the dev server).
- A representative space (`bear_identification`) renders with: new dot-separated
  Resources footer, correct order (manual → embed → content → resources), `📖 Manual`
  heading, no `<hr>`, no prev/next nav block.
- Footer visually matches a tool page's Resources footer (screenshot comparison).
- No regression on the tools page (untouched).
