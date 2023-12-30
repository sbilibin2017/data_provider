from datetime import datetime
from uuid import UUID

import pytest

from src.data_provider.repositories import PlayerRepository


@pytest.mark.asyncio
async def test_player_attributes():
    player_repository = PlayerRepository()
    assert hasattr(player_repository, "fit")
    assert hasattr(player_repository, "generate")


@pytest.mark.asyncio
async def test_player():
    player_repository = PlayerRepository()
    player_repository.fit()
    generated = await player_repository.generate()
    assert hasattr(generated, "id")
    assert hasattr(generated, "name")
    assert hasattr(generated, "updated_at")
    assert hasattr(generated, "nationality")
    assert hasattr(generated, "hometown")
    assert hasattr(generated, "birthday")
    assert isinstance(generated.id, UUID)
    assert isinstance(generated.name, str)
    assert isinstance(generated.updated_at, datetime)
    assert isinstance(generated.nationality, str)
    assert isinstance(generated.hometown, str)
    assert isinstance(generated.birthday, str)
