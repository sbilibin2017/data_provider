from typing import Any, Protocol, TypeVar

from src.data_provider.core.settings import Settings
from src.data_provider.interfaces.core.logger import ILogger

T = TypeVar("T", covariant=True)


class IDataProviderBaseRepository(Protocol[T]):
    @property
    def logger(self) -> ILogger:
        ...

    @logger.setter
    def logger(self) -> ILogger:
        ...

    async def generate(self, *args: Any | None, **kwargs: Any | None) -> T:
        ...


class IDataProviderRepository(IDataProviderBaseRepository[T], Protocol[T]):
    @property
    def settings(self) -> Settings:
        ...

    @settings.setter
    def settings(self) -> Settings:
        ...

    def fit(self) -> None:
        ...


__all__ = ["IDataProviderBaseRepository", "IDataProviderRepository"]
