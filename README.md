# Variant Effect API MVP

This repository hosts a minimal viable product of the **AlphaGenome** functional variant effect API. It provides research‑use access to the model developed by Google DeepMind.

## Overview
- Minimal, functional API for variant effect predictions.
- Built following clinical‑grade software practices to ease future certification.
- Licensed under the MIT License (placeholder – to be adjusted in the future).

## Compliance and Quality
- Branch protection on `main` requires pull‑request reviews and passing CI prior to merge, supporting traceability and controlled release (IEC 62304, ISO 13485).
- CI executes pytest to validate changes.
- Secrets are stored in **Google Secret Manager** rather than GitHub Secrets, aligning with ISO/IEC 27001 guidance.

## Cloud Build Integration
Google Cloud Build triggers build a Docker image and push it to Artifact Registry:
```yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', '${REGION}-docker.pkg.dev/${PROJECT_ID}/alphagenome-repo/alphagenome-mvp:$COMMIT_SHA', '.']
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', '${REGION}-docker.pkg.dev/${PROJECT_ID}/alphagenome-repo/alphagenome-mvp:$COMMIT_SHA']
images:
- '${REGION}-docker.pkg.dev/${PROJECT_ID}/alphagenome-repo/alphagenome-mvp:$COMMIT_SHA'
```

## Disclaimer
This project is provided for research use only and should not be used for clinical decision‑making.
