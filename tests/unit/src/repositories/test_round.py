from uuid import UUID, uuid4

import pytest

from src.data_provider.repositories import RoundRepository


@pytest.mark.asyncio
async def test_round_attributes():
    round_repository = RoundRepository()
    assert not hasattr(round_repository, "fit")
    assert hasattr(round_repository, "generate")


@pytest.mark.asyncio
async def test_round():
    ct_id, t_id = uuid4(), uuid4()
    round_repository = RoundRepository()
    generated = await round_repository.generate(
        ct_id=ct_id, t_id=t_id, round=1, outcome="exploded", winner_id=t_id
    )
    assert hasattr(generated, "winner_id")
    assert isinstance(generated.winner_id, UUID)
