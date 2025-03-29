from src.core.entities import User
from src.repository import UserRepository


class UsersUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def register(self, user: User) -> int:
        return await self._user_repository.save(user)

    async def verify(self, user_id: int) -> bool:
        user = await self._user_repository.get_by_user_id(user_id)
        return True if user else False
