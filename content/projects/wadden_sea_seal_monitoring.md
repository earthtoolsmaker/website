---
title: Wadden Sea Seal Monitoring
summary: Automated seal population monitoring system using AI to count, classify, and identify individual seals from aerial imagery in the Wadden Sea.
clients:
  - name: Wageningen Marine Research
    link: https://www.wur.nl/en/Research-Results/Research-Institutes/marine-research.htm
    logo: /images/clients/wageningen-marine-research/logo.png
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
space: /spaces/seal_identification/
tools:
  - Computer Vision
  - Machine Learning
  - Deep Learning
status: completed
date: 2025-11-24
pinned: true
image: /images/projects/wadden_sea_seal_monitoring/cover.jpg
---

The Wadden Sea, a UNESCO World Heritage Site stretching between the Netherlands and Denmark, hosts critical breeding colonies of grey seals and harbour seals. Understanding the health and dynamics of these populations is essential for marine conservation efforts in the region. Research teams at Wageningen Marine Research conduct aerial surveys multiple times annually, photographing seal colonies from aircraft to monitor population trends, age structure, and reproductive success.

{{< image_carousel id="wadden-sea-intro" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/wadden-sea.jpg" alt="Aerial view of the Wadden Sea" caption="The Wadden Sea, a UNESCO World Heritage Site, features extensive tidal flats and sandbanks that serve as critical haul-out sites for seal colonies." >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/cover.jpg" alt="Seals on a sandbank in the Wadden Sea" caption="Grey seals and harbour seals hauled out on a sandbank in the Wadden Sea, the focus of our automated monitoring system." >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/wadden-sea-map.png" alt="Map of the Wadden Sea" caption="The Wadden Sea stretches along the coasts of the Netherlands, Germany, and Denmark." >}}
{{< /image_carousel >}}

However, analyzing these aerial images has traditionally been an enormously time-consuming task. Researchers spend hundreds of hours manually counting and classifying individual seals across thousands of photographs, identifying species, life stages, positions, and vital status. This tedious work leaves limited time for the higher-level biological analysis and statistical modeling that drives conservation decisions.

We partnered with Wageningen Marine Research to develop an end-to-end AI-powered system that automates the detection, counting, and classification of seals from aerial imagery. The system employs advanced computer vision models to handle five distinct classification tasks, coupled with a seal re-identification capability that enables long-term tracking of individual animals. Researchers now use an intuitive web application to review and refine AI predictions, dramatically reducing manual workload while maintaining scientific rigor.

## Vital for Marine Ecosystems

Seals play crucial roles in the Wadden Sea ecosystem and serve as important indicators of marine environmental health:

- **Apex predators**: Maintain balance in fish populations and marine food webs through selective predation
- **Ecosystem health indicators**: Population trends reflect broader changes in marine ecosystem quality and prey availability
- **Nutrient cycling**: Transfer nutrients between offshore feeding grounds and coastal haul-out sites
- **Biodiversity support**: Contribute to the ecological complexity of the UNESCO World Heritage Site
- **Scientific value**: Long-term monitoring provides data for understanding climate change impacts on marine mammals
- **Economic and cultural importance**: Support eco-tourism and represent iconic species of European coastal heritage

## Conservation and Monitoring Challenges

Effective seal population management in the Wadden Sea faces several challenges:

- **Labor-intensive surveys**: Manual counting and classification of thousands of seals across aerial photographs requires hundreds of researcher hours per survey season
- **Multi-attribute monitoring**: Researchers must simultaneously record species (grey vs harbour), life stage (adult vs pup), position (on land vs in water), vitality (alive vs dead), and sex (male vs female)
- **Seasonal breeding dynamics**: Precise pup counts and sex ratios during breeding season are critical for understanding population health but difficult to obtain manually
- **Image quality variation**: Aerial photographs vary in lighting, angle, resolution, and seal density, requiring expert judgment for accurate classification
- **Individual tracking needs**: Understanding movement patterns, site fidelity, and individual life histories requires non-invasive identification methods
- **Long-term data consistency**: Maintaining standardized counting protocols across years and different observers is challenging without automated assistance

## How Automated Monitoring Helps Conservation

An AI-powered seal monitoring system addresses these challenges and amplifies conservation impact:

- **Increased efficiency**: Automated detection and classification reduces analysis time from hundreds of hours to a fraction, enabling more frequent surveys
- **Standardized methodology**: Consistent AI-driven classification reduces observer bias and improves data comparability across years
- **Enhanced accuracy**: Deep learning models trained on thousands of examples can detect subtle differences and reduce counting errors
- **Focus on biology**: Researchers spend less time on tedious counting and more time on ecological interpretation and conservation strategy
- **Individual life histories**: Re-identification capabilities enable tracking of individual seals across seasons and years, revealing movement patterns and survival rates
- **Scalable monitoring**: The system can process large image datasets quickly, enabling expansion to additional colonies and more comprehensive coverage

## Project Scope and Objectives

In partnership with Wageningen Marine Research, we developed a comprehensive monitoring solution for two seal species in the Wadden Sea: grey seals (*Halichoerus grypus*) and harbour seals (*Phoca vitulina*). The project delivers two integrated AI systems working in tandem:

**Multi-Classifier Detection System**: Automatically processes aerial images to detect all seals and classify them across five critical attributes:
- **Species**: Grey seal vs harbour seal
- **Life stage**: Adult vs pup
- **Location**: On land (haul-out) vs swimming in water
- **Vitality**: Alive vs dead
- **Sex**: Male vs female

**Seal Re-Identification System**: Employs advanced computer vision to identify individual seals based on unique whisker patterns and facial features, enabling non-invasive long-term tracking without physical tagging.

Both systems integrate into a web application where researchers review AI predictions, make corrections when needed, and export validated data for statistical analysis.

## Developed Tools: Multi-Classifier Detection System

### Detection and Classification Pipeline

![Detection Pipeline](/images/projects/wadden_sea_seal_monitoring/seals/pipeline-detection-classification.png)
*Overview of the multi-classifier detection pipeline from aerial imagery to classified seal counts*

The detection system operates in multiple stages:

**1. Seal Detection**: A deep learning object detection model scans aerial photographs to locate all individual seals, regardless of density, overlap, or positioning. The model handles challenging conditions including partially submerged animals, varying lighting, and different camera angles.

**2. Multi-Attribute Classification**: Once detected, each seal is processed through five specialized classification heads:

- **Species Classifier**: Distinguishes grey seals from harbour seals based on body size, head shape, and coloration patterns. Grey seals are larger with more elongated snouts, while harbour seals have rounder heads and spotted coats.
- **Life Stage Classifier**: Identifies adults versus pups based on size ratios and, during breeding season, proximity to larger adults. Pup counts are critical for calculating birth rates and population growth.
- **Location Classifier**: Determines whether seals are hauled out on land/sandbanks or swimming in shallow water. This helps understand habitat use and behavior patterns.
- **Vitality Classifier**: Detects deceased individuals, which is important for mortality monitoring and understanding causes of death during breeding season.
- **Sex Classifier**: Differentiates males from females based on size dimorphism and, when visible, secondary sexual characteristics. Sex ratios inform breeding biology and population structure analyses.

### Web Application for Review and Validation

{{< image_carousel id="webapp-review" items="2" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/seals/webapp-screen-2.png" alt="Web Application Review Interface" caption="Researchers review and validate AI predictions through an intuitive web interface" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/seals/webapp-screen-3.png" alt="Web Application Review Interface" caption="Researchers review and validate AI predictions through an intuitive web interface" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/seals/webapp-detour-screen-2.png" alt="Web Application Review detouring tools" caption="Web application tools for reviewing and adjusting AI predictions" >}}
{{< /image_carousel >}}

The web application provides researchers with powerful tools to interact with AI predictions:

- **Visual Overlay**: Detected seals are highlighted with bounding boxes and color-coded labels showing all five classification attributes
- **Batch Review**: Researchers can quickly scan through hundreds of detections, focusing attention on uncertain predictions flagged by the model
- **One-Click Corrections**: Simple interface to update any classification attribute or add missed seals that the model failed to detect
- **Confidence Scoring**: Model displays confidence levels for each prediction, helping researchers prioritize quality control efforts
- **Export Functionality**: Validated data exports to spreadsheets and databases for integration with existing research workflows

## Developed Tools: Seal Re-Identification System

### Non-Invasive Individual Tracking

Traditional methods for tracking individual marine mammals often involve physical tags, which require capture and handling—stressful for animals and logistically challenging for researchers. Our seal re-identification system provides a completely non-invasive alternative by recognizing unique natural markings.

Seals possess stable, distinctive whisker patterns and facial features that remain consistent across their lifetimes. Similar to human facial recognition or the spot patterns used in trout identification, these natural markers enable AI-powered individual identification from photographs alone.

### Re-Identification Pipeline

![Re-Identification Pipeline](/images/projects/wadden_sea_seal_monitoring/reid/pipeline.png)
*Two-stage re-identification pipeline: feature extraction followed by similarity matching against database*

The seal re-identification system operates in two stages:

**1. Feature Extraction**: A deep learning model processes cropped seal face images to extract high-dimensional feature embeddings that capture unique whisker configurations, facial markings, and head shape characteristics. These embeddings are designed to remain stable across different poses, lighting conditions, and image quality.

**2. Similarity Matching**: When a new seal is photographed, its embedding is compared against a database of known individuals using cosine similarity or Euclidean distance metrics. The system returns the top-k most similar matches with confidence scores, allowing researchers to confirm identity or register a new individual.

### Example Matches and Unique Features

{{< image_carousel id="seal-reid-matches" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_different_seasons.png" alt="Same seal photographed in different seasons" caption="The same individual seal successfully re-identified across different survey seasons, demonstrating the system's ability to track seals over time." shadow="false" rounded="false" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_whisker_patterns.png" alt="Matching whisker patterns between sightings" caption="Re-identification based on unique whisker spot patterns that remain stable throughout a seal's lifetime." shadow="false" rounded="false" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_spot_patterns.png" alt="Matching spot patterns between sightings" caption="Distinctive spot patterns on the seal's coat provide reliable identification markers across different photographs." shadow="false" rounded="false" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_facial_patterns.png" alt="Matching facial patterns between sightings" caption="Facial feature matching identifies the same individual seal using unique head shape and marking patterns." shadow="false" rounded="false" >}}
{{< /image_carousel >}}

### Conservation Insights from Re-Identification

Tracking individual seals over time unlocks powerful conservation insights:

- **Site Fidelity**: Understanding which individuals return to the same haul-out sites year after year versus those that move between colonies
- **Movement Patterns**: Mapping how seals distribute across the Wadden Sea throughout different seasons and life stages
- **Survival Rates**: Calculating individual survival probabilities by tracking re-sightings across multiple survey years
- **Reproductive Success**: Identifying individual females and tracking their pupping success over time
- **Colony Dynamics**: Understanding immigration, emigration, and social structure within breeding colonies
- **Behavioral Ecology**: Linking individual identification with behavioral observations and habitat use patterns

This individual-level data complements population-wide counts to provide a comprehensive picture of Wadden Sea seal ecology and conservation status.

## Impact and Future Applications

The automated seal monitoring system has transformed research workflows at Wageningen Marine Research:

- **Time Savings**: Researchers estimate 85-90% reduction in time spent on manual counting and classification tasks
- **Research Focus**: Scientists now dedicate more effort to biological interpretation, statistical modeling, and conservation recommendations rather than tedious data entry
- **Improved Data Quality**: Standardized AI classification reduces observer bias and improves consistency across survey years
- **Expanded Capacity**: The efficiency gains enable processing of larger image datasets and potentially more frequent surveys
- **Individual Insights**: Re-identification capabilities provide entirely new dimensions of data on seal behavior, movement, and life history
- **Scalable Framework**: The system architecture can be adapted for seal monitoring in other regions or extended to additional marine mammal species

By combining cutting-edge computer vision with ecological expertise, this project demonstrates how AI can amplify conservation science without replacing the critical judgment and biological knowledge of field researchers.

## Try the Seal Re-Identification System

Experience the re-identification model in action through our interactive demonstration. Upload images of seal faces to see how the system extracts unique features and matches individuals:

{{< hf_space "earthtoolsmaker-seal-reid" >}}
