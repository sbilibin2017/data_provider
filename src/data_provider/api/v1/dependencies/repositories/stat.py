from fastapi import Depends

from src.data_provider.api.v1.dependencies import get_logger
from src.data_provider.interfaces import IDataProviderBaseRepository, ILogger
from src.data_provider.repositories import StatRepository
from src.data_provider.schemas import StatSchema


def get_stat_repository(
    logger: ILogger = Depends(get_logger),
) -> IDataProviderBaseRepository[StatSchema]:
    return StatRepository(logger)
