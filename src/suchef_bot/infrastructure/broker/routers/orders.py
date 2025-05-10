import logging

from faststream.rabbit import RabbitRouter, RabbitExchange, ExchangeType
from dishka.integrations.base import FromDishka

from aiogram import Bot

from src.suchef_bot.core.entities import Order
from src.suchef_bot.bot.messages import OrderMessage
from src.suchef_bot.core.interfaces import UserRepository
from src.suchef_bot.constants import PROJECT_NAME


logger = logging.getLogger(__name__)

orders_router = RabbitRouter()

exchange = RabbitExchange("orders", type=ExchangeType.FANOUT)


@orders_router.subscriber("suchef-orders", exchange=exchange)
async def send_orders(
        order: Order,
        user_repository: FromDishka[UserRepository],
        bot: FromDishka[Bot]
) -> None:
    if order.project == PROJECT_NAME:
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
