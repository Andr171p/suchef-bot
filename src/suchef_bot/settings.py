from dotenv import load_dotenv

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from .constants import ENV_PATH, DRIVER

load_dotenv(ENV_PATH)


class EmbeddingsSettings(BaseModel):
    model_name: str = "deepvk/USER-bge-m3"  # 1024 dimensional
    model_kwargs: dict = {"device": "cpu"}
    encode_kwargs: dict = {"normalize_embeddings": False}


class BotSettings(BaseSettings):
    token: str = ""

    model_config = SettingsConfigDict(env_prefix="BOT_")


class GigaChatSettings(BaseSettings):
    api_key: str = ""
    scope: str = ""

    model_config = SettingsConfigDict(env_prefix="GIGACHAT_")


class PostgresSettings(BaseSettings):
    host: str = "postgres"
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"
    db: str = "postgres"

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

    @property
    def url(self) -> str:
        return f"postgresql+{DRIVER}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class RabbitSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5672
    user: str = ""
    password: str = ""

    model_config = SettingsConfigDict(env_prefix="RABBIT_")

    @property
    def url(self) -> str:
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}/"


class RedisSettings(BaseSettings):
    host: str = "redis"
    port: int = 6379

    @property
    def url(self) -> str:
        return f"redis://{self.host}:{self.port}/0"


class ElasticsearchSettings(BaseSettings):
    host: str = "elasticsearch"
    port: int = 9200
    username: str = ""
    password: str = ""

    model_config = SettingsConfigDict(env_prefix="ELASTICSEARCH_")

    @property
    def url(self) -> str:
        return f"http://{self.ELASTIC_HOST}:{self.ELASTIC_PORT}"

    @property
    def auth(self) -> tuple[str, str]:
        return self.username, self.password


class APISettings(BaseSettings):
    url: str = ""

    model_config = SettingsConfigDict(env_prefix="API_")


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()
    giga_chat: GigaChatSettings = GigaChatSettings()
    postgres: PostgresSettings = PostgresSettings()
    rabbit: RabbitSettings = RabbitSettings()
    redis: RedisSettings = RedisSettings()
    elasticsearch: ElasticsearchSettings = ElasticsearchSettings()
    api: APISettings = APISettings()
    embeddings: EmbeddingsSettings = EmbeddingsSettings()
