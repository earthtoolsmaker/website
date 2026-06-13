# Animal reID page refresh — layout & copy

**Date:** 2026-06-13
**Branch:** `worktree-animal-reid-page-refresh` (off `main`)
**File touched:** `content/tools/animal-reid/index.md` (only)

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

### Out of scope

- No SCSS changes.
- No section reordering or merging.
- No changes to the top "Try Interactive Demos" button, the image carousel, the
  `hf_space` demo embeds, or the resources/techniques/projects/guides tabs.
- No changes to front matter.

## Verification

- `hugo` builds with no errors.
- Rendered page shows the `.about-cta` card as the closer, styled identically to the
  About page's CTA (bordered, centered, single button), with the button linking to
  `/contact/`.
- Intro reads cleaner; no content lost.
