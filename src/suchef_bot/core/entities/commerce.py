from typing import List
from datetime import datetime

from pydantic import BaseModel, field_validator, PositiveInt

from src.suchef_bot.constants import URL, ORDER_STATUS
from src.suchef_bot.utils import (
    format_phone_number,
    format_order_number,
    format_address
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
    def convert_date(cls, date: str) -> datetime:
        return datetime.fromisoformat(date)

    @field_validator(
        "cooking_time_from",
        "cooking_time_to",
        "delivery_time_from",
        "delivery_time_to"
    )
    def convert_time(cls, time: str) -> datetime:
        return datetime.fromisoformat(time)

    @field_validator("phones")
    def validate_phones(cls, phones: List[str]) -> List[str]:
        return [format_phone_number(phone) for phone in phones]

    @field_validator("delivery_adress")
    def format_adress(cls, adress: str) -> str:
        return format_address(adress)


class Bonus(BaseModel):
    flyers: PositiveInt
    chips: PositiveInt


class Promo(BaseModel):
    url: str
    title: str

    @field_validator("url")
    def format_url(cls, url: str) -> str:
        return f"{URL}{url}"
