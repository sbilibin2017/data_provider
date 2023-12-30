import random
from typing import Any
from uuid import UUID

from src.data_provider.core import Logger
from src.data_provider.interfaces import ILogger
from src.data_provider.schemas import RoundOutcomeEnum, RoundSchema
from src.data_provider.utils import singleton


@singleton
class RoundRepository:
    def __init__(
        self,
        logger: ILogger = Logger(),
    ):
        self.logger = logger

    async def generate(self, *args: Any, **kwargs: Any) -> RoundSchema:
        data: dict[str, Any] = {}
        if kwargs is not None:
            data.update(**kwargs)

        winner_id: UUID = random.choice([data["ct_id"], data["t_id"]])
        if winner_id == data["ct_id"]:
            outcome = random.choice(list(RoundOutcomeEnum))
        else:
            outcome = random.choice(list(RoundOutcomeEnum))

        data["winner_id"] = winner_id
        data["outcome"] = outcome

        return RoundSchema(**data)
