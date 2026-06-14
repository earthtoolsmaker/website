# Project Pages Revamp — Design

**Date:** 2026-06-14
**Status:** Approved
**Scope:** Individual project pages (`content/projects/*`), rendered by `layouts/projects/single.html`. Brings them in line with the redesigned post/about/support pages (Newsreader headings, teal/coral palette, rounded cards, section dividers, CTA bands).

## Goal

Fully revamp the individual project page from the current two-column "content + tan sidebar widget" layout into an **editorial single-column** layout that matches the rest of the redesigned site. Wrap the existing long-form article body in modern, mostly auto-derived sections (hero, facts bar, partner strip, CTA band, related/next cards) so existing project markdown needs no edits.

Only `layouts/projects/single.html` and its new styling change. Project markdown bodies are left untouched. Two **optional** front-matter fields are introduced but never required.

## Decisions (validated via visual brainstorming)

- **Layout:** Direction A — editorial single-column (chosen over a refined two-column-with-sidebar). Long articles with wide images/tables read best in one centered column, matching the post page.
- **Sections around the body:** all four auto-derived sections in scope — facts bar, partner strip, status-aware CTA band, related + next-project cards.
- **New optional front matter:** `tagline` and `stats`, both render-only-when-present.
- The old sidebar widgets are retired from this template (not deleted).

## Page structure (top → bottom)

### 1. Hero

Full-bleed cover image (`.Params.image`) with a dark gradient overlay for legibility, reusing the about/support `about-hero` overlay pattern. Overlay (constrained to `container-wide`) contains:

- **Kicker** — uppercase, letter-spaced, dot-separated: status label (`completed` → "Completed", `fundraising` → "Seeking funding") + primary tool (first of `tools`).
- **Title** — `.Title` in Newsreader.
- **Tagline** — `tagline` front-matter, falling back to `summary`.
- **Stats row** (only if `stats` present) — 1–3 large value/label pairs.
- **Fallback:** if a project has no `image`, the hero uses the teal gradient (`--secondary-color` → `--primary-color`) with no `<img>`.

### 2. Facts bar

Slim strip directly under the hero, rendering only the pieces that exist:

- **Action links** — GitHub (`github_repo`) and ML Space (`space`) using the same icons as the current `widget-project-meta` (`fa-brands fa-github`, `images/social/hf.svg`).
- **Tool chips** — `tools` as small rounded chips.
- **Date** — `.Date.Format "2 January, 2006"` in muted text.

### 3. Reading column

`.Content` rendered untouched in a centered single column (~780px, matching the post page) with the same typographic rhythm as `_post.scss` (heading spacing, links, blockquotes/`<cite>`, code, lists, tables, images, iframes/`hf_space` embeds). The existing markdown bodies are **not** edited. The current in-content fundraising `support-cta` partial is removed from the body here (replaced by the CTA band, section 5).

### 4. Partner strip

Uniform grayscale logo row built from `clients` (same treatment as the spaces/partner pages — grayscale, no link underline, uniform SVG/img sizing, `partner-bg-inverted` honored). Preceded by a `section__info` heading + squiggle. Skipped entirely when there are no `clients`.

### 5. CTA band

Dark-teal `support__cta-band` before the footer, status-aware:

- `completed` → "Want a system like this?" → **Talk to us** (`/contact/`) + ghost **See our work** (`/projects/`).
- `fundraising` → "Help fund this project" → **Sponsor this project** / **Talk to us** (`/contact/`).

Reuses the `.support__cta-band` / `.button--ghost` styles verbatim.

### 6. Related reading

`related_posts` rendered as the modern `.article` cards, under a `section__info` heading. Reuses the existing article-card markup/styles (respecting the shared `.article__*` constraint — no edits to shared classes; wrapper-scoped overrides only if needed). Skipped when `related_posts` is empty.

### 7. Next project

`PrevInSection` rendered as a single project/`.article` card (modernizing the current `.project__nav` block), under a `section__info` heading. Skipped when there is no `PrevInSection` (last project in section).

## New optional front matter

Both optional; render-only-when-present; zero forced content edits.

```yaml
tagline: One punchy line for the hero.   # falls back to `summary`
stats:                                   # 1–3 entries; hero stats row
  - value: "1M+"
    label: salmon tracked
  - value: "7"
    label: species recognized
```

## Files touched

- `layouts/projects/single.html` — rewritten as the Direction A composition above.
- `assets/sass/4-layouts/_project-single.scss` — **new** partial: hero overlay variant, facts bar, reading-column typography, partner strip, section spacing. Registered in the SASS manifest (`assets/sass/main.scss` or equivalent).
- Possibly small new partials under `layouts/partials/` for the hero / facts bar / next-project card if it keeps `single.html` readable (decided during implementation).
- No changes to project markdown content. `tagline`/`stats` added to project files later, ad hoc.

## Reuse (no changes to these)

- `responsive-image.html`, `project-card.html`, the `.article` card styles.
- `about-hero` overlay CSS, `support__cta-band`, `button--ghost`, the `section__info` heading + squiggle SVG.
- Partner-strip grayscale treatment from the spaces/partner pages.

## Retired (left in place, not deleted)

- `layouts/partials/sidebar-widgets/widget-project-meta.html`
- `layouts/partials/sidebar-widgets/widget-recent-projects-and-related-posts.html`

These become unused by `projects/single.html`. Implementation will grep for other references and report; they are not removed as part of this change.

## Edge cases

No `image` → gradient hero · no `github_repo`/`space` → hide those links · no `tools` → no chips/kicker tool · no `clients` → no partner strip · no `stats`/`tagline` → fall back/skip · no `related_posts` → skip · last project → no next-project card.

## Non-goals

- No changes to the projects **list** page (`layouts/projects/list.html`), homepage project section, or `project-card.html`.
- No required front-matter changes; no edits to existing project markdown bodies.
- No deletion of the retired sidebar widgets.
- No global style changes — all new CSS scoped to the project-single layout.

## Verification

- `hugo` builds with no errors/warnings (static build is ground truth — local `hugo server` can serve stale pages).
- Screenshot-check representative projects: **wild_salmon_migration_monitoring** (partners + space + github + related post, `completed`), **carpathian-bear-deterrence** (`fundraising` → CTA variant), **snow_leopard_monitoring**, and one with no related posts / minimal metadata to confirm graceful degradation.
- Confirm hero, facts bar, partner strip, CTA band, and cards all render and degrade correctly; confirm reading-column typography on tables, blockquotes, and embeds.
- Snap chromium screenshots use `$HOME` paths + a virtual-time-budget.
