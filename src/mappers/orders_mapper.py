from typing import List, Union

from src.core.entities import Order


class OrdersMapper:
    @staticmethod
    def from_response(response: dict) -> List[Union[Order, None]]:
        return [Order(**order) for order in response["data"]["orders"]]
