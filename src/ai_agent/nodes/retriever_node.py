from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.retrievers import BaseRetriever

from src.ai_agent.state import State
from src.ai_agent.utils import format_docs
from src.ai_agent.nodes.base_node import BaseNode


class RetrieverNode(BaseNode):
    def __init__(self, retriever: "BaseRetriever") -> None:
        self._retriever = retriever

    async def execute(self, state: State) -> dict:
        print("---RETRIEVE---")
        user_question = state["user_question"]
        documents = await self._retriever.ainvoke(user_question)
        context = format_docs(documents)
        return {"user_question": user_question, "context": context}
