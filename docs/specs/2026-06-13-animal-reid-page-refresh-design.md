# Animal reID page refresh — layout & copy

**Date:** 2026-06-13
**Branch:** `worktree-animal-reid-page-refresh` (off `main`)
**Files touched:** `content/tools/animal-reid/index.md`; `layouts/shortcodes/tabs.html` (one-line guard, Phase 2)

> Phase 1 (CTA card + intro polish) is implemented. Phase 2 (layout/organization +
> emoji removal) is described in its own section at the bottom of this doc.

## Goal

Improve the layout and copy of the Animal reID tool page. The main weakness is the
closing section — a bare `## Get Started` heading, a verbose paragraph, and a small
"Get in Touch" button. Replace it with the site's existing `.about-cta` card (the
light bordered CTA used on the About page's "What We Do" section), and do a light,
targeted copy pass. No section reordering.

## Decisions

- **CTA style:** Light bordered card — the `.about-cta` component (Image #1 reference),
  single button → `/contact/`.
- **Scope:** CTA + targeted copy/layout polish. Surgical, single file.
- **No CSS changes.** `.about-cta` is a top-level selector in
  `assets/sass/4-layouts/_about.scss` (not nested under an `.about` parent), so its
  styles already apply globally. Reusing the markup needs zero SCSS edits. The class
  remains shared with the About page; the SCSS is untouched, so both stay in sync.
- The page's `index.md` already uses raw HTML for its buttons, so inlining the
  `.about-cta` markup matches the existing file style (no new partial/shortcode —
  YAGNI).

## Changes

### 1. Replace the closing section

**Remove** (current end of page):

```markdown
## Get Started

Interested in applying Animal reID to your conservation project? We offer consultation on selecting the right identification approach, custom development for new species, and collaborative research opportunities.

<br/>
<div style="text-align: center;">
  <a href="/contact/" class="button">Get in Touch</a>
</div>
```

**Replace with** the `.about-cta` card:

```html
<div class="about-cta">
  <h3 class="about-cta__title">Have a species to identify?</h3>
  <p class="about-cta__description">Tell us about your animals and your image data — we'll give you an honest read on which identification approach fits and what it would take.</p>
  <a href="/contact/" class="link-no-decoration button button--middle">Start a project</a>
</div>
```

The `## Get Started` H2 is dropped — it would be redundant directly above the card's
own title. The card's built-in `margin-top: 48px` provides the spacing, so the
trailing `<br/>` pair before this section can be removed.

### 2. Targeted copy polish (no reordering)

Tighten the two intro paragraphs under the H1, cutting redundancy while keeping the
species range. Proposed:

> Animal reID is a modular computer vision framework for identifying individual
> animals. It adapts to each species by choosing the right technique — facial
> recognition, spot-pattern matching, or local feature analysis.
>
> From bears in British Columbia and trout in river systems to snow leopards in
> Central Asia and seals in coastal waters, it gives researchers non-invasive tools
> for wildlife monitoring and conservation.

Any other flabby phrasing found during implementation gets a light touch only —
Key Features, Conservation Impact, demos tabs, and resources tabs keep their
structure and content.

### Out of scope (Phase 1 — superseded by Phase 2 below)

- No SCSS changes.
- No section reordering or merging.
- No changes to the top "Try Interactive Demos" button, the image carousel, the
  `hf_space` demo embeds, or the resources/techniques/projects/guides tabs.
- No changes to front matter.

## Verification (Phase 1)

- `hugo` builds with no errors.
- Rendered page shows the `.about-cta` card as the closer, styled identically to the
  About page's CTA (bordered, centered, single button), with the button linking to
  `/contact/`.
- Intro reads cleaner; no content lost.

---

# Phase 2 — Layout, organization & emoji removal

## Decisions

- **Structure: story-led.** Final section order:
  1. Hero "Try Interactive Demos" button (unchanged)
  2. H1 + intro (Phase 1)
  3. Image carousel (unchanged)
  4. `## Why Animal reID` — Key Features + Conservation Impact **merged into one list**
  5. `## Interactive Demos` (`{#demos}` anchor kept) — same four `hf_space` embeds
  6. `## How It Works` — the Techniques content promoted out of the Resources tabs
  7. `## Resources & Documentation` — now only **Projects + Guides** tabs
  8. `.about-cta` card (Phase 1)
- **Copy: restructure + merge.** Fold the two bullet lists into capability+impact
  bullets; dedupe the redundant "Try" tab; rewrite section intros to fit the flow.
- **Emoji: none anywhere.** Stricter than About/Support. No heading emojis, no
  per-bullet emojis, no tab-label emojis, no `space_card` emoji (the cards live in
  the removed "Try" tab anyway).
- **Headings: plain markdown** `##` (no squiggle SVG, no template change for headings).

## Changes

### 1. `tabs` shortcode guard — `layouts/shortcodes/tabs.html`

Render the icon `<span>` only when an icon is present, so emoji-free labels don't
leave an 8px dangling gap:

```go-html-template
{{ if $icon }}<span class="tabs__tab-icon">{{ $icon | safeHTML }}</span>{{ end }}
```

Backward-compatible: biowatch (the only other `tabs` user) passes non-empty FA icons
via the `icon::text` form, so its spans still render. Emoji-free labels use the
`::Label` form (empty icon → span omitted).

### 2. Merge Key Features + Conservation Impact → `## Why Animal reID`

Replace both sections with one. Proposed body (no emojis):

> Animal reID combines proven techniques into one adaptable system for individual
> identification:
>
> - **One framework, many species** — proven on bears, trout, seals, and snow
>   leopards, and extensible to new species.
> - **The right technique for your data** — metric learning, local feature matching,
>   or a hybrid, matched to your species and imagery.
> - **Non-invasive by design** — identify individuals from camera-trap and
>   observation images, with no tagging or marking.
> - **Population trends over time** — match new sightings against historical
>   databases to track survival, movement, and behavior.
> - **Built to scale in the field** — automate identification to cut field costs and
>   cover larger areas with existing networks.

### 3. Promote Techniques → `## How It Works`

Lift the existing "Techniques" tab content (Metric Learning for Facial Recognition +
Local Feature Matching for Spot Patterns) out of the Resources tabs into a top-level
`## How It Works` section, placed after the demos. Copy intact.

### 4. Trim Resources tabs → Projects + Guides

- Remove the "Try" tab (re-linked the same demo spaces — duplication).
- Remove the "Techniques" tab (promoted to How It Works).
- Keep Projects + Guides; emoji-free labels `labels="::Projects|::Guides"`.
- Renumber surviving panels to `index="0"` (Projects) and `index="1"` (Guides) so
  tab buttons (indexed by label order) match panels.

### 5. Strip remaining emojis

- Demo tab labels → `labels="::Bear|::Trout|::Seal|::Snow Leopard"`.
- No emojis in any heading or bullet.

## Out of scope (Phase 2)

- No SCSS changes.
- No changes to the hero button, carousel, the four `hf_space` embeds, the CTA card,
  or front matter.
- No changes to the Projects/Guides card content (only their tab labels/indexes).

## Verification (Phase 2)

- `hugo` builds with no errors.
- Section order matches the list above; only one bullet list (no Features/Impact
  duplication).
- Resources block shows exactly two tabs (Projects, Guides) and they switch correctly
  in the built HTML (tab `data-tab` indexes align with panel `data-panel`).
- Biowatch tabs still render their FA icons (shortcode change is backward-compatible).
- `grep` of the rendered `index.html` finds no emoji characters in the page body.
