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

{{< image_carousel id="biowatch-gallery" >}}
  {{< carousel_image src="./images/medias.png" alt="Biowatch Medias" caption="Browse and manage thousands of camera trap images and videos with powerful search and filtering capabilities." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/activity.png" alt="Biowatch Activity" caption="Analyze temporal activity patterns to understand when and how wildlife uses different areas." shadow="false" rounded="false" >}}
  {{< carousel_image src="./images/overview.png" alt="Biowatch Overview" caption="Get a comprehensive overview of your camera trap deployment with interactive maps and statistics." shadow="false" rounded="false" >}}
{{< /image_carousel >}}

## Key Features

- 🗺️ __Interactive Maps__: Visualize camera trap locations and wildlife sightings with interactive maps and spatial analysis tools.
- 📊 __Data Analysis__: Generate insights with powerful analytics tools, species identification, and temporal activity patterns.
- 🗃️ __Media Management__: Organize, tag, and search through thousands of camera trap images and videos with ease.
<br />
<br />

<p><iframe src="https://www.youtube.com/embed/Ei9zOd_5Qkc" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Biowatch video demo and updates</em>
<br/>


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
