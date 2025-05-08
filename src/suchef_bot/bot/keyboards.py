from typing import List

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)

from ..constants import URL, PROMO_URL


def start_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text="Регистрация", request_contact=True)]]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите для мгновенной регистрации"
    )


def payment_keyboard(url: str) -> InlineKeyboardMarkup:
    keyboard: List[List[InlineKeyboardButton]] = []
    if url:
        keyboard.append(
            [InlineKeyboardButton(text="Оплатить", url=url)]
        )
    else:
        keyboard.append(
            [InlineKeyboardButton(text="Не оплачен", callback_data="not payment")]
        )
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def confirmed_payment_keyboard(url: str) -> InlineKeyboardMarkup:
    keyboard: List[List[InlineKeyboardButton]] = []
    if url:
        keyboard.append(
            [InlineKeyboardButton(text="ОПЛАЧЕН", url=url)]
        )
    else:
        keyboard.append(
            [InlineKeyboardButton(text="ОПЛАЧЕН", callback_data="confirmed")]
        )
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def bonus_keyboard() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text="Перейти на сайт", url=URL)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def promo_keyboard(text: str) -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text=text, url=PROMO_URL)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
