from ..entities import User
from ..interfaces import UserRepository


class Registration:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def register(self, user: User) -> None:
        exists_user = await self._user_repository.read(user.telegram_id)
        if not exists_user:
            await self._user_repository.create(user)

    async def login(self, telegram_id: int) -> bool:
        user = await self._user_repository.read(telegram_id)
        return True if user else False
