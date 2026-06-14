---
title: "Biowatch: Camera Trap Data, Visualized"
summary: A free, open-source desktop application for visualizing camera trap data to support conservation efforts.
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
pinned: true
date: 2025-02-20
image: /images/projects/biowatch-app/cover.png
aliases:
  - /projects/observation_visualisations_app/
---

## 🦊 Biowatch is Here

What started as a prototype is now **[Biowatch](/tools/biowatch/)** — a free, open-source desktop application that lets conservationists analyze, visualize, and explore camera trap datasets entirely offline. It runs on Windows, macOS, and Linux, and your sensitive wildlife data never leaves your computer.

<div style="display: flex; gap: 1em; flex-wrap: wrap; margin: 1.5em 0;">
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

## What Biowatch Does

Biowatch turns a folder of raw camera trap images, or a published dataset, into an interactive study you can explore:

- **Import from anywhere** — scan a folder of your own images, open a [Camtrap DP](https://camtrap-dp.tdwg.org/) package, or pull curated datasets straight from [GBIF](https://www.gbif.org/) and [LILA BC](https://lila.science/). Wildlife Insights and DeepFaune CSV exports are supported too.
- **On-device species identification** — run AI models locally to detect and identify animals as a study is built. SpeciesNet (Google, 2,000+ species worldwide), MegaDetector (Microsoft), DeepFaune (CNRS, Europe), and Manas (snow leopards in the Himalayas) are available, with a coverage map to pick the right one for your region.
- **Interactive spatio-temporal analysis** — an Explore tab with camera locations rendered as species pie charts, abundance markers, density heatmaps, or hex grids, alongside daily-activity clocks and seasonal timelines.
- **Species filtering** — select species to compare their distributions and activity patterns, with consistent colors across maps and charts.
- **Review and correct** — step through images in a gallery viewer, adjust bounding boxes, and fix AI predictions before they become observations.
- **Deployment insights** — per-deployment activity timelines, heatmaps, and editable metadata you can export and re-import as CSV.
- **Standards-based export** — publish to GBIF as a Camtrap DP package, or export media organized into one folder per species.

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

<div style="display: flex; gap: 1em; flex-wrap: wrap; margin: 1.5em 0;">
  <a class="link-no-decoration" href="/tools/biowatch/">
    <button class="button button--cta">Download Biowatch</button>
  </a>
  <a class="link-no-decoration" href="https://biowatch.earthtoolsmaker.org/" target="_blank">
    <button class="button">Read the Manual</button>
  </a>
</div>
