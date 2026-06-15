---
title: Biowatch
weight: 30
show_title: true
button_cta: Download and Install
icon: /images/logos/biowatch-icon.png
card_tint: "#e0efec"
summary: Open-source desktop app for analyzing camera trap data. Runs 100% locally — your sensitive wildlife data never leaves your computer.
github_repo: https://github.com/earthtoolsmaker/biowatch
project: /projects/biowatch-app
hide_meta_links: true
date: 2025-05-01
js:
  - /js/biowatch.js
  - /js/tabs.js
all_downloads_url: https://github.com/earthtoolsmaker/biowatch/releases/tag/v1.0.11
---

<!--
  Hero background video: static/videos/biowatch-hero.mp4
  Source: Pexels "Red fox in snowy forest adventure" (pexels.com/video/red-fox-in-snowy-forest-adventure-35628259/)
  License: Pexels License (free for commercial use, no attribution required).
-->
<div class="tool-hero">
  <video class="tool-hero__video" autoplay muted loop playsinline preload="auto" aria-label="A red fox moving through a snowy forest, as a wildlife camera might capture it">
    <source src="/videos/biowatch-hero.mp4" type="video/mp4">
  </video>
  <div class="tool-hero__overlay">
    <h1 class="tool-hero__title">Analyze Camera Trap Data</h1>
    <p class="tool-hero__tagline">A free, open-source desktop app to explore, visualize, and analyze your camera-trap datasets — 100% offline, on your own machine.</p>
  </div>
</div>

<section class="about-stats about-stats--three tools-stats">
  <div class="about-stats__grid">
    <div class="about-stats__item">
      <div class="about-stats__value">100%</div>
      <div class="about-stats__label">offline &amp; private</div>
    </div>
    <div class="about-stats__item">
      <div class="about-stats__value">4</div>
      <div class="about-stats__label">on-device AI models</div>
    </div>
    <div class="about-stats__item">
      <div class="about-stats__value">Free</div>
      <div class="about-stats__label">open source</div>
    </div>
  </div>
</section>

Biowatch is a free, open-source desktop application that lets you analyze, visualize, and explore camera trap datasets entirely offline. Your sensitive wildlife data never gets uploaded to any server — everything runs locally on your computer.

