from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


def pay_kb(url: str) -> InlineKeyboardMarkup:
    keyboard_list = []
    if url:
        keyboard_list.append(
            [InlineKeyboardButton(text="Оплатить", url=url)]
        )
    else:
        keyboard_list.append(
            [InlineKeyboardButton(text="Не оплачен", callback_data="not payment")]
        )
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard


def confirmed_kb(url: str) -> InlineKeyboardMarkup:
    keyboard_list: List[List[InlineKeyboardButton]] = []
    if url:
        keyboard_list.append(
            [InlineKeyboardButton(text="ОПЛАЧЕН", url=url)]
        )
    else:
        keyboard_list.append(
            [InlineKeyboardButton(text="ОПЛАЧЕН", callback_data="confirmed")]
        )
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
