---
title: Trout Identitication
subtitle: Conservation
summary: Non invasive technology to monitor trout population using computer vision technology to accurately identify individual fish.
clients:
  - name: Aeria
    link: https://aeria.ai/
    logo: /images/clients/aeria/logo.png
space: /spaces/trout_identification/
tools:
  - Machine Learning
  - Computer Vision
status: completed
pinned: false
date: 2024-12-08
image: /images/projects/trout_identification/cover.png
---

## Context

Trouts are freshwater fish belonging to the family Salmonidae, which also
includes salmon and char. They are found in various habitats, including rivers,
lakes, and streams, and are known for their vibrant colors and distinctive
markings.

![Westslope Cutthroat Trout](/images/projects/trout_identification/wct_example.png)
*Gallery / Westslope Cutthroat Trout*

The Westslope Cutthroat Trout (Oncorhynchus clarkii lewisi) is a distinctive
subspecies of cutthroat trout native to the freshwater systems of British
Columbia, Canada, and parts of the northwestern United States. 
The Westslope Cutthroat Trout is one of two cutthroat trout sub-species that
occur naturally in Canada. This species is found in two distinct populations:
one in Alberta and one in British Columbia (Pacific). Renowned for its striking
appearance, this trout features a vibrant coloration that includes a
golden-yellow body adorned with numerous small black spots, and a
characteristic red or orange slash beneath its jaw. The Westslope Cutthroat
Trout thrives in cold, clear streams, rivers, and lakes, where it plays a vital
role in the aquatic ecosystem. Due to its specific habitat needs, this species
is often used as an indicator of ecosystem health.

![Elk River](/images/projects/trout_identification/map_elk_river.png)
*Gallery / Map of the Elk River where the trout population is monitored*

One fascinating aspect of trouts is their stable and unique spot patterns. Just
like human fingerprints, these patterns can be used to identify individual
fish. Each trout has a distinct arrangement of spots, which remain consistent
throughout its life. Researchers and biologists utilize these unique markings
to study trout populations, monitor their health, and track their movements in
the wild. This method of identification not only aids in conservation efforts
but also enhances our understanding of trout behavior and ecology, highlighting
the importance of these remarkable fish in freshwater ecosystems.

![Stable Spot patterns](/images/projects/trout_identification/lightglue/lightglue_matching.png)
*Gallery / Unique spot patterns are like fingerprints*


## A vital role for the ecosystems

The Westslope Cutthroat Trout plays a crucial role in its ecosystem for several reasons:

- __Biodiversity Support__: As a native species, the Westslope Cutthroat Trout
contributes to the overall biodiversity of freshwater ecosystems. Its presence
helps maintain a balanced food web.
- __Prey and Predator Dynamics__: This trout serves as both a predator and prey
within its habitat. It feeds on insects, crustaceans, and smaller fish, helping
to control these populations. In turn, it is a food source for larger
predators, such as birds of prey, bears, and other fish species.
- __Nutrient Cycling__: The Westslope Cutthroat Trout contributes to nutrient
cycling in aquatic ecosystems. As it feeds and excretes waste, it helps to
recycle nutrients that support the growth of aquatic plants and microorganisms.
- __Indicator Species__: The health of Westslope Cutthroat Trout populations
can indicate the overall health of freshwater ecosystems. Their sensitivity to
changes in water quality and habitat conditions makes them valuable indicators
for environmental monitoring.
- __Cultural and Economic Importance__: This trout is significant for local
communities, particularly for recreational fishing and tourism. Healthy
populations can support local economies and promote conservation efforts.
- __Habitat Formation__: The activities of Westslope Cutthroat Trout, such as
spawning, can influence the physical characteristics of their habitats. Their
nesting behaviors can help create and maintain suitable environments for other
aquatic organisms.

Overall, the Westslope Cutthroat Trout is vital for maintaining the ecological
balance and health of freshwater ecosystems in British Columbia and beyond.

## Conservation concerns

In some regions, the Westslope Cutthroat Trout is considered a species
of concern or is listed as threatened or endangered.

Many populations of Westslope Cutthroat Trout have experienced
significant declines, leading to concerns about their long-term
viability. The species faces several conservation threats that impact
its populations and habitats:

- __Habitat Loss and Degradation__: Urban development, agriculture, and
logging can lead to the destruction and alteration of natural habitats.
This includes the loss of riparian zones, which are crucial for
maintaining water quality and providing shelter.
- __Habitat Fragmentation__: Habitat fragmentation caused by dams,
roads, and other barriers can isolate populations, making it difficult
for them to migrate, breed, and maintain genetic diversity.
- __Pollution__: Runoff from agricultural practices, industrial
activities, and urban areas can introduce pollutants into waterways,
negatively affecting water quality and the health of trout populations.
- __Invasive Species__: The introduction of non-native fish species,
such as brook trout and rainbow trout, can lead to competition for
resources, hybridization, and predation, which threaten the survival of
Westslope Cutthroat Trout.
- __Climate Change__: Changes in temperature and precipitation patterns
can alter stream flows and water temperatures, impacting the habitats
that Westslope Cutthroat Trout rely on for spawning and growth.
- __Overfishing__: Unsustainable fishing practices can deplete local
populations, particularly in areas where fishing pressure is high. This
can lead to reduced genetic diversity and population declines.

