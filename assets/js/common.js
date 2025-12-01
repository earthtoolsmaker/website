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
  // Zoom Image
  ======================= */
  const lightense = document.querySelector(".page__content img, .post__content img, .project-content img, .gallery__image img"),
  imageLink = document.querySelectorAll(".page__content a img, .post__content a img, .project-content a img, .gallery__image a img");

  if (imageLink) {
    for (var i = 0; i < imageLink.length; i++) imageLink[i].parentNode.classList.add("image-link");
    for (var i = 0; i < imageLink.length; i++) imageLink[i].classList.add("no-lightense");
  }

  if (lightense) {
    Lightense(".page__content img:not(.no-lightense), .post__content img:not(.no-lightense), .project-content img:not(.no-lightense), .gallery__image img:not(.no-lightense)", {
    padding: 60,
    offset: 30
    });
  }


  /* ============================
  // Partners Slider
  ============================ */
  if (document.querySelector(".partners-slider")) {
    var partnersSlider = tns({
      container: ".partners-slider",
      items: 1,
      slideBy: 1,
      gutter: 32,
      nav: true,
      mouseDrag: true,
      autoplay: false,
      speed: 500,
      controlsContainer: "#partners-controls"
    });
  }

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

    // Lightbox functionality
    var lightbox = document.getElementById(id + '-lightbox');
    if (!lightbox) return;

    var lightboxImage = lightbox.querySelector('.image-lightbox__image');
    var lightboxCaption = lightbox.querySelector('.image-lightbox__caption');
    var lightboxClose = lightbox.querySelector('.image-lightbox__close');
    var lightboxOverlay = lightbox.querySelector('.image-lightbox__overlay');
    var lightboxPrev = lightbox.querySelector('.image-lightbox__prev');
    var lightboxNext = lightbox.querySelector('.image-lightbox__next');
    var lightboxCurrent = lightbox.querySelector('.image-lightbox__current');
    var lightboxTotal = lightbox.querySelector('.image-lightbox__total');

    // Collect only original images (exclude Tiny Slider clones) for lightbox navigation
    var images = Array.from(carouselContainer.querySelectorAll('.image-carousel__slide:not(.tns-slide-cloned) img'));
    // Collect ALL images (including clones) for click handlers
    var allImages = Array.from(carouselContainer.querySelectorAll('.image-carousel__slide img'));
    var currentIndex = 0;

    // Update lightbox total count
    if (lightboxTotal) {
      lightboxTotal.textContent = images.length;
    }

    function openLightbox(index) {
      currentIndex = index;
      updateLightboxImage();
      lightbox.classList.add('is-active');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lightbox-open');
      // Focus the close button for accessibility
      if (lightboxClose) {
        lightboxClose.focus();
      }
    }

    function closeLightbox() {
      lightbox.classList.remove('is-active');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lightbox-open');
    }

    function updateLightboxImage() {
      var img = images[currentIndex];
      if (img) {
        lightboxImage.src = img.src;
        lightboxImage.alt = img.alt;
        if (lightboxCurrent) {
          lightboxCurrent.textContent = currentIndex + 1;
        }
        // Update caption (empty string hides it via CSS :empty)
        if (lightboxCaption) {
          lightboxCaption.textContent = img.dataset.caption || '';
        }
      }
    }

    function nextImage() {
      currentIndex = (currentIndex + 1) % images.length;
      updateLightboxImage();
    }

    function prevImage() {
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      updateLightboxImage();
    }

    // Click on ANY image (including clones) to open lightbox
    allImages.forEach(function(img) {
      img.addEventListener('click', function() {
        // Find the matching original image by src
        var originalIndex = images.findIndex(function(origImg) {
          return origImg.src === img.src;
        });
        if (originalIndex !== -1) {
          openLightbox(originalIndex);
        }
      });
    });

    // Close lightbox
    if (lightboxClose) {
      lightboxClose.addEventListener('click', closeLightbox);
    }
    if (lightboxOverlay) {
      lightboxOverlay.addEventListener('click', closeLightbox);
    }

    // Navigate lightbox
    if (lightboxNext) {
      lightboxNext.addEventListener('click', nextImage);
    }
    if (lightboxPrev) {
      lightboxPrev.addEventListener('click', prevImage);
    }

    // Keyboard navigation for lightbox
    document.addEventListener('keydown', function(e) {
      if (!lightbox.classList.contains('is-active')) return;

      if (e.key === 'Escape') {
        closeLightbox();
        e.preventDefault();
      }
      if (e.key === 'ArrowRight') {
        nextImage();
        e.preventDefault();
      }
      if (e.key === 'ArrowLeft') {
        prevImage();
        e.preventDefault();
      }
    });
  });


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