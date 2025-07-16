from collections.abc import AsyncIterable

from dishka import Provider, provide, Scope, from_context, make_async_container

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from elasticsearch import Elasticsearch

from redis.asyncio import Redis as AsyncRedis

from faststream.rabbit import RabbitBroker

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from langchain_gigachat import GigaChat

from langchain.retrievers import EnsembleRetriever
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_elasticsearch import ElasticsearchStore
from langchain_community.retrievers import ElasticSearchBM25Retriever

from langchain_core.embeddings import Embeddings
from langchain_core.retrievers import BaseRetriever
from langchain_core.language_models import BaseChatModel
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever

from langgraph.checkpoint.base import BaseCheckpointSaver

from .core.use_cases import Registration, ChatAssistant, CustomerService
from .core.interfaces import (
    AiAgent,
    UserRepository,
    MessageRepository,
    UNFGateway,
    PromoGateway
)

from .ai_agent.agents import RAGAgent
from .ai_agent.nodes import RetrieverNode, GenerationNode

from .infrastructure.rest import UNFApiGateway
from .infrastructure.crawlers import PromoCrawlerGateway
from .infrastructure.database.session import create_session_maker
from .infrastructure.database.repositories import SQLUserRepository, SQLMessageRepository
from .infrastructure.checkpoints.redis import AsyncRedisCheckpointSaver

from .settings import Settings
from .constants import (
    PROMO_URL,
    SIMILARITY_WEIGHT,
    BM25_WEIGHT
)


class AppProvider(Provider):
    app_settings = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_bot(self, app_settings: Settings) -> Bot:
        return Bot(
            token=app_settings.bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

    @provide(scope=Scope.APP)
    def get_rabbit_broker(self, app_settings: Settings) -> RabbitBroker:
        return RabbitBroker(url=app_settings.rabbit.url)

    @provide(scope=Scope.APP)
    def get_session_maker(self, app_settings: Settings) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(app_settings.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self,
            session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    @provide(scope=Scope.APP)
    def get_embeddings(self, app_settings: Settings) -> Embeddings:
        return HuggingFaceEmbeddings(
            model_name=app_settings.embeddings.model_name,
            model_kwargs=app_settings.embeddings.model_kwargs,
            encode_kwargs=app_settings.embeddings.encode_kwargs
        )

    @provide(scope=Scope.APP)
    def get_elasticsearch(self, app_settings: Settings) -> Elasticsearch:
        return Elasticsearch(
            hosts=app_settings.elasticsearch.url,
            basic_auth=app_settings.elasticsearch.auth
        )

    @provide(scope=Scope.APP)
    def get_redis(self, app_settings: Settings) -> AsyncRedis:
        return AsyncRedis.from_url(app_settings.redis.redis_url)

    @provide(scope=Scope.APP)
    def get_vector_store(self, app_settings: Settings, embeddings: Embeddings) -> VectorStore:
        return ElasticsearchStore(
            es_url=app_settings.elasticsearch.url,
            es_user=app_settings.elasticsearch.username,
            es_password=app_settings.elasticsearch.password,
            index_name="suchef-vectors",
            embedding=embeddings
        )

    @provide(scope=Scope.APP)
    def get_vector_store_retriever(self, vector_store: VectorStore) -> VectorStoreRetriever:
        return vector_store.as_retriever()

    @provide(scope=Scope.APP)
    def get_bm25_retriever(self, elasticsearch: Elasticsearch) -> ElasticSearchBM25Retriever:
        return ElasticSearchBM25Retriever(
            client=elasticsearch,
            index_name="suchef-docs",
        )

    @provide(scope=Scope.APP)
    def get_retriever(
            self,
            vector_store_retriever: VectorStoreRetriever,
            bm25_retriever: ElasticSearchBM25Retriever
    ) -> BaseRetriever:
        return EnsembleRetriever(
            retrievers=[vector_store_retriever, bm25_retriever],
            weights=[SIMILARITY_WEIGHT, BM25_WEIGHT]
        )

    @provide(scope=Scope.APP)
    def get_model(self, app_settings: Settings) -> BaseChatModel:
        return GigaChat(
            credentials=app_settings.giga_chat.api_key,
            scope=app_settings.giga_chat.scope,
            verify_ssl_certs=False,
            profanity_check=False,
        )

    @provide(scope=Scope.APP)
    def get_checkpoint_saver(self, redis: AsyncRedis) -> BaseCheckpointSaver:
        return AsyncRedisCheckpointSaver(redis)

    @provide(scope=Scope.APP)
    def get_retriever_node(self, retriever: BaseRetriever) -> RetrieverNode:
        return RetrieverNode(retriever)

    @provide(scope=Scope.APP)
    def get_generation_node(self, model: BaseChatModel) -> GenerationNode:
        return GenerationNode(model)

    @provide(scope=Scope.APP)
    def get_ai_agent(
            self,
            retriever_node: RetrieverNode,
            generation_node: GenerationNode,
            checkpoint_saver: BaseCheckpointSaver
    ) -> AiAgent:
        return RAGAgent(
            retriever_node=retriever_node,
            generation_node=generation_node,
            checkpoint_saver=checkpoint_saver
        )

    @provide(scope=Scope.APP)
    def get_chat_assistant(self, ai_agent: AiAgent) -> ChatAssistant:
        return ChatAssistant(ai_agent)

    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return SQLUserRepository(session)

    @provide(scope=Scope.REQUEST)
    def get_message_repository(self, session: AsyncSession) -> MessageRepository:
        return SQLMessageRepository(session)

    @provide(scope=Scope.APP)
    def get_promo_gateway(self) -> PromoGateway:
        return PromoCrawlerGateway(PROMO_URL)

    @provide(scope=Scope.APP)
    def get_unf_gateway(self, app_settings: Settings) -> UNFGateway:
        return UNFApiGateway(app_settings.api.url)

    @provide(scope=Scope.REQUEST)
    def get_registration(self, user_repository: UserRepository) -> Registration:
        return Registration(user_repository)

    @provide(scope=Scope.REQUEST)
    def get_customer_service(
            self,
            unf_gateway: UNFGateway,
            promo_gateway: PromoGateway,
            user_repository: UserRepository
    ) -> CustomerService:
        return CustomerService(
            unf_gateway=unf_gateway,
            promo_gateway=promo_gateway,
            user_repository=user_repository
        )


settings = Settings()

container = make_async_container(AppProvider(), context={Settings: settings})
