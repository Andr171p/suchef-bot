from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.state import State

from src.core.use_cases import OrdersUseCase


class OrdersNode(BaseNode):
    def __init__(self, orders_use_case: OrdersUseCase) -> None:
        self._orders_use_case = orders_use_case

    async def execute(self, state: State) -> dict:
        print("---RECEIVING ORDER STATUS---")
        user_id = state["user_id"]
        orders = await self._orders_use_case.get(user_id)
        return {"orders": orders}
