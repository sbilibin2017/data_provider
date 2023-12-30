from pydantic import BaseModel

from src.data_provider.schemas.league import LeagueSchema
from src.data_provider.schemas.serie import SerieSchema
from src.data_provider.schemas.tournament import TournamentSchema


class MatchSchema(BaseModel):
    league: LeagueSchema
    serie: SerieSchema
    tournament: TournamentSchema

    class Config:
        frozen = True
