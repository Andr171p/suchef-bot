from dishka import make_async_container

from src.di.providers import (
    DatabaseProvider,
    OrdersProvider,
    BrokerProvider,
    BotProvider
)


container = make_async_container(
    DatabaseProvider(),
    OrdersProvider(),
    BrokerProvider(),
    BotProvider()
)
