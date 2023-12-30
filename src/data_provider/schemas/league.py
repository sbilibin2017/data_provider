from src.data_provider.schemas import IdMixin, NameMixin, UpdatedAtMixin


class LeagueSchema(IdMixin, NameMixin, UpdatedAtMixin):
    pass
