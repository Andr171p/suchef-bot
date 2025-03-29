from typing import List, Union

from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseRepository(ABC):
    @abstractmethod
    async def save(self, model: BaseModel) -> int:
        raise NotImplemented

    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> Union[BaseModel, List[BaseModel]]:
        raise NotImplemented

    @abstractmethod
    async def get_all(self) -> List[BaseModel]:
        raise NotImplemented
