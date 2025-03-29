from faststream.rabbit import RabbitBroker

from src.consumer.router import orders_router
from src.di.container import container


async def run_consumer() -> None:
    broker = await container.get(RabbitBroker)
    broker.include_router(orders_router)
    await broker.start()
