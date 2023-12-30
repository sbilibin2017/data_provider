from pydantic_settings import BaseSettings

from src.data_provider.core.settings.app import AppSettings
from src.data_provider.core.settings.data_provider import DataProviderSettings
from src.data_provider.utils import singleton


@singleton
class Settings(BaseSettings):
    data_provider: DataProviderSettings = (
        DataProviderSettings()
    )  # pyright: ignore
    app: AppSettings = AppSettings()  # pyright: ignore


def get_settings() -> Settings:
    return Settings()


__all__ = [
    "Settings",
]
