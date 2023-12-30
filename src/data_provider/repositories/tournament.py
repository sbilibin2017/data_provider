import gc
import random
from functools import cache
from typing import Any

from src.data_provider.core import Logger, Settings
from src.data_provider.interfaces import ILogger
from src.data_provider.schemas import TournamentSchema
from src.data_provider.utils import singleton


@singleton
class TournamentRepository:
    def __init__(
        self,
        settings: Settings = Settings(),
        logger: ILogger = Logger(),
    ):
        self.settings = settings
        self.logger = logger
        self.count: int = settings.data_provider.tournament.count
        self.prefix: str = settings.data_provider.tournament.prefix

    @cache
    def fit(self) -> None:
        self.data = []
        for _ in range(self.count):
            d = {}
            d["name"] = f"{self.prefix}_{_+1}"
            d["prizepool"] = "{size},{currency}".format(
                size=random.choice(
                    [
                        1000,
                        5000,
                        10000,
                        50000,
                        100000,
                        500000,
                        1000000,
                        5000000,
                    ]
                ),
                currency=random.choice(["ru ruble", "us dollar", "ch yuan"]),
            )
            self.data.append(d)
            del d
        gc.collect()

    async def generate(self, *args: Any, **kwargs: Any) -> TournamentSchema:
        data = random.choice(self.data)
        if kwargs is not None:
            data.update(**kwargs)
        return TournamentSchema(**data)
