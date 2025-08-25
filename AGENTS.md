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
| core-api | Variant effect API service | not started | scaffold service |

## Progress Log
- Initial repository scaffolding: README, LICENSE, .gitignore, docs, CI workflow.

## Suggested Next Step
- Create `services/core-api` with initial API endpoints and tests.

## Microservice Status
| Service | Status |
|---------|--------|
| core-api | not started |

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
└── docs
    ├── PROJECT_INSTRUCTIONS.md
    └── STANDARDS_REFERENCES.md
```
