from src.core.entities import Order
from src.gateways import OrdersSenderGateway
from src.repository import UserRepository


class OrdersNotificationsUseCase:
    def __init__(
        self, 
        orders_sender_gateway: OrdersSenderGateway,
        user_repository: UserRepository
    ) -> None:
        self._orders_sender_gateway = orders_sender_gateway
        self._user_repository = user_repository

    async def notify(self, order: Order) -> None:
        phone_numbers = order.phones
        for phone_number in phone_numbers:
            user_id = await self._user_repository.get_user_id_by_phone_number(phone_number)
            await self._orders_sender_gateway.send(user_id, order)
