# AlphaGenomeServices

This repository hosts **research-use services** for AlphaGenome workflows.  
First service: **VariantEffectService** – functional variant effect predictions.

## Overview
- Minimal, functional API for variant effect predictions.
- Built following clinical-grade software practices to ease future certification.
- Licensed under MIT License (placeholder).

## Compliance and Quality
- Branch protection on main requires PR reviews + passing CI (IEC 62304, ISO 13485).
- CI executes pytest.
- Secrets are stored in Google Secret Manager (ISO/IEC 27001).
- Cloud Build pushes Docker images to Artifact Registry.

## Cloud Build Integration (example)
```yaml
steps:
- name: gcr.io/cloud-builders/docker
  args: ['build','-t','${REGION}-docker.pkg.dev/${PROJECT_ID}/alphagenome/variant-effect:$COMMIT_SHA','.']
- name: gcr.io/cloud-builders/docker
  args: ['push','${REGION}-docker.pkg.dev/${PROJECT_ID}/alphagenome/variant-effect:$COMMIT_SHA']
images:
- '${REGION}-docker.pkg.dev/${PROJECT_ID}/alphagenome/variant-effect:$COMMIT_SHA'
```

## Disclaimer
Research use only. Not for clinical decision-making.
