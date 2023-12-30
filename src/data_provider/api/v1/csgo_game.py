from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.data_provider.api.v1 import Response
from src.data_provider.api.v1.dependencies import get_csgo_game_service
from src.data_provider.interfaces import IDataProviderService
from src.data_provider.schemas import CsgoGameSchema

router: APIRouter = APIRouter(prefix="/api/v1", tags=["csgo_game"])


@router.get("/")
async def generate_csgo_game(
    csgo_game_service: IDataProviderService[CsgoGameSchema] = Depends(
        get_csgo_game_service
    ),
) -> Response[CsgoGameSchema]:
    data = await csgo_game_service.generate()
    return Response[CsgoGameSchema](data=data, status=HTTPStatus.OK)
