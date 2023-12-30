import gc
import random
from functools import cache
from typing import Any

from src.data_provider.core import Logger, Settings
from src.data_provider.interfaces import ILogger
from src.data_provider.schemas import SerieSchema
from src.data_provider.utils import singleton


@singleton
class SerieRepository:
    def __init__(
        self,
        settings: Settings = Settings(),
        logger: ILogger = Logger(),
    ):
        self.settings = settings
        self.logger = logger
        self.count: int = settings.data_provider.serie.count
        self.prefix: str = settings.data_provider.serie.prefix

    @cache
    def fit(self) -> None:
        self.data = []
        for _ in range(self.count):
            d = {}
            d["name"] = f"{self.prefix}_{_+1}"
            d["tier"] = random.choice(["a", "b", "c", "d"])
            self.data.append(d)
            del d
        gc.collect()

    async def generate(self, *args: Any, **kwargs: Any) -> SerieSchema:
        data = random.choice(self.data)
        if kwargs is not None:
            data.update(**kwargs)
        return SerieSchema(**data)
