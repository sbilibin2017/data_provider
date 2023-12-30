from datetime import datetime
from uuid import UUID

import pytest

from src.data_provider.repositories import TeamRepository


@pytest.mark.asyncio
async def test_player_attributes():
    team_repository = TeamRepository()
    assert hasattr(team_repository, "fit")
    assert hasattr(team_repository, "generate")


@pytest.mark.asyncio
async def test_team():
    team_repository = TeamRepository()
    team_repository.fit()
    generated = await team_repository.generate()
    assert hasattr(generated, "id")
    assert hasattr(generated, "name")
    assert hasattr(generated, "updated_at")
    assert hasattr(generated, "location")
    assert isinstance(generated.id, UUID)
    assert isinstance(generated.name, str)
    assert isinstance(generated.updated_at, datetime)
    assert isinstance(generated.location, str)
