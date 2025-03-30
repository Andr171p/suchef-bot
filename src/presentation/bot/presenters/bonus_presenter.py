from aiogram.types import Message

from src.core.entities import Bonus
from src.presentation.bot.messages import BonusMessage


class BonusPresenter:
    @staticmethod
    async def present(message: Message, bonus: Bonus) -> None:
        bonus_message = BonusMessage(bonus)
        await message.answer_photo(
            photo=bonus_message.photo,
            caption=bonus_message.text,
            reply_markup=bonus_message.keyboard
        )
