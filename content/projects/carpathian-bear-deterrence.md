---
title: Bear Deterrence in the Carpathians
summary: Utilizing low-power technology to detect and deter bears from encroaching on Romanian farms.
tagline: Spotting bears at the farm's edge and scaring them off — harmlessly — before conflict starts.
stats:
  - value: "Real-time"
    label: bear detection
  - value: "Low-power"
    label: edge device
  - value: "Non-lethal"
    label: deterrent
aliases:
  - /projects/human_wildlife_bear_conflict/
clients:
  - name: HackThePlanet
    link: https://www.hack-the-planet.io
    logo: /images/clients/hacktheplanet/logo.png
  - name: Foundation Conservation Carpathia
    link: https://www.carpathia.org/
    logo: /images/clients/carpathia/logo.svg
related_posts:
  - how-to-build-a-real-time-bear-detection-system
github_repo: https://gitlab.com/fruitpunch/projects/ai-for-bears/face-detection-and-segmentation/albear
space: /demos/human_wildlife_bear_conflict/
tools:
  - "Computer Vision"
  - "Machine Learning"
pressures:
  - name: Habitat loss &amp; fragmentation
    desc: "Deforestation, farming and infrastructure shrink and split bear habitat, making it harder to forage, den and breed."
  - name: Human–wildlife conflict
    desc: "As people move into bear country, raids on livestock and crops trigger retaliation — and bears are often killed in response."
  - name: Poaching &amp; trade
    desc: "Bears are still poached for fur, claws and organs used in medicine, rituals or as trophies."
  - name: Climate change
    desc: "Shifting food and vegetation patterns and warmer winters disrupt denning, foraging and the timing bears rely on."
  - name: Habitat degradation
    desc: "Mining, logging and disturbance degrade the habitats bears need, even where they aren't lost outright."
  - name: Weak legal protection
    desc: "In some regions, thin legal protection or weak enforcement leaves bears exposed to exploitation."
status: completed
date: 2024-04-02
pinned: true
image: /images/projects/human_wildlife_conflict_bear/cover_unsplash.jpg
---

The Carpathian Mountains of Romania are home to the largest brown bear
population in Europe. Bears and people have shared these valleys for
centuries, but as villages expand and bears learn that farms mean easy
calories, encounters are becoming more frequent — and more dangerous for
both sides.

![Carpathian village](/images/projects/human_wildlife_conflict_bear/skydancer/carpathian_village.webp)
*A village in the Carpathian Mountains, Romania, where bears regularly venture close to farms and homes*

Brown bears serve as pivotal indicators and umbrella species, playing a
crucial role in ecological balance. Managing Human-Wildlife Conflict in
regions inhabited by these apex predators is paramount for safeguarding
the overall health of ecosystems.

