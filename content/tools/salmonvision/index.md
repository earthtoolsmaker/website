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
manual_url: https://salmonvision.org/user-guide/
project: /projects/wild_salmon_migration_monitoring
js:
  - /js/biowatch.js
  - /js/tabs.js
date: 2024-10-01
---

<div class="tool-hero">
  <video class="tool-hero__video" autoplay muted loop playsinline preload="auto" aria-label="Underwater footage of salmon migrating upstream">
    <source src="/videos/salmonvision-hero.mp4" type="video/mp4">
  </video>
  <div class="tool-hero__overlay">
    <h1 class="tool-hero__title">Automate Salmon Monitoring</h1>
    <p class="tool-hero__tagline">Empowering wild salmon conservation through collaborative, AI-powered monitoring.</p>
  </div>
</div>

SalmonVision is a collaborative system for counting wild salmon as they return to their natal streams. It combines underwater cameras, sonar, and drones with computer-vision models that detect, classify, and count fish in real time — turning a labour-intensive manual task into precise, automated reports.

Built with the Pacific Salmon Foundation, the Wild Salmon Center, Lumax AI, and Simon Fraser University, it gives conservationists the reliable population data they need to manage fisheries, protect habitat, and meet regulatory targets.

<section class="about-stats about-stats--three tools-stats">
  <div class="about-stats__grid">
    <div class="about-stats__item">
      <div class="about-stats__value">24/7</div>
      <div class="about-stats__label">automated monitoring</div>
    </div>
    <div class="about-stats__item">
      <div class="about-stats__value">20</div>
      <div class="about-stats__label">monitoring projects</div>
    </div>
    <div class="about-stats__item">
      <div class="about-stats__value">1M+</div>
      <div class="about-stats__label">salmon counted</div>
    </div>
  </div>
</section>

{{< image_carousel id="salmonvision-gallery" items="2" >}}
  {{< carousel_image src="/images/tools/salmonvision/review-interface.png" alt="Reviewing salmon detections in the SalmonVision web app" caption="Review interface: the model boxes each fish, classifies the species (Pink, Sockeye…), and tallies counts along a timeline for a reviewer to confirm." >}}
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

<p><iframe src="https://lumax-eco-sonar-smolt.hf.space" loading="lazy" frameborder="0" style="width:100%;height:1000px;border:0;"></iframe></p>

{{< /tab >}}
{{< /tabs >}}

<br/>
<br/>

## See SalmonVision in Action

Inside the web app, the model tracks each fish across frames and proposes a species and count for a reviewer to confirm. The short clip below — from the SalmonVision user guide — shows a review session in progress.

<p><video controls muted loop playsinline preload="metadata" style="width:100%;border-radius:12px;"><source src="/videos/salmonvision-tracking.mp4" type="video/mp4"></video></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Reviewing detections in the SalmonVision web app — bounding boxes, species labels, and counts on a timeline.</em>
<br/>

And in the field, the video below — filmed at Bear Creek River — shows the underwater monitoring system going live: as fish swim past, the camera activates and the system counts them in real time.

<p><iframe src="https://www.youtube.com/embed/V-rZSeM5YtY" loading="lazy" frameborder="0" allowfullscreen style="width:100%;height:auto;aspect-ratio:16/9;"></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Underwater Camera Activated at Bear Creek River: Monitoring System Now Live</em>
<br/>

## Frequently Asked Questions

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">How accurate is it?</h3>
    <p class="support__card-description">Models reach over 95% accuracy for salmon detection and counting in good conditions, with 90–95% species classification. Accuracy depends on water clarity, lighting, and camera placement.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">What footage does it work with?</h3>
    <p class="support__card-description">Video from underwater cameras, weirs, fish ladders, and drones, in standard formats and across a wide range of field conditions.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Which species can it identify?</h3>
    <p class="support__card-description">The main Pacific salmon species — Steelhead, Sockeye, Pink, Coho, Chum, and Chinook — plus other fish such as trout, whitefish, and lamprey.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Is it open source?</h3>
    <p class="support__card-description">The computer-vision models are released under the MIT license, and the training datasets under CC BY-NC-SA 4.0, to support conservation worldwide.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">What does it cost?</h3>
    <p class="support__card-description">The web application is free for educational and research use. Conservation groups and Indigenous communities may qualify for subsidized or complimentary access.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Can you build a custom model?</h3>
    <p class="support__card-description">Yes — models can be fine-tuned or built from scratch for your specific watershed, camera setup, or target species.</p>
  </div>

</div>

<br/>
<br/>

<div class="about-cta">
  <h3 class="about-cta__title">Explore the full SalmonVision platform</h3>
  <p class="about-cta__description">See deployments, count dashboards, and how to get involved on the SalmonVision website.</p>
  <a href="https://salmonvision.org" class="link-no-decoration button button--middle" target="_blank">Visit SalmonVision</a>
</div>
