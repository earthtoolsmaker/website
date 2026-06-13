# Partners Page — Design Spec

**Date:** 2026-06-13
**Status:** Approved (design), pending implementation
**Reference:** Inspired by https://www.hack-the-planet.io/partners/

## Goal

Add a `/partners/` page that showcases the organizations EarthToolsMaker (ETM)
builds conservation technology with. ETM is a conservation-tech studio/consultancy
(not a foundation-funded nonprofit), so the page is a **showcase of collaborators**
— social proof and a "who we work with" overview — rather than a funder/grant
funnel like the Hack The Planet reference.

## Decisions (locked)

- **Purpose:** Showcase of collaborators (logos + short descriptions, grouped by type).
- **Data source:** A curated data file (full editorial control), not auto-derived from project front matter.
- **Grouping:** By partner type (categories).
- **Navigation:** Linked from the **footer menu** only (alongside About, Support, Contact). Not added to the main header nav.

## Architecture

Follows the existing custom-page convention used by `about` and `support`:

| File | Role |
|------|------|
| `content/partners.md` | Front matter (`layout: partners`, `title`, hero fields) + short markdown intro body. |
| `layouts/page/partners.html` | Template: hero → intro → grouped partner sections → CTA. |
| `data/partners.toml` | Curated source of truth. One entry per partner. |
| `assets/scss/_partners.scss` (or project's SCSS convention) | Page styling, imported into the main stylesheet. |

Logos reference existing files under `assets/images/clients/<org>/...` and are
Hugo-processed (the same approach `params.testimonial_item` logos use in `config.toml`).

### Data model (`data/partners.toml`)

Categories are defined in order; each partner belongs to one category.

```toml
[[partner]]
name     = "Pacific Salmon Foundation"
logo     = "images/clients/psf/logo.png"   # path under assets/
link     = "https://psf.ca/"
category = "funders"                         # maps to a category heading
blurb    = "One-to-two sentence description of the collaboration."
```

Category keys → display headings (order top-to-bottom):

1. `conservation` → "Conservation Organizations"
2. `research` → "Research Institutions"
3. `technology` → "Technology Partners"
4. `funders` → "Funders & Supporters"

The template groups partners by `category` and renders categories in this fixed order.
Empty categories render nothing.

## Page layout (top → bottom)

1. **Hero** — reuse the about-style hero (`hero_title`, `hero_description` front matter).
   - Title: "Partners" (or similar). Intro line: e.g. "The organizations we build conservation technology with."
2. **Intro paragraph** — 2–3 sentences (markdown body) on how ETM collaborates with conservation teams.
3. **Grouped partner sections** — for each non-empty category: a section heading (one emoji max, per project style) + a responsive card grid. Each card = logo + partner name (linked to their site, `target="_blank" rel="noopener"`) + short blurb.
4. **CTA** — a single restrained line linking to `/contact/`: "Building conservation tech and want to collaborate? Get in touch." No grant/funder funnels.

## Initial partner roster

Drawn from existing logos in `assets/images/clients/`. Names/links sourced from
existing project front matter and `config.toml` testimonials where available.
Category assignments and a few unverified orgs (`osi`, `rbc`, `ai2`, `carpathia`,
`cornell_lab`, `inbo`, `sfu`, `sovon`, `wild_salmon_centre`) will be confirmed
during implementation (correct full name, link, logo variant, category).

- **Conservation Organizations:** Carpathia, Citibats Cambodia, Elephant Listening Project, OSI-Panthera, Wild Salmon Center, BearID
- **Research Institutions:** Cornell Lab of Ornithology, INBO, SFU, Sovon, Wageningen Marine Research
- **Technology Partners:** Pyronear, ReefSupport, Hack The Planet, Lumax AI, AI2
- **Funders & Supporters:** Pacific Salmon Foundation, BC Hydro, RBC

(Final categorization confirmed when building `data/partners.toml`.)

## Styling

- Match the restrained look of the About/Support pages: one emoji per section heading max, none in body copy.
- Logo cards: consistent sizing, transparent/`logo_without_text` variants preferred where available for visual consistency on a grid.
- Responsive grid (e.g. CSS grid, auto-fill) consistent with existing card patterns on the site.

## Out of scope

- Auto-syncing the partner list from project front matter.
- "Ways to partner" / funder / grant call-to-action sections (HTP-style engagement funnels).
- Adding Partners to the main header navigation.

## Verification

- `hugo` builds with exit code 0 (no template errors).
- `/partners/` renders the hero, all four category sections with correct logos/links, and the CTA.
- Footer shows a working "Partners" link.
- Page visually matches the restraint of About/Support (spot-check via local build / screenshot).
