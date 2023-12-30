from typing import Protocol


class ILogger(Protocol):
    async def info(self, msg: str) -> None:
        ...

    async def error(self, msg: str) -> None:
        ...
