from typing import Literal, List
from typing_extensions import TypedDict

from src.core.entities import Order


class State(TypedDict):
    user_id: int
    user_question: str
    answer: str
    context: str
    orders: List[Order]
    action: Literal["retrieve", "order_status"]
