from fastapi import Depends

from src.data_provider.api.v1.dependencies import (get_league_repository,
                                                   get_logger,
                                                   get_map_repository,
                                                   get_player_repository,
                                                   get_round_repository,
                                                   get_serie_repository,
                                                   get_stat_repository,
                                                   get_team_repository,
                                                   get_tournament_repository,)
from src.data_provider.interfaces import (IDataProviderBaseRepository,
                                          IDataProviderRepository,
                                          IDataProviderService, ILogger,)
from src.data_provider.schemas import (CsgoGameSchema, LeagueSchema, MapSchema,
                                       PlayerSchema, RoundSchema, SerieSchema,
                                       StatSchema, TeamSchema,
                                       TournamentSchema,)
from src.data_provider.services import CsgoGameService


def get_csgo_game_service(
    map_repository: IDataProviderRepository[MapSchema] = Depends(
        get_map_repository
    ),
    league_repository: IDataProviderRepository[LeagueSchema] = Depends(
        get_league_repository
    ),
    serie_repository: IDataProviderRepository[SerieSchema] = Depends(
        get_serie_repository
    ),
    tournament_repository: IDataProviderRepository[TournamentSchema] = Depends(
        get_tournament_repository
    ),
    team_repository: IDataProviderRepository[TeamSchema] = Depends(
        get_team_repository
    ),
    player_repository: IDataProviderRepository[PlayerSchema] = Depends(
        get_player_repository
    ),
    stat_repository: IDataProviderBaseRepository[StatSchema] = Depends(
        get_stat_repository
    ),
    round_repository: IDataProviderBaseRepository[RoundSchema] = Depends(
        get_round_repository
    ),
    logger: ILogger = Depends(get_logger),
) -> IDataProviderService[CsgoGameSchema]:
    return CsgoGameService(
        map_repository,
        league_repository,
        serie_repository,
        tournament_repository,
        team_repository,
        player_repository,
        stat_repository,
        round_repository,
        logger,
    )
