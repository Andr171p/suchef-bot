from typing import TYPE_CHECKING, Sequence, Union

if TYPE_CHECKING:
    from src.database.database_manager import DatabaseManager

from sqlalchemy import select

from src.database.crud.base_crud import BaseCRUD
from src.database.models import UserModel


class UserCRUD(BaseCRUD):
    def __init__(self, manager: "DatabaseManager") -> None:
        self._manager = manager

    async def create(self, user: UserModel) -> int:
        async with self._manager.session() as session:
            session.add(user)
            id = user.id
            await session.commit()
            await session.refresh(user)
        return id

    async def read_by_user_id(self, user_id: int) -> Union[UserModel, None]:
        async with self._manager.session() as session:
            stmt = (
                select(UserModel)
                .where(UserModel.user_id == user_id)
            )
            user = await session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_by_phone_number(self, phone_number: str) -> Union[UserModel, None]:
        async with self._manager.session() as session:
            stmt = (
                select(UserModel)
                .where(UserModel.phone_number == phone_number)
            )
            user = await session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_phone_number_by_user_id(self, user_id: int) -> str:
        async with self._manager.session() as session:
            stmt = (
                select(UserModel.phone_number)
                .where(UserModel.user_id == user_id)
            )
            phone_number = await session.execute(stmt)
        return phone_number.scalar_one_or_none()
    
    async def read_user_id_by_phone_number(self, phone_number: str) -> Union[int, None]:
        async with self._manager.session() as session:
            stmt = (
                select(UserModel.user_id)
                .where(UserModel.phone_number == phone_number)
            )
            user_id = await session.execute(stmt)
        return user_id.scalar_one_or_none()

    async def read_all(self) -> Union[Sequence[UserModel], None]:
        async with self._manager.session() as session:
            stmt = select(UserModel)
            users = await session.execute(stmt)
        return users.scalars().all()

    async def update(self, user: UserModel) -> UserModel:
        async with self._manager.session() as session:
            await session.merge(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def delete(self, user_id: int) -> Union[UserModel, None]:
        async with self._manager.session() as session:
            stmt = (
                select(UserModel)
                .where(UserModel.user_id == user_id)
            )
            user = await session.execute(stmt)
            if user:
                await session.delete(user)
                await session.commit()
        return user.scalar_one_or_none()
