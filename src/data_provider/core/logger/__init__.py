from aiologger.loggers.json import JsonLogger

from src.data_provider.utils import singleton


@singleton
class Logger:
    def __init__(self) -> None:
        self.logger = JsonLogger.with_default_handlers()

    async def info(self, msg: str) -> None:
        await self.logger.info(msg)

    async def error(self, msg: str) -> None:
        await self.logger.error(msg)


__all__ = ["Logger"]
