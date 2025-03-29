from src.core.entities import Bonus
from src.apis import BonusAPI
from src.repository import UserRepository


class BonusUseCase:
    def __init__(self, bonus_api: BonusAPI, user_repository: UserRepository) -> None:
        self._bonus_api = bonus_api
        self._user_repository = user_repository

    async def get(self, user_id: int) -> Bonus:
        phone_number = await self._user_repository.get_phone_number_by_user_id(user_id)
        bonus = await self._bonus_api.get_by_phone_number(phone_number)
        return bonus
