from typing import Union, List

from src.repository.base_repository import BaseRepository
from src.database.models import UserModel
from src.database.crud import UserCRUD
from src.suchef_bot.core import User


class UserRepository(BaseRepository):
    def __init__(self, crud: "UserCRUD") -> None:
        self._crud = crud

    async def save(self, user: User) -> int:
        id = await self._crud.create(UserModel(**user.model_dump()))
        return id

    async def get_by_user_id(self, user_id: int) -> Union[User, None]:
        user = await self._crud.read_by_user_id(user_id)
        return User.model_validate(user) if user else None

    async def get_phone_number_by_user_id(self, user_id: int) -> str:
        return await self._crud.read_phone_number_by_user_id(user_id)
    
    async def get_user_id_by_phone_number(self, phone_number: str) -> int:
        return await self._crud.read_user_id_by_phone_number(phone_number)

    async def get_all(self) -> List[Union[User, None]]:
        users = await self._crud.read_all()
        return [User.model_validate(user) for user in users] if users else []
