from typing import List, Optional

from aiogram.types import Message

from src.core.entities import Order
from src.presentation.bot.messages import OrderMessage, NoOrdersMessage


class OrdersPresenter:
    @staticmethod
    async def present(message: Message, orders: List[Optional[Order]]) -> None:
        if len(orders) == 0:
            no_orders_message = NoOrdersMessage()
            await message.answer(no_orders_message.text)
        else:
            for order in orders:
                order_message = OrderMessage(order)
                await message.answer_photo(
                    photo=order_message.photo,
                    caption=order_message.text,
                    reply_markup=order_message.keyboard
                )
