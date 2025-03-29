from abc import ABC, abstractmethod


class BaseSenderService(ABC):
    @abstractmethod
    async def send(self, *args) -> bool:
        raise NotImplemented

    @abstractmethod
    async def send_with_photo(self, *args) -> bool:
        raise NotImplemented
