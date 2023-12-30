from uuid import UUID

from src.data_provider.schemas.mixins import IdMixin, NameMixin, UpdatedAtMixin


class TournamentSchema(IdMixin, NameMixin, UpdatedAtMixin):
    serie_id: UUID | None = None
    prizepool: str
