import os
from typing import Literal
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from .constants import ENV_PATH


load_dotenv(ENV_PATH)


class EmbeddingsSettings(BaseSettings):
    MODEL_NAME: str = "deepvk/USER-bge-m3"  # 1024 dimensional
    MODEL_KWARGS: dict = {"device": "cpu"}
    ENCODE_KWARGS: dict = {"normalize_embeddings": False}


class BotSettings(BaseSettings):
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")


class GigaChatSettings(BaseSettings):
    GIGACHAT_API_KEY: str = os.getenv("GIGACHAT_API_KEY")
    GIGACHAT_SCOPE: str = os.getenv("GIGACHAT_SCOPE")


class PostgresSettings(BaseSettings):
    PG_HOST: str = os.getenv("POSTGRES_HOST")
    PG_PORT: int = os.getenv("POSTGRES_PORT")
    PG_USER: str = os.getenv("POSTGRES_USER")
    PG_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    PG_DB: str = os.getenv("POSTGRES_DB")

    DRIVER: Literal["asyncpg"] = "asyncpg"

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+{self.DRIVER}://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}"


class RabbitSettings(BaseSettings):
    RABBIT_HOST: str = os.getenv("RABBIT_HOST")
    RABBIT_PORT: int = os.getenv("RABBIT_PORT")
    RABBIT_USER: str = os.getenv("RABBIT_USER")
    RABBIT_PASSWORD: str = os.getenv("RABBIT_PASSWORD")

    @property
    def rabbit_url(self) -> str:
        return f"amqp://{self.RABBIT_USER}:{self.RABBIT_PASSWORD}@{self.RABBIT_HOST}:{self.RABBIT_PORT}/"


class RedisSettings(BaseSettings):
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"


class ElasticsearchSettings(BaseSettings):
    ELASTIC_HOST: str = "elasticsearch"
    ELASTIC_PORT: int = 9200
    ELASTIC_USER: str = os.getenv("ELASTIC_USER")
    ELASTIC_PASSWORD: str = os.getenv("ELASTIC_PASSWORD")

    @property
    def elasticsearch_url(self) -> str:
        return f"http://{self.ELASTIC_HOST}:{self.ELASTIC_PORT}"


class UNFSettings(BaseSettings):
    UNF_URL: str = os.getenv("UNF_URL")


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()
    giga_chat: GigaChatSettings = GigaChatSettings()
    postgres: PostgresSettings = PostgresSettings()
    rabbit: RabbitSettings = RabbitSettings()
    redis: RedisSettings = RedisSettings()
    elasticsearch: ElasticsearchSettings = ElasticsearchSettings()
    unf: UNFSettings = UNFSettings()
    embeddings: EmbeddingsSettings = EmbeddingsSettings()
