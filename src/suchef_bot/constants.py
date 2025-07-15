from pathlib import Path
from typing import Literal

DRIVER = "asyncpg"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

STATUS_TEMPLATES_DIR = BASE_DIR / "assets" / "statuses" / "templates"
STATUS_IMAGES_DIR = BASE_DIR / "assets" / "statuses" / "images"

BONUSES_IMAGES_DIR = BASE_DIR / "assets" / "bonuses" / "photos"
BONUSES_TEMPLATES_DIR = BASE_DIR / "assets" / "bonuses" / "templates"

PROJECT_NAME = "Сушеф.рф"

URL = "https://imp72.ru"
PROMO_URL = "https://imp72.ru/catalog/akcii/"

ORDER_STATUS = Literal[
    "Новый",
    "Принят оператором",
    "Передан на кухню",
    "Готовится",
    "Приготовлен",
    "Укомплектован",
    "Готов для выдачи",
    "Передан курьеру",
    "Доставлен",
    "Завершен успешно",
    "Отменен"
]
PAY_STATUS = Literal[
    "NEW",
    "CONFIRMED"
]

MIN_BONUS = 0

SIMILARITY_WEIGHT = 0.6
BM25_WEIGHT = 0.4
