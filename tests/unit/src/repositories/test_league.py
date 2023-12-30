from datetime import datetime
from uuid import UUID

import pytest

from src.data_provider.repositories import LeagueRepository


@pytest.mark.asyncio
async def test_league_attributes():
    league_repository = LeagueRepository()
    assert hasattr(league_repository, "fit")
    assert hasattr(league_repository, "generate")


@pytest.mark.asyncio
async def test_league():
    league_repository = LeagueRepository()
    league_repository.fit()
    generated = await league_repository.generate()
    assert hasattr(generated, "id")
    assert hasattr(generated, "name")
    assert hasattr(generated, "updated_at")
    assert isinstance(generated.id, UUID)
    assert isinstance(generated.name, str)
    assert isinstance(generated.updated_at, datetime)
