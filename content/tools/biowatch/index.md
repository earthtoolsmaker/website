---
title: Biowatch
show_title: true
button_cta: Download and Install
icon: /images/logos/biowatch-icon.png
summary: Biowatch is a powerful tool for wildlife researchers and conservationists to analyze, visualize, and explore CamtrapDP datasets with ease.
github_repo: https://github.com/earthtoolsmaker/biowatch
project: /projects/observation_visualisations_app
date: 2025-05-01
js: /js/biowatch.js
all_downloads_url: https://github.com/earthtoolsmaker/biowatch/releases/tag/v1.0.11
---

<div class="tool-container-button-cta" id="container-button-download-biowatch">
  <a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch-setup.exe" id="download-windows">
    <button class="button">
      Biowatch for Windows
    </button>
  </a>
  <a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch.dmg" id="download-mac">
    <button class="button">
      Biowatch for Mac
    </button>
  </a>
  <a class="link-no-decoration" href="https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch.AppImage" id="download-linux">
    <button class="button">
      Biowatch for Linux
    </button>
  </a>
</div>

# Explore Camera Trap Datasets with Biowatch

Biowatch is a powerful tool for wildlife researchers and conservationists to
analyze, visualize, and explore [CamtrapDP
datasets](https://camtrap-dp.tdwg.org/) with ease.

<div class="gallery-box">
  <div class="gallery">
      <img src="./images/medias.png" loading="lazy" alt="Biowatch Medias" class="lightense-enabled" />
      <img src="./images/activity.png" loading="lazy" alt="Biowatch Activity" class="lightense-enabled" />
      <img src="./images/overview.png" loading="lazy" alt="Biowatch Overview" class="lightense-enabled" />
  </div>
</div>
<br />
<br />

## Key Features

- 🗺️ __Interactive Maps__: Visualize camera trap locations and wildlife sightings with interactive maps and spatial analysis tools.
- 📊 __Data Analysis__: Generate insights with powerful analytics tools, species identification, and temporal activity patterns.
- 🗃️ __Media Management__: Organize, tag, and search through thousands of camera trap images and videos with ease.
<br />
<br />


## About


Biowatch was developed to help researchers, conservationists, and wildlife
enthusiasts analyze camera trap data more effectively. Our mission is to
provide tools that make wildlife monitoring more accessible and insightful.

Whether you're tracking endangered species, studying animal behavior, or
monitoring biodiversity, Biowatch provides the tools you need to turn your
camera trap data into actionable insights.

<script>
window.addEventListener("load", () => {
  console.log(getOsInfo());
  const { os, url, text } = getOsInfo();
  const container = document.getElementById("container-button-download-biowatch");
  container.querySelector(`#download-${os} button`).classList.add("tool-button-cta")
});
</script>
