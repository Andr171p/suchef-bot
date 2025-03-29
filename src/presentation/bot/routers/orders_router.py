from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.core.use_cases import OrdersUseCase
from src.presentation.bot.presenters import OrdersPresenter


orders_router = Router()


@orders_router.message(Command("orders"))
async def get_orders(message: Message, orders_use_case: FromDishka[OrdersUseCase]) -> None:
    user_id = message.from_user.id
    orders = await orders_use_case.get(user_id)
    await OrdersPresenter.present(message, orders)
