import logging

from abc import ABC, abstractmethod

from langchain_core.retrievers import BaseRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser

from .states import AgentState
from .utils import format_documents
from .templates import GENERATION_TEMPLATE


logger = logging.getLogger(__name__)


class BaseNode(ABC):
    @abstractmethod
    async def execute(self, state: AgentState) -> dict: pass

    async def __call__(self, state: AgentState) -> dict: pass


class RetrieverNode(BaseNode):
    def __init__(self, retriever: BaseRetriever) -> None:
        self.retriever = retriever

    async def execute(self, state: AgentState) -> dict:
        logger.info("---RETRIEVE---")
        messages = state["messages"]
        last_message = messages[-1]
        query = last_message.content
        documents = await self.retriever.ainvoke(query)
        return {"context": format_documents(documents)}


class GenerationNode(BaseNode):
    def __init__(self, model: BaseChatModel) -> None:
        self._llm_chain = (
            ChatPromptTemplate.from_template(GENERATION_TEMPLATE)
            | model
            | StrOutputParser()
        )

    async def execute(self, state: AgentState) -> dict:
        logger.info("---GENERATE---")
        messages = state["messages"]
        last_message = messages[-1]
        question = last_message.content
        context = state["context"]
        message = await self._llm_chain.ainvoke({"question": question, "context": context})
        return {"messages": [message]}
