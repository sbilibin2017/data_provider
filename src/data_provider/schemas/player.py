from src.data_provider.schemas.mixins import IdMixin, NameMixin, UpdatedAtMixin


class PlayerSchema(IdMixin, NameMixin, UpdatedAtMixin):
    nationality: str
    hometown: str
    birthday: str
