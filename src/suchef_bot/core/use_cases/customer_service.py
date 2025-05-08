from typing import List, Optional

from ..entities import Order, Bonus, Promo
from ..interfaces import UNFGateway, PromoGateway, UserRepository


class CustomerService:
    def __init__(
            self,
            unf_gateway: UNFGateway,
            promo_gateway: PromoGateway,
            user_repository: UserRepository
    ) -> None:
        self._unf_gateway = unf_gateway
        self._promo_gateway = promo_gateway
        self._user_repository = user_repository

    async def get_orders(self, telegram_id: int) -> List[Optional[Order]]:
        phone_number = await self._user_repository.get_phone_number_by_telegram_id(telegram_id)
        orders = await self._unf_gateway.get_orders(phone_number)
        return orders

    async def get_bonus(self, telegram_id: int) -> Optional[Bonus]:
        phone_number = await self._user_repository.get_phone_number_by_telegram_id(telegram_id)
        bonus = await self._unf_gateway.get_bonus(phone_number)
        return bonus

    async def get_promos(self) -> List[Promo]:
        return await self._promo_gateway.get_promos()
