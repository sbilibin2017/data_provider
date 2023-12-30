import gc
import random
from functools import cache
from typing import Any

from src.data_provider.core import Logger, Settings
from src.data_provider.interfaces import ILogger
from src.data_provider.schemas import TeamSchema
from src.data_provider.utils import singleton


@singleton
class TeamRepository:
    def __init__(
        self,
        settings: Settings = Settings(),
        logger: ILogger = Logger(),
    ):
        self.settings = settings
        self.logger = logger
        self.count: int = settings.data_provider.team.count
        self.prefix: str = settings.data_provider.team.prefix

    @cache
    def fit(self) -> None:
        self.data = []
        for _ in range(self.count):
            d = {}
            d["name"] = f"{self.prefix}_{_+1}"
            d["location"] = f"location_{random.randint(1, 101)}"
            self.data.append(d)
            del d
        gc.collect()

    async def generate(self, *args: Any, **kwargs: Any) -> TeamSchema:
        data = random.choice(self.data)
        return TeamSchema(**data)
