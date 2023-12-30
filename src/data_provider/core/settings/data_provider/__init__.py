from pydantic_settings import BaseSettings

from src.data_provider.core.settings.data_provider.league import LeagueSettings
from src.data_provider.core.settings.data_provider.map import MapSettings
from src.data_provider.core.settings.data_provider.player import PlayerSettings
from src.data_provider.core.settings.data_provider.serie import SerieSettings
from src.data_provider.core.settings.data_provider.team import TeamSettings
from src.data_provider.core.settings.data_provider.tournament import \
    TournamentSettings


class DataProviderSettings(BaseSettings):
    map: MapSettings = MapSettings()  # pyright: ignore
    league: LeagueSettings = LeagueSettings()  # pyright: ignore
    serie: SerieSettings = SerieSettings()  # pyright: ignore
    tournament: TournamentSettings = TournamentSettings()  # pyright: ignore
    team: TeamSettings = TeamSettings()  # pyright: ignore
    player: PlayerSettings = PlayerSettings()  # pyright: ignore


__all__ = [
    "DataProviderSettings",
]
