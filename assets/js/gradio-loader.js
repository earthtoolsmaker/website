// Shows a spinning pangolin overlay over each embedded Gradio app until the HF
// Space is ready, then fades the overlay out and the demo in. Reveal fires on
// (ready signal OR max-timeout) but never before a minimum display time, so a
// fast load does not flicker and a failed detection never traps the spinner.
(function () {
  "use strict";

  var MIN_DISPLAY_MS = 2000;
  var MAX_WAIT_MS = 15000;
  var FADE_MS = 400;

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

    // Primary signal: gradio dispatches "render" on the element once mounted.
    app.addEventListener("render", requestReveal, { once: true });

    // Backstop: watch for the real Gradio container appearing (light or shadow DOM).
    observer = new MutationObserver(function () {
      var container =
        app.querySelector(".gradio-container") ||
        (app.shadowRoot && app.shadowRoot.querySelector(".gradio-container"));
      if (container) requestReveal();
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
