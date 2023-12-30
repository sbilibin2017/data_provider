from pydantic import BaseModel


class StatSchema(BaseModel):
    kills: int
    deaths: int
    assists: int
    flash_assists: int
    headshots: int
    first_kills_diff: int
    k_d_diff: int
    adr: int
    kast: int
    rating: int

    class Config:
        frozen = True
