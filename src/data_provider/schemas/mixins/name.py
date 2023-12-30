from pydantic import BaseModel


class NameMixin(BaseModel):
    name: str
