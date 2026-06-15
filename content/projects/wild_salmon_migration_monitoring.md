---
title: Wild Salmon Migration Monitoring
summary: The project monitors wild salmon migration to ensure the number passing through meets state regulations, addressing threats from human activities like fisheries and dams.
tagline: Automated, multi-sensor counting that keeps Pacific salmon runs within regulation.
stats:
  - value: "14"
    label: fish species recognized
  - value: "3"
    label: sensing modalities
  - value: "24/7"
    label: automated counting
  - value: "20"
    label: sites monitored
  - value: "1M+"
    label: salmon counted
github_repo: https://github.com/Salmon-Computer-Vision/salmon-computer-vision/tree/master
space: /demos/wild_salmon_migration_monitoring/
clients:
  - name: Pacific Salmon Foundation
    link: https://psf.ca/
    logo: /images/clients/psf/logo.png
    bg: inverted
  - name: Wild Salmon Centre
    link: https://wildsalmoncenter.org/
    logo: /images/clients/wild_salmon_centre/logo.png
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
  - name: Simon Fraser University
    link: https://sfu.ca/
    logo: /images/clients/sfu/logo.png
related_posts:
  - tracking-the-journey-how-to-monitor-wild-salmon-migrations
tools:
  - Computer Vision
  - Machine Learning
  - Sonar
  - Drones
threats:
  - name: Habitat loss
    desc: "Urban development, logging and agriculture degrade and destroy the spawning and rearing streams salmon depend on."
  - name: Dams &amp; barriers
    desc: "Dams, weirs and culverts obstruct migration routes, cutting fish off from the spawning and rearing habitat upstream."
  - name: Overfishing
    desc: "Unsustainable harvest depletes populations and erodes the genetic diversity that keeps runs resilient."
  - name: Climate change
    desc: "Warming water and shifting flows disrupt migration timing and the narrow temperature windows salmon need to survive and spawn."
  - name: Pollution
    desc: "Runoff from farms, industry and urban areas contaminates waterways, harming salmon health and survival."
  - name: Disease &amp; parasites
    desc: "Contact with farmed fish can spread diseases and parasites to wild salmon, weakening already-stressed populations."
status: completed
pinned: true
weight: 2
date: 2024-08-20
image: /images/projects/wild_salmon_migration_monitoring/cover.png
js:
  - /js/tabs.js
---

Pacific salmon are born in freshwater, migrate out to the ocean, and then fight
their way back — often hundreds of miles — to spawn in the very stream where
they hatched. After spawning they die, and their bodies feed the river that
raised them. That return is the heartbeat of British Columbia's watersheds: it
feeds bears, eagles and orcas, carries ocean nutrients far inland, and anchors
the culture and economy of the communities along the water.

