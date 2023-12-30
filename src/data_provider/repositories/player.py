import gc
import random
from datetime import date
from functools import cache
from typing import Any

from src.data_provider.core import Logger, Settings
from src.data_provider.interfaces import ILogger
from src.data_provider.schemas import PlayerSchema
from src.data_provider.utils import singleton


@singleton
class PlayerRepository:
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
            d["nationality"] = f"nationality_{random.randint(1, 101)}"
            d["hometown"] = f"hometown_{random.randint(1, 101)}"
            d["birthday"] = date(
                year=random.randint(1995, 2005),
                month=random.randint(1, 12),
                day=random.randint(1, 28),
            ).isoformat()
            self.data.append(d)
            del d
        gc.collect()

    async def generate(self, *args: Any, **kwargs: Any) -> PlayerSchema:
        data = random.choice(self.data)
        if kwargs is not None:
            data.update(**kwargs)
        return PlayerSchema(**data)
