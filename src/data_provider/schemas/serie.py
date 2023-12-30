from enum import Enum
from uuid import UUID

from src.data_provider.schemas.mixins import IdMixin, NameMixin, UpdatedAtMixin


class SerieTierEnum(str, Enum):
    a = "a"
    b = "b"
    c = "c"
    d = "d"


class SerieSchema(IdMixin, NameMixin, UpdatedAtMixin):
    league_id: UUID | None = None
    tier: SerieTierEnum
