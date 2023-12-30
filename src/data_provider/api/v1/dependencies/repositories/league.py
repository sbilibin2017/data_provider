from fastapi import Depends

from src.data_provider.api.v1.dependencies import get_logger, get_settings
from src.data_provider.core import Settings
from src.data_provider.interfaces import IDataProviderRepository, ILogger
from src.data_provider.repositories import LeagueRepository
from src.data_provider.schemas import LeagueSchema


def get_league_repository(
    settings: Settings = Depends(get_settings),
    logger: ILogger = Depends(get_logger),
) -> IDataProviderRepository[LeagueSchema]:
    return LeagueRepository(settings, logger)
