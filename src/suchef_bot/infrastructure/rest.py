import logging

from typing import Optional, List

import aiohttp

from ..core.interfaces import UNFGateway
from ..core.entities import Order, Bonus


logger = logging.getLogger(__name__)


class UNFApiGateway(UNFGateway):
    def __init__(self, url: str) -> None:
        self.url = url

    async def get_orders(self, phone_number: str) -> Optional[List[Optional[Order]]]:
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        json = {"command": "status", "telefon": phone_number}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url=self.url,
                    headers=headers,
                    json=json
                ) as response:
                    data = await response.json()
            return [Order.model_validate(order) for order in data["data"]["orders"]]
        except aiohttp.ClientError as e:
            logger.error("Error while receiving orders: %s", e)

    async def get_bonus(self, phone_number: str) -> Optional[Bonus]:
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        json = {"command": "bonus", "telefon": phone_number, "project": "Сушеф.рф"}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url=self.url,
                    headers=headers,
                    json=json
                ) as response:
                    data = await response.json()
            return Bonus.model_validate(data["data"])
        except aiohttp.ClientError as e:
            logger.error("Error while receiving bonus: %s", e)
