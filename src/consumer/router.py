from faststream.rabbit import (
    RabbitRouter,
    RabbitQueue,
    RabbitExchange,
    ExchangeType
)
from dishka.integrations.faststream import FromDishka

from src.core.entities import Order
from src.core.use_cases import OrdersNotificationsUseCase


orders_router = RabbitRouter()


@orders_router.subscriber(
    queue=RabbitQueue("suchef-orders", exclusive=True),
    exchange=RabbitExchange(name="orders", type=ExchangeType.FANOUT, durable=True),
    filter=lambda message: message.get("project") != "Дисконт Суши"
)
async def handle_orders(
        order: Order,
        orders_notifications_use_case: FromDishka[OrdersNotificationsUseCase]
) -> None:
    await orders_notifications_use_case.notify(order)
