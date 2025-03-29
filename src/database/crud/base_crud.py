from typing import TYPE_CHECKING, Sequence, Union

if TYPE_CHECKING:
    from src.database.database_manager import DatabaseManager
    from src.database.models import BaseModel

from abc import ABC, abstractmethod


class BaseCRUD(ABC):
    _manager: "DatabaseManager"

    @abstractmethod
    async def create(self, model: "BaseModel") -> int:
        raise NotImplemented

    @abstractmethod
    async def read_by_user_id(self, user_id: int) -> Union["BaseModel", Sequence["BaseModel"]]:
        raise NotImplemented

    @abstractmethod
    async def read_all(self) -> Sequence["BaseModel"]:
        raise NotImplemented
