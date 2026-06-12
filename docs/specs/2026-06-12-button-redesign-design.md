# Button Redesign: "Full Ink"

**Date:** 2026-06-12
**Status:** Approved

## Goal

Replace the current button styles (oversized dark pills with a scale-up hover) with a
bold "Full Ink" style: inked border, hard offset shadow, press-in hover. Chosen by the
user from rendered design directions during brainstorming.

## Core style

Applies to `.button` in `assets/sass/3-modules/_buttons.scss` (full rewrite of the
file's button rules). Revised 2026-06-12 after a second visual iteration: borderless,
with a hover color change ("Borderless + hover darkens").

- No border
- Corner radius: `6px`
- Shadow: `4px 4px 0 #161616` (hard offset, no blur) — the shadow alone defines the edge
- Padding: `12px 24px`; font-size `15px`; font-weight `700`; line-height `1.4`
- Transition: `box-shadow .12s ease, transform .12s ease, background .12s ease, color .12s ease`
- **Hover (press-in + darken):** `transform: translate(3px, 3px)`; shadow shrinks to
  `1px 1px 0`; background darkens (per-variant colors below)
- **Active (full press):** `transform: translate(4px, 4px)`; shadow `0 0 0` (gone)
- **Focus:** replace the current `outline: none` with a visible `:focus-visible`
  outline (e.g. `2px solid var(--secondary-color)` with `2px` offset) for keyboard
  accessibility

## Variants

Class names are unchanged — no template or content edits needed for the core system.

| Class | Background | Text | Hover background |
|---|---|---|---|
| `.button` (default) | deep teal `#006d77` (`--secondary-color`) | white | darker teal `#00444c` |
| `.button--secondary` | white | deep teal `#006d77` | light gray `#f0f0f0` |
| `.button--cta` | terracotta `#e29578` (`--tertiary-color`) | dark `#161616` | deeper terracotta `#d77f5e` |

- `.button--middle` — pure size modifier: wider horizontal padding (`12px 40px`)
- `.button--big` — unchanged: `display: block; width: 100%`
- All variants share the same border, shadow, and hover/active/focus behavior.

## Color variables

Button colors stay wired through CSS variables in
`assets/sass/0-settings/_color-scheme.scss`:

- `--button-color: var(--white)`
- `--button-background-color: var(--secondary-color)` (was `--dark`)
- `--button-background-hover: #00444c` (darker teal; variant hover colors are set
  directly in the variant rules). `--button-color-hover` is removed along with its
  usages (`_buttons.scss`, `_subscribe.scss`).
- New variable: `--button-shadow-color: var(--dark)` for the offset shadow.
- The `:root[dark]` block gets the same treatment for consistency, but dark mode is
  disabled site-wide (`color_scheme = "light"` in config.toml), so no separate dark
  design is required.

## Stragglers (full-coverage scope)

1. **Tool page CTAs** — `assets/sass/4-layouts/_tool.scss`
   (`.tool-container-button-cta`): delete the nested `.button` padding/radius
   overrides and the `.tool-button-cta` color overrides so the buttons inherit the
   new standard styles. The flex container layout rules stay.
2. **Subscribe icon button** — `assets/sass/3-modules/_subscribe.scss`
   (`.subscribe-button`): keeps its 50px circle (`border-radius: 50%`) and absolute
   position, but gets the ink treatment: borderless, `2px 2px 0` offset shadow,
   press-in hover (`translate(2px, 2px)`, shadow `0 0 0`, background darkens to
   `var(--button-background-hover)`), teal background.

## Out of scope

- No template (`layouts/`) or content (`content/`) changes.
- No changes to nav links, tags, cards, or other non-button interactive elements.
- The `.link-no-decoration` helper and `.button--cta-container` layout block in
  `_buttons.scss` stay as-is.

## Verification

1. `hugo` builds with no errors.
2. Visual pass on `hugo -D server`: home page (hero buttons, services "Start a
   project", timeline), a tool page (Biowatch CTAs), a project page, the subscribe
   form, blog pagination ("Load More Posts"), and the donate/sponsor CTA shortcode.
3. Hover, active, and keyboard-focus states behave as specced on each variant.
