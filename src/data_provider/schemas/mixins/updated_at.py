import random
from datetime import datetime

from pydantic import BaseModel, Field


def generate_updated_at() -> datetime:
    return datetime(
        year=random.randint(2012, 2025),
        month=random.randint(1, 12),
        day=random.randint(1, 28),
        hour=random.randint(0, 23),
    )


class UpdatedAtMixin(BaseModel):
    updated_at: datetime = Field(default_factory=generate_updated_at)
