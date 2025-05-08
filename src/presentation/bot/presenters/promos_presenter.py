from typing import List

from aiogram.types import Message

from src.suchef_bot.core import Promo
from src.presentation.bot.keyboards import promo_kb


class PromosPresenter:
    @staticmethod
    async def present(message: Message, promos: List[Promo]) -> None:
        for promo in promos:
            await message.answer_photo(
                photo=promo.url,
                reply_markup=promo_kb(promo.title)
            )
