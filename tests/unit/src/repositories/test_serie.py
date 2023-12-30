from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

import pytest

from src.data_provider.repositories import SerieRepository


@pytest.mark.asyncio
async def test_serie_attributes():
    serie_repository = SerieRepository()
    assert hasattr(serie_repository, "fit")
    assert hasattr(serie_repository, "generate")


@pytest.mark.asyncio
async def test_serie():
    serie_repository = SerieRepository()
    serie_repository.fit()
    generated = await serie_repository.generate(league_id=uuid4())
    assert hasattr(generated, "id")
    assert hasattr(generated, "name")
    assert hasattr(generated, "updated_at")
    assert hasattr(generated, "league_id")
    assert hasattr(generated, "tier")
    assert isinstance(generated.id, UUID)
    assert isinstance(generated.name, str)
    assert isinstance(generated.updated_at, datetime)
    assert isinstance(generated.league_id, UUID)
    assert isinstance(generated.tier, Enum)
