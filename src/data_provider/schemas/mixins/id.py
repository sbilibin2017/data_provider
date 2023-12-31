from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class IdMixin(BaseModel):
    id: UUID = Field(default_factory=uuid4)
