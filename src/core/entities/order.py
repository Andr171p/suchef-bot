from typing import List

from pydantic import BaseModel, field_validator

from src.misc import formatters


class Order(BaseModel):
    client: str
    number: str
    date: str
    status: str
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
    def validate_number(cls, number: str) -> str:
        return formatters.format_number(number)

    @field_validator("date")
    def validate_date(cls, date: str) -> str:
        return formatters.format_date(date)

    @field_validator(
        "cooking_time_from",
        "cooking_time_to",
        "delivery_time_from",
        "delivery_time_to"
    )
    def validate_time(cls, time: str) -> str:
        return formatters.format_time(time)

    @field_validator("phones")
    def validate_phones(cls, phones: List[str]) -> List[str]:
        return [formatters.format_phone(phone) for phone in phones]

    @field_validator("delivery_adress")
    def validate_adress(cls, adress: str) -> str:
        return formatters.format_address(adress)
