from pydantic import BaseModel

from src.data_provider.schemas.player import PlayerSchema
from src.data_provider.schemas.stat import StatSchema
from src.data_provider.schemas.team import TeamSchema


class TeamOpponentPlayerStatSchema(BaseModel):
    team: TeamSchema
    opponent: TeamSchema
    player: PlayerSchema
    stat: StatSchema
