from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserOrm
from src.suchef_bot.core.entities import User
from src.suchef_bot.core.interfaces import UserRepository


class SQLUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user: User) -> None:
        try:
            user_orm = UserOrm(**user.model_dump())
            self.session.add(user_orm)
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while creating user: {e}")

    async def read(self, telegram_id: int) -> Optional[User]:
        try:
            stmt = (
                select(UserOrm)
                .where(UserOrm.telegram_id == telegram_id)
            )
            result = await self.session.execute(stmt)
            user_orm = result.scalar_one_or_none()
            return User.model_validate(user_orm) if user_orm else None
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading user: {e}")

    async def get_by_phone_number(self, phone_number: str) -> Optional[User]:
        try:
            stmt = (
                select(UserOrm)
                .where(UserOrm.phone_number == phone_number)
            )
            result = await self.session.execute(stmt)
            user_orm = result.scalar_one_or_none()
            return User.model_validate(user_orm) if user_orm else None
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while receiving user: {e}")

    async def get_telegram_id_by_phone_number(self, phone_number: str) -> int:
        try:
            stmt = (
                select(UserOrm.telegram_id)
                .where(UserOrm.phone_number == phone_number)
            )
            telegram_id = await self.session.execute(stmt)
            return telegram_id.scalar()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while receiving telegram_id: {e}")

    async def get_phone_number_by_telegram_id(self, telegram_id: int) -> str:
        try:
            stmt = (
                select(UserOrm.phone_number)
                .where(UserOrm.telegram_id == telegram_id)
            )
            phone_number = await self.session.execute(stmt)
            return phone_number.scalar()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while receiving phone_number: {e}")

    async def list(self) -> List[User]:
        try:
            stmt = select(UserOrm)
            results = await self.session.execute(stmt)
            users_orm = results.scalars().all()
            return [User.model_validate(user_orm) for user_orm in users_orm]
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading users: {e}")
