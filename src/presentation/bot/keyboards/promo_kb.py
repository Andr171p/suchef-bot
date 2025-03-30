from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


def promo_kb(text: str) -> InlineKeyboardMarkup:
    keyboard_list = [
        [InlineKeyboardButton(text=text, url="https://imp72.ru/catalog/akcii/")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
