from pydantic_settings import SettingsConfigDict

from src.data_provider.core.settings.mixins import BaseSettingsMixin


class PlayerSettings(BaseSettingsMixin):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="player_",
        frozen=True,
    )
