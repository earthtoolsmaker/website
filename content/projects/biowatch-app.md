---
title: "Biowatch: Camera Trap Data, Visualized"
summary: A free, open-source desktop application for visualizing camera trap data to support conservation efforts.
tags: ["camera traps", "vision"]
related_projects:
  - snow_leopard_monitoring
  - bear_identification
  - bird_flu_monitoring
related_spaces:
  - /demos/bear_identification/
  - /demos/snowleopard_identification/
tagline: A free, open-source desktop app that turns a folder of camera-trap images into living ecological insight — entirely offline.
stats:
  - value: "Free"
    label: "& open-source"
  - value: "100%"
    label: offline
  - value: "Win / macOS / Linux"
    label: desktop app
tools:
  - Computer Vision
  - Machine Learning
  - Camera Traps
  - Interactive Map
clients:
  - name: OSI Panthera
    link: https://www.osi-panthera.org/
    logo: /images/clients/osi-panthera/logo.jpg
  - name: INBO
    link: https://www.inbo.be/
    logo: /images/clients/inbo/logo.jpg
status: completed
github_repo: https://github.com/earthtoolsmaker/biowatch
pinned: false
date: 2025-02-20
image: /images/projects/biowatch-app/cover.png
aliases:
  - /projects/observation_visualisations_app/
---

## Biowatch is Here

What started as a prototype is now **[Biowatch](/tools/biowatch/)** — a free, open-source desktop application that lets conservationists analyze, visualize, and explore camera trap datasets entirely offline. It runs on Windows, macOS, and Linux, and your sensitive wildlife data never leaves your computer.

<div style="display: flex; gap: 1em; flex-wrap: wrap; justify-content: center; margin: 1.5em 0;">
  <a class="link-no-decoration" href="/tools/biowatch/">
    <button class="button button--cta">Download Biowatch</button>
  </a>
  <a class="link-no-decoration" href="https://biowatch.earthtoolsmaker.org/" target="_blank">
    <button class="button">Read the Manual</button>
  </a>
</div>

## From Raw Footage to Real Insight

Camera traps have transformed wildlife monitoring: they gather huge volumes of data non-invasively and at low cost. But AI that classifies the species in those images only solves half the problem. Conservationists still have to make sense of the results—spot spatial patterns, track activity over time, and turn millions of detections into ecological insight—often without specialist software or a dedicated data team.

Most tools stop at classification, or live on the web behind accounts and uploads. Biowatch is different. It's a desktop app that keeps your data private, handles large datasets without lengthy uploads, and works in remote field locations. Installation is a simple double-click—no technical expertise required—and unlike web platforms such as [Wildlife Insights](https://www.wildlifeinsights.org/), nothing ever leaves your machine.

![How Biowatch works — import images or datasets, identify species on-device, explore the results on maps and activity charts, then export to GBIF or tidy per-species folders](/images/projects/biowatch-app/diagrams/workflow.svg)
*From raw images to a published study: import from anywhere, identify species on
your own machine, explore patterns in space and time, then export to open
standards — all without your data leaving your computer.*

## What Biowatch Does

Biowatch turns a folder of raw camera trap images, or a published dataset, into an interactive study you can explore.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Import from anywhere</h3>
    <p class="support__card-description">Scan a folder of your own images, open a <a href="https://camtrap-dp.tdwg.org/">Camtrap DP</a> package, or pull curated datasets straight from <a href="https://www.gbif.org/">GBIF</a> and <a href="https://lila.science/">LILA BC</a> — Wildlife Insights and DeepFaune CSV exports included.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">On-device species ID</h3>
    <p class="support__card-description">Run AI models locally to detect and identify animals as a study builds: SpeciesNet (Google, 2,000+ species), MegaDetector (Microsoft), DeepFaune (CNRS, Europe) and Manas (Himalayan snow leopards), with a coverage map to pick the right one for your region.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Explore in space &amp; time</h3>
    <p class="support__card-description">See camera locations as species pie-charts, abundance, density heatmaps or hex grids, alongside daily-activity clocks and seasonal timelines — and filter species to compare their distributions and patterns.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Review &amp; correct</h3>
    <p class="support__card-description">Step through images in a gallery viewer, adjust bounding boxes, and fix AI predictions before they ever become observations.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Deployment insights</h3>
    <p class="support__card-description">Per-camera activity timelines and heatmaps, with editable metadata you can export and re-import as CSV.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Standards-based export</h3>
    <p class="support__card-description">Publish to GBIF as a Camtrap DP package, or export media organized into one tidy folder per species.</p>
  </div>

</div>

Everything runs locally. No cloud uploads, no accounts, no tracking—ideal for the sensitive location data of endangered species.

{{< image_carousel id="biowatch-project-gallery" items="1" items_tablet="1" items_mobile="1" >}}
  {{< carousel_image src="/images/projects/biowatch-app/overview.png" alt="Biowatch study overview" caption="Overview: each study opens with an interactive map, key metrics, the best captures, and the full species distribution with IUCN status." >}}
  {{< carousel_image src="/images/projects/biowatch-app/explore-map.png" alt="Explore tab density heatmap" caption="Explore: switch the map between species pie-charts, abundance, a density heatmap, or a hex grid, alongside activity charts." >}}
  {{< carousel_image src="/images/projects/biowatch-app/annotation.png" alt="Gallery viewer with bounding boxes" caption="Annotate: step through images, adjust bounding boxes, and correct AI predictions before they become observations." >}}
  {{< carousel_image src="/images/projects/biowatch-app/ai-models.png" alt="On-device AI model settings with coverage map" caption="On-device AI: download SpeciesNet, MegaDetector, DeepFaune, or Manas and pick the right model for your region from the coverage map." >}}
  {{< carousel_image src="/images/projects/biowatch-app/deployments.png" alt="Per-deployment activity timeline" caption="Deployments: per-camera activity timelines, heatmaps, and editable metadata you can export and re-import as CSV." >}}
  {{< carousel_image src="/images/projects/biowatch-app/export.png" alt="Camtrap DP export dialog" caption="Export: publish to GBIF as a Camtrap DP package, or export media organized into one folder per species." >}}
{{< /image_carousel >}}

<p style="text-align:center;"><em>A glimpse of Biowatch in action — explore the full <a href="https://biowatch.earthtoolsmaker.org/">online manual</a> for guided walkthroughs.</em></p>

## Free, Open Source, and Built in the Open

Biowatch is free to download for Windows, macOS, and Linux, and the full source is on [GitHub](https://github.com/earthtoolsmaker/biowatch) for anyone to inspect, use, or improve. Built together with conservation partners, it closes the gap between AI classification and practical insight—making wildlife monitoring more effective, more private, and more accessible.

<div style="display: flex; gap: 1em; flex-wrap: wrap; justify-content: center; margin: 1.5em 0;">
  <a class="link-no-decoration" href="/tools/biowatch/">
    <button class="button button--cta">Download Biowatch</button>
  </a>
  <a class="link-no-decoration" href="https://biowatch.earthtoolsmaker.org/" target="_blank">
    <button class="button">Read the Manual</button>
  </a>
</div>
