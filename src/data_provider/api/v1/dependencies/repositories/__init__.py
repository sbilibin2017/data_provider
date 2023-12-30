from .league import get_league_repository
from .map import get_map_repository
from .player import get_player_repository
from .round import get_round_repository
from .serie import get_serie_repository
from .stat import get_stat_repository
from .team import get_team_repository
from .tournament import get_tournament_repository

__all__ = [
    "get_league_repository",
    "get_serie_repository",
    "get_tournament_repository",
    "get_map_repository",
    "get_team_repository",
    "get_player_repository",
    "get_round_repository",
    "get_stat_repository",
]
