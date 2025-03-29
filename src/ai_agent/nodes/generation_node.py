from langchain_core.runnables import Runnable
from langchain.prompts import ChatPromptTemplate
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser

from src.ai_agent.state import State
from src.ai_agent.nodes.base_node import BaseNode

from src.config import BASE_DIR
from src.misc.file_readers import read_txt


TEMPLATE_PATH = BASE_DIR / "prompts" / "generation_prompt"


class GenerationNode(BaseNode):
    def __init__(self, model: BaseChatModel) -> None:
        self._model = model

    def _create_chain(self) -> Runnable:
        prompt = ChatPromptTemplate.from_template(read_txt(TEMPLATE_PATH))
        return prompt | self._model | StrOutputParser()

    async def execute(self, state: State) -> dict:
        print("---GENERATE---")
        chain = self._create_chain()
        user_question = state["user_question"]
        context = state["context"]
        answer = await chain.ainvoke({
            "context": context,
            "user_question": user_question
        })
        return {"answer": answer}
