# Project Instructions – AlphaGenomeServices

All development must align with:
- ISO 13485, IEC 62304, ISO 14971, IEC 62366-1
- ISO/IEC 27001, 27017, 27018, 27701
- HIPAA, GDPR

## Expectations
- Comments explain WHY decisions were made (traceability).
- Secrets in Secret Manager, IAM least privilege.
- All changes tied to requirements/test cases.
- Identify risks + mitigations (ISO 14971).
- Avoid PHI unless explicitly declared (HIPAA/GDPR).
- Usability notes (IEC 62366-1).
- Deploy via Cloud Run + Batch, with logging/monitoring.

## Naming Conventions

- **Inside the repo (folders, docs):** use **PascalCase** (e.g., `VariantEffectService`).
- **For infrastructure (Docker images, Cloud Run, URLs):** use **kebab-case** (e.g., `variant-effect-service`).

This separation avoids conflicts:
- PascalCase improves readability in code and matches class/module conventions.
- kebab-case ensures compatibility with Docker, Kubernetes, and DNS constraints.

## Note
All outputs marked **research-only** unless validated.
