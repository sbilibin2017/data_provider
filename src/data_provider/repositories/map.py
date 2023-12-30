import gc
import random
from functools import cache
from typing import Any

from src.data_provider.core import Logger, Settings
from src.data_provider.interfaces import ILogger
from src.data_provider.schemas import MapSchema
from src.data_provider.utils import singleton


@singleton
class MapRepository:
    def __init__(
        self,
        settings: Settings = Settings(),
        logger: ILogger = Logger(),
    ):
        self.settings = settings
        self.logger = logger
        self.count: int = self.settings.data_provider.map.count
        self.prefix: str = self.settings.data_provider.map.prefix

    @cache
    def fit(self) -> None:
        self.data = []
        for _ in range(self.count):
            d = {}
            d["name"] = f"{self.prefix}_{_+1}"
            self.data.append(d)
            del d
        gc.collect()

    async def generate(self, *args: Any, **kwargs: Any) -> MapSchema:
        data = random.choice(self.data)
        if kwargs is not None:
            data.update(**kwargs)
        return MapSchema(**data)
