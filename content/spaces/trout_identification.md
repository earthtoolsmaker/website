---
title: Trout Identification
emoji: 🕵️
summary: A computer vision system analyzes the spot patterns of trout to identify individual fish. This innovative, non-invasive approach aims to monitor trout populations in British Columbia over time, ultimately supporting and enhancing conservation efforts in the region.
github_repo: https://github.com/earthtoolsmaker/bear-conservation
date: 2024-12-08
hero_image: /images/pages/spaces/trout_identification/hero.jpg
project: /projects/trout_identification/
hf_space: earthtoolsmaker-trout-reid
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/trout-reID/tree/main
manual_steps:
  - step_name: Image Selection
    description: Choose an image from the examples provided below, or upload your own data.
  - step_name: Run the ML model
    description: Click the 'Identify' button to initiate the machine learning model.
  - step_name: Visualize the results
    description: The system will standardize the fish images and compare them to our database of trout from British Columbia. It then identifies the individual fish that has the highest probability of matching. If no match is found, the fish is classified as a new entry.
---
