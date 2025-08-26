# Agents Guide

This document defines conventions for AI agents collaborating on this repository.

## Microservices Architecture Rules
- Services live under `services/<name>`.
- Each service contains:
  - `src/` – application code
  - `tests/` – pytest suite
  - `docs/` – service documentation
  - `Dockerfile` – container definition

## Folder Structure Template
```
services/
└── <service-name>/
    ├── src/
    ├── tests/
    ├── docs/
    └── Dockerfile
```

## Agent Responsibilities
- Maintain documentation and follow coding standards.
- Run `pytest` before committing.
- Update this file with progress notes and next steps.
- Ensure work aligns with IEC 62304, ISO 13485 and ISO/IEC 27001.

## Deployment Approach
- Build Docker images with Google Cloud Build.
- Push images to Google Artifact Registry.
- Retrieve secrets from Google Secret Manager.

## Status Tracking
| Service | Description | Status | Next Step |
|---------|-------------|--------|-----------|
| VariantEffectService | Variant effect prediction API | scaffolding complete | integrate real model |

## Progress Log
- Initial repository scaffolding: README, LICENSE, .gitignore, docs, CI workflow.
- Added `VariantEffectService` with FastAPI endpoints, tests, docs, and Dockerfile.
- Refactored `VariantEffectService` endpoints and tests to async/await for concurrency readiness; updated CI dependencies.
- Updated repository metadata and CI workflow.

## Suggested Next Step
- Integrate real variant effect model into `VariantEffectService`.

## Microservice Status
| Service | Status |
|---------|--------|
| VariantEffectService | scaffolding complete |

## Project Tree
```
.
├── .github
│   └── workflows
│       └── ci.yml
├── .gitignore
├── AGENTS.md
├── LICENSE
├── README.md
├── docs
│   ├── PROJECT_INSTRUCTIONS.md
│   └── STANDARDS_REFERENCES.md
└── services
    ├── __init__.py
    └── VariantEffectService
        ├── Dockerfile
        ├── __init__.py
        ├── docs
        │   └── README.md
        ├── src
        │   ├── __init__.py
        │   └── main.py
        └── tests
            ├── __init__.py
            └── test_main.py
```