{{< image_carousel id="biowatch-gallery" >}}
  {{< carousel_image src="./images/overview.png" alt="Biowatch study overview" caption="Overview: every study opens with an interactive map, key metrics, the best captures, and the full species distribution with IUCN status." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/explore.png" alt="Biowatch Explore tab" caption="Explore: map camera locations as species pie-charts, abundance, or density heatmaps, with daily-activity and seasonal charts alongside." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/media.png" alt="Biowatch media library" caption="Media: browse, filter, and search thousands of camera trap images and videos by species, deployment, and detection." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/annotation.png" alt="Reviewing AI detections with bounding boxes" caption="Annotate: step through images, adjust bounding boxes, and correct AI predictions before they become observations." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/ai-models.png" alt="On-device AI model settings" caption="On-device AI: download SpeciesNet, MegaDetector, DeepFaune, or Manas and pick the right model for your region from the coverage map." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/export.png" alt="Camtrap DP export dialog" caption="Export: publish to GBIF as a Camtrap DP package, or export your media organized into one folder per species." shadow="false" rounded="false" >}}
{{< /image_carousel >}}

<div class="tool-container-button-cta" id="container-button-download-biowatch">
  <a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch-setup.exe" id="download-windows">
    <button class="button" style="background-color: #0078D6;">
      <i class="fa-brands fa-windows" style="margin-right: 0.5em;"></i>Biowatch for Windows
    </button>
  </a>
  <a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch.dmg" id="download-mac">
    <button class="button" style="background-color: #000000;">
      <i class="fa-brands fa-apple" style="margin-right: 0.5em;"></i>Biowatch for Mac
    </button>
  </a>
  <a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch.AppImage" id="download-linux">
    <button class="button" style="background-color: #FCC624; color: #000000;">
      <i class="fa-brands fa-linux" style="margin-right: 0.5em;"></i>Biowatch for Linux
    </button>
  </a>
</div>

<div class="about-cta" style="margin-bottom: 64px;">
  <h3 class="about-cta__title">New to Biowatch?</h3>
  <p class="about-cta__description">The full online manual walks you through every feature — importing data, exploring studies, annotating images, running AI models, and exporting — with step-by-step guides and screenshots.</p>
  <a href="https://biowatch.earthtoolsmaker.org/" target="_blank" class="link-no-decoration button button--middle">Read the Manual</a>
</div>

## Why Biowatch?

Three things set it apart:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">100% offline &amp; private</h3>
    <p class="support__card-description">Your research data stays on your machine — no cloud uploads, no accounts, no tracking. Built for the sensitive location data of endangered species.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Open source</h3>
    <p class="support__card-description">Inspect the code, contribute improvements, or adapt it to your needs — built transparently by the conservation community, for the conservation community.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">On-device AI</h3>
    <p class="support__card-description">Run powerful species-identification models directly on your computer, with no internet required after setup.</p>
  </div>

</div>

## Key Features

Everything from raw captures to published data:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Import from anywhere</h3>
    <p class="support__card-description">Start from your own image folders, a <a href="https://camtrap-dp.tdwg.org/" target="_blank" rel="noopener">Camtrap DP</a> package, or curated public datasets from <a href="https://www.gbif.org/" target="_blank" rel="noopener">GBIF</a> and <a href="https://lila.science/" target="_blank" rel="noopener">LILA</a> — or try the one-click demo dataset.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">On-device species ID</h3>
    <p class="support__card-description">Detect and identify animals with local AI models — SpeciesNet, MegaDetector, DeepFaune, and Manas — and pick the best fit for your region from a coverage map.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Interactive maps</h3>
    <p class="support__card-description">See camera locations as species pie-charts, abundance markers, or density heatmaps, and filter everything to an area you draw.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Activity &amp; trends</h3>
    <p class="support__card-description">Compare species with daily-activity clocks, seasonal timelines, and per-deployment activity charts.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Media management</h3>
    <p class="support__card-description">Browse, filter, and search thousands of images and videos, review AI detections, and correct bounding boxes.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Standards-based export</h3>
    <p class="support__card-description">Publish to GBIF as a Camtrap DP package, or export your media organized into one folder per species.</p>
  </div>

</div>

## About

Biowatch grew out of a simple conviction: researchers shouldn't have to choose between modern AI tooling and keeping control of sensitive wildlife data.

Whether you're tracking endangered species, studying behavior, or monitoring biodiversity, it turns raw camera-trap captures into clear results — on your own machine, with no cloud, no subscriptions, and no lock-in.

## Installation

{{< tabs labels="<i class='fa-brands fa-windows' style='color: #0078D6;'></i>::Windows|<i class='fa-brands fa-apple' style='color: #555555;'></i>::macOS|<i class='fa-brands fa-linux' style='color: #000000;'></i>::Linux" id="installation-tabs" >}}
{{< tab index="0" markdown="true" >}}
<a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch-setup.exe"><button class="button" style="background-color: #0078D6;"><i class="fa-brands fa-windows" style="margin-right: 0.5em;"></i>Download for Windows</button></a>

1. Run `biowatch-setup.exe`
2. Follow the installation wizard
3. Launch Biowatch from the Start menu or desktop shortcut
{{< /tab >}}
{{< tab index="1" markdown="true" >}}
<a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch.dmg"><button class="button" style="background-color: #000000;"><i class="fa-brands fa-apple" style="margin-right: 0.5em;"></i>Download for Mac</button></a>

1. Open the `.dmg` disk image
2. Drag Biowatch to your Applications folder
3. On first launch, right-click the app and select "Open" (required for apps from outside the App Store)
{{< /tab >}}
{{< tab index="2" markdown="true" >}}
<a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch.AppImage"><button class="button" style="background-color: #FCC624; color: #000000;"><i class="fa-brands fa-linux" style="margin-right: 0.5em;"></i>Download AppImage</button></a>

**AppImage (recommended):**
1. Make it executable: `chmod +x Biowatch.AppImage`
2. Run it: `./Biowatch.AppImage`

**Debian/Ubuntu:**
1. Download the `.deb` package from [all releases](https://github.com/earthtoolsmaker/biowatch/releases)
2. Install: `sudo dpkg -i Biowatch_*.deb`
{{< /tab >}}
{{< /tabs >}}

<div class="support__cta-band">
  <div class="support__cta-band-text">
    <h3 class="support__cta-band-title">Ready to try it?</h3>
    <p class="support__cta-band-description">Biowatch is free and open source — and built in the open. Download it for Windows, macOS, or Linux, or help us keep developing it.</p>
  </div>
  <div class="support__cta-band-buttons">
    <a class="link-no-decoration" href="#container-button-download-biowatch"><button class="button">Download Biowatch</button></a>
    <a class="link-no-decoration" href="/support/"><button class="button button--ghost">Support development</button></a>
  </div>
</div>

<script>
window.addEventListener("load", () => {
  const { os } = getOsInfo();

  // Highlight the appropriate download button
  if (os) {
    const container = document.getElementById("container-button-download-biowatch");
    container.querySelector(`#download-${os} button`).classList.add("tool-button-cta");
  }

  // Auto-select the tab matching the user's OS
  const osToTabIndex = { "windows": 0, "mac": 1, "linux": 2 };
  const tabIndex = osToTabIndex[os];
  if (tabIndex !== undefined) {
    const tabsContainer = document.querySelector('.tabs[data-tabs]');
    if (tabsContainer) {
      const targetTab = tabsContainer.querySelector(`[data-tab="${tabIndex}"]`);
      if (targetTab) {
        targetTab.click();
      }
    }
  }
});
</script>
