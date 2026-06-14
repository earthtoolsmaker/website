# Project Content Cards — Design

**Date:** 2026-06-14
**Status:** Approved
**Scope:** The markdown **bodies** of `content/projects/*` — selectively grouping already-list-shaped content into card grids. Complements `2026-06-14-project-pages-revamp-design.md`, which revamped the project *template* and explicitly listed "no edits to project markdown bodies" as a non-goal. This spec covers that excluded piece. No template or CSS changes.

## Goal

Make long project articles more scannable by converting discrete, list-shaped passages into the same card grids the spaces pages already use, **and** by lightly improving the copy as we go — without losing technical depth or accuracy. Done one project at a time.

## Copy polish (in scope)

Alongside the structural carding, give each article a light editorial pass: tighten wordiness, cut marketing buzzwords ("holistic", "innovative", "seamlessly", "cutting-edge"), prefer active voice and concrete nouns, and keep the EarthToolsMaker voice (plain, confident, field-grounded — matching the about/support/spaces pages). Preserve every factual and technical claim; never invent numbers or capabilities. Leave specialized technical passages, quotes, captions, and links intact unless a change is a clear improvement.

## The card convention ("light" intensity)

**Component:** reuse `support__grid` + `support__card`, written as raw HTML inside the markdown (Goldmark has unsafe HTML enabled; the spaces pages already do exactly this). No new CSS, no template edits.

```html
<div class="support__grid">
  <div class="support__card">
    <h3 class="support__card-title">Title</h3>
    <p class="support__card-description">Description.</p>
  </div>
  <!-- ... -->
</div>
```

**What gets carded** — only content that is *already* a discrete list/sequence:
- Bulleted benefit/reason lists where each item has a bold lead-in (title = lead-in, description = the rest of the item)
- "How it works" / step sequences
- Already-enumerated scope/objective lists

**What stays untouched prose:** narrative context, pull-quotes, images, galleries, videos, conclusions. No paragraph rewriting.

**Pattern:** keep the section's intro sentence (as prose, or `support__section-intro`), then the grid, then any closing paragraph stays prose.

**Default to `support__card`.** The richer `support__track` variant (eyebrow label + proof line + offers list) is tied to the support page's data structure and reserved for special cases — not used by default.

## Sibling-page consistency

The project page is the **deep version**; the matching space page is the **condensed demo**; related blog posts are the **full essays**. When a space already cards a topic in condensed form (e.g. forest-fire's "Why Early Detection Matters" = 3 cards), the project page keeps its fuller list rather than collapsing to match. Same component and tone, different depth.

## First project — Early Forest Fire Detection

`content/projects/early_forest_fire_detection.md`. One clean candidate under "light":

- **"Forests Protection"** — the 5 bolded bullets (Biodiversity Conservation, Carbon Sequestration, Water Resources, Economic Impact, Human Health) → a 5-card `support__grid` (renders 3 + 2). Keep all five (deep version). Titles = the bold lead-ins; descriptions = the existing bullet text. The intro line ("Protecting forests from fire is crucial for several reasons:") and the closing summary paragraph stay as prose.

Everything else (Context, Project Scope, Setup, Temporal Verification, Conclusion) stays as-is. Optional follow-up (deferred, would nudge into "medium"): a pipeline card grid mirroring the space's "How Detection Works" — decided after seeing the first change rendered.

## Verification

- `hugo` builds with no errors/warnings (static build is ground truth; `hugo server` can serve stale pages).
- Screenshot-check the rendered `/projects/early_forest_fire_detection/` — card grid renders inside `.post__content` and matches the spaces-page look.

## Non-goals

- No template or CSS changes (`layouts/`, `assets/` untouched).
- No new front matter.
- No heavy reshaping of structure (still "light"); no collapsing the project's deep lists to match condensed space cards. Copy polish stays editorial — it does not change what the article claims.
- Not a bulk pass — projects are converted one at a time, each reviewed.