Implementing non-invasive methods to deter bears from approaching farms
and livestock holds promise in fostering harmonious relations between
humans and bears. Together with
[HackThePlanet](https://www.hack-the-planet.io) and [Foundation
Conservation Carpathia](https://www.carpathia.org/), we develop and
field-test smart detection and deterrent systems that keep bears out of
villages — without harming them.

Our ongoing research and development of a software tool aim to offer a
cost-effective, scalable, and versatile solution applicable not only to
bears but also to other species. This initiative has the potential to
significantly contribute to resolving human-wildlife conflicts on a
global scale.

<iframe src="https://www.youtube-nocookie.com/embed/aoro5FeN8hE" loading="lazy" frameborder="0" allowfullscreen></iframe>

<span class="gallery-box">
  <span class="gallery"></span>
  <em>Living With Bears — Technology, Coexistence & Conservation, by <a target="_blank" href="https://hack-the-planet.io">HackThePlanet</a></em>
</span>
<br/>

## Why bears matter

As apex predators and ecosystem engineers, bears shape the forests around them —
and their presence is a sign of a healthy, balanced environment.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Apex predator</h3>
    <p class="support__card-description">By keeping deer, elk and fish populations in check, bears prevent overgrazing and keep plant communities — and everything that depends on them — in balance.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Gardener &amp; recycler</h3>
    <p class="support__card-description">Roaming omnivores, they scatter seeds as they travel and enrich the soil through carcasses and dung — spreading plants and cycling nutrients across the forest.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Engineer &amp; indicator</h3>
    <p class="support__card-description">Digging dens and turning logs reshapes habitat for other species, and a healthy bear population is one of the clearest signals of a healthy ecosystem.</p>
  </div>

</div>

{{< image_carousel id="bear-individuals" items="2" >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bear1.jpg" alt="An individual brown bear" caption="An individual brown bear from the BearID Project." >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bear2.jpg" alt="An individual brown bear" caption="An individual brown bear from the BearID Project." >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bear3.jpg" alt="An individual brown bear" caption="An individual brown bear from the BearID Project." >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bear4.jpg" alt="An individual brown bear" caption="An individual brown bear from the BearID Project." >}}
{{< /image_carousel >}}
<p class="media-caption">Different individuals from the <a href="https://bearresearch.org" target="_blank">BearID Project</a>.</p>

## Conservation concerns

Even Europe's strongest bear population is under pressure from several
directions at once. Tap each to learn more.

{{< threats "pressures" >}}

## How the system works

The pieces are simple by design: a motion sensor and a night-vision camera,
wired to a small **Raspberry Pi** that runs a bear-detection model right at the
edge. The moment the model spots a bear, it fires the deterrent — no internet
connection, no mains power required.

![How it works — an AI camera detects an approaching bear on a low-power device, which triggers the sky-dancer deterrent](/images/projects/human_wildlife_conflict_bear/diagrams/pipeline.svg)
*The camera watches the farm's edge, a bear is detected on the device itself,
the controller fires, and the sky-dancer scares the bear off.*

We build the detection software; [HackThePlanet](https://hack-the-planet.io)
handles the electronics and packaging; and [Foundation Conservation
Carpathia](https://www.carpathia.org/) runs the field deployments in the
Carpathians. The model is tuned for **high recall** — catching every real bear
that approaches — while keeping false alarms low, so everyday activity like
livestock feeding doesn't set it off and farmers keep trusting it.

![Installing the AI camera](/images/projects/human_wildlife_conflict_bear/skydancer/installing_ai_camera.webp)
*Installing the AI camera at the edge of a farm in the Carpathian Mountains — photo courtesy of <a href="https://www.hack-the-planet.io" target="_blank">HackThePlanet</a>*

## Built for the field

Out in remote farmland, on battery power, around a wary wild animal, the system
has to meet some hard constraints:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Low-power &amp; low-maintenance</h3>
    <p class="support__card-description">It has to sip power and keep running for long stretches with little upkeep, far from the grid.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Safe for all</h3>
    <p class="support__card-description">The deterrent must be completely harmless — to the bear, and to the people living and working nearby.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Few false alarms</h3>
    <p class="support__card-description">A low false-positive rate keeps the farming community trusting the system, so a feeding cow never sets it off.</p>
  </div>

</div>

Bears make this genuinely hard: they're most active at dawn and dusk, but as
opportunistic feeders they can turn up at any hour — and where people are
around, they often shift to the cover of night.

{{< image_carousel id="bear-cameratrap" items="2" >}}
  {{< carousel_image src="/images/projects/human_wildlife_conflict_bear/bears/bear4.jpg" alt="Camera trap bear picture" caption="A camera-trap photo of a bear near the deployment farms in Romania." >}}
  {{< carousel_image src="/images/projects/human_wildlife_conflict_bear/bears/bear1.jpg" alt="Camera trap bear picture" caption="A camera-trap photo of a bear near the deployment farms in Romania." >}}
  {{< carousel_image src="/images/projects/human_wildlife_conflict_bear/bears/bear2.jpg" alt="Camera trap bear picture" caption="A camera-trap photo of a bear near the deployment farms in Romania." >}}
  {{< carousel_image src="/images/projects/human_wildlife_conflict_bear/bears/bear3.jpg" alt="Camera trap bear picture" caption="A camera-trap photo of a bear near the deployment farms in Romania." >}}
{{< /image_carousel >}}
<p class="media-caption">Camera-trap pictures of bears in Romania, near the farms where the system is deployed.</p>

## Deterrent

The chosen deterrent system consists of an inflatable tube man — a
sky-dancer — capable of rapid inflation upon bear detection in a video
frame. This solution offers
affordability, low power consumption, and harmlessness, with easy
replaceability. However, it remains uncertain whether bears can learn to
disregard the deterrent over time, necessitating iterative improvements to the
system as required in the future.

{{< image_carousel id="bear-skydancer" items="2" >}}
  {{< carousel_image src="/images/projects/human_wildlife_conflict_bear/skydancer/installing_blower.webp" alt="The HackThePlanet team installing the sky-dancer blower unit" caption="The HackThePlanet team installing the sky-dancer's blower unit." >}}
  {{< carousel_image src="/images/projects/human_wildlife_conflict_bear/skydancer/deterrent_station_aerial.webp" alt="Aerial view of the deterrent station with the sky-dancer activated" caption="An aerial view of the deterrent station with the sky-dancer activated." >}}
  {{< carousel_image src="/images/projects/human_wildlife_conflict_bear/skydancer/skydancer_carpathia.webp" alt="The sky-dancer deterrent deployed in a Carpathian meadow" caption="The inflatable sky-dancer deployed in a Carpathian meadow." >}}
{{< /image_carousel >}}
<p class="media-caption">The inflatable sky-dancer deterrent in the field — photos courtesy of <a href="https://www.hack-the-planet.io/projects/carpathia-skydancer-prototype/" target="_blank">HackThePlanet</a>.</p>

## Field Testing the Sky-Dancer in the Carpathians

In 2023, [HackThePlanet](https://www.hack-the-planet.io) deployed AI
cameras and Smart Deterrents across the Carpathian Mountains to keep
brown bears out of villages. The system worked — for most bears. But
some repeat-offender "problem bears" eventually figure out that the
light and sound from a deterrent, however unpredictable, isn't actually
dangerous. They learn, they adapt, and they come back.

This is where the sky-dancer comes in. Motion is fundamentally different
from light and sound: a sky-dancer moves erratically, changes shape, and
looms unpredictably, making it much harder for a bear to dismiss as
background noise. In 2024, the team returned to the same area in
partnership with [Foundation Conservation
Carpathia](https://www.carpathia.org/) to field-test the prototype: an
inflatable sky-dancer wired into the Smart Deterrent system, activating
the moment the AI camera detects an approaching bear.

Field testing is ongoing. Early observations from the partner team
suggest that the addition of dynamic motion does change bear behaviour
at the deterrent station — particularly for individuals that had begun
to ignore audio-only systems.

## Conclusion

The state-of-the-art Machine Learning model developed for real-time, low-power
bear detection marks a significant milestone in mitigating human-wildlife
conflicts. By fostering the creation of open-source tools, this project makes a
substantial contribution toward harmonizing the coexistence of farmers and
predators like bears. Moreover, its potential extends beyond bear management,
offering promising avenues for resolving human-wildlife conflicts across
diverse species.

<iframe src="https://www.youtube.com/embed/1AH17GkMWzg" loading="lazy" frameborder="0" allowfullscreen></iframe>

<span class="gallery-box">
  <span class="gallery"></span>
  <em>Instant Bear Scare Device Demo by <a target="_blank" href="https://hack-the-planet.io">HackThePlanet</a></em>
</span>
<br/>

{{< demo_cta >}}
