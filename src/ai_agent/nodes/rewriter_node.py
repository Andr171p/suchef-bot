from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.prompts import BasePromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.output_parsers import BaseTransformOutputParser

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.state import State


class RewriterNode(BaseNode):
    def __init__(
            self,
            prompt: "BasePromptTemplate",
            model: "BaseChatModel",
            parser: "BaseTransformOutputParser",
    ) -> None:
        self._chain = prompt | model | parser

    def execute(self, state: State) -> dict:
        print("---REWRITE QUESTION---")
        question = state["question"]
        rewritten_question = self._chain.invoke({"question": question})
        return {"question": rewritten_question}
