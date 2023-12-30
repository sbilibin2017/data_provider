from datetime import datetime
from uuid import UUID

import pytest

from src.data_provider.repositories import MapRepository


@pytest.mark.asyncio
async def test_map_attributes():
    map_repository = MapRepository()
    assert hasattr(map_repository, "fit")
    assert hasattr(map_repository, "generate")


@pytest.mark.asyncio
async def test_map():
    map_repository = MapRepository()
    map_repository.fit()
    generated = await map_repository.generate()
    assert hasattr(generated, "id")
    assert hasattr(generated, "name")
    assert hasattr(generated, "updated_at")
    assert isinstance(generated.id, UUID)
    assert isinstance(generated.name, str)
    assert isinstance(generated.updated_at, datetime)
