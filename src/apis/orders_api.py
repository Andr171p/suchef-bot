from typing import List, Union

from src.http import HTTPClient
from src.http.responses import JsonResponse
from src.suchef_bot.core import Order
from src.mappers import OrdersMapper


class OrdersAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def get_by_phone_number(self, phone_number: str) -> List[Union[Order, None]]:
        async with HTTPClient(JsonResponse()) as http_client:
            response = await http_client.post(
                url=self._base_url,
                json={
                    "command": "status",
                    "telefon": phone_number
                },
                headers={"Content-Type": "application/json; charset=UTF-8"}
            )
        return OrdersMapper.from_response(response)
