---
title: Wild Salmon Migration Monitoring
summary: The project monitors wild salmon migration to ensure the number passing through meets state regulations, addressing threats from human activities like fisheries and dams.
github_repo: https://github.com/Salmon-Computer-Vision/salmon-computer-vision/tree/master
space: /spaces/wild_salmon_migration_monitoring/
clients:
  - name: Pacific Salmon Foundation
    link: https://psf.ca/
    logo: /images/clients/psf/logo.png
  - name: Wild Salmon Centre
    link: https://wildsalmoncenter.org/
    logo: /images/clients/wild_salmon_centre/logo.png
  - name: Aeria
    link: https://aeria.ai/
    logo: /images/clients/aeria/logo.png
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
status: completed
pinned: true
date: 2024-08-20
image: /images/projects/wild_salmon_migration_monitoring/cover.png
---

## Context

Pacific salmon are anadromous, meaning they begin life in freshwater,
migrate to the ocean, and return to freshwater to spawn and die. Adult
salmon travel long distances, often hundreds of miles, to reach their
birthplace. Overcoming various obstacles, they engage in courtship and
breeding. The males and females release sperm and eggs simultaneously,
which settle in nests (redds) prepared by the females. After spawning,
the adult salmon die, their bodies providing nutrients to the
surrounding environment.
One can learn more about the Pacific salmon life cycle [here](https://psf.ca/learn/species-lifecycle/).

Wild salmon are integral to the ecological, cultural, and economic
fabric of British Columbia, underscoring the importance of their
effective conservation and management.

Through a collaborative partnership with the [Pacific Salmon Foundation
(PSF)](https://psf.ca/),
the [Wild Salmon Center](https://wildsalmoncenter.org/),
[Aeria](https://aeria.ai/), and [Simon Fraser University](https://sfu.ca/), we
developed an automated tracking and counting system -
[__SalmonVision__](https://salmonvision.org/) - designed to monitor a wide
range of salmon species returning to their natal streams.

![System Overview](/images/projects/wild_salmon_migration_monitoring/system_overview.png)
*Gallery / System overview of the [__SalmonVision__](https://salmonvision.org/) application*

## Wild salmons are vital for the ecosystems

Wild salmon in British Columbia (BC), Canada, play a crucial role in the
ecosystem for several reasons:

- __Nutrient Cycling__: When salmon return to their natal streams to spawn and
die, their bodies decompose and release essential nutrients into the freshwater
systems. These nutrients, including nitrogen and phosphorus, support the growth
of aquatic plants and microorganisms, which are the foundation of the food web.
- __Food Source for Wildlife__: Salmon are a key food source for a variety of
wildlife, including bears, eagles, wolves, and other predators. The presence of
salmon influences the population and health of these species, creating a ripple
effect throughout the ecosystem.
- __Forest Health__: The nutrients from decomposing salmon carcasses also
benefit surrounding forests. Trees and plants near salmon-bearing streams grow
more robustly due to the nutrient input, contributing to overall forest health
and biodiversity.
- __Marine and Freshwater Link__: Salmon act as a crucial link between marine
and freshwater ecosystems. As they migrate from the ocean to freshwater
streams, they transport marine nutrients inland, enriching freshwater habitats.
- __Biodiversity__: The presence of salmon supports a diverse range of species,
both directly and indirectly. Healthy salmon populations contribute to the
overall biodiversity of the region, making the ecosystem more resilient to
changes and disturbances.
- __Cultural Importance__: For many Indigenous communities in BC, salmon are
not only a vital food source but also hold significant cultural and spiritual
value. The health of salmon populations is deeply intertwined with the cultural
heritage and traditions of these communities.
- __Economic Value__: Salmon fisheries are economically important for BC,
providing jobs and supporting local economies. Sustainable management of salmon
populations is crucial for the long-term viability of these economic
activities.

Overall, wild salmon are integral to the ecological, cultural, and economic
fabric of British Columbia, highlighting the importance of conserving and
managing their populations effectively.

## Conservation concerns

Wild salmon in British Columbia and around the world face several main
conservation threats.

> We must take every step in our control now as climate-change related trends
> will make things more difficult for salmon populations in the years ahead.
> This demands urgency for Pacific salmon and for the 130+ species, including
> grizzlies, orcas and eagles, that depend on Pacific salmon.
>
> <cite>– Pacific Salmon Foundation</cite>

- __Habitat Destruction__: Urban development, logging, and agriculture
can degrade and destroy salmon habitats, particularly spawning and
rearing streams.
- __Dams and Barriers__: Dams and other barriers obstruct salmon
migration routes, preventing access to critical spawning and rearing
habitats.
- __Overfishing__: Unsustainable fishing practices can deplete salmon
populations, reducing their numbers and genetic diversity.
- __Climate Change__: Rising temperatures and changing precipitation
patterns affect water temperatures and stream flows, disrupting salmon
life cycles and habitats.
- __Pollution__: Runoff from agriculture, industry, and urban areas can
contaminate waterways with pollutants, negatively impacting salmon
health and survival.
- __Disease and Parasites__: Increased interactions with farmed salmon
and other fish can spread diseases and parasites to wild salmon
populations, weakening their health and resilience.

## How can a Wild Salmon Migration Monitoring system benefit conservation?

A wild salmon migration monitoring system benefits the conservation of wild
salmon in several key ways:

- __Accurate Population Tracking__: By automatically counting salmon as they
migrate, the system provides precise data on population sizes and trends. This
information is crucial for assessing the health of salmon populations and
identifying any declines or increases.
- __Informed Management Decisions__: With reliable data on salmon numbers and
migration patterns, conservationists and resource managers can make informed
decisions about fishing quotas, habitat restoration projects, and other
management actions to support salmon conservation.
- __Identifying Threats__: The monitoring system can help identify specific
threats to salmon during their migration, such as obstacles created by dams or
pollution levels in certain areas. Addressing these threats becomes more
feasible with concrete data.
- __Supporting Regulatory Compliance__: By ensuring that the number of salmon
passing through specific areas meets state regulations, the system helps
enforce legal protections for salmon populations. This compliance is essential
for maintaining sustainable salmon fisheries.
- __Enhancing Habitat Protection__: Data from the monitoring system can
highlight critical habitats that are essential for salmon spawning and rearing.
Protecting these habitats becomes a priority, ensuring that salmon have safe
and suitable environments for reproduction and growth.
- __Long-term Monitoring__: Continuous monitoring over multiple seasons and
years provides long-term data that is vital for understanding trends and the
impacts of environmental changes, such as climate change, on salmon
populations.
- __Community and Stakeholder Engagement__: By providing transparent and
accessible data, the system can engage local communities, Indigenous groups,
and other stakeholders in salmon conservation efforts. Informed communities are
more likely to support and participate in conservation initiatives.

## Project Scope and Collaboration

This project involves a close collaboration with the [Pacific Salmon
Foundation](https://psf.ca/), the [Wild Salmon
Center](https://wildsalmoncenter.org/),
[Aeria](https://aeria.ai/), and [Simon Fraser
University](https://www.sfu.ca/) to develop an advanced monitoring
system. The system automatically counts different fish species
migrating back to their natal streams, utilizing underwater cameras,
sonar technology, drone imagery, and satellite connectivity for data streaming,
and computer vision systems to generate automated count reports.

![Web application overview](/images/projects/wild_salmon_migration_monitoring/webapp_overview.png)
*Gallery / Overview of the web application developed to centralize counts reports and video clips*

### Main Salmon species

Below is a table showcasing the seven main salmon species found in Canada, all
of which our systems can automatically recognize and count.

| Species | Description | Image |
|---------|-------------|-------|
| [Steelhead](https://psf.ca/info/steelhead/)  | Found primarily in eastern Pacific waters, Steelhead can live up to eight years and spawn up to three times, although many, especially males, do not survive that long. They can grow large, with some reaching over 30 pounds and 45 inches in length, though most are between eight and 20 pounds. | ![Steelhead](/images/projects/wild_salmon_migration_monitoring/species/steelhead-trout.png) |
| [Sockeye](https://psf.ca/info/sockeye/) | Sockeye salmon, known for their slim, streamlined bodies and brilliant colors, inhabit rivers and lakes of the Pacific Northwest. They are culturally significant to First Nations and provide essential nutrition to many communities. At maturity, usually around four years old, Sockeye weigh between five to 12 pounds and measure 20 to 28 inches in length. | ![Pink](/images/projects/wild_salmon_migration_monitoring/species/sockeye.png) |
| [Pink](https://psf.ca/info/pink/) | Pink salmon are the smallest and most populous Pacific salmon in British Columbia, and the least vulnerable to extinction. They typically weigh between three to 11 pounds and measure 18 to 24 inches in length. | ![Pink](/images/projects/wild_salmon_migration_monitoring/species/pink_0.png) |
| [Coho](https://psf.ca/info/coho/) | Coho salmon are highly adaptable and found in rivers and streams across North America. They typically weigh 8 to 12 pounds and measure 18 to 24 inches in length. | ![Coho](/images/projects/wild_salmon_migration_monitoring/species/coho.png) |
| [Chum](https://psf.ca/info/chum/) | Chum salmon are the second largest in the Oncorhynchus genus, after Chinook. They typically weigh between 12 to 15 pounds and measure 35 to 45 inches in length. | ![Chum](/images/projects/wild_salmon_migration_monitoring/species/chum.png) |
| [Chinook](https://psf.ca/info/chinook/) | Chinook are the largest Pacific salmon, capable of weighing over 100 pounds, though they typically average around 30 pounds. At maturity, they measure between 40 to 60 inches in length. | ![Chinook](/images/projects/wild_salmon_migration_monitoring/species/chinook.png) |

<em style="font-size:14px;line-height:1.4em;display:block;">
Gallery / Main Pacific Salmon species in Canada - courtesy to Pacific Salmon
  Foundation for the images
</em>
<br/>

Additionally, our system categorizes the following fish species: Bull Trout,
Rainbow Trout, Whitefish, Shiner, Pikeminnow, Jack Chinook, Lamprey, and
Cutthroat Trout.

### Deployed Systems

#### Underwater Cameras

We have deployed underwater cameras equipped with motion sensors. Upon
detecting motion, the camera activates, enabling our computer vision system to
precisely count fish movements and classify the species.

<p><iframe src="https://www.youtube.com/embed/V-rZSeM5YtY" loading="lazy" frameborder="0" allowfullscreen></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Underwater Camera Activated at Bear Creek River: Monitoring System Now Live
</em>
<br/>

This enables the generation of daily counts of fish moving back to their native
streams.

#### Sonar

Sonar, short for __Sound Navigation and Ranging__, is a technology that uses
sound waves to detect objects underwater. It works by emitting pulses of sound
waves (sonar pings) and then listening for the echoes bounced back from objects
in the water. By analyzing the time it takes for the sound waves to return and
the characteristics of the echoes, sonar systems can determine the distance,
size, shape, and sometimes even the composition of underwater objects. Sonar is
widely used in various applications such as navigation, underwater mapping,
fishing, and military operations.

![Sonar setup at Haida](/images/projects/wild_salmon_migration_monitoring/sonar/haida-sonar.jpg)
*Gallery/ Setting up sonars at Haida site*

The system is coupled with a sonar that also performs fish counting.

<p><iframe src="https://www.youtube.com/embed/DlKYhipkSNk" loading="lazy" frameborder="0" allowfullscreen></iframe></p>

#### Drone imagery

Drones are increasingly utilized in certain regions to monitor and
classify the number of fish migrating upstream. They provide aerial
perspectives that aid in accurately reporting fish populations and their
movement patterns.

![Drone Imagery](/images/projects/wild_salmon_migration_monitoring/drone/drone_imagery.webp)
*Gallery / Photogrammetry of a fresh water stream where salmon migrate -
Courtesy to [Aeria.ai](https://aeria.ai) for the picture*

## Conclusion

Overall, a wild salmon migration monitoring system is a powerful tool for
conserving wild salmon by providing the data needed for effective management,
identifying and addressing threats, and engaging stakeholders in conservation
efforts.

One can try out the model from the [ML Space]({{< ref
"/spaces/wild_salmon_migration_monitoring" >}}) or directly from the snippet below:

{{< hf_space "earthtoolsmaker-salmon-vision" >}}
