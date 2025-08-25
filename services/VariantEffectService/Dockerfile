# Dockerfile for VariantEffectService
# Uses official Python image to ensure maintainability (IEC 62304).
FROM python:3.11-slim

WORKDIR /app
COPY src/ /app/src/

# Install runtime dependencies; kept minimal to reduce attack surface (ISO/IEC 27001).
RUN pip install --no-cache-dir fastapi uvicorn

# Expose default FastAPI port
EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
