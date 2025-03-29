from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from aiohttp import ClientResponse

from src.http.responses.base_response import BaseResponse


class TextResponse(BaseResponse):
    async def fetch(self, response: "ClientResponse") -> Union[str, None]:
        if not self.is_ok(response):
            return
        return await response.text()
