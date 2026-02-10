---
title: Monitoring Smolt Salmon Migration with Sonar
summary: An innovative use of sonar imagery to monitor and analyze the migration patterns of smolt salmon as they journey from freshwater to the ocean
clients:
  - name: BC Hydro 
    link: https://www.bchydro.com/
    logo: /images/clients/bc-hydro/logo.png
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
tools:
  - Machine Learning
  - Computer Vision
  - Sonar
date: 2026-01-10
image: /images/projects/monitoring_smolt_salmon_migration_with_sonar/cover.png
---

Monitoring smolt — juvenile salmon migrating downstream toward the ocean — is essential for understanding salmon population health and evaluating the impact of hydroelectric infrastructure on fish survival. In partnership with [BC Hydro](https://www.bchydro.com/) and [Lumax AI](https://lumax.ai/), we are developing an automated system to detect, track, and count smolt from ARIS sonar imagery collected at Cho':lhsh?ta Lake (Jansen Lake), British Columbia.

{{< image_carousel id="smolt-monitoring-intro" items="2" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_overview.png" alt="Jansen Lake Map" caption="Jansen Lake, British Columbia, located on Vancouver Island" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_satellite.png" alt="Jansen Lake Satellite" caption="Jansen Lake, British Columbia, Satellite close up" >}}
{{< /image_carousel >}}

## Why count smolt?

### What are smolt?

Smolt are juvenile salmonids (8–14 cm) undergoing smoltification — the physiological transformation that prepares them for the transition from freshwater to saltwater. During this critical life stage, they migrate downstream through rivers and past infrastructure on their way to the ocean.

![Salmon lifecycle](/images/projects/monitoring_smolt_salmon_migration_with_sonar/lifecycle_salmon.png)
*Salmon lifecycle — courtesy of the [Pacific Salmon Foundation](https://psf.ca/learn/species-lifecycle/)*

### Why the smolt stage is critical

The downstream migration is one of the most dangerous periods in a salmon's life. Smolt must navigate past dams, turbines, and other infrastructure that can cause direct mortality or disorientation. They swim close to the water surface where they are vulnerable to predators, and they often travel in dense groups over short time windows. Climate change is adding further pressure through altered river flows and rising water temperatures, compressing migration windows and increasing stress on already vulnerable juveniles.

### Why accurate counting matters

Reliable smolt counts are fundamental for salmon conservation:

- __Population trend assessment__: Tracking smolt numbers over multiple years reveals whether salmon populations are growing, stable, or declining — providing early warning of population collapse.
- __Evaluating dam impact__: Hydroelectric operators like [BC Hydro](https://www.bchydro.com/) need to understand how their infrastructure affects downstream fish survival. Accurate counts above and below dams quantify this impact.
- __Regulatory compliance__: Hydroelectric facilities operate under environmental regulations that require monitoring and mitigating impacts on fish populations. Automated counting provides the consistent, auditable data needed for compliance.
- __Informing management actions__: Smolt abundance data feeds directly into decisions about dam operations, habitat restoration priorities, and fishing quotas for returning adults.

### The challenge of current methods

Traditional smolt counting relies on manual review of sonar footage, which is time-consuming and error-prone. Analysts must watch hours of recordings by hand, identifying and counting individual fish in noisy acoustic images. Dense migration events — where thousands of smolt pass in a short period — make manual review particularly impractical. The sheer volume of data generated during peak migration windows means that manual methods simply cannot scale to provide the continuous, reliable counts that conservation demands.

## What is ARIS Sonar?

ARIS sonar creates acoustic images using sound reflections, enabling fish detection in conditions where optical cameras fail: turbid water, zero visibility, and nighttime. It produces high-resolution, video-like acoustic image sequences that are well suited for detecting and counting small fish like smolt.

![Sonar Aris Frame](/images/projects/monitoring_smolt_salmon_migration_with_sonar/sonar_aris_frame.png)

## Our Approach

### Project scope

The overarching goal of this project is to assess the feasibility of automated smolt enumeration from ARIS sonar data. We do this by reviewing existing methods, selecting the most promising candidates, and developing an end-to-end analysis pipeline combining deep learning-based object detection with tracking algorithms.

### Sonar analysis challenges

Hydroacoustic imaging is a widely used and effective method to enumerate fish in waterways, but the analysis of large amounts of data is time-consuming and requires trained personnel. Methods to facilitate the analysis of sonar data are much needed but challenging to develop, especially due to background noise and variation in the intensity and type of the return signal of fish. Significant progress has been made in background subtraction and object detection in software such as [Echoview](https://echoview.com/) and [ArisFish](https://arisfish.software.informer.com/), but reliable algorithms to detect, track, and enumerate fish in an automated workflow remain elusive.

Over the last years, the fast development of Artificial Intelligence (AI), in particular Deep Neural Networks, has led to rapid progress in image analysis, including automated detection and tracking of fish in sonar imagery. Smolt present unique challenges compared to adult salmon: their small size (8–14 cm) makes them harder to detect and separate from noise, they swim close to the noisy water surface, and they can migrate in dense groups over short time periods.

### Key technical achievements

Some key technical achievements of this project include:
- Automated conversion and preprocessing of proprietary .aris format with motion-enhanced noise reduction
- Detection and tracking of individual smolt using deep learning
- Length estimation of the detected smolt

### Study site

The [Alouette River](https://en.wikipedia.org/wiki/Alouette_River) is the target site for deployment of sonar smolt enumeration. For the first year we used smolt data from the outflow of Jansen Lake, as data collection at the Alouette River was not possible in 2025. In the second and third year of the project we will apply the workflow to the Alouette River.
