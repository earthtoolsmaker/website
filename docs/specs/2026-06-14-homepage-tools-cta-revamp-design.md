# Homepage tools section + "build technology that matters" CTA — Design

**Date:** 2026-06-14
**Branch:** `worktree-homepage-tools-cta-revamp`

## Goal

Revamp the homepage to (1) showcase a curated set of the open-source tools we
offer, and (2) add a call-to-action inviting people to support or partner with
us — "Help us build technology that matters".

## Current state

- Homepage (`layouts/index.html`) composes: hero → projects → testimonials →
  blog → tags.
- 4 tools exist in `content/tools/`: `pyronear`, `salmonvision`, `biowatch`,
  `animal-reid`.
- The tool card markup (`.tool` article) lives inline in
  `layouts/tools/list.html`.
- Reusable CTA partials already exist (`tools-cta.html`, `projects-cta.html`,
  `spaces-cta.html`, `support-cta.html`), all built on the shared `.about-cta`
  styling.
- Section sections (projects, testimonials, blog) are config-driven via
  `config.toml` `params`.

## New homepage flow

hero → projects → **tools** → **build-CTA** → testimonials → blog → tags

The tools section and its CTA are inserted directly after `section-projects`,
so the tools sit right under the projects they power.

## Components

### 1. `tool-card.html` partial (DRY extraction)

Extract the existing `.tool` card markup from `layouts/tools/list.html` into a
new `layouts/partials/tool-card.html` partial that takes a tool page as context
(`.`). Update `tools/list.html` to call the partial inside its range loop.

- No visual change to the `/tools/` page.
- The card renders: tinted logo header (`card_tint`, `logo_container`),
  optional `subtitle`, linked `title`, and `summary`.

### 2. `section-tools.html` partial

New `layouts/partials/section-tools.html`, rendered from `index.html` after
`section-projects.html`. Gated on `params.home_tools.enable`.

Contents:
- Section header matching the site pattern: `params.home_tools.title` (default
  `🛠️ Our Tools`) inside `.section__info`/`.section__head` with the squiggle
  SVG used by the projects/services sections.
- A one-line intro paragraph (e.g. "Free, open-source software we build with
  field teams — download and run it yourself.").
- The featured tool cards in a `.container > .row`, each rendered via
  `tool-card.html`.
- A `View all tools →` link to `/tools/` (styled like the existing
  `button button--cta` "View all" links in the projects section).
- The build-CTA (`build-cta.html`) at the end of the section.

**Tool selection (config-driven):** the partial reads
`params.home_tools.featured` — a list of tool slugs in display order — and looks
each one up among `where site.RegularPages "Section" "tools"`. Slugs that don't
resolve are skipped silently. This mirrors how the projects/testimonials
sections are configured and lets the featured set be reordered or swapped
without editing templates.

### 3. `build-cta.html` partial

New `layouts/partials/build-cta.html`, built on the existing `.about-cta`
structure (consistent with `tools-cta.html`/`projects-cta.html`, no new CSS):

- Title: **"Help us build technology that matters"**
- Description: a short line about supporting or partnering with us.
- Buttons:
  - `Support our work 🌍` → `/support/` (primary, `button button--cta`)
  - `Partner with us` → `/contact/` (secondary, `button button--ghost`)

Accepts an optional `class` (like the other CTA partials) for placement
variants.

### 4. Config

Add to `config.toml`:

```toml
[params.home_tools]
  enable = true
  title = "🛠️ Our Tools"
  featured = ["pyronear", "salmonvision", "biowatch"]  # slugs, in display order
```

## Styling

Reuses existing classes — `.section`, `.section__info`, `.section__head`,
`.section__title`, the `.tool` card styles, `.about-cta`, and the `col col-4`
grid. At most a small intro-text rule may be added if no existing class fits;
no new card or CTA components.

## Out of scope

- No changes to the `/tools/` page content or the tool cards' visual design.
- No new tool content.
- No changes to the existing `tools-cta.html` (different messaging; left as-is
  for the `/tools/` page).

## Verification

- `hugo` builds with no errors/warnings.
- Homepage renders the tools section (3 cards in order: Pyronear, SalmonVision,
  Biowatch) followed by the build-CTA, between projects and testimonials.
- `/tools/` page is visually unchanged after the card extraction.
- CTA buttons link to `/support/` and `/contact/`.
