from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class RoundOutcomeEnum(str, Enum):
    defused = "defused"
    exploded = "exploded"
    eliminated = "eliminated"
    timeout = "timeout"


class RoundSchema(BaseModel):
    ct_id: UUID
    t_id: UUID
    round: int
    winner_id: UUID
    outcome: RoundOutcomeEnum

    class Config:
        frozen = True
