---
title: Trout Identification
summary: Non-invasive technology for monitoring trout populations using computer vision to accurately identify individual fish.
tagline: Recognising individual trout by their spot patterns — like fingerprints — without ever touching the fish.
clients:
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
space: /demos/trout_identification/
related_posts:
  - how-to-prepare-data-for-identification
  - local-feature-matching-lightglue
tools:
  - Machine Learning
  - Computer Vision
pressures:
  - name: Habitat loss
    desc: "Urban development, farming and logging strip away the streamside habitat and clean water these trout depend on."
  - name: Fragmentation
    desc: "Dams, roads and other barriers cut populations off from one another, blocking migration and eroding genetic diversity."
  - name: Pollution
    desc: "Runoff from farms, industry and towns degrades the water quality these sensitive fish need."
  - name: Invasive species
    desc: "Introduced brook and rainbow trout compete with, hybridise with, and prey on the native cutthroat."
  - name: Climate change
    desc: "Shifting temperatures and flows warm and reshape the cold, clear streams cutthroat rely on to spawn."
  - name: Overfishing
    desc: "Heavy or unsustainable fishing pressure thins local populations and their genetic diversity."
status: completed
pinned: true
date: 2024-12-08
github_repo: https://github.com/earthtoolsmaker/trout-reid
image: /images/projects/trout_identification/cover.png
---

Trout are freshwater members of the salmon family, prized for their vivid colours
and markings. The **Westslope Cutthroat Trout** — named for the red-orange slash
under its jaw — is native to the cold, clear streams of British Columbia and the
northwestern US, and because it is so sensitive to water quality, its health is a
barometer for the whole stream.

Every cutthroat carries something remarkable: a pattern of black spots as unique
as a fingerprint, and stable for life. Together with [Lumax AI](https://lumax.ai/),
we built a system that reads those spot patterns to **recognise individual trout
from a photo** — no tags, no handling, no stress to the fish.

![From a photo to an identity — normalize the trout, extract its spot-pattern keypoints, and match them against a database](/images/projects/trout_identification/diagrams/pipeline.svg)
*A photo is straightened and cut out, the trout's unique spots become keypoints,
and those keypoints are matched against a database of known fish.*

{{< image_carousel id="trout-intro" items="2" >}}
  {{< carousel_image src="/images/projects/trout_identification/wct_example.png" alt="Westslope Cutthroat Trout" caption="The Westslope Cutthroat Trout — note the golden body, black spots, and the red slash beneath the jaw that gives it its name." >}}
  {{< carousel_image src="/images/projects/trout_identification/map_elk_river.png" alt="Map of the Elk River" caption="The Elk River, British Columbia, where this trout population is monitored." >}}
{{< /image_carousel >}}

## Why this trout matters

A native species in cold, clear water, the Westslope Cutthroat is woven through
the health of its whole stream.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Food-web role</h3>
    <p class="support__card-description">Both predator and prey — it eats insects and smaller fish, and in turn feeds birds, bears and larger fish, helping keep the web in balance.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Indicator species</h3>
    <p class="support__card-description">Sensitive to water quality and habitat, healthy cutthroat populations signal a healthy stream — and warn early when something is wrong.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Culture &amp; habitat</h3>
    <p class="support__card-description">It anchors recreational fishing and local economies, cycles nutrients, and its spawning even helps shape the streambed for other species.</p>
  </div>

</div>

## Under pressure

In many areas the Westslope Cutthroat is a species of concern, with populations
in decline. Tap each pressure to learn more.

{{< threats "pressures" >}}

## How the system works

Recognising a trout takes two steps: prepare the photo, then match the spots.

### Prepare the photo

Each raw photo is **normalized** — the fish is cut out from its background and
straightened into a standard pose — and its unique spots are extracted as
**keypoints**. Getting this right is what makes the later matching accurate.

| Original photo | Normalized trout | Extracted keypoints |
|:-------:|:----------:|:---------:|
| ![Picture 1](/images/projects/trout_identification/images/raw/1.jpg) | ![Normalized 1](/images/projects/trout_identification/images/normalized/1.webp) | ![Keypoints 1](/images/projects/trout_identification/images/keypoints/1.webp) |
| ![Picture 2](/images/projects/trout_identification/images/raw/2.jpg) | ![Normalized 2](/images/projects/trout_identification/images/normalized/2.webp) | ![Keypoints 2](/images/projects/trout_identification/images/keypoints/2.webp) |
| ![Picture 3](/images/projects/trout_identification/images/raw/3.jpg) | ![Normalized 3](/images/projects/trout_identification/images/normalized/3.webp) | ![Keypoints 3](/images/projects/trout_identification/images/keypoints/3.webp) |
| ![Picture 4](/images/projects/trout_identification/images/raw/4.jpg) | ![Normalized 4](/images/projects/trout_identification/images/normalized/4.webp) | ![Keypoints 4](/images/projects/trout_identification/images/keypoints/4.webp) |
| ![Picture 5](/images/projects/trout_identification/images/raw/5.jpg) | ![Normalized 5](/images/projects/trout_identification/images/normalized/5.webp) | ![Keypoints 5](/images/projects/trout_identification/images/keypoints/5.webp) |

### Match the spots

The keypoints from a new photo are compared against a database of known trout. A
strong enough match returns that individual — and its PIT tag and name; a weak
match means it is a fish we have not seen before, ready to be registered. The
pairs below show the matcher at work: genuine matches on the left, where the
spot patterns line up, and non-matches on the right, where they don't.

| ✅ Keypoints match | ❌ Keypoints do not match |
|:-----:|:---------:|
| ![Match 1](/images/projects/trout_identification/images/matches/match_1.webp) | ![Non Match 1](/images/projects/trout_identification/images/matches/non_match_1.webp) |
| ![Match 2](/images/projects/trout_identification/images/matches/match_2.webp) | ![Non Match 2](/images/projects/trout_identification/images/matches/non_match_2.webp) |
| ![Match 3](/images/projects/trout_identification/images/matches/match_3.webp) | ![Non Match 3](/images/projects/trout_identification/images/matches/non_match_3.webp) |
| ![Match 4](/images/projects/trout_identification/images/matches/match_4.webp) | ![Non Match 4](/images/projects/trout_identification/images/matches/non_match_4.webp) |

## Conclusion

Reading a trout by its spots turns population monitoring into something fast,
repeatable and completely non-invasive — gathering the data researchers need
without ever disturbing the fish or their habitat. As pressure on freshwater
ecosystems grows, methods like this help track individual trout over time and
target conservation where it matters most.

{{< demo_cta >}}
