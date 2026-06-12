---
title: Biowatch
show_title: true
button_cta: Download and Install
icon: /images/logos/biowatch-icon.png
summary: Open-source desktop app for analyzing camera trap data. Runs 100% locally — your sensitive wildlife data never leaves your computer.
github_repo: https://github.com/earthtoolsmaker/biowatch
project: /projects/observation_visualisations_app
date: 2025-05-01
js:
  - /js/biowatch.js
  - /js/tabs.js
all_downloads_url: https://github.com/earthtoolsmaker/biowatch/releases/tag/v1.0.11
---

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

# Analyze Camera Trap Data — Privately, On Your Machine

Biowatch is a free, open-source desktop application that lets you analyze, visualize, and explore camera trap datasets entirely offline. Your sensitive wildlife data never gets uploaded to any server — everything runs locally on your computer.

{{< image_carousel id="biowatch-gallery" >}}
  {{< carousel_image src="./images/overview.png" alt="Biowatch study overview" caption="Overview: every study opens with an interactive map, key metrics, the best captures, and the full species distribution with IUCN status." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/explore.png" alt="Biowatch Explore tab" caption="Explore: map camera locations as species pie-charts, abundance, or density heatmaps, with daily-activity and seasonal charts alongside." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/media.png" alt="Biowatch media library" caption="Media: browse, filter, and search thousands of camera trap images and videos by species, deployment, and detection." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/annotation.png" alt="Reviewing AI detections with bounding boxes" caption="Annotate: step through images, adjust bounding boxes, and correct AI predictions before they become observations." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/ai-models.png" alt="On-device AI model settings" caption="On-device AI: download SpeciesNet, MegaDetector, DeepFaune, or Manas and pick the right model for your region from the coverage map." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/export.png" alt="Camtrap DP export dialog" caption="Export: publish to GBIF as a Camtrap DP package, or export your media organized into one folder per species." shadow="false" rounded="false" >}}
{{< /image_carousel >}}

## Why Biowatch?

- __100% Offline & Private__: Your research data stays on your machine. No cloud uploads, no accounts, no tracking. Perfect for sensitive location data of endangered species.
- __Open Source__: Inspect the code, contribute improvements, or adapt it for your needs. Built transparently by the conservation community, for the conservation community.
- __On-Device AI__: Run powerful species identification models directly on your computer — no internet required after setup.

## Key Features

- 🗺️ __Interactive Maps__: Visualize camera trap locations and wildlife sightings with interactive maps and spatial analysis tools.
- 📊 __Data Analysis__: Generate insights with temporal activity patterns, species distributions, and deployment statistics.
- 🗃️ __Media Management__: Browse, filter, and search through thousands of camera trap images and videos.
- 🤖 __AI Species Identification__: Automatically classify wildlife using state-of-the-art models.
- 📦 __CamtrapDP Compatible__: Import and export using the [Camera Trap Data Package](https://camtrap-dp.tdwg.org/) standard for seamless data sharing with GBIF and biodiversity platforms.
- 📁 __Flexible Export__: Export images organized by species or as standardized CamtrapDP packages ready for publication.

## Installation

{{< tabs labels="<i class='fa-brands fa-windows' style='color: #0078D6;'></i>::Windows|<i class='fa-brands fa-apple' style='color: #555555;'></i>::macOS|<i class='fa-brands fa-linux' style='color: #000000;'></i>::Linux" id="installation-tabs" >}}
{{< tab index="0" markdown="true" >}}
1. Download the installer above
2. Run `biowatch-setup.exe`
3. Follow the installation wizard
4. Launch Biowatch from the Start menu or desktop shortcut
{{< /tab >}}
{{< tab index="1" markdown="true" >}}
1. Download the `.dmg` file above
2. Open the disk image
3. Drag Biowatch to your Applications folder
4. On first launch, right-click the app and select "Open" (required for apps from outside the App Store)
{{< /tab >}}
{{< tab index="2" markdown="true" >}}
**AppImage (recommended):**
1. Download the `.AppImage` file above
2. Make it executable: `chmod +x Biowatch.AppImage`
3. Run it: `./Biowatch.AppImage`

**Debian/Ubuntu:**
1. Download the `.deb` package from [all releases](https://github.com/earthtoolsmaker/biowatch/releases)
2. Install: `sudo dpkg -i Biowatch_*.deb`
{{< /tab >}}
{{< /tabs >}}

<br />

<p><iframe src="https://www.youtube.com/embed/Ei9zOd_5Qkc" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Biowatch video demo and updates</em>
<br/>


## About

Biowatch was developed to help researchers, conservationists, and wildlife enthusiasts analyze camera trap data more effectively — without compromising on data privacy or requiring expensive cloud services.

Whether you're tracking endangered species in remote locations, studying animal behavior, or monitoring biodiversity, Biowatch provides the tools you need to turn your camera trap data into actionable insights while keeping full control of your data.

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
