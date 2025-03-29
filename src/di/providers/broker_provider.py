from dishka import Provider, provide, Scope

from faststream.rabbit import RabbitBroker

from src.config import settings


class BrokerProvider(Provider):
    @provide(scope=Scope.APP)
    def get_broker(self) -> RabbitBroker:
        return RabbitBroker(url=settings.rabbit.url)
