---
title: SalmonVision
weight: 20
show_title: false
button_cta: Visit SalmonVision
icon: /images/logos/salmon-vision-logo.svg
logo_container: true
card_tint: "#dceef1"
summary: Underwater cameras, sonar and drones combined with innovative AI technology to enable precise and automated salmon counting in rivers.
github_repo: https://github.com/Salmon-Computer-Vision/salmon-computer-vision
project: /projects/wild_salmon_migration_monitoring
js:
  - /js/biowatch.js
  - /js/tabs.js
date: 2024-10-01
---

# Automate Salmon Monitoring

SalmonVision is a collaborative system for counting wild salmon as they return to their natal streams. It combines underwater cameras, sonar, and drones with computer-vision models that detect, classify, and count fish in real time — turning a labour-intensive manual task into precise, automated reports.

Built with the Pacific Salmon Foundation, the Wild Salmon Center, Lumax AI, and Simon Fraser University, it gives conservationists the reliable population data they need to manage fisheries, protect habitat, and meet regulatory targets.

{{< image_carousel id="salmonvision-gallery" items="2" >}}
  {{< carousel_image src="/images/projects/wild_salmon_migration_monitoring/system_overview.png" alt="SalmonVision system overview" caption="System overview: cameras, sonar, and drones feed a computer-vision pipeline that counts and classifies migrating salmon." >}}
  {{< carousel_image src="/images/projects/wild_salmon_migration_monitoring/webapp_overview.png" alt="SalmonVision web application" caption="Web application: count reports and video clips from every site, centralized in one dashboard." >}}
  {{< carousel_image src="/images/projects/wild_salmon_migration_monitoring/sonar/haida-sonar.jpg" alt="Sonar setup at the Haida site" caption="Sonar in the field: an acoustic counter deployed at the Haida site for low-visibility water." >}}
  {{< carousel_image src="/images/projects/wild_salmon_migration_monitoring/drone/drone_imagery.webp" alt="Drone photogrammetry of a salmon stream" caption="Drone photogrammetry of a freshwater stream where salmon migrate — courtesy of Lumax AI." >}}
{{< /image_carousel >}}

<div class="about-cta">
  <h3 class="about-cta__title">See the models in action</h3>
  <p class="about-cta__description">Run the SalmonVision models on real underwater-camera and sonar footage, and watch them count migrating fish — right from your browser.</p>
  <a href="#demos" class="link-no-decoration button button--middle">Try the live demos</a>
</div>

<br/>
<br/>

## Why SalmonVision

SalmonVision pairs multi-sensor hardware with computer vision to deliver counts that were previously impossible to gather at scale.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Automated counting</h3>
    <p class="support__card-description">Computer-vision models count and classify fish migrating upstream in real time, replacing slow, error-prone manual tallies.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Multi-sensor coverage</h3>
    <p class="support__card-description">Underwater cameras, sonar, and drones work in unison to track populations across clear, murky, and hard-to-reach river conditions.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Species classification</h3>
    <p class="support__card-description">Models recognize the main Pacific salmon species — and other fish — on the fly, not just a single overall count.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Exportable reports</h3>
    <p class="support__card-description">Daily count reports are generated and exported to support fisheries management, habitat protection, and regulatory compliance.</p>
  </div>

</div>

<br/>
<br/>

## How It Works

Three sensing modalities feed the same computer-vision pipeline, each suited to different sites and water conditions.

<div class="support__grid">

  <div class="support__card support__track">
    <span class="support__track-label">Optical</span>
    <h3 class="support__card-title">Underwater cameras</h3>
    <p class="support__card-description">Motion-triggered underwater cameras wake when a fish passes, and the computer-vision system counts and classifies each individual by species.</p>
  </div>

  <div class="support__card support__track">
    <span class="support__track-label">Acoustic</span>
    <h3 class="support__card-title">Sonar</h3>
    <p class="support__card-description">Acoustic sonar counts fish in low-visibility water where cameras struggle — including juvenile smolt migrating downstream past dams and turbines.</p>
  </div>

  <div class="support__card support__track">
    <span class="support__track-label">Aerial</span>
    <h3 class="support__card-title">Drones</h3>
    <p class="support__card-description">Aerial photogrammetry surveys whole stream reaches from above, helping estimate fish populations and movement where fixed sensors can't reach.</p>
  </div>

</div>

<br/>
<br/>

## Interactive Demos {#demos}

Two interactive demos let you run the SalmonVision models on real data, right from this website.

{{< tabs labels="::Underwater camera|::Sonar smolt" id="salmonvision-demos" >}}
{{< tab index="0" >}}

Choose an underwater-camera clip and watch the model draw boxes around salmon, classify the species, and count individuals.

{{< hf_space "earthtoolsmaker-salmon-vision" >}}

{{< /tab >}}
{{< tab index="1" >}}

Run the sonar pipeline on ARIS footage to detect, track, and count juvenile smolt as they migrate downstream.

{{< hf_space "Lumax-eco-sonar-smolt" "5.49.1" >}}

{{< /tab >}}
{{< /tabs >}}

<br/>
<br/>

## See SalmonVision in Action

The video below, filmed at Bear Creek River, shows the underwater monitoring system going live: as fish swim past, the camera activates and the system counts them in real time.

<p><iframe src="https://www.youtube.com/embed/V-rZSeM5YtY" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Underwater Camera Activated at Bear Creek River: Monitoring System Now Live</em>
<br/>

<div class="about-cta">
  <h3 class="about-cta__title">Explore the full SalmonVision platform</h3>
  <p class="about-cta__description">See deployments, count dashboards, and how to get involved on the SalmonVision website.</p>
  <a href="https://salmonvision.org" class="link-no-decoration button button--middle" target="_blank">Visit SalmonVision</a>
</div>
