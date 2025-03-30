from dishka import make_async_container

from src.di.providers import (
    BotProvider,
    BonusProvider,
    BrokerProvider,
    PromosProvider,
    OrdersProvider,
    DatabaseProvider
)


container = make_async_container(
    BotProvider(),
    BonusProvider(),
    BrokerProvider(),
    PromosProvider(),
    OrdersProvider(),
    DatabaseProvider()
)
