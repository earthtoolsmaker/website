---
title: Interactive desktop application for visualizing camera trap data
summary: An open-source desktop application for visualizing camera trap data to support conservation efforts.
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
status: fundraising
github_repo: https://github.com/earthtoolsmaker/biowatch
pinned: true
date: 2025-02-20
image: /images/projects/observation_visualisations_app/cover.jpg
---

## 😇 Looking for Funding

{{< donate_sponsor_cta >}}

<br/>

## The Growing Role of Recording Devices in Conservation

In recent years, conservation efforts have increasingly relied on various recording devices such as camera traps and acoustic sensors. Their growing popularity is driven by technological advancements, reduced costs, and the ability to collect extensive data non-invasively. These tools have revolutionized wildlife monitoring, providing researchers with invaluable data on animal behavior, population dynamics, and ecosystem changes.  However, as the volume of recorded data grows, so does the challenge of managing, analyzing, and effectively utilizing it.

## Advancements in Machine Learning for Camera Trap Data

Machine learning (ML) has played a pivotal role in addressing data processing challenges, leading to the development of numerous tools designed to automate species identification and behavior analysis. Surveys such as the [Camera Trap Data Management Survey on Wildlabs](https://wildlabs.net/discussion/camera-trap-data-management-survey-results) and catalogs like the [Camera Trap ML Survey showcase](https://agentmorris.github.io/camera-trap-ml-survey/) the growing ecosystem of ML-based solutions. However, while AI-driven classification has made data processing more efficient, the focus has largely remained on the automation aspect rather than on how conservationists can explore and interpret the processed results.

## Bridging the Gap: Making Data Accessible to Conservationists

Despite advancements in AI, conservationists often struggle to make use of processed data due to a lack of technical skills or funding for specialized analytics. Simply classifying species in images is not enough—researchers need user-friendly tools to interactively explore trends, spatial patterns, and ecological insights derived from their datasets.

To address this challenge, we are developing a cross-platform desktop application that will enable conservationists to locally import classified observations and visualize the data through interactive tools. Unlike web-based platforms like [Wildlife Insights](https://www.wildlifeinsights.org/), a desktop app ensures data privacy, supports large datasets without the need for extensive uploads, and remains accessible in remote field locations. Our goal is to create an application that is easy to install and use—requiring no technical expertise beyond a simple double-click installation.

## Features

Our application will provide a suite of visualization tools designed to enhance data exploration:

- Spatio-temporal analysis: An interactive map displaying camera trap locations, heatmaps, and species distribution over time.
- Species filtering: Users can filter observations by species to analyze trends and behavioral patterns.
- Daily and seasonal activity patterns: Charts displaying animal activity fluctuations at different times of the day and across seasons.
- Advanced analytics: Population estimation models, multi-species interaction analysis, and individual animal tracking.

{{< gallery caption="Gallery / Current Prototype for visualizing camera trap data on an interactive map" >}}
  {{< gallery_image src="/images/projects/observation_visualisations_app/map.png" alt="Interactive map showing camera trap locations" >}}
  {{< gallery_image src="/images/projects/observation_visualisations_app/bounding_boxes.png" alt="Grid of wildlife pictures with bounding boxes" >}}
  {{< gallery_image src="/images/projects/observation_visualisations_app/seasonal_daily_activity.png" alt="4 circular charts showing daily activity over the year" >}}
{{< /gallery >}}

## Technical Approach

We are building our application using [Electron](https://www.electronjs.org/) and [React](https://react.dev/), leveraging their popularity and strong ecosystems to encourage contributions and maximise longevity. [Mapbox](https://www.mapbox.com/) will be used for interactive mapping, and the project will be open-source on GitHub to encourage community collaboration and contributions.

## Conclusion

With this interactive data exploration tool, we aim to bridge the gap between AI-powered classification and practical conservation insights. By empowering researchers and conservationists with intuitive visualizations, we hope to make wildlife monitoring more effective and accessible, ultimately contributing to better conservation outcomes.
