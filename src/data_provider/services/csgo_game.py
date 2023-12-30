import random
from datetime import datetime
from uuid import UUID

from src.data_provider.core import Logger
from src.data_provider.interfaces import (IDataProviderBaseRepository,
                                          IDataProviderRepository, ILogger,)
from src.data_provider.repositories import (LeagueRepository, MapRepository,
                                            PlayerRepository, RoundRepository,
                                            SerieRepository, StatRepository,
                                            TeamRepository,
                                            TournamentRepository,)
from src.data_provider.schemas import (CsgoGameSchema, LeagueSchema, MapSchema,
                                       MatchSchema, PlayerSchema, RoundSchema,
                                       SerieSchema, StatSchema,
                                       TeamOpponentPlayerStatSchema,
                                       TeamSchema, TournamentSchema,)
from src.data_provider.utils import singleton


@singleton
class CsgoGameService:
    def __init__(
        self,
        map_repository: IDataProviderRepository[MapSchema] = MapRepository(),
        league_repository: IDataProviderRepository[
            LeagueSchema
        ] = LeagueRepository(),
        serie_repository: IDataProviderRepository[
            SerieSchema
        ] = SerieRepository(),
        tournament_repository: IDataProviderRepository[
            TournamentSchema
        ] = TournamentRepository(),
        team_repository: IDataProviderRepository[
            TeamSchema
        ] = TeamRepository(),
        player_repository: IDataProviderRepository[
            PlayerSchema
        ] = PlayerRepository(),
        stat_repository: IDataProviderBaseRepository[
            StatSchema
        ] = StatRepository(),
        round_repository: IDataProviderBaseRepository[
            RoundSchema
        ] = RoundRepository(),
        logger: ILogger = Logger(),
    ):
        self.logger = logger
        self.map_repository = map_repository
        self.map_repository.fit()
        self.league_repository = league_repository
        self.league_repository.fit()
        self.serie_repository = serie_repository
        self.serie_repository.fit()
        self.tournament_repository = tournament_repository
        self.tournament_repository.fit()
        self.team_repository = team_repository
        self.team_repository.fit()
        self.player_repository = player_repository
        self.player_repository.fit()
        self.stat_repository = stat_repository
        self.round_repository = round_repository

    async def generate(self) -> CsgoGameSchema:
        begin_at: datetime = await self._generate_begin_at()
        map: MapSchema = await self.map_repository.generate()
        league: LeagueSchema = await self.league_repository.generate()
        serie: SerieSchema = await self.serie_repository.generate(
            league_id=league.id
        )
        tournament: TournamentSchema = (
            await self.tournament_repository.generate(serie_id=serie.id)
        )
        match: MatchSchema = await self._merge_league_serie_tournament(
            league, serie, tournament
        )
        teams: list[TeamSchema] = await self._generate_2teams()
        players: list[PlayerSchema] = await self._generate_10players()
        stats: list[StatSchema] = await self._generate_10stats()
        teams_opponents_players_stats: list[
            TeamOpponentPlayerStatSchema
        ] = await self._merge_team_opponent_player_stat(teams, players, stats)
        rounds: list[RoundSchema] = await self._generate_rounds(teams)
        return CsgoGameSchema(
            begin_at=begin_at,
            map=map,
            match=match,
            players=teams_opponents_players_stats,
            rounds=rounds,
        )

    async def _generate_begin_at(self) -> datetime:
        return datetime(
            year=random.randint(2012, 2026),
            month=random.randint(1, 12),
            day=random.randint(1, 29),
            hour=random.randint(0, 24),
        )

    async def _merge_league_serie_tournament(
        self,
        league: LeagueSchema,
        serie: SerieSchema,
        tournament: TournamentSchema,
    ) -> MatchSchema:
        return MatchSchema(league=league, serie=serie, tournament=tournament)

    async def _generate_2teams(self) -> list[TeamSchema]:
        teams: list[TeamSchema] = []
        team_ids: list[UUID] = []
        counter: int = 0
        while counter < 2:
            team: TeamSchema = await self.team_repository.generate()
            if team.id not in team_ids:
                teams.append(team)
                team_ids.append(team.id)
                counter += 1
        return teams

    async def _generate_10players(self) -> list[PlayerSchema]:
        players: list[PlayerSchema] = []
        player_ids: list[UUID] = []
        counter: int = 0
        while counter < 10:
            player: PlayerSchema = await self.player_repository.generate()
            if player.id not in player_ids:
                players.append(player)
                player_ids.append(player.id)
                counter += 1
        return players

    async def _generate_10stats(self) -> list[StatSchema]:
        return [await self.stat_repository.generate() for _ in range(10)]

    async def _merge_team_opponent_player_stat(
        self,
        teams: list[TeamSchema],
        players: list[PlayerSchema],
        stats: list[StatSchema],
    ) -> list[TeamOpponentPlayerStatSchema]:
        teams_opponents_players_stats: list[TeamOpponentPlayerStatSchema] = []
        for player, stat in zip(players[:5], stats[:5]):
            teams_opponents_players_stats.append(
                TeamOpponentPlayerStatSchema(
                    team=teams[0], opponent=teams[1], player=player, stat=stat
                )
            )
        for player, stat in zip(players[5:], stats[5:]):
            teams_opponents_players_stats.append(
                TeamOpponentPlayerStatSchema(
                    team=teams[1], opponent=teams[0], player=player, stat=stat
                )
            )
        return teams_opponents_players_stats

    async def _generate_rounds(
        self, teams: list[TeamSchema]
    ) -> list[RoundSchema]:
        ct_id, t_id = [t.id for t in teams]
        ct_win_round_counter, t_win_round_counter = 0, 0
        round_number = 1
        rounds: list[RoundSchema] = []
        while round_number <= 15:
            current_round_h1: RoundSchema = (
                await self.round_repository.generate(
                    ct_id=ct_id, t_id=t_id, round=round_number
                )
            )
            rounds.append(current_round_h1)
            round_number += 1
            if current_round_h1.winner_id == current_round_h1.ct_id:
                ct_win_round_counter += 1
            else:
                t_win_round_counter += 1
        ct_id, t_id = t_id, ct_id
        ct_win_round_counter, t_win_round_counter = (
            t_win_round_counter,
            ct_win_round_counter,
        )
        while True:
            current_round_h2: RoundSchema = (
                await self.round_repository.generate(
                    ct_id=ct_id, t_id=t_id, round=round_number
                )
            )
            rounds.append(current_round_h2)
            round_number += 1
            if current_round_h2.winner_id == current_round_h2.ct_id:
                ct_win_round_counter += 1
                if ct_win_round_counter == 16:
                    break
            else:
                t_win_round_counter += 1
                if t_win_round_counter == 16:
                    break
        return rounds
