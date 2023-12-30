from src.data_provider.schemas.mixins import IdMixin, NameMixin, UpdatedAtMixin


class MapSchema(IdMixin, NameMixin, UpdatedAtMixin):
    pass
