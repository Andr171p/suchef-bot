from dishka import Provider, provide, Scope

from aiogram import Bot

from src.apis import OrdersAPI
from src.gateways import OrdersGateway
from src.repository import UserRepository
from src.database.crud import UserCRUD
from src.database import DatabaseManager
from src.services.sender import TelegramSenderService
from src.core.use_cases import OrdersUseCase, OrdersNotificationsUseCase
from src.config import settings


class OrdersProvider(Provider):
    @provide(scope=Scope.APP)
    def get_user_crud(self, manager: DatabaseManager) -> UserCRUD:
        return UserCRUD(manager)

    @provide(scope=Scope.APP)
    def get_user_repository(self, crud: UserCRUD) -> UserRepository:
        return UserRepository(crud)

    @provide(scope=Scope.APP)
    def get_orders_api(self) -> OrdersAPI:
        return OrdersAPI(settings.api.url)

    @provide(scope=Scope.APP)
    def get_sender_service(self, bot: Bot) -> TelegramSenderService:
        return TelegramSenderService(bot)

    @provide(scope=Scope.APP)
    def get_orders_gateway(self, sender_service: TelegramSenderService) -> OrdersGateway:
        return OrdersGateway(sender_service)

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
            orders_gateway: OrdersGateway,
            user_repository: UserRepository
    ) -> OrdersNotificationsUseCase:
        return OrdersNotificationsUseCase(orders_gateway, user_repository)
