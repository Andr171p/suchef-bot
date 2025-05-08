from aiogram.types import FSInputFile
from aiogram.types import InputFile, InlineKeyboardMarkup

from src.config import BASE_DIR
from src.suchef_bot.core import Order
from src.misc.file_readers import read_txt
from src.presentation.bot.keyboards import pay_kb, confirmed_kb


STATUSES_TEMPLATES_DIR = BASE_DIR / "statuses" / "templates"

STATUSES_PHOTOS_DIR = BASE_DIR / "statuses" / "images"


class OrderMessage:
    def __init__(self, order: Order) -> None:
        self.order = order

    @property
    def photo(self) -> InputFile:
        file_path = STATUSES_PHOTOS_DIR / f"{self.order.status}.png"
        return FSInputFile(file_path)

    @property
    def text(self) -> str:
        if self.order.status == "Принят оператором":
            file_path = (
                STATUSES_TEMPLATES_DIR / 
                f"{self.order.status}" / 
                f"{self.order.delivery_method}.txt"
            )
        else:
            file_path = STATUSES_TEMPLATES_DIR / f"{self.order.status}.txt"
        text = read_txt(file_path)
        return text.format(**self.order.model_dump())

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        if self.order.pay_status == "CONFIRMED":
            return confirmed_kb(self.order.pay_link)
        return pay_kb(self.order.pay_link)
