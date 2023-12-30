from datetime import datetime
from uuid import UUID, uuid4

import pytest

from src.data_provider.repositories import TournamentRepository


@pytest.mark.asyncio
async def test_tournament_attributes():
    tournament_repository = TournamentRepository()
    assert hasattr(tournament_repository, "fit")
    assert hasattr(tournament_repository, "generate")


@pytest.mark.asyncio
async def test_tournament():
    tournament_repository = TournamentRepository()
    tournament_repository.fit()
    generated = await tournament_repository.generate(serie_id=uuid4())
    assert hasattr(generated, "id")
    assert hasattr(generated, "name")
    assert hasattr(generated, "updated_at")
    assert hasattr(generated, "serie_id")
    assert hasattr(generated, "prizepool")
    assert isinstance(generated.id, UUID)
    assert isinstance(generated.name, str)
    assert isinstance(generated.updated_at, datetime)
    assert isinstance(generated.serie_id, UUID)
    assert isinstance(generated.prizepool, str)
