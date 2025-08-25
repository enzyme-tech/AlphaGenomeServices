# VariantEffectService

Minimal FastAPI service exposing variant effect predictions.

## Endpoints
- `GET /health` – service status for monitoring (IEC 62304).
- `POST /predict` – placeholder variant effect result; no PHI processed (GDPR, HIPAA).

## Notes
This service is a research prototype and does not provide clinical decision support.
