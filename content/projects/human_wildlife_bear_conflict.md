---
title: Human-Wildlife Conflict
subtitle: Appeasing human-bear conflict
summary: Utilizing low-power technology to detect and deter bears from encroaching on Romanian farms.
client: 
  name: HackThePlanet
  link: https://www.hack-the-planet.io
  logo: /images/clients/hacktheplanet/logo.png
github_repo: https://gitlab.com/fruitpunch/projects/ai-for-bears/face-detection-and-segmentation/albear
tools: 
  - "Computer Vision"
  - "Machine Learning"
date: 2024-04-02
image: images/projects/human_wildlife_conflict_bear/cover.png
---

Brown bears serve as pivotal indicators and umbrella species, playing a
crucial role in ecological balance. Managing Human-Wildlife Conflict in
regions inhabited by these apex predators is paramount for safeguarding
the overall health of ecosystems.

Implementing non-invasive methods to deter bears from approaching farms
and livestock holds promise in fostering harmonious relations between
humans and bears.

![Pipeline Overview](/images/projects/human_wildlife_conflict_bear/pipeline_overview.png)
*Bear Scare System Overview*

Our ongoing research and development of a software tool aim to offer a
cost-effective, scalable, and versatile solution applicable not only to
bears but also to other species. This initiative has the potential to
significantly contribute to resolving human-wildlife conflicts on a
global scale.

## Bears are vital for healthy ecosystems

Bears play a crucial role in maintaining healthy ecosystems due to their
position as apex predators and their significant influence on various
ecological processes. Here are several reasons why bears are vital for
ecosystem health:

- __Regulation of Prey Populations:__ As apex predators, bears help control
   populations of prey species such as deer, elk, and fish. By regulating these
populations, bears prevent overgrazing and maintain the balance of plant
communities, which in turn affects other species dependent on those plants.
- __Seed Dispersal:__ Bears are omnivores and consume a diverse diet,
   including fruits, berries, and nuts. As they travel through their habitats,
bears inadvertently scatter seeds through their feces, helping to disperse
plant species and promote biodiversity.
- __Nutrient Cycling:__ When bears catch prey or forage for food, they often
   leave behind carcasses or plant remains. These organic materials provide
nutrients to the soil and support the growth of vegetation. Additionally, bear
feces contribute to nutrient cycling by enriching the soil with nitrogen,
phosphorus, and other essential elements.
- __Ecosystem Engineering:__ Bears are known to engage in behaviors that shape
   their environment, such as excavating dens or overturning logs in search of
food. These activities can have cascading effects on ecosystem dynamics by
creating habitats for other species or influencing nutrient cycling.
- __Indicator Species:__ Bears serve as indicators of ecosystem health. Their
   presence, abundance, and behavior can provide insights into the overall
condition of the ecosystem, including factors such as habitat quality, food
availability, and human impacts.

Overall, the presence of bears in an ecosystem signifies a healthy and balanced
environment. Protecting and conserving bear populations is not only essential
for their survival but also for the integrity and resilience of the ecosystems
they inhabit.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/bear_identification/bears/bear1.jpg" loading="lazy">
    <img src="/images/projects/bear_identification/bears/bear2.jpg" loading="lazy">
    <img src="/images/projects/bear_identification/bears/bear3.jpg" loading="lazy">
    <img src="/images/projects/bear_identification/bears/bear4.jpg" loading="lazy">
  </div>
  <em>Gallery / Different individuals from the <a href="https://bearresearch.org" target="_blank">BearID Project</a></em>
</div>

## Conservation concerns

Conservation concerns for brown bears stem from various factors that threaten
their populations and habitats. Some of the key reasons include:

- __Habitat Loss and Fragmentation:__ Human activities such as deforestation,
   urbanization, agriculture, and infrastructure development have led to the
loss and fragmentation of brown bear habitats. As their habitats shrink and
become fragmented, brown bears face challenges in finding suitable areas for
foraging, denning, and breeding.
- __Human-Wildlife Conflict:__ Encounters between brown bears and humans often
   result in conflicts, particularly in regions where humans have encroached
upon bear habitats. Conflicts arise due to predation on livestock, crop damage,
and perceived threats to human safety. In response, bears may be persecuted
through hunting or lethal control measures, further exacerbating conservation
concerns.
- __Illegal Poaching and Trade:__ Brown bears are targeted by poachers for
   their body parts, including fur, claws, and organs, which are used in
traditional medicine, cultural practices, or as trophies. Illegal poaching and
trade contribute to population declines and disrupt ecosystem dynamics.
- __Climate Change:__ Climate change is altering brown bear habitats by
   affecting food availability, altering vegetation patterns, and impacting
