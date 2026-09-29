# Card redesign

## Goal

Bring the listing cards (projects, blog posts, tools, demos) in line with the newer pages (Partners page cards, stats card): white surface, hairline border, 14px radius, soft shadow, teal accents. Today the four card types share one older look (cream background, coral left bar on the title, lift on hover) implemented three times in SCSS and nine times in markup. This redesign replaces all of it with one card partial and one SCSS module.

Direction chosen in the visual companion: **"C, no chip"**, a photo-led card with no topic tag.

## Anatomy

```
+-----------------------------+
|                             |
|   media band (10:7)         |   photo / logo on tint / SVG illustration
|                             |
+-----------------------------+
|  Title in Newsreader        |
|  Excerpt, two lines max,    |
|  grey ...                   |
|                             |   (body grows: footers line up per row)
|  Meta                    >  |   partner or date, chevron
+-----------------------------+
```

- **Surface:** `background: var(--white)`, `border: 1px solid var(--light-gray)`, `border-radius: 14px`, `box-shadow: 0 14px 32px -22px rgba(0, 0, 0, 0.3)`, `overflow: hidden`. Same values as `.partner-card` and `.stats-card--flat`.
- **Media band:** full bleed (no inner padding, no inner radius), 10:7 ratio as today. One of:
  - **photo** (projects, posts): `responsive-image.html` with lqip + lazy, `object-fit: cover`, as today.
  - **logo** (tools): the logo centred on `card_tint` (default `var(--accent-color)`), with the `logo_container` chip variant kept as is.
  - **illustration** (demos): `space-image.html` SVG, `object-fit: cover`.
- **Body:** padding about `16px 18px 16px`, column flex, grows to fill the card.
  - **Title:** `$heading-font-family`, about 19px, line-height 1.2, `--heading-font-color`. No left bar.
  - **Excerpt:** 14.5px, line-height 1.55, `--text-alt-color`, clamped to 2 lines for every type (tools were 3).
  - **Footer:** `margin-top: auto` so footers line up along each grid row. Meta on the left (12.5px, weight 600, `--text-alt-color`), chevron on the right (`fa-chevron-right`, 12px, `#c3c8cf` as on the stats card). When there is no meta, the chevron still sits on the right.
- **Hover / focus-visible:** no lift. Title turns `--secondary-color`, chevron turns `--secondary-color` and shifts 2px right (0.2s). The existing photo treatment stays: 50% grayscale on desktop, full colour on hover (moved from `.article__*` selectors in `_lazy-images.scss` to the new card selectors). Transitions off under `prefers-reduced-motion`.
- **Click target:** the whole card, via the title link's `::after` overlay, as today. Keyboard focus shows a `--secondary-color` outline on the card.

## Footer meta

| Type | Meta |
|------|------|
| Project | name of the first entry in `clients` |
| Post | date, `2 Jan, 2006`, in a `<time datetime>` |
| Tool | first client of the page at its `project` param |
| Demo | first client of the page at its `project` param |

If the lookup finds nothing (no `project` param, the linked page doesn't exist, or it has no clients), the footer shows only the chevron. Today that applies to the `animal-reid` tool and the `human_wildlife_bear_conflict` demo.

## Architecture

### `layouts/partials/card.html` (new)

Renders one card from a dict. It knows nothing about page types.

| Key | Required | Meaning |
|-----|----------|---------|
| `href` | yes | card link |
| `title` | yes | title text |
| `excerpt` | no | body text |
| `image` | one media key | photo path (`/images/...`), rendered via `responsive-image.html` |
| `illustration` | one media key | SVG path, rendered via `space-image.html` |
| `logo` | one media key | logo path; with optional `tint` and `logo_chip` (bool) |
| `meta` | no | footer text |
| `date` | no | a `time.Time`; renders as the meta in a `<time>` element (wins over `meta`) |
| `class` | no | column classes on the `<article>`; default `col col-4 col-w-6 col-t-12` |

### `layouts/partials/card-for-page.html` (new)

Takes a page, builds the dict from its section and calls `card.html`: projects (`image`, `summary`, client meta), posts (`image`, `description`, `date`), tools (`icon` as `logo`, `card_tint`, `logo_container`, `summary`, project client meta), demos (`card_image` as `illustration`, `summary`, project client meta). Also accepts an optional `class` override, so the call is `{{ partial "card-for-page.html" (dict "page" . "class" "...") }}`, or `{{ partial "card-for-page.html" (dict "page" .) }}` for the default.

### Call sites

| File | Change |
|------|--------|
| `partials/project-card.html`, `partials/article.html`, `partials/tool-card.html` | become one-line wrappers around `card-for-page.html`, so the existing `partial "project-card.html" .` style calls (home, listings, project pages, support, `_default/list.html`) keep working unchanged |
| `partials/related-posts.html` | inline card replaced by `card-for-page.html` with `class "col col-6 col-t-12 animate"` |
| `projects/single.html` (demo cards) | inline card replaced by `card-for-page.html` |
| `demos/list.html` | inline card replaced by `card-for-page.html` |
| `shortcodes/project_card.html`, `article_card.html`, `space_card.html` | call `card.html` with their args (`excerpt` / `description` / `summary` as excerpt). If `link` resolves with `site.GetPage`, meta comes from that page (client or date), so `animal-reid`'s embedded cards match the listings; otherwise `article_card` falls back to its `date` string. The inline link-style resets move into the SCSS. |

### SCSS

- New `assets/sass/3-modules/_card.scss` with a `.card` block (`.card`, `.card__content`, `__media`, `__logo`, `__logo--chip`, `__body`, `__title`, `__link`, `__excerpt`, `__footer`, `__meta`, `__chevron`), imported in `main.scss`.
- Resets for links inside prose (`.page__content`, `.tool-content`, `.post__content`) scoped in `_card.scss`, as `.stats-card` does, so shortcode cards look the same as listing cards.
- Delete the card rules from `_article.scss`, `_tools.scss` (`.tool`, `.tool__content` ... `.tool__excerpt`) and `_spaces.scss` (`.space`, `.space__content` ... `.space__excerpt`). The `.tool__nav*` / `.space__nav*` page-navigation rules in `4-layouts/` are unrelated and stay.
- Update `_lazy-images.scss` (grayscale, picture sizing) and `_post.scss:401` (`.article__title a:hover`) to the new selectors, or drop the latter if the card hover already covers it.
- If `_article.scss` ends up empty, remove it and its import.

## Out of scope

- The sidebar widget (`widget-recent-projects-and-related-posts.html`), partner cards, stats card, species cards, support cards.
- Grid, column counts, section spacing, listing order and limits.
- Dark mode: follows `.partner-card` (uses `var(--white)`), no separate treatment.

## Verification

- `hugo` builds with no new warnings.
- Visual check at desktop, tablet and 375px on: home (projects, tools, blog), `/projects/`, `/posts/`, `/tools/`, `/demos/`, a project page (related projects, demo cards, related posts), a post (You may also like), `/support/` (project cards), `/tools/animal-reid/` (shortcode cards).
- Footers line up across each grid row; meta matches the table above on every listing; missing-meta cards show the chevron only.
- Hover and keyboard focus: title and chevron go teal, photo goes full colour, no lift.
- `grep` finds no remaining `article__`, `tool__content`, `space__content` card markup in `layouts/`.
