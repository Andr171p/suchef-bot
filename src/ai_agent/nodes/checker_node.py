import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.prompts import BasePromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.output_parsers import BaseTransformOutputParser

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.states import GraphState


class CheckerNode(BaseNode):
    def __init__(
            self,
            prompt: "BasePromptTemplate",
            model: "BaseChatModel",
            parser: "BaseTransformOutputParser"
    ) -> None:
        self._chain = prompt | model | parser

    @staticmethod
    def _get_generation_mark_from_response(response: str) -> bool:
        numbers = re.findall(r'\d+', response)
        mark = int(numbers[0])
        return True if mark >= 5 else False

    def execute(self, state: GraphState) -> dict:
        print("---CHECK GENERATION QUALITY---")
        question = state["question"]
        generation = state["generation"]
        context = state["context"]
        response = self._chain.invoke({"question": question, "generation": generation})
        is_ok = self._get_generation_mark_from_response(response)
        return {
            "question": question,
            "generation": generation,
            "context": context,
            "is_ok": is_ok
        }
