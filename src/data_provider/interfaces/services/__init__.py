from typing import Protocol, TypeVar

from src.data_provider.interfaces.core.logger import ILogger

T = TypeVar("T", covariant=True)


class IDataProviderService(Protocol[T]):
    @property
    def logger(self) -> ILogger:
        ...

    @logger.setter
    def logger(self) -> ILogger:
        ...

    async def generate(self) -> T:
        ...


__all__ = ["IDataProviderService"]
