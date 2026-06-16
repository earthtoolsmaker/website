// Shows a spinning pangolin overlay over each embedded Gradio app until the HF
// Space is ready, then fades the overlay out and the demo in. Reveal fires on
// (ready signal OR max-timeout) but never before a minimum display time, so a
// fast load does not flicker and a failed detection never traps the spinner.
(function () {
  "use strict";

  var MIN_DISPLAY_MS = 2000;
  // Cold HF Spaces can take much longer than a warm one to render. Gradio fires
  // `render` only when the real app mounts (not during the building/sleeping
  // phase), so we lean on that; this is just a last-resort cap so a Space that
  // never renders eventually reveals (showing Gradio's own error) rather than
  // spinning forever.
  var MAX_WAIT_MS = 30000;
  // Must cover the longest reveal transition in _gradio-loader.scss (0.55s)
  // so the loader isn't removed from layout before its dissolve finishes.
  var FADE_MS = 600;

  function initEmbed(embed) {
    var loader = embed.querySelector("[data-gradio-loader]");
    var app = embed.querySelector("gradio-app");
    if (!loader || !app) return;

    var start = Date.now();
    var revealed = false;
    var observer = null;
    var maxTimer = null;

    function cleanup() {
      if (observer) { observer.disconnect(); observer = null; }
      if (maxTimer) { clearTimeout(maxTimer); maxTimer = null; }
    }

    function reveal() {
      if (revealed) return;
      revealed = true;
      cleanup();
      embed.classList.add("is-ready");
      setTimeout(function () { loader.style.display = "none"; }, FADE_MS);
    }

    function requestReveal() {
      var elapsed = Date.now() - start;
      if (elapsed >= MIN_DISPLAY_MS) {
        reveal();
      } else {
        setTimeout(reveal, MIN_DISPLAY_MS - elapsed);
      }
    }

    // Primary signal: gradio dispatches "render" on the element only once the
    // real app has mounted — NOT during the building/sleeping/error phase.
    app.addEventListener("render", requestReveal, { once: true });

    // Backstop (in case `render` is absent on some gradio version): reveal when
    // actual interactive content exists. The building/sleeping screen has no
    // form controls, so this won't fire prematurely the way watching for the
    // bare .gradio-container shell did.
    observer = new MutationObserver(function () {
      if (app.querySelector("button, input, textarea")) requestReveal();
    });
    observer.observe(app, { childList: true, subtree: true });

    // Hard fallback so the overlay never sticks if no signal arrives.
    maxTimer = setTimeout(requestReveal, MAX_WAIT_MS);
  }

  function init() {
    var embeds = document.querySelectorAll("[data-gradio-embed]");
    for (var i = 0; i < embeds.length; i++) initEmbed(embeds[i]);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
