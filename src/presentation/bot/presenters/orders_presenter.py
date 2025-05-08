from typing import List, Optional

from aiogram.types import Message

from src.suchef_bot.core import Order
from src.presentation.bot.messages import OrderMessage


class OrdersPresenter:
    @staticmethod
    async def present(message: Message, orders: List[Optional[Order]]) -> None:
        if len(orders) == 0:
            await message.answer("У Вас нет активных заказов на текущую дату")
        else:
            for order in orders:
                order_message = OrderMessage(order)
                await message.answer_photo(
                    photo=order_message.photo,
                    caption=order_message.text,
                    reply_markup=order_message.keyboard
                )
