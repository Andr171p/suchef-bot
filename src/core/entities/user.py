from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: Optional[str]
    phone_number: str

    class Config:
        from_attributes = True
