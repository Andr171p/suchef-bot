from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.suchef_bot.core.use_cases import BonusUseCase
from src.presentation.bot.presenters import BonusPresenter


bonus_router = Router()


@bonus_router.message(Command("flyers"))
async def get_bonus(message: Message, bonus_use_case: FromDishka[BonusUseCase]) -> None:
    user_id = message.from_user.id
    bonus = await bonus_use_case.get_bonus(user_id)
    await BonusPresenter.present(message, bonus)
