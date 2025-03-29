from pydantic import BaseModel


class Bonus(BaseModel):
    flyers: int
    chips: int
