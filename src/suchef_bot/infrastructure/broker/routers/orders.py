import logging

from faststream.rabbit import RabbitRouter, RabbitExchange, ExchangeType
from dishka.integrations.base import FromDishka

from aiogram import Bot

from src.suchef_bot.core.entities import Order
from src.suchef_bot.bot.messages import OrderMessage
from src.suchef_bot.core.interfaces import UserRepository


logger = logging.getLogger(__name__)

orders_router = RabbitRouter()

exchange = RabbitExchange("orders", auto_delete=True, type=ExchangeType.FANOUT)


@orders_router.subscriber("suchef-orders")
async def send_orders(
        order: Order,
        user_repository: FromDishka[UserRepository],
        bot: FromDishka[Bot]
) -> None:
    for phone_number in order.phones:
        telegram_id = await user_repository.get_telegram_id_by_phone_number(phone_number)
        order_message = OrderMessage(order)
        await bot.send_photo(
            chat_id=telegram_id,
            photo=order_message.image,
            caption=order_message.text,
            reply_markup=order_message.keyboard
        )
        logger.info(
            "Order message delivered successfully to user with telegram_id: %s",
            telegram_id
        )