![The Pacific salmon life cycle](/images/projects/wild_salmon_migration_monitoring/lifecycle_salmon.png)
*The Pacific salmon life cycle — courtesy of the [Pacific Salmon Foundation](https://psf.ca/learn/species-lifecycle/).*

Knowing how many fish actually make it back is the single most important number
in salmon management — escapement targets exist to guarantee enough survive to
spawn. But counting them by hand, river by river, season after season, simply
does not scale. Together with the [Pacific Salmon Foundation](https://psf.ca/),
the [Wild Salmon Center](https://wildsalmoncenter.org/),
[Lumax AI](https://lumax.ai/) and [Simon Fraser University](https://www.sfu.ca/),
we built [__SalmonVision__](https://salmonvision.org/) — a multi-sensor system
that counts and identifies migrating salmon automatically, around the clock.

> We must take every step in our control now as climate-change related trends
> will make things more difficult for salmon populations in the years ahead.
> This demands urgency for Pacific salmon and for the 130+ species, including
> grizzlies, orcas and eagles, that depend on Pacific salmon.
>
> <cite>– Pacific Salmon Foundation</cite>

![From underwater footage to a counted run — the SalmonVision pipeline](/images/projects/wild_salmon_migration_monitoring/diagrams/pipeline.svg)
*Sensors watch the river, a computer-vision model detects and identifies each
fish, and individuals are tallied into a count managers can act on.*

<p><video autoplay muted loop playsinline preload="metadata" style="width:100%;border-radius:12px;"><source src="/videos/salmonvision-hero.mp4" type="video/mp4"></video></p>
<p class="media-caption">Wild salmon holding in the current, filmed by an underwater monitoring camera.</p>

## Why wild salmon matter

Salmon are a keystone species: pull them out of the picture and the whole web
around the river begins to fray.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">A nutrient highway</h3>
    <p class="support__card-description">Returning salmon carry marine nutrients far inland. As their bodies decompose, nitrogen and phosphorus feed the streams, the surrounding forests, and the bears, eagles and wolves that depend on the run.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">A cultural keystone</h3>
    <p class="support__card-description">For many First Nations across British Columbia, salmon are central to food security, heritage and spiritual life. The health of the run and the health of the community are inseparable.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Biodiversity &amp; economy</h3>
    <p class="support__card-description">Healthy salmon populations underpin the region's biodiversity and sustain fisheries, tourism and local livelihoods — which is exactly why well-managed, sustainable runs matter.</p>
  </div>

</div>

## Salmon under pressure

Wild salmon in BC and around the world are squeezed from every side. Habitat is
lost to development and logging; dams and culverts block migration routes;
unsustainable fishing thins the run; pollution degrades the water; and a warming
climate raises river temperatures and scrambles the timing of the migration.
Each pressure compounds the others — and you cannot manage what you cannot
measure. That is why an accurate, continuous count is the foundation beneath
every other conservation decision.

{{< threats >}}

## How SalmonVision counts a run

At the core is a computer-vision model that watches the river and does the work
a human reviewer used to do by hand — frame by frame, fish by fish.

![How the vision model turns one underwater frame into an identified fish](/images/projects/wild_salmon_migration_monitoring/diagrams/detection.svg)
*Each frame runs through the model, which boxes every fish and labels its
species with a confidence score.*

### Three ways we count

No single sensor works in every river, so SalmonVision pairs the same vision
pipeline with three complementary ways of seeing the water.

<div class="support__grid">

  <div class="support__card support__track">
    <span class="support__track-label">Optical</span>
    <h3 class="support__card-title">Underwater cameras</h3>
    <p class="support__card-description">Motion-triggered cameras wake as a fish passes and feed clear footage to the model, which counts and classifies each individual by species.</p>
    <div class="support__track-proof">The <strong>workhorse</strong> of most sites — best in clear, well-lit water.</div>
    <ul class="support__track-offers">
      <li>Species-level counts</li>
      <li>Real-time, motion-triggered</li>
      <li>Daily count reports</li>
    </ul>
  </div>

  <div class="support__card support__track">
    <span class="support__track-label">Acoustic</span>
    <h3 class="support__card-title">Sonar</h3>
    <p class="support__card-description">Acoustic sonar counts fish in murky, dark or turbulent water where cameras fail — including juvenile smolt migrating downstream past dams.</p>
    <div class="support__track-proof">Sees with <strong>sound</strong>, so it keeps working in zero visibility and at night.</div>
    <ul class="support__track-offers">
      <li>Works in silty, dark water</li>
      <li>Day and night</li>
      <li>Counts juvenile smolt too</li>
    </ul>
  </div>

  <div class="support__card support__track">
    <span class="support__track-label">Aerial</span>
    <h3 class="support__card-title">Drones</h3>
    <p class="support__card-description">Aerial photogrammetry surveys whole stream reaches from above, reaching places fixed sensors can't and mapping where fish move.</p>
    <div class="support__track-proof">Covers <strong>wide reaches</strong> and remote stretches in a single flight.</div>
    <ul class="support__track-offers">
      <li>Whole-reach coverage</li>
      <li>Maps movement patterns</li>
      <li>Reaches remote sites</li>
    </ul>
  </div>

</div>

### In the field

Three complementary sensors, one shared vision pipeline — switch between them to
see each in action.

{{< tabs labels="::Underwater cameras|::Sonar|::Drones" id="salmon-field" >}}
{{< tab index="0" markdown="true" >}}

Motion-triggered underwater cameras are the backbone of the system. When a fish
swims into view, the camera wakes and the model counts and classifies it in real
time.

{{< youtube id=V-rZSeM5YtY >}}
<p class="media-caption">An underwater monitoring camera goes live at Bear Creek — as fish pass, the system wakes and counts them.</p>

{{< /tab >}}
{{< tab index="1" markdown="true" >}}

Where the water is silty, dark or fast, light-based cameras struggle. Sonar uses
sound instead, so it keeps counting in zero-visibility conditions and at night.
We push the same idea further in our sister project on [monitoring juvenile
smolt with ARIS sonar]({{< ref "/projects/monitoring_smolt_salmon_migration_with_sonar" >}}).

![Setting up sonar at the Haida site](/images/projects/wild_salmon_migration_monitoring/sonar/haida-sonar.jpg)
*An acoustic sonar counter deployed at the Haida site, where silty water defeats optical cameras.*

{{< youtube id=DlKYhipkSNk >}}
<p class="media-caption">Sonar detects and counts fish acoustically — no light required.</p>

{{< /tab >}}
{{< tab index="2" markdown="true" >}}

For wider stretches of river, drones survey from above — mapping reaches that
fixed sensors can't cover.

![Drone photogrammetry of a salmon stream](/images/projects/wild_salmon_migration_monitoring/drone/drone_imagery.webp)
*Photogrammetry of a freshwater stream where salmon migrate — courtesy of [Lumax AI](https://lumax.ai).*

{{< /tab >}}
{{< /tabs >}}

### In the web app

Every detection flows into a review app, where counts are tallied on a timeline
and a person can confirm the model's work — turning continuous footage into
trustworthy, exportable reports.

![A salmon under review in the SalmonVision web app](/images/tools/salmonvision/review-interface.png)
*In the review interface, each fish is tracked, boxed and classified by species
for a reviewer to confirm.*

<p><video controls muted loop playsinline preload="metadata" style="width:100%;border-radius:12px;"><source src="/videos/salmonvision-tracking.mp4" type="video/mp4"></video></p>
<p class="media-caption">Reviewing detections in the app — bounding boxes, species labels and a running count on a timeline.</p>

<div class="about-cta">
  <h3 class="about-cta__title">Explore the full SalmonVision platform</h3>
  <p class="about-cta__description">See deployments, live count dashboards, and how to get involved on the SalmonVision website.</p>
  <a href="https://salmonvision.org" class="link-no-decoration button button--middle" target="_blank" rel="noopener">Visit SalmonVision</a>
</div>

## The species we recognize

SalmonVision identifies the main Pacific salmon species as they pass the
camera — not just a single overall fish count.

{{< salmon_species >}}

Beyond the salmon above, the system also recognizes Bull Trout, Rainbow Trout,
Whitefish, Shiner, Pikeminnow, Jack Chinook, Lamprey, and Cutthroat Trout.

## Built with First Nations

First Nations across the North and Central Coast of British Columbia are at the
heart of this work — contributing data and expertise to train the models, and
leading their use for salmon stewardship within their own territories, alongside
the research and conservation partners who sustain SalmonVision.

## Conclusion

A wild salmon migration monitoring system turns the hardest, most tedious part
of conservation — counting — into reliable, continuous data. With accurate
numbers in hand, managers can set fishing quotas, prioritize habitat
restoration, hold infrastructure to account, and give communities a transparent
picture of the runs they depend on.

{{< demo_cta >}}
