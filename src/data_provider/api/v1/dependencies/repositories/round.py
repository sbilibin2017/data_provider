from fastapi import Depends

from src.data_provider.api.v1.dependencies import get_logger
from src.data_provider.interfaces import IDataProviderBaseRepository, ILogger
from src.data_provider.repositories import RoundRepository
from src.data_provider.schemas import RoundSchema


def get_round_repository(
    logger: ILogger = Depends(get_logger),
) -> IDataProviderBaseRepository[RoundSchema]:
    return RoundRepository(logger)
