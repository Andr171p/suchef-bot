from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aiohttp import ClientResponse

from abc import ABC, abstractmethod


class BaseResponse(ABC):
    @staticmethod
    def is_ok(response: "ClientResponse") -> bool:
        return 200 <= response.status < 300

    @abstractmethod
    async def fetch(self, response: "ClientResponse") -> Any:
        raise NotImplemented
