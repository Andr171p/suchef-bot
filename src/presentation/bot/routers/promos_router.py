from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.core.use_cases import PromosUseCase
from src.presentation.bot.presenters import PromosPresenter


promos_router = Router()


@promos_router.message(Command("promos"))
async def get_promos(message: Message, promos_use_case: FromDishka[PromosUseCase]) -> None:
    promos = await promos_use_case.get_promos()
    await PromosPresenter.present(message, promos)
