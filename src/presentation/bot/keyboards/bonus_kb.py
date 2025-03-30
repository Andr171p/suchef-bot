from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


def bonus_kb() -> InlineKeyboardMarkup:
    keyboard_list = [
        [InlineKeyboardButton(text="Перейти на сайт", url="https://imp72.ru")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
