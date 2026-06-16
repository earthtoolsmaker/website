# Live Demo Pangolin Loader — Design

Date: 2026-06-16
Branch: `worktree-arthur+demo-pangolin-loader`

## Problem

Individual live demo pages embed a Hugging Face Space via `<gradio-app>`. While the
Space wakes up (cold start), the bare `<gradio-app>` shows a loading glitch / error
status message before the real demo appears. We want to cover that boot phase with a
spinning pangolin-logo animation, then transition smoothly to the live demo once it is
ready.

## Goal

Show a pangolin-spinner overlay on top of every Gradio embed until the Space is ready
(with a minimum display so it never flickers and a max-timeout fallback so it never
sticks), then fade the overlay out and fade the demo in.

## Scope

Two embed sites, both fed by one shared partial:

1. `layouts/demos/single.html` — the individual live demo pages.
2. `layouts/shortcodes/hf_space.html` — the `hf_space` shortcode used elsewhere.

Out of scope: the projects/spaces card embeds that do not render a live `<gradio-app>`.

## Approach

**Shared wrapper partial + one JS controller + SCSS.** Markup lives in one partial so the
two embed sites stay in sync; a single site-wide JS controller drives every embed on a
page; SCSS owns the spinner and fade.

### Components

#### 1. Shared partial — `layouts/partials/gradio-embed.html`

Renders the loader overlay + `<gradio-app>` inside a positioned wrapper. Parameters
(passed via `dict`): `src` (the `<space>.hf.space` host, required) and
`gradio_js_version` (optional, default `5.4.0`).

```html
{{- $src := .src -}}
{{- $ver := .gradio_js_version | default "5.4.0" -}}
<div class="gradio-embed" data-gradio-embed>
  <div class="gradio-embed__loader" data-gradio-loader aria-hidden="true">
    {{ $pangolin := resources.Get "images/logos/etm-logo.png" }}
    {{ with $pangolin }}<img class="gradio-embed__pangolin" src="{{ .RelPermalink }}" alt="">{{ end }}
    <p class="gradio-embed__label">Waking up the live demo…</p>
  </div>
  <script type="module"
    src="https://gradio.s3-us-west-2.amazonaws.com/{{ $ver }}/gradio.js"></script>
  <gradio-app src="https://{{ $src }}.hf.space"
    initial_height="0px" theme_mode="light" eager="true" container="false"></gradio-app>
</div>
```

The script tag is duplicated per embed today; consolidating it is not required for this
change (a page only embeds one Space in practice). Keep current behavior: load the
version-pinned gradio.js next to the app.

#### 2. Both templates call the partial

- `layouts/demos/single.html`: replace the inline `<script>` + `<gradio-app>` block
  (lines ~58–73) with
  `{{ partial "gradio-embed.html" (dict "src" .Params.hf_space "gradio_js_version" .Params.gradio_js_version) }}`.
- `layouts/shortcodes/hf_space.html`: replace its inline block with
  `{{ partial "gradio-embed.html" (dict "src" (.Get 0) "gradio_js_version" (.Get 1)) }}`
  (preserve the existing `.hf-space__gradio margin-bottom margin-top` wrapper around it).

#### 3. JS controller — `assets/js/gradio-loader.js`

Loaded site-wide the same way `common.js` is (verify the existing include mechanism and
mirror it). For each `[data-gradio-embed]`:

1. On `DOMContentLoaded`, the loader overlay is visible; the `<gradio-app>` sits beneath.
2. Start a **min-display timer = 2000 ms** and a **max fallback timer = 15000 ms**.
3. **Detect readiness.** Primary signal: the `render` event dispatched on the
   `<gradio-app>` element. Backstop: a `MutationObserver` that resolves when the real
   Gradio container/content appears under the app. *The exact ready signal must be
   verified against a real (sleeping) Space during implementation — adjust if `render`
   does not fire reliably for the pinned gradio version.*
4. **Reveal** when `(ready OR max-timeout fired) AND min-2s elapsed`. Revealing adds a
   class that fades the overlay out and the demo in over ~400 ms; after the transition,
   the loader is removed from layout (`display:none`) so it never traps clicks.
5. Each embed is independent; timers/observers are scoped per element.

#### 4. SCSS — new partial `assets/sass/.../_gradio-loader.scss` (or fold into `_space.scss`)

- `.gradio-embed` — `position: relative`.
- `.gradio-embed__loader` — absolutely positioned, fills the wrapper, `min-height` ~480px
  so it reserves vertical space while `<gradio-app>` is still `0px` tall; centered column
  (pangolin + label); site background so the boot glitch underneath is fully hidden.
- `.gradio-embed__pangolin` — sized ~72px; continuous spin
  `animation: gradio-pangolin-spin 1.1s linear infinite` where the keyframe is
  `rotate(0) → rotate(360deg)` (same idea as the header `bm-roll`, but infinite).
- `.gradio-embed__label` — muted text using existing type tokens.
- Reveal classes: `.gradio-embed.is-ready .gradio-embed__loader { opacity: 0; }` then
  removed via JS; `.gradio-embed__loader { transition: opacity .4s ease; }`.

### Reduced motion

Under `@media (prefers-reduced-motion: reduce)`: pangolin does not spin (static image +
label), and the fade is instant. Mirrors the existing 404 / header reduced-motion pattern.

### Error-flash handling

Because the overlay sits on top of `<gradio-app>` (opaque background, higher stacking)
until reveal, the boot-time error/status message is hidden the entire time. The
max-timeout guarantees the overlay never sticks permanently even if readiness detection
fails.

## Success criteria

1. Site builds (`hugo`) with no errors.
2. On a demo page with a cold Space, the spinning pangolin shows immediately; the boot
   error/status message is never visible.
3. The overlay stays at least ~2s, then fades out and the live demo fades in once ready.
4. If readiness is never detected, the overlay fades out by ~15s (no permanent spinner).
5. With `prefers-reduced-motion: reduce`, the pangolin is static and the transition is
   instant.
6. Both the demo pages and the `hf_space` shortcode render through the shared partial.

## Out of scope / non-goals

- No change to which Spaces are embedded or their gradio versions.
- No retry/health-check logic against the Space beyond the readiness signal + timeout.
- No new build tooling.
