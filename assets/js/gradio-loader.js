// Shows a spinning pangolin overlay over each embedded Gradio demo until its HF
// Space iframe has loaded, then fades the overlay out and the demo in. Reveal
// fires on (iframe load OR max-timeout) but never before a minimum display time,
// so a fast load does not flicker and a stalled load never traps the spinner.
//
// We embed via <iframe> rather than the <gradio-app> web component: HuggingFace's
// `.hf.space` CORS preflight currently omits `Access-Control-Allow-Credentials`,
// which blocks the component's credentialed cross-origin /config fetch. Inside an
// iframe the app talks to its own origin (no cross-origin preflight). HF already
// serves the iframe-resizer contentWindow script inside every Space, so we load
// the version-matched parent library to auto-height the iframe to its content.
(function () {
  "use strict";

  var MIN_DISPLAY_MS = 2000;
  // Last-resort cap so the overlay reveals even if the iframe never fires `load`
  // (e.g. a cold Space that is slow to serve its first byte).
  var MAX_WAIT_MS = 30000;
  // Must cover the longest reveal transition in _gradio-loader.scss (0.55s)
  // so the loader isn't removed from layout before its dissolve finishes.
  var FADE_MS = 600;

  // iframe-resizer parent library, version-matched to the contentWindow script
  // HuggingFace embeds inside every Space page (4.3.1). Loaded once.
  var RESIZER_SRC =
    "https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.3.1/iframeResizer.min.js";

  var resizerPromise = null;
  function loadResizer() {
    if (resizerPromise) return resizerPromise;
    resizerPromise = new Promise(function (resolve, reject) {
      if (window.iFrameResize) return resolve();
      var s = document.createElement("script");
      s.src = RESIZER_SRC;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });
    return resizerPromise;
  }

  function initEmbed(embed) {
    var loader = embed.querySelector("[data-gradio-loader]");
    var iframe = embed.querySelector("[data-gradio-iframe]");
    if (!loader || !iframe) return;

    var start = Date.now();
    var revealed = false;
    var maxTimer = setTimeout(requestReveal, MAX_WAIT_MS);

    function reveal() {
      if (revealed) return;
      revealed = true;
      clearTimeout(maxTimer);
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

    iframe.addEventListener("load", function () {
      loadResizer()
        .then(function () {
          if (window.iFrameResize) {
            window.iFrameResize({ checkOrigin: false, log: false }, iframe);
          }
        })
        .catch(function () { /* keep the iframe's fixed fallback height */ })
        .then(requestReveal);
    });
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
