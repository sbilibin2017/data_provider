import pytest

from src.data_provider.schemas import CsgoGameSchema
from src.data_provider.services import CsgoGameService

@pytest.mark.asyncio
async def test_csgo_game_attributes():
    csgo_game_service = CsgoGameService()
    assert hasattr(csgo_game_service, "generate")


@pytest.mark.asyncio
async def test_csgo_game():
    csgo_game_service = CsgoGameService()
    generated = await csgo_game_service.generate()
    assert isinstance(generated, CsgoGameSchema)
