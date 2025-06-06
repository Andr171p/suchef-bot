from typing import List

from pydantic import BaseModel, field_validator, Field

from src.suchef_bot.constants import URL, ORDER_STATUS, MIN_BONUS
from src.suchef_bot.utils import (
    format_phone_number,
    format_order_number,
    format_address,
    format_date,
    format_time
)


class Order(BaseModel):
    client: str
    number: str
    date: str
    status: ORDER_STATUS
    amount: float
    pay_link: str
    pay_status: str
    cooking_time_from: str
    cooking_time_to: str
    delivery_time_from: str
    delivery_time_to: str
    project: str
    trade_point: str
    trade_point_card: str
    delivery_method: str
    delivery_adress: str
    phones: List[str]

    @field_validator("number")
    def format_order_number(cls, number: str) -> str:
        return format_order_number(number)

    @field_validator("date")
    def format_date(cls, date: str) -> str:
        return format_date(date)

    @field_validator(
        "cooking_time_from",
        "cooking_time_to",
        "delivery_time_from",
        "delivery_time_to"
    )
    def format_time(cls, time: str) -> str:
        return format_time(time)

    @field_validator("phones")
    def format_phones(cls, phones: List[str]) -> List[str]:
        return [format_phone_number(phone) for phone in phones]

    @field_validator("delivery_adress")
    def format_adress(cls, adress: str) -> str:
        return format_address(adress)


class Bonus(BaseModel):
    flyers: int = Field(ge=MIN_BONUS)
    chips: int = Field(ge=MIN_BONUS)


class Promo(BaseModel):
    url: str
    title: str

    @field_validator("url")
    def format_url(cls, url: str) -> str:
        return f"{URL}{url}"
