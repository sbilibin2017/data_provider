import pytest

from src.data_provider.repositories import StatRepository


@pytest.mark.asyncio
async def test_stat_attributes():
    round_repository = StatRepository()
    assert not hasattr(round_repository, "fit")
    assert hasattr(round_repository, "generate")


@pytest.mark.asyncio
async def test_stat():
    stat_repository = StatRepository()
    generated = await stat_repository.generate()
    assert hasattr(generated, "kills")
    assert isinstance(generated.kills, int)
