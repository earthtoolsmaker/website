---
title: "Biowatch: Camera Trap Data, Visualized"
summary: A free, open-source desktop application for visualizing camera trap data to support conservation efforts.
clients:
  - name: OSI Panthera
    link: https://www.osi-panthera.org/
    logo: /images/clients/osi-panthera/logo.jpg
  - name: OSI
    link: https://www.science-camps.com/
    logo: /images/clients/osi/logo.png
tools:
  - React
  - Electron
  - Mapbox
  - Camtrap DP
status: completed
github_repo: https://github.com/earthtoolsmaker/biowatch
pinned: true
date: 2025-02-20
image: /images/projects/observation_visualisations_app/cover.png
---

## 🦊 Biowatch is Here

What started as a prototype is now **Biowatch** — a free, open-source desktop application that lets conservationists analyze, visualize, and explore camera trap datasets entirely offline. It runs on Windows, macOS, and Linux, and your sensitive wildlife data never leaves your computer.

<div style="display: flex; gap: 1em; flex-wrap: wrap; margin: 1.5em 0;">
  <a class="link-no-decoration" href="/tools/biowatch/">
    <button class="button button--cta">Download Biowatch</button>
  </a>
  <a class="link-no-decoration" href="https://biowatch.earthtoolsmaker.org/" target="_blank">
    <button class="button">Read the Manual</button>
  </a>
</div>

## The Growing Role of Recording Devices in Conservation

In recent years, conservation efforts have increasingly relied on various recording devices such as camera traps and acoustic sensors. Their growing popularity is driven by technological advancements, reduced costs, and the ability to collect extensive data non-invasively. These tools have revolutionized wildlife monitoring, providing researchers with invaluable data on animal behavior, population dynamics, and ecosystem changes. However, as the volume of recorded data grows, so does the challenge of managing, analyzing, and effectively utilizing it.

## Bridging the Gap: Making Data Accessible to Conservationists

Despite advancements in AI, conservationists often struggle to make use of processed data due to a lack of technical skills or funding for specialized analytics. Simply classifying species in images is not enough—researchers need user-friendly tools to interactively explore trends, spatial patterns, and ecological insights derived from their datasets.

Biowatch addresses this challenge. Unlike web-based platforms like [Wildlife Insights](https://www.wildlifeinsights.org/), this desktop app keeps your data private, handles large datasets without lengthy uploads, and stays usable in remote field locations. Installation is a simple double-click—no technical expertise required.

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
  {{< carousel_image src="/images/projects/observation_visualisations_app/overview.png" alt="Biowatch study overview" caption="Overview: each study opens with an interactive map, key metrics, the best captures, and the full species distribution with IUCN status." >}}
  {{< carousel_image src="/images/projects/observation_visualisations_app/explore-map.png" alt="Explore tab density heatmap" caption="Explore: switch the map between species pie-charts, abundance, a density heatmap, or a hex grid, alongside activity charts." >}}
  {{< carousel_image src="/images/projects/observation_visualisations_app/annotation.png" alt="Gallery viewer with bounding boxes" caption="Annotate: step through images, adjust bounding boxes, and correct AI predictions before they become observations." >}}
  {{< carousel_image src="/images/projects/observation_visualisations_app/ai-models.png" alt="On-device AI model settings with coverage map" caption="On-device AI: download SpeciesNet, MegaDetector, DeepFaune, or Manas and pick the right model for your region from the coverage map." >}}
  {{< carousel_image src="/images/projects/observation_visualisations_app/deployments.png" alt="Per-deployment activity timeline" caption="Deployments: per-camera activity timelines, heatmaps, and editable metadata you can export and re-import as CSV." >}}
  {{< carousel_image src="/images/projects/observation_visualisations_app/export.png" alt="Camtrap DP export dialog" caption="Export: publish to GBIF as a Camtrap DP package, or export media organized into one folder per species." >}}
{{< /image_carousel >}}

<p style="text-align:center;"><em>A glimpse of Biowatch in action — explore the full <a href="https://biowatch.earthtoolsmaker.org/">online manual</a> for guided walkthroughs.</em></p>

## Technical Approach

Biowatch is built with [Electron](https://www.electronjs.org/) and [React](https://react.dev/), chosen for their strong ecosystems to encourage contributions and maximise longevity. [Mapbox](https://www.mapbox.com/) powers the interactive mapping, and the project is fully open-source on GitHub to encourage community collaboration. AI models run on device, so identification works without an internet connection once a model is downloaded.

## Conclusion

Biowatch bridges the gap between AI-powered classification and practical conservation insights. By giving researchers and conservationists intuitive, private, and offline visualizations, we hope to make wildlife monitoring more effective and accessible—ultimately contributing to better conservation outcomes.

The app is free to download and the code is open for anyone to inspect, use, and improve.
