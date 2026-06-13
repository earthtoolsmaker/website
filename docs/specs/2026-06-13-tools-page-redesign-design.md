# Tools page redesign — design

**Date:** 2026-06-13
**Status:** Approved

## Goal

Restyle the `content/tools/` listing page so its cards match the shared card
system used by spaces and blog, remove the clashing purple→red gradient behind
the tool logos, and add a stats band above the grid. Each logo sits on a soft,
per-tool brand tint.

## Motivation

The tools cards are the last listing on the site using the old visual language:
a chunky `#ede0d4` head, a 32px title, a `--text-gradient` subtitle, and brand
logos floated over `linear-gradient(#9198e5, #e66465)` (purple→red). That
gradient clashes with the site's teal/terracotta palette. Spaces and blog
already share a clean card system (`.space__*` / `.article__*`): alt-color
fill, hairline border, soft shadow, 70%-aspect image, small uppercase subtitle,
18px title with a terracotta left-accent. Tools should join that system.

## Decisions (from brainstorming)

- **Image area:** keep each tool's brand **logo** centered (logos are the
  tools' identity) — do not generate illustrations or use screenshots.
- **Backdrop:** replace the gradient with a **per-tool brand tint**.
- **Page structure:** add a **stats band** above the cards, mirroring spaces.

## Scope

In scope (only these files):

- `layouts/tools/list.html` — rewrite card markup + add stats band.
- `assets/sass/3-modules/_tools.scss` — replace card styles with the shared
  card system; remove the now-orphaned `.tool__head` / gradient / icon-over-
  gradient rules.
- `content/tools/{animal-reid,biowatch,pyronear,salmonvision}/index.md` — add
  the new `card_tint` front-matter field.

Out of scope: tool single pages (`layouts/tools/single.html`), spaces, blog,
the global color scheme, and any unrelated refactoring.

## Design

### 1. Card chrome & typography (match `.space__*` / `.article__*`)

Rewrite the `.tool` article markup to the shared structure:

- `.tool__content` — `position:relative`, flex column, `padding:14px`,
  `border-radius:16px`, `background:var(--background-alt-color)`,
  `border:1px solid var(--border-color)`, `box-shadow:0 6px 26px rgba(0,0,0,.05)`,
  `transition:transform .3s ease`, `:hover { transform:translateY(-8px) }`.
  Mobile: `padding:12px`.
- `.tool__image` — the 70%-aspect block (`&::after { padding-top:70% }`),
  `border-radius:10px`, `overflow:hidden`. This is where the logo +
  per-tool tint live (see §2).
- `.tool__inner` / `.tool__info` — flex column, `margin:16px 6px 2px`.
- `.tool__subtitle` — small uppercase, `font-size:12px`, `font-weight:700`,
  `letter-spacing:.06em`, `text-transform:uppercase`, `color:var(--text-alt-color)`,
  `padding-left:15px`. Replaces the old `--text-gradient` subtitle.
- `.tool__title` — `font-size:18px`, `padding-left:12px`,
  `border-left:3px solid var(--tertiary-color)`; the `a::after` full-card click
  overlay with `border-radius:16px`. Replaces the old 32px title.
- `.tool__excerpt` — `font-size:14.5px`, `line-height:1.55`,
  `color:var(--text-alt-color)`, `-webkit-line-clamp:3`.

The whole-card link overlay (`a::after`) is preserved so the entire card is
clickable, as in spaces.

### 2. Per-tool brand tint + logo

The logo image area replaces the gradient with a soft per-tool tint:

- New optional front-matter field **`card_tint`** on each tool's `index.md`,
  holding a CSS color. The template sets it as an inline custom property
  (e.g. `style="--tool-tint: {{ .Params.card_tint }}"`) on `.tool__image`, and
  the SCSS uses `background: var(--tool-tint, <fallback>)`.
- Fallback when `card_tint` is unset: a neutral brand tint (a pale teal/blush).
- Tints are light/pastel so the logos read clearly.
- The existing **cream chip** for `logo_container` tools (Pyronear,
  SalmonVision) is preserved — those logos keep their rounded panel; other
  logos (Biowatch, Animal reID) sit directly on the tint.

Proposed default tints (light, on-brand):

| Tool         | `card_tint` direction |
|--------------|-----------------------|
| Biowatch     | sage / teal           |
| Pyronear     | warm terracotta       |
| SalmonVision | water blue-teal       |
| Animal reID  | blush                 |

Exact hex values chosen during implementation to stay pastel and legible
against each logo.

### 3. Stats band

Add an `about-stats`-style section above the card grid, reusing the same markup
spaces uses (`section about-stats … animate` → `about-stats__grid` →
`about-stats__item` with `about-stats__value` + `about-stats__label`). A
`tools-stats` modifier class is added for any spacing tweaks.

**Stats content (values + labels) is deferred — the user will provide the
copy.** Implementation builds the band structure with placeholder items wired
up; the user supplies the final figures before merge.

## Cleanup

The rewrite makes these orphaned and they are removed from `_tools.scss`:
`.tool__head`, `.tool__image-container` (gradient, grayscale filter),
`.tool__image` gradient background, and the old 32px `.tool__title` /
`--text-gradient` `.tool__subtitle` rules. The `.tool__icon` /
`.tool__icon-container` rules for centering the logo (and the cream chip) are
retained/adapted since logos are still shown.

## Verification

- `hugo` builds clean (no template errors).
- Tools listing renders 4 cards visually consistent with the spaces grid:
  same border, shadow, radius, subtitle/title/excerpt treatment.
- No purple→red gradient remains; each card shows its logo on its brand tint.
- Stats band renders above the grid.
- Screenshot the static build (`public/`) per local-preview quirks (restart
  hugo / build is ground truth) to confirm.
