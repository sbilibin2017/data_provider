from datetime import datetime

from src.data_provider.schemas.map import MapSchema
from src.data_provider.schemas.match import MatchSchema
from src.data_provider.schemas.mixins import IdMixin
from src.data_provider.schemas.round import RoundSchema
from src.data_provider.schemas.team_opponent_player_stat import \
    TeamOpponentPlayerStatSchema


class CsgoGameSchema(IdMixin):
    begin_at: datetime
    map: MapSchema
    match: MatchSchema
    players: list[TeamOpponentPlayerStatSchema]
    rounds: list[RoundSchema]