hibernation behaviors. Changes in climate can lead to mismatches in the timing
of key events, such as denning and berry ripening, which can negatively impact
brown bear populations.
- __Habitat Degradation:__ Human activities such as mining, logging, and
   recreational activities can degrade brown bear habitats through habitat
destruction, pollution, and disturbance. Degraded habitats may not be able to
support healthy brown bear populations or provide essential resources for their
survival.
- __Inadequate Legal Protections:__ In some regions, brown bears may lack
   adequate legal protections or face weak enforcement of existing conservation
laws. This can result in unchecked exploitation, habitat destruction, and other
threats to brown bear populations.

Addressing these conservation concerns requires concerted efforts involving
habitat protection, mitigating human-wildlife conflicts, combating illegal
poaching and trade, implementing climate adaptation strategies, and promoting
policies that ensure the long-term survival of brown bears and their habitats.

## Project Scope and Objectives

Our collaboration aims to lead the development of innovative,
non-invasive solutions for detecting bears in real-time environments.
The primary focus of our efforts lies in pioneering software tools for
bear detection, while our partner, [HackThePlanet](https://hack-the-planet.io),
specializes in the electronic packaging aspect.

Our system integrates a motion sensor and a CCTV night vision camera,
both of which are controlled by a microcontroller. The microcontroller
hosts a bear detection model, which promptly triggers a bear deterrent
mechanism upon detection, effectively deterring the bear and ensuring
safety.

The detection system's priority is to optimize recall, ensuring it
accurately localizes bears with high precision when they approach.
Simultaneously, it aims to minimize false positives, particularly those
that may arise from routine activities such as livestock feeding around
the farms.

![Pipeline Overview](/images/projects/human_wildlife_conflict_bear/pipeline_overview.png)
*Bear Scare System Overview*

## Addressing Challenges in Brown Bear Detection

Brown bears present an ideal opportunity to advance bear detection technology for use on low-power devices:

- __Activity Patterns:__ Brown bears are primarily crepuscular,
exhibiting peak activity during dawn and dusk. However, their behavior
may vary based on factors such as food availability, season, and human
presence. In regions with significant human activity, brown bears might
adjust their behavior to minimize encounters, potentially increasing
activity during nighttime. While opportunistic feeders, their activity
can occur at any time of day or night, depending on food availability.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear4.jpg" loading="lazy" alt="camera trap bear picture 4" \>
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear1.jpg" loading="lazy" alt="camera trap bear picture 1" \>
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear2.jpg" loading="lazy" alt="camera trap bear picture 2" \>
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear3.jpg" loading="lazy" alt="camera trap bear picture 3" \>
  </div>
  <em>Gallery / Camera trap pictures of bears in Romania, near the farms where the system is deployed</em>
</div>

- __System Requirements:__ The detection system must prioritize low
power consumption, require minimal maintenance, and operate effectively
in remote environments.
- __Deterrent Safety:__ Any deterrent system employed should ensure the
safety of both animals and humans, posing no harm to either.
- __False Positive Mitigation:__ It is essential for the detection model
to maintain a low false positive rate, fostering trust within the
farming community that will utilize the system.

## Deterrent

The chosen deterrent system consists of an inflatable tube man, capable of
rapid inflation upon bear detection in a video frame. This solution offers
affordability, low power consumption, and harmlessness, with easy
replaceability. However, it remains uncertain whether bears can learn to
disregard the deterrent over time, necessitating iterative improvements to the
system as required in the future.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/human_wildlife_conflict_bear/inflatable_tube_man/tube1.gif" loading="lazy" alt="Inflatable Tube Man 1" \>
    <img src="/images/projects/human_wildlife_conflict_bear/inflatable_tube_man/tube2.gif" loading="lazy" alt="Inflatable Tube Man 2" \>
  </div>
  <em>Gallery / Camera trap pictures of bears in Romania, near the farms where the system is deployed</em>
</div>

## Conclusion

The state-of-the-art Machine Learning model developed for real-time, low-power bear detection marks a significant milestone in mitigating human-wildlife conflicts. By fostering the creation of open-source tools, this project makes a substantial contribution toward harmonizing the coexistence of farmers and predators like bears. Moreover, its potential extends beyond bear management, offering promising avenues for resolving human-wildlife conflicts across diverse species.

<p>
  <iframe src="https://www.youtube.com/embed/1AH17GkMWzg" loading="lazy" frameborder="0" allowfullscreen></iframe>
  <em>Instant Bear Scare Device Demo</em>
</p>
