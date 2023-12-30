from fastapi import FastAPI
from src.data_provider import app_factory
from src.data_provider.api.v1 import csgo_game
from fastapi.responses import ORJSONResponse


app: FastAPI = app_factory.create(
    routers=(csgo_game.router,),
    title="PandaScore csgo game mock data provider",
    version="1.0.0",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)
