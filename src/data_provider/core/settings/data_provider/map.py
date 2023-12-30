from pydantic_settings import SettingsConfigDict

from src.data_provider.core.settings.mixins import BaseSettingsMixin


class MapSettings(BaseSettingsMixin):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="map_",
        frozen=True,
    )
