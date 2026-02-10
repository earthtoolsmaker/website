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

This project assessed the feasibility of automated smolt enumeration from ARIS sonar imagery using deep learning-based computer vision. Working with ARIS sonar data from the outflow of Cho’:lhsh?ta Lake (Jansen Lake), British Columbia, we developed and tested an end-to-end analysis pipeline combining object detection models with tracking algorithms.

{{< image_carousel id="smolt-monitoring-intro" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_overview.png" alt="Jansen Lake Map" caption="Jansen Lake, British Columbia, located on Vancouver Island" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_satellite.png" alt="Jansen Lake Satellite" caption="Jansen Lake, British Columbia, Satellite close up" >}}
{{< /image_carousel >}}

Some key technical achievements include: 
- automated conversion and preprocessing of proprietary .aris format with motion enhanced noise reduction
- detection and tracking of individual smolt
- length estimation of the detected smolt

## Introduction

Hydroacoustic imaging is a widely used and effective method to enumerate fish in waterways but the analysis of the large amounts of data is time consuming and requires trained personnel. 
Methods to facilitate the analysis of hydroacoustic data (hereafter sonar) are much needed but challenging to develop especially due to the background noise and variation in the intensity and type of the return signal of fish. Significant progress has been made in e.g. background subtracking and object detection in software such as []Echoview](https://echoview.com/) and [ArisFish](https://arisfish.software.informer.com/) but reliable algorithms to detect, track and enumerate fish in an automated workflow remains elusive.
Over the last years the fast development of Artificial Intelligence (AI), in particular Deep Neural Networks, has led to rapid progress of image analysis, including automated detection and tracking of fish in sonar imagery. In this project we focus on smolt, which are small (8-14 cm) salmonids on their way to the ocean. Besides the small size which makes them harder to detect and separate from noise compared to adult salmon, they also swim close to the (noisy) water surface and can migrate in dense groups over a short time period. 
The overarching goal of the current project is to assess the feasibility of automated smolt enumeration from sonar data. We do this through first reviewing existing methods and selecting the most promising candidate. 

The [Alouette River](https://en.wikipedia.org/wiki/Alouette_River) is the target site for deployment of sonar smolt enumeration but we were unfortunately not able to collect data in 2025 but could instead use smolt data from the outflow of Jansen Lake. In the second and third year of the project we will apply the workflow to the Alouette River.

## What is ARIS Sonar?

ARIS sonar creates acoustic images using sound reflections, enabling fish detection in conditions where optical cameras fail: turbid water, zero visibility, and nighttime. 

![Sonar Aris Frame](/images/projects/monitoring_smolt_salmon_migration_with_sonar/sonar_aris_frame.png)

## Why count smolt?

Conservation efforts, population monitoring, and migration tracking all depend on accurate fish counts.

The traditional methods rely on manual counting methods which are time-consuming and error prone. Analysts must review hours of sonar footage by hand.
