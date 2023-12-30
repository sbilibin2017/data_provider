from src.data_provider.schemas.mixins import IdMixin, NameMixin, UpdatedAtMixin


class TeamSchema(IdMixin, NameMixin, UpdatedAtMixin):
    location: str | None = None
