from collections.abc import AsyncIterable

from dishka import (
    Provider,
    provide,
    Scope,
    from_context,
    make_async_container
)

from faststream.rabbit import RabbitBroker

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from .core.use_cases import Registration, ChatAssistant, CustomerService
from .core.interfaces import AiAgent, UserRepository, UNFGateway, PromoGateway

from .infrastructure.rest import UNFApiGateway
from .infrastructure.crawlers import PromoCrawlerGateway
from .infrastructure.database.session import create_session_maker
from .infrastructure.database.repositories import SQLUserRepository

from .constants import PROMO_URL
from .settings import Settings


class AppProvider(Provider):
    config = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_rabbit_broker(self, config: Settings) -> RabbitBroker:
        return RabbitBroker(...)

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Settings) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self,
            session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return SQLUserRepository(session)

    @provide(scope=Scope.APP)
    def get_promo_gateway(self) -> PromoGateway:
        return PromoCrawlerGateway(PROMO_URL)

    @provide(scope=Scope.APP)
    def get_unf_gateway(self, config: Settings) -> UNFGateway:
        return UNFApiGateway(config.unf.UNF_URL)

    @provide(scope=Scope.REQUEST)
    def get_registration(self, user_repository: UserRepository) -> Registration:
        return Registration(user_repository)

    @provide(scope=Scope.REQUEST)
    def get_customer_service(
            self,
            unf_gateway: UNFGateway,
            promo_gateway: PromoGateway,
            user_repository: UserRepository
    ) -> CustomerService:
        return CustomerService(
            unf_gateway=unf_gateway,
            promo_gateway=promo_gateway,
            user_repository=user_repository
        )


settings = Settings()

container = make_async_container(AppProvider(), context={Settings: settings})
