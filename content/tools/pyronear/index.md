---
title: Pyronear
weight: 10
show_title: false
button_cta: Visit Pyronear
icon: /images/logos/pyronear_logo_letters.png
logo_container: true
summary: Democratizing open and low-tech solutions for fighting wildfires. An early detection solution that is open source, efficient, automatic, energy-efficient, economical and modular.
github_repo: https://github.com/earthtoolsmaker/pyronear-mlops
landing_page_url: https://pyronear.org/en/
project: /projects/early_forest_fire_detection
js: /js/biowatch.js
date: 2025-05-01
---

<div class="tool-container-button-cta">
  <a class="link-no-decoration" href="https://pyronear.org/en" target="_blank">
    <button class="button tool-button-cta">
    Visit Pyronear
    </button>
  </a>
</div>

## Wildfire Early Real Time Detection System

Pyronear is a complete fire risk management solution. It consists of an early
wildfire detection algorithm, implemented on a microcomputer, connected to
cameras positioned on high spots with a view on the forest. The detectors
communicate fire alerts to a database that is connected to a supervision
platform for fire departments.

{{< image_carousel id="pyronear-gallery" items="2" >}}
  {{< carousel_image src="./images/platform1.png" alt="Pyronear Platform Alert" caption="Fire alert triggered on the Pyronear web platform, showing detected wildfire location and camera feed." >}}
  {{< carousel_image src="./images/platform2.png" alt="Pyronear Platform Overview" caption="Fire management platform interface for fire departments to monitor and respond to alerts." >}}
{{< /image_carousel >}}
<br />
<br />

## Key Features

- 🧠 __Cutting-Edge AI Model__: Advanced computer vision models are designed to
detect wildfires in real time. These models continuously improve their accuracy
through regular retraining with incoming data.
- 🔥 __Web Fire Management Platform__: An intuitive web application that
showcases recent fire alerts and enhances fire management efficiency for fire
departments.

## See Pyronear in Action

The video below, filmed in the Forest of Fontainebleau, shows how the system
works end to end: a firefighter walks through the full pipeline, from the
cameras spotting the first signs of smoke to the alert reaching the fire
department.

<p><iframe src="https://www.youtube.com/embed/W3DxacGsdks" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">End-to-end demonstration of the Pyronear system in the Forest of Fontainebleau
</em>
<br/>

The computer vision model detected a forest fire in Fontainebleau from a
distance of 35 kilometers in real time, setting a new record for the Pyronear
system. The video below shows a thin black smoke rising in the distance.

<p><iframe src="https://www.youtube.com/embed/i9Qy-zY16Ew" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Real-time forest fire detection from 35 kilometers away in Fontainebleau
</em>
<br/>

## Try the Models in Your Browser

Two interactive demos let you run the Pyronear models on real data, right
from this website:

- 🔥 [__Single-frame detection__]({{< ref "/spaces/early_forest_fire_detection" >}}) —
  upload a camera image and watch the detector draw boxes around smoke.
- 🕐 [__Temporal smoke verification__]({{< ref "/spaces/temporal_smoke_verification" >}}) —
  the second-stage model that watches whole *sequences*: real wildfires get
  caught within minutes while clouds, fog, and haze look-alikes are rejected.
  This is the model that cuts false alarms by 4× in production.

Below, the temporal verifier judging real camera sequences — pick one and
watch it play:

{{< hf_space "achouffe-temporal-smoke-pyronear" "6.18.0" >}}
