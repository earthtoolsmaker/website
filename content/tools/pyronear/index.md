---
title: Pyronear
weight: 10
show_title: false
button_cta: Visit Pyronear
icon: /images/logos/pyronear_logo_letters.png
logo_container: true
card_tint: "#fce3d8"
summary: Democratizing open and low-tech solutions for fighting wildfires. An early detection solution that is open source, efficient, automatic, energy-efficient, economical and modular.
github_repo: https://github.com/pyronear
project: /projects/early_forest_fire_detection
js:
  - /js/biowatch.js
  - /js/tabs.js
date: 2025-05-01
---

# Open, Real-Time Wildfire Detection

Pyronear is a complete, open-source fire-detection system. A computer-vision model runs on a low-power microcomputer wired to cameras on high vantage points, watching the forest for the first signs of smoke. When it detects a fire, it sends an alert to a supervision platform used by fire departments — efficient, automatic, energy-efficient, and modular by design.

The video below, filmed in the Forest of Fontainebleau, shows how the system works end to end: a firefighter walks through the full pipeline, from the cameras spotting the first signs of smoke to the alert reaching the fire department.

<p><iframe src="https://www.youtube.com/embed/W3DxacGsdks" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">End-to-end demonstration of the Pyronear system in the Forest of Fontainebleau</em>
<br/>

{{< image_carousel id="pyronear-gallery" items="2" >}}
  {{< carousel_image src="./images/platform1.png" alt="Pyronear Platform Alert" caption="Fire alert triggered on the Pyronear web platform, showing detected wildfire location and camera feed." >}}
  {{< carousel_image src="./images/platform2.png" alt="Pyronear Platform Overview" caption="Fire management platform interface for fire departments to monitor and respond to alerts." >}}
{{< /image_carousel >}}

<div class="about-cta">
  <h3 class="about-cta__title">See the models in action</h3>
  <p class="about-cta__description">Run the Pyronear detector on real camera images and watch the temporal verifier judge live wildfire sequences — right from your browser.</p>
  <a href="#demos" class="link-no-decoration button button--middle">Try the live demos</a>
</div>

<br/>
<br/>

## Why Pyronear

Pyronear pairs cutting-edge detection with open, low-tech hardware that communities can deploy themselves.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Cutting-edge AI detection</h3>
    <p class="support__card-description">Computer-vision models detect wildfire smoke in real time and keep improving as new field data comes in.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Web fire-management platform</h3>
    <p class="support__card-description">An intuitive web app surfaces recent alerts and streamlines response for fire departments.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Open source and low-tech</h3>
    <p class="support__card-description">Built in the open on affordable, off-the-shelf hardware that communities can deploy and maintain themselves.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Energy-efficient and economical</h3>
    <p class="support__card-description">Runs on low-power microcomputers at the edge, keeping running costs and energy use low.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Modular by design</h3>
    <p class="support__card-description">Detection, alerting, and the supervision platform are separable pieces you can adapt to local needs.</p>
  </div>

</div>

<br/>
<br/>

## Interactive Demos {#demos}

Two interactive demos let you run the Pyronear models on real data, right from this website.

{{< tabs labels="::Single-frame detection|::Temporal verification" id="pyronear-demos" >}}
{{< tab index="0" >}}

Upload a camera image and watch the detector draw boxes around smoke.

{{< hf_space "earthtoolsmaker-forest-fire-pyronear" >}}

{{< /tab >}}
{{< tab index="1" >}}

The second-stage model watches whole sequences: real wildfires get caught within minutes while clouds, fog, and haze look-alikes are rejected. This is the model that cuts false alarms by 4× in production.

{{< hf_space "achouffe-temporal-smoke-pyronear" "6.18.0" >}}

{{< /tab >}}
{{< /tabs >}}

<br/>
<br/>

## How It Works

Pyronear catches fires in two stages: a fast detector proposes candidate smoke, then a temporal model confirms it before an alert goes out.

<div class="support__grid support__grid--two">

  <div class="support__card support__track">
    <span class="support__track-label">Stage one</span>
    <h3 class="support__card-title">Single-frame detection</h3>
    <p class="support__card-description">A computer-vision model runs on each camera frame in real time, proposing candidate regions wherever it sees something that looks like smoke. It runs on a low-power microcomputer at the camera site, so only alerts — not video — travel over the network.</p>
    <div class="support__track-proof">In production, it detected a fire in Fontainebleau from 35 kilometers away.</div>
    <ul class="support__track-offers">
      <li>Real-time inference at the edge on low-power hardware</li>
      <li>Continuously retrained as new field data arrives</li>
      <li>Sends lightweight alerts, not raw footage</li>
    </ul>
  </div>

  <div class="support__card support__track">
    <span class="support__track-label">Stage two</span>
    <h3 class="support__card-title">Temporal verification</h3>
    <p class="support__card-description">Candidate detections are tracked over time and a temporal classifier decides whether they actually behave like smoke. Real wildfires get confirmed within minutes, while clouds, fog, and haze look-alikes are filtered out before anyone is alerted.</p>
    <div class="support__track-proof">Cuts false alarms by 4× compared with single-frame detection alone.</div>
    <ul class="support__track-offers">
      <li>Tracks candidates across a full image sequence</li>
      <li>Rejects clouds, fog, and haze that fool single frames</li>
      <li>Keeps fire departments focused on real events</li>
    </ul>
  </div>

</div>

<br/>
<br/>

## See Pyronear in Action

The computer vision model detected a forest fire in Fontainebleau from a distance of 35 kilometers in real time, setting a new record for the Pyronear system. The video below shows a thin black smoke rising in the distance.

<p><iframe src="https://www.youtube.com/embed/i9Qy-zY16Ew" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Real-time forest fire detection from 35 kilometers away in Fontainebleau</em>
<br/>

<div class="about-cta">
  <h3 class="about-cta__title">Explore the full Pyronear platform</h3>
  <p class="about-cta__description">See live deployments, the fire-management platform, and how to get involved on the Pyronear website.</p>
  <a href="https://pyronear.org/en" class="link-no-decoration button button--middle" target="_blank">Visit Pyronear</a>
</div>
