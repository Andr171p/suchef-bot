from abc import ABC, abstractmethod
from typing import Optional, List

from .entities import (
    Order,
    Bonus,
    Promo,
    User,
    BaseMessage
)


class AiAgent(ABC):
    @abstractmethod
    async def generate(self, thread_id: str, query: str) -> str: pass


class UNFGateway(ABC):
    @abstractmethod
    async def get_orders(self, phone_number: str) -> List[Optional[Order]]: pass

    @abstractmethod
    async def get_bonus(self, phone_number: str) -> Optional[Bonus]: pass


class PromoGateway(ABC):
    @abstractmethod
    async def get_promos(self) -> List[Promo]: pass


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> None: pass

    @abstractmethod
    async def read(self, telegram_id: int) -> Optional[User]: pass

    @abstractmethod
    async def get_by_phone_number(self, phone_number: str) -> Optional[User]: pass

    @abstractmethod
    async def get_telegram_id_by_phone_number(self, phone_number: str) -> int: pass

    @abstractmethod
    async def get_phone_number_by_telegram_id(self, telegram_id: int) -> str: pass

    @abstractmethod
    async def list(self) -> List[User]: pass


class MessageRepository(ABC):
    @abstractmethod
    async def bulk_create(self, messages: List[BaseMessage]) -> None: pass

    @abstractmethod
    async def read(self, chat_id: str) -> List[BaseMessage]: pass

    @abstractmethod
    async def list(self) -> List[BaseMessage]: pass
