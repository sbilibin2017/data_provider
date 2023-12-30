from fastapi import Depends

from src.data_provider.api.v1.dependencies import get_logger, get_settings
from src.data_provider.core import Settings
from src.data_provider.interfaces import IDataProviderRepository, ILogger
from src.data_provider.repositories import TeamRepository
from src.data_provider.schemas import TeamSchema


def get_team_repository(
    settings: Settings = Depends(get_settings),
    logger: ILogger = Depends(get_logger),
) -> IDataProviderRepository[TeamSchema]:
    return TeamRepository(settings, logger)
