from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.suchef_bot.core.use_cases import CustomerService
from ..messages import OrderMessage, BonusMessage, PromoMessage


customer_router = Router()


@customer_router.message(Command("orders"))
async def get_orders(message: Message, customer_service: FromDishka[CustomerService]) -> None:
    orders = await customer_service.get_orders(message.from_user.id)
    if not orders:
        await message.answer(...)  # TODO
        return
    for order in orders:
        order_message = OrderMessage(order)
        await message.answer_photo(
            photo=order_message.image,
            caption=order_message.text,
            reply_markup=order_message.keyboard
        )


@customer_router.message(Command("flyers"))
async def get_bonus(message: Message, customer_service: FromDishka[CustomerService]) -> None:
    bonus = await customer_service.get_bonus(message.from_user.id)
    if not bonus:
        await message.answer(...)  # TODO
        return
    bonus_message = BonusMessage(bonus)
    await message.answer_photo(
        photo=bonus_message.image,
        caption=bonus_message.text,
        reply_markup=bonus_message.keyboard
    )


@customer_router.message(Command("promos"))
async def get_promos(message: Message, customer_service: FromDishka[CustomerService]) -> None:
    promos = await customer_service.get_promos()
    if not promos:
        await message.answer(...)  # TODO
        return
    for promo in promos:
        promo_message = PromoMessage(promo)
        await message.answer_photo(
            photo=promo_message.image,
            reply_markup=promo_message.keyboard
        )
