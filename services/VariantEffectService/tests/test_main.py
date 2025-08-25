"""Tests for VariantEffectService endpoints."""

import pytest
from httpx import ASGITransport, AsyncClient

from ..src.main import app


@pytest.mark.asyncio
async def test_health() -> None:
    """Ensure the health endpoint reports service availability (IEC 62304)."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_predict_placeholder() -> None:
    """Verify the placeholder prediction is returned without error."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/predict", json={"variant": "chr1:A>T"})
    assert response.status_code == 200
    assert response.json() == {"effect": "unknown"}
