from dishka import Provider, provide, Scope

from aiogram import Bot

from src.apis import OrdersAPI
from src.gateways import OrdersSenderGateway
from src.repository import UserRepository
from src.services.sender import TelegramSenderService
from src.core.use_cases import OrdersUseCase, OrdersNotificationsUseCase
from src.config import settings


class OrdersProvider(Provider):
    @provide(scope=Scope.APP)
    def get_orders_api(self) -> OrdersAPI:
        return OrdersAPI(settings.api.url)

    @provide(scope=Scope.APP)
    def get_sender_service(self, bot: Bot) -> TelegramSenderService:
        return TelegramSenderService(bot)

    @provide(scope=Scope.APP)
    def get_orders_sender_gateway(self, sender_service: TelegramSenderService) -> OrdersSenderGateway:
        return OrdersSenderGateway(sender_service)

    @provide(scope=Scope.APP)
    def get_orders_use_case(
            self,
            orders_api: OrdersAPI,
            user_repository: UserRepository
    ) -> OrdersUseCase:
        return OrdersUseCase(orders_api, user_repository)

    @provide(scope=Scope.APP)
    def get_orders_notifications_use_case(
            self,
            orders_sender_gateway: OrdersSenderGateway,
            user_repository: UserRepository
    ) -> OrdersNotificationsUseCase:
        return OrdersNotificationsUseCase(orders_sender_gateway, user_repository)
