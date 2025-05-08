from typing import Optional

from pydantic import BaseModel, field_validator, ConfigDict

from src.suchef_bot.utils import format_phone_number


class User(BaseModel):
    telegram_id: int
    username: Optional[str]
    phone_number: str

    model_config = ConfigDict(from_attributes=True)

    @field_validator("phone_number")
    def format_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)
