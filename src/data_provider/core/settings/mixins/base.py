from pydantic import Field
from pydantic_settings import BaseSettings


class BaseSettingsMixin(BaseSettings):
    count: int = Field(alias="count")  # pyright: ignore
    prefix: str = Field(alias="prefix")  # pyright: ignore
