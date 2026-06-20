document.addEventListener("DOMContentLoaded", function() {
  'use strict';

  var html = document.querySelector('html'),
    body = document.querySelector("body"),
    menuToggle = document.querySelector(".hamburger"),
    menuList = document.querySelector(".main-nav"),
    toggleTheme = document.querySelector(".toggle-theme-js"),
    toggleTheme = document.querySelector(".toggle-theme"),
    btnScrollToTop = document.querySelector(".top");


  /* =======================================================
  // Menu + Theme Switcher
  ======================================================= */
  menuToggle.addEventListener("click", () => {
    menu();
  });

  // Condense the sticky header after a little scroll. Use hysteresis (turn on
  // higher than off) so the ~20px height change from condensing — which shortens
  // the page and can nudge scrollY back across a single threshold on short pages
  // like /contact/ — can't make the state oscillate.
  var header = document.querySelector(".header");
  if (header) {
    var CONDENSE_ON = 48, CONDENSE_OFF = 8;
    var onScroll = function () {
      var y = window.scrollY;
      if (!header.classList.contains("is-scrolled")) {
        if (y > CONDENSE_ON) header.classList.add("is-scrolled");
      } else if (y < CONDENSE_OFF) {
        header.classList.remove("is-scrolled");
      }
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Logo click: spin the pangolin, then navigate once the animation finishes
  var logoLink = document.querySelector(".logo__link");
  var brandmark = logoLink && logoLink.querySelector(".brandmark");
  var panImg = brandmark && brandmark.querySelector(".brandmark__pan img");
  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (brandmark && panImg && !prefersReducedMotion) {
    logoLink.addEventListener("click", function (event) {
      // Let the browser handle new-tab / modified / non-primary clicks normally
      if (event.defaultPrevented || event.button !== 0 ||
          event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
        return;
      }
      event.preventDefault();
      var href = logoLink.getAttribute("href");
      var navigated = false;
      var go = function () {
        if (navigated) return;
        navigated = true;
        window.location.href = href;
      };
      // Restart the spin from the top, even if a hover spin was mid-flight
      brandmark.classList.remove("is-spinning");
      void brandmark.offsetWidth; // force reflow so the animation re-triggers
      brandmark.classList.add("is-spinning");
      panImg.addEventListener("animationend", go, { once: true });
      setTimeout(go, 900); // fallback if animationend doesn't fire
    });
  }

  // Close menu when clicking outside
  document.addEventListener("click", (event) => {
    const isMenuOpen = menuList.classList.contains("is-visible");
    const clickedInsideMenu = menuList.contains(event.target);
    const clickedHamburger = menuToggle.contains(event.target);

    if (isMenuOpen && !clickedInsideMenu && !clickedHamburger) {
      menuClose();
    }
  });

  // Close menu when pressing Escape key
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuList.classList.contains("is-visible")) {
      menuClose();
    }
  });

  function menuOpen() {
    menuList.classList.add("is-open");
  }

  function menuClose() {
    menuToggle.classList.remove("is-open");
    menuList.classList.remove("is-visible");
  }

  if (toggleTheme) {
    toggleTheme.addEventListener("click", () => {
      darkMode();
    });
  };


  // Menu
  function menu() {
    menuToggle.classList.toggle("is-open");
    menuList.classList.toggle("is-visible");
  }


  // Theme Switcher
  function darkMode() {
    if (html.classList.contains('dark-mode')) {
      html.classList.remove('dark-mode');
      localStorage.removeItem("theme");
      document.documentElement.removeAttribute("dark");
    } else {
      html.classList.add('dark-mode');
      localStorage.setItem("theme", "dark");
      document.documentElement.setAttribute("dark", "");
    }
  }


  /* =======================
  // Animation Load Page
  ======================= */
  setTimeout(function(){
    body.classList.add("is-in");
  },150)


  /* ================================================================
  // Stop Animations During Window Resizing and Switching Theme Modes
  ================================================================ */
  let disableTransition;

  if (toggleTheme) {
    toggleTheme.addEventListener("click", () => {
      stopAnimation();
    });

    window.addEventListener("resize", () => {
      stopAnimation();
    });

    function stopAnimation() {
      document.body.classList.add("disable-animation");
      clearTimeout(disableTransition);
      disableTransition = setTimeout(() => {
        document.body.classList.remove("disable-animation");
      }, 100);
    }
  }


  /* =======================
  // Responsive Videos
  ======================= */
  reframe(".post__content iframe:not(.reframe-off), .page__content iframe:not(.reframe-off), .project-content iframe:not(.reframe-off)");


  /* =======================
  // LazyLoad Images
  ======================= */
  var lazyLoadInstance = new LazyLoad({
    elements_selector: ".lazy",
    // Handle <picture> elements with data-srcset on source elements
    callback_loaded: function(el) {
      // When an image loads, also activate srcset on sibling sources
      var picture = el.closest('picture');
      if (picture) {
        picture.querySelectorAll('source[data-srcset]').forEach(function(source) {
          source.srcset = source.dataset.srcset;
          source.removeAttribute('data-srcset');
        });
      }
      // Add loaded class for LQIP blur transition
      el.classList.add('loaded');
    }
  })


  /* =======================
  // Zoom Image — intentionally disabled
  // The Lightense full-screen zoom on content/gallery images was broken, so it
  // is turned off. Full-screen expand is handled only by the dedicated
  // image-carousel lightbox further down.
  ======================= */


  /* ============================
  // Partners Slider
  ============================ */
  if (document.querySelector(".about-partners-slider")) {
    var aboutPartnersSlider = tns({
      container: ".about-partners-slider",
      items: 2,
      slideBy: 1,
      gutter: 24,
      nav: false,
      controls: false,
      mouseDrag: true,
      autoplay: true,
      autoplayButtonOutput: false,
      autoplayTimeout: 3000,
      speed: 500,
      responsive: {
        768: {
          items: 3,
        },
        1024: {
          items: 5,
        }
      }
    });
  }

  /* ============================
  // Team Bio Toggle
  ============================ */
  document.querySelectorAll(".team-card__image").forEach(function (toggle) {
    toggle.addEventListener("click", function () {
      var card = toggle.closest(".team-card");
      if (card) {
        card.classList.toggle("team-card--open");
        toggle.setAttribute("aria-expanded", card.classList.contains("team-card--open"));
      }
    });
  });

  /* ============================
  // Testimonials Slider
  ============================ */
  if (document.querySelector(".my-slider")) {
    var slider = tns({
      container: ".my-slider",
      items: 3,
      slideBy: 1,
      gutter: 32,
      nav: true,
      mouseDrag: true,
      autoplay: false,
      speed: 500,
      controlsContainer: "#customize-controls",
      responsive: {
        1024: {
          items: 3,
        },
        768: {
          items: 2,
        },
        0: {
          items: 1,
        }
      }
    });
  }


  /* ============================
  // Image Carousel with Lightbox
  ============================ */

  /* ============================
  // Shared image lightbox (used by carousels and standalone images)
  ============================ */
  var pageLightbox = document.getElementById('page-lightbox');
  var openImageLightbox = function () {}; // no-op default if no lightbox on page

  // Resolve the highest-resolution source for an image. Body/cover images are
  // wrapped in <picture> with a width-capped srcset and a smaller fallback
  // `src` (e.g. 800px), so img.src can be SMALLER than what's displayed.
  // Prefer the largest candidate across the picture's <source> srcsets and the
  // img's own srcset; fall back to currentSrc, then src.
  function largestImageSrc(img) {
    var best = { url: null, w: -1 };
    function consider(srcset) {
      if (!srcset) return;
      srcset.split(',').forEach(function (part) {
        var seg = part.trim().split(/\s+/);
        if (!seg[0]) return;
        var w = seg[1] && seg[1].slice(-1) === 'w' ? parseInt(seg[1], 10) : 0;
        if (w >= best.w) { best.w = w; best.url = seg[0]; }
      });
    }
    var picture = img.closest('picture');
    if (picture) {
      picture.querySelectorAll('source').forEach(function (s) {
        // Prefer real srcset; data-srcset is the lazy-load placeholder form.
        consider(s.getAttribute('srcset') || s.getAttribute('data-srcset'));
      });
    }
    consider(img.getAttribute('srcset') || img.getAttribute('data-srcset'));
    return best.url || img.currentSrc || img.src;
  }

  if (pageLightbox) {
    var lbImage = pageLightbox.querySelector('.image-lightbox__image');
    var lbCaption = pageLightbox.querySelector('.image-lightbox__caption');
    var lbClose = pageLightbox.querySelector('.image-lightbox__close');
    var lbOverlay = pageLightbox.querySelector('.image-lightbox__overlay');
    var lbPrev = pageLightbox.querySelector('.image-lightbox__prev');
    var lbNext = pageLightbox.querySelector('.image-lightbox__next');
    var lbCurrent = pageLightbox.querySelector('.image-lightbox__current');
    var lbTotal = pageLightbox.querySelector('.image-lightbox__total');

    var lbImages = [];
    var lbIndex = 0;
    var lbMode = 'single';

    function lbRender() {
      var item = lbImages[lbIndex];
      if (!item) return;
      lbImage.src = item.src;
      lbImage.alt = item.alt || '';
      if (lbCaption) lbCaption.textContent = item.caption || '';
      if (lbCurrent) lbCurrent.textContent = lbIndex + 1;
      if (lbTotal) lbTotal.textContent = lbImages.length;
    }

    function lbNextImage() {
      if (lbMode !== 'gallery') return;
      lbIndex = (lbIndex + 1) % lbImages.length;
      lbRender();
    }

    function lbPrevImage() {
      if (lbMode !== 'gallery') return;
      lbIndex = (lbIndex - 1 + lbImages.length) % lbImages.length;
      lbRender();
    }

    function lbCloseFn() {
      pageLightbox.classList.remove('is-active');
      pageLightbox.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lightbox-open');
    }

    openImageLightbox = function (images, startIndex, mode) {
      lbImages = images || [];
      lbIndex = startIndex || 0;
      lbMode = mode === 'gallery' ? 'gallery' : 'single';
      if (!lbImages.length) return;
      pageLightbox.classList.toggle('is-single', lbMode === 'single');
      lbRender();
      pageLightbox.classList.add('is-active');
      pageLightbox.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lightbox-open');
      if (lbClose) lbClose.focus();
    };

    if (lbClose) lbClose.addEventListener('click', lbCloseFn);
    if (lbOverlay) lbOverlay.addEventListener('click', lbCloseFn);
    if (lbNext) lbNext.addEventListener('click', lbNextImage);
    if (lbPrev) lbPrev.addEventListener('click', lbPrevImage);

    document.addEventListener('keydown', function (e) {
      if (!pageLightbox.classList.contains('is-active')) return;
      if (e.key === 'Escape') { lbCloseFn(); e.preventDefault(); }
      if (e.key === 'ArrowRight') { lbNextImage(); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { lbPrevImage(); e.preventDefault(); }
    });
  }

  document.querySelectorAll('.image-carousel').forEach(function(carouselContainer) {
    var slider = carouselContainer.querySelector('.image-carousel__slider');
    if (!slider) return;

    var id = slider.id;
    var items = parseInt(slider.dataset.items) || 3;
    var itemsTablet = parseInt(slider.dataset.itemsTablet) || 2;
    var itemsMobile = parseInt(slider.dataset.itemsMobile) || 1;
    var gutter = parseInt(slider.dataset.gutter) || 20;
    var loop = slider.dataset.loop !== 'false';

    // Initialize Tiny Slider carousel
    var carousel = tns({
      container: '#' + id,
      items: items,
      slideBy: 1,
      gutter: gutter,
      nav: true,
      navPosition: 'bottom',
      mouseDrag: true,
      autoplay: false,
      loop: loop,
      speed: 500,
      controlsContainer: '#' + id + '-controls',
      responsive: {
        1024: {
          items: items,
        },
        768: {
          items: itemsTablet,
        },
        0: {
          items: itemsMobile,
        }
      }
    });

    // Keyboard navigation for carousel when focused
    slider.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowLeft') {
        carousel.goTo('prev');
        e.preventDefault();
      }
      if (e.key === 'ArrowRight') {
        carousel.goTo('next');
        e.preventDefault();
      }
    });

    // Lightbox: feed the shared page-level lightbox in gallery mode.
    if (!pageLightbox) return;

    // Build the gallery image list from original (non-clone) slides
    var originalImages = Array.from(
      carouselContainer.querySelectorAll('.image-carousel__slide:not(.tns-slide-cloned) img')
    );
    var galleryItems = originalImages.map(function (img) {
      return { src: largestImageSrc(img), alt: img.alt, caption: img.dataset.caption || '' };
    });

    // Click ANY slide image (including clones) -> open shared lightbox at matching index
    var allSlideImages = Array.from(carouselContainer.querySelectorAll('.image-carousel__slide img'));
    allSlideImages.forEach(function (img) {
      img.addEventListener('click', function () {
        var idx = originalImages.findIndex(function (o) { return o.src === img.src; });
        if (idx !== -1) openImageLightbox(galleryItems, idx, 'gallery');
      });
    });
  });


  /* ============================
  // Standalone content images: click-to-expand (desktop only)
  ============================ */
  (function () {
    if (!pageLightbox) return;
    var desktop = window.matchMedia('(min-width: 768px) and (pointer: fine)');
    if (!desktop.matches) return; // mobile / touch: no handlers, no zoom cursor

    var content = document.querySelector('.post__content');
    if (!content) return;

    var candidates = Array.from(content.querySelectorAll('img'));
    candidates.forEach(function (img) {
      if (img.closest('.image-carousel')) return;      // carousels handle their own
      if (img.classList.contains('no-zoom')) return;   // explicit opt-out
      if (img.classList.contains('no-lightense')) return; // existing opt-out convention
      if (img.closest('a')) return;                    // linked image: let the link win

      img.classList.add('is-zoomable');
      img.addEventListener('click', function () {
        openImageLightbox([{ src: largestImageSrc(img), alt: img.alt, caption: img.alt }], 0, 'single');
      });
    });
  })();


  // =====================
  // Load More Posts
  // =====================
  var load_posts_button = document.querySelector('.load-more-posts');

  load_posts_button&&load_posts_button.addEventListener("click",function(e){e.preventDefault();var o=document.querySelector(".pagination"),e=pagination_next_url.split("/page")[0]+"/page/"+pagination_next_page_number+"/";fetch(e).then(function(e){if(e.ok)return e.text()}).then(function(e){var n=document.createElement("div");n.innerHTML=e;for(var t=document.querySelector(".grid"),a=n.querySelectorAll(".grid__post"),i=0;i<a.length;i++)t.appendChild(a.item(i));new LazyLoad({elements_selector:".lazy"});pagination_next_page_number++,pagination_next_page_number>pagination_available_pages_number&&(o.style.display="none")})});


  /* =======================
  // Scroll Top Button
  ======================= */
  btnScrollToTop.addEventListener("click", function () {
    if (window.scrollY != 0) {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
      })
    }
  });

});