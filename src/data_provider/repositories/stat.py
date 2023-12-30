import random
from typing import Any

from src.data_provider.core import Logger
from src.data_provider.interfaces import ILogger
from src.data_provider.schemas import StatSchema
from src.data_provider.utils import singleton


@singleton
class StatRepository:
    def __init__(
        self,
        logger: ILogger = Logger(),
    ):
        self.logger = logger

    async def generate(self, *args: Any, **kwargs: Any) -> StatSchema:
        return StatSchema(
            kills=random.randint(0, 21),
            deaths=random.randint(0, 21),
            assists=random.randint(0, 41),
            headshots=random.randint(0, 17),
            flash_assists=random.randint(0, 41),
            k_d_diff=random.randint(0, 5),
            first_kills_diff=random.randint(-5, 5),
            adr=random.randint(0, 301),
            kast=random.randint(0, 101),
            rating=random.randint(0, 1001),
        )