Overall, addressing these threats and concerns is essential for the
conservation of the Westslope Cutthroat Trout and the health of the
ecosystems they inhabit.

## Developed Tools

### Pipeline Overview

Throughout this project, a variety of tools were developed to
effectively utilize the unique biomarkers of trouts for enhanced
identification and monitoring.

![ML Pipeline for Trout Identification](/images/projects/trout_identification/pipeline.png)
*Gallery / Overview of the ML pipeline developed to identify trouts*

### Preprocessing Stage

The preprocessing stage is meticulously designed to transform a raw
image of a trout into a normalized, segmented representation of the
fish. This critical step ensures high accuracy during the subsequent
identification phase of the pipeline.

The table below illustrates how the preprocessing stage transforms the original
image into a normalized representation of the trout, allowing for the
extraction of its unique markings.

| Original Picture | Normalized Trout | Extracted Keypoints |
|:-------:|:----------:|:---------:|
| ![Picture 1](/images/projects/trout_identification/images/raw/1.jpg) | ![Normalized 1](/images/projects/trout_identification/images/normalized/1.webp) | ![Keypoints 1](/images/projects/trout_identification/images/keypoints/1.webp) |
| ![Picture 2](/images/projects/trout_identification/images/raw/2.jpg) | ![Normalized 2](/images/projects/trout_identification/images/normalized/2.webp) | ![Keypoints 2](/images/projects/trout_identification/images/keypoints/2.webp) |
| ![Picture 3](/images/projects/trout_identification/images/raw/3.jpg) | ![Normalized 3](/images/projects/trout_identification/images/normalized/3.webp) | ![Keypoints 3](/images/projects/trout_identification/images/keypoints/3.webp) |
| ![Picture 4](/images/projects/trout_identification/images/raw/4.jpg) | ![Normalized 4](/images/projects/trout_identification/images/normalized/4.webp) | ![Keypoints 4](/images/projects/trout_identification/images/keypoints/4.webp) |
| ![Picture 5](/images/projects/trout_identification/images/raw/5.jpg) | ![Normalized 5](/images/projects/trout_identification/images/normalized/5.webp) | ![Keypoints 5](/images/projects/trout_identification/images/keypoints/5.webp) |

### Identification Stage

Once the trout image is normalized, the algorithm extracts key
biomarkers, specifically the unique spot patterns of the trout, and
compares them against a comprehensive database of known trout. If the
comparison yields a sufficiently high score, the system identifies the
fish as a match and retrieves its associated PIT tag and name.
Conversely, if the comparison score is low, it indicates that the trout
does not correspond to any entries in the database, and the system
classifies it as a new individual.

The table below demonstrates the functionality of the matching algorithm using
the extracted keypoints. On the left, you will find examples of matching pairs,
while the right side displays examples of non-matching pairs.

| ✅ Keypoints match | ❌ Keypoints do not match |
|:-----:|:---------:|
| ![Match 1](/images/projects/trout_identification/images/matches/match_1.webp) | ![Non Match 1](/images/projects/trout_identification/images/matches/non_match_1.webp) |
| ![Match 2](/images/projects/trout_identification/images/matches/match_2.webp) | ![Non Match 2](/images/projects/trout_identification/images/matches/non_match_2.webp) |
| ![Match 3](/images/projects/trout_identification/images/matches/match_3.webp) | ![Non Match 3](/images/projects/trout_identification/images/matches/non_match_3.webp) |
| ![Match 4](/images/projects/trout_identification/images/matches/match_4.webp) | ![Non Match 4](/images/projects/trout_identification/images/matches/non_match_4.webp) |

## Conclusion

In conclusion, a non-invasive trout identification system represents a
transformative approach to monitoring trout populations effectively and
sustainably. By utilizing unique spot patterns and other distinguishing
features, researchers can gather critical data without disturbing the
fish or their habitats. The advancement of these techniques not only
enhances our understanding of trout ecology but also supports targeted
conservation efforts. As we strive to protect and preserve aquatic
ecosystems worldwide, such innovative methods will play a vital role in
ensuring the long-term survival of trout species and the health of the
environments they inhabit.

One can try out the model from the [ML Space]({{< ref
"/spaces/trout_identification" >}}) or directly from the snippet below:

{{< hf_space "earthtoolsmaker-trout-reid" >}}
