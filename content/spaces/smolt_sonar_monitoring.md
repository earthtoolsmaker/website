---
title: Smolt Sonar Monitoring
emoji: 🔊
summary: A computer vision system that processes ARIS sonar imagery to automatically detect, track, and count juvenile salmon (smolt) during their downstream migration. The system leverages a YOLOv11 detection model combined with BoTSort tracking to monitor smolt populations, supporting conservation efforts and sustainable fisheries management.
date: 2026-01-10
project: /projects/monitoring_smolt_salmon_migration_with_sonar/
hf_space: Lumax-eco-sonar-smolt
hf_space_code: https://huggingface.co/spaces/Lumax/eco-sonar-smolt/tree/main
manual_steps:
  - step_name: Video Selection
    description: Choose a preprocessed sonar video from the examples provided below, or upload your own sonar footage.
  - step_name: Run the ML model
    description: Click the 'Submit' button to initiate the detection and tracking pipeline.
  - step_name: Visualize the results
    description: The system will generate an annotated video with bounding boxes around detected smolt, track their movement, and count individuals by migration direction.
---
