---
title: Bear Identification
summary: Noninvasive technologies to identify and monitor bears, facilitating their conservation.
tags: ["bear", "identification", "vision"]
related_projects:
  - carpathian-bear-deterrence
  - trout_identification
  - snow_leopard_monitoring
related_spaces:
  - /demos/trout_identification/
  - /demos/snowleopard_identification/
tagline: Recognising individual brown bears by their faces — from a camera-trap photo, with no tags and no handling.
clients:
  - name: BearID
    link: https://bearresearch.org
    logo: /images/clients/bearid/logo.png
    bg: inverted
related_posts:
  - bear-face-segmentation-guide
  - bear-identification-with-metric-learning-guide
github_repo: https://github.com/earthtoolsmaker/bear-conservation
space: /demos/bear_identification/
tools:
  - Computer Vision
  - Machine Learning
pressures:
  - name: Habitat loss &amp; fragmentation
    desc: "Deforestation, farming, urbanisation and infrastructure shrink and split bear habitat, making it harder to forage, den and breed."
  - name: Human–wildlife conflict
    desc: "As people move into bear country, raids on livestock and crops trigger retaliation — and bears are often hunted or killed in response."
  - name: Poaching &amp; trade
    desc: "Bears are poached for fur, claws and organs used in traditional medicine, rituals or as trophies."
  - name: Climate change
    desc: "Shifting food and vegetation patterns and warmer winters disrupt denning, foraging and the timing bears rely on."
  - name: Habitat degradation
    desc: "Mining, logging, pollution and disturbance degrade the habitats bears need, even where they aren't lost outright."
  - name: Weak legal protection
    desc: "In some regions, thin legal protection or weak enforcement leaves bears exposed to exploitation."
status: completed
date: 2024-04-03
pinned: false
image: /images/projects/bear_identification/cover.png
---

Brown bears are charismatic apex predators and umbrella species — protecting
them protects whole ecosystems. But they are elusive, range over vast
territories, and carry no natural tags, so simply knowing *which* bears are
out there, and how many, is genuinely hard. The toolkit for non-invasive bear
research is thin, which leaves population trends poorly understood.

Together with the [BearID Project](https://bearresearch.org/), we built a
computer-vision system that **recognises individual bears by their faces** —
straight from a camera-trap photo, with no tags, no collars and no handling.

![From a camera-trap photo to an identity — detect the bear's face, turn it into a fingerprint, and match it against known individuals](/images/projects/bear_identification/diagrams/pipeline.svg)
*A camera-trap photo comes in, the bear's face is found and cut out, turned
into a numerical "fingerprint", and matched against a database of known
individuals.*

> Our research and software tool will provide a replicable technique and
> general approach that can be applied to other species beyond bears, which
> could aid conservation efforts worldwide.
>
> <cite>– BearID Project</cite>

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

## Under pressure

Brown bears face pressure from several directions at once. Tap each to learn more.

{{< threats "pressures" >}}

## Why identify individual bears

Telling individuals apart — not just spotting *a* bear — is what turns camera-trap
images into real conservation data.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Population &amp; movement</h3>
    <p class="support__card-description">Counting and re-spotting known individuals reveals population trends and how bears move through the landscape, guiding conservation and habitat management.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Behaviour &amp; social life</h3>
    <p class="support__card-description">Following individuals over time opens up the study of social interactions, mating and reproduction — the foundations of effective conservation strategy.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Conflict &amp; land use</h3>
    <p class="support__card-description">Knowing which bears turn up where pinpoints high-conflict areas, informs bear-proofing and corridors, and helps measure whether coexistence measures actually work.</p>
  </div>

</div>

## Why bears are hard to tell apart

Brown bears extend facial recognition beyond primates — and in doing so expose
challenges that apply to a wide range of species:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">No unique markings</h3>
    <p class="support__card-description">Unlike spotted or striped species, brown bears have no consistent coat pattern to identify them — so the face becomes the most reliable signature.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Morphological variation</h3>
    <p class="support__card-description">Their build varies widely across regions and habitats, making a single, universally accurate recognition model hard to pin down.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Seasonal &amp; age change</h3>
    <p class="support__card-description">Bears gain and lose dramatic amounts of weight across the seasons and over their lives, so their faces have to be recognised despite changing appearance.</p>
  </div>

</div>

The pictures below show the same individual — **Chunk** (`bf32`), one of the
well-known Brooks River bears — at different times and places. A person finds it
hard; the model has to learn to see past the seasons, angles and lighting to the
bear underneath.

{{< image_carousel id="bear-bf32" items="2" >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bf32_3.jpg" alt="The same bear, bf32, photographed at a different time" caption="Chunk (bf32) — the same individual at a different time and place." >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bf32_1.jpg" alt="The same bear, bf32, photographed at a different time" caption="Chunk (bf32) — the same individual at a different time and place." >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bf32_2.jpg" alt="The same bear, bf32, photographed at a different time" caption="Chunk (bf32) — the same individual at a different time and place." >}}
  {{< carousel_image src="/images/projects/bear_identification/bears/bf32_4.jpg" alt="The same bear, bf32, photographed at a different time" caption="Chunk (bf32) — the same individual at a different time and place." >}}
{{< /image_carousel >}}
<p class="media-caption">One individual — Chunk (bf32) — across seasons and locations, from the <a href="https://bearresearch.org" target="_blank">BearID Project</a>.</p>

## How the system works

Recognising a bear takes two steps, each handled by an open-source model.

### Detect the face

The first model scans a camera-trap photo and **finds the bear's head**, cutting
it out and straightening it into a clean, standard view of the face. Getting this
right is what makes the matching that follows accurate.

### Match the fingerprint

The second model turns each face into a numerical **fingerprint** — a point in a
high-dimensional space where photos of the same bear land close together and
different bears land far apart. Identifying a new photo is then simply a matter
of finding its nearest neighbours: a strong enough match returns a known
individual, while a weak one flags a bear we haven't seen before, ready to be added.

Camera traps make all of this possible — collecting images day and night, in
places from Arctic tundra to temperate forest, without a researcher present and
without disturbing the animals.

{{< image_carousel id="bear-cameratrap" items="2" >}}
  {{< carousel_image src="/images/projects/bear_identification/camera_traps/camera1.png" alt="A camera trap in the field" caption="A camera trap deployed in the field." >}}
  {{< carousel_image src="/images/projects/bear_identification/camera_traps/camera3.jpg" alt="A camera trap in the field" caption="A camera trap deployed in the field." >}}
{{< /image_carousel >}}
<p class="media-caption">Camera traps collect images non-invasively, day and night, without a researcher present.</p>

## Conclusion

Reading a bear by its face turns population monitoring into something
non-invasive, repeatable and scalable — gathering the data researchers need
without ever tagging or handling an animal. Because the approach is open-source
and not specific to bears, it offers a replicable blueprint that can be adapted
to other species and strengthen conservation efforts worldwide.

{{< demo_cta >}}
