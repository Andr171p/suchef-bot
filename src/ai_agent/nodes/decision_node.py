from typing import Literal

from langchain_core.runnables import Runnable
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.language_models import BaseChatModel

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.state import State

from src.misc.file_readers import read_txt
from src.config import BASE_DIR


TEMPLATE_PATH = BASE_DIR / "prompts" / ...


NEXT_STEPS = Literal[
    "retrieve",
    "order_status"
]


class DecisionNode(BaseNode):
    def __init__(self, model: BaseChatModel) -> None:
        self._model = model

    def _create_chain(self) -> Runnable:
        prompt = ChatPromptTemplate.from_template(read_txt(TEMPLATE_PATH))
        return prompt | self._model | StrOutputParser()

    @staticmethod
    def _get_action_from_response(response: str) -> NEXT_STEPS:
        return "retrieve" if "retrieve" in response else "order_status"

    async def execute(self, state: State) -> dict:
        print("---DECISION MAKING---")
        chain = self._create_chain()
        user_question = state["user_question"]
        response = await chain.ainvoke({"user_question": user_question})
        action = self._get_action_from_response(response)
        return {"user_question": user_question, "action": action}
