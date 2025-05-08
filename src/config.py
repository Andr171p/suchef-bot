import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Literal
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class DatabaseSettings(BaseSettings):
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASSWORD")
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")

    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/railway"


class RabbitSettings(BaseSettings):
    user: str = os.getenv("RMQ_USER")
    password: str = os.getenv("RMQ_PASSWORD")
    host: str = os.getenv("RMQ_HOST")
    port: str = os.getenv("RMQ_PORT")

    url: str = f"amqp://{user}:{password}@{host}:{port}"

    queue_name: str = "orders"
    bind_queue_name: str = "suchef-orders"


class APISettings(BaseSettings):
    url: str = os.getenv("API_URL")
    headers: dict = {"Content-Type": "application/json; charset=UTF-8"}

    class Commands:
        status: Literal["status"] = "status"
        bonus: Literal["bonus"] = "bonus"

    cmd: Commands = Commands()

    # status: Literal["status"] = "status"
    # bonus: Literal["bonus"] = "bonus"


class StaticSettings(BaseSettings):
    start: Path = BASE_DIR / "assets" / "texts" / "start.json"
    auth: Path = BASE_DIR / "assets" / "texts" / "auth.json"
    exc: Path = BASE_DIR / "assets" / "texts" / "exc.json"
    statuses: Path = BASE_DIR / "assets" / "texts" / "statuses.json"

    texts_dir: Path = BASE_DIR / "assets" / "texts"
    photo_dir: Path = BASE_DIR / "assets" / "images"


class BotSettings(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class ProjectSettings(BaseSettings):
    url: str = os.getenv("PROJECT_URL")
    name: Literal["Сушеф.рф"] = "Сушеф.рф"

    promo: str = os.getenv("PROMO_URL")


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()
    db: DatabaseSettings = DatabaseSettings()
    static: StaticSettings = StaticSettings()
    rabbit: RabbitSettings = RabbitSettings()
    api: APISettings = APISettings()
    project: ProjectSettings = ProjectSettings()


settings = Settings()
