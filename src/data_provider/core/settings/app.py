from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="app_",
        frozen=True,
    )

    host: str = Field(alias="host")  # pyright: ignore
    port: int = Field(alias="port")  # pyright: ignore
    n_threads: int = Field(alias="n_threads")  # pyright: ignore
    debug: int = Field(alias="debug")  # pyright: ignore
