from aiogram.types import (
    InlineKeyboardMarkup,
    FSInputFile,
    InputFile
)

from src.presentation.bot.keyboards import bonus_kb
from src.misc.file_readers import read_txt
from src.suchef_bot.core import Bonus
from src.config import BASE_DIR


PHOTO_PATH = BASE_DIR / "assets" / "bonuses" / "images" / "flyers.png"

TEMPLATES_DIR = BASE_DIR / "assets" / "bonuses" / "templates"


class BonusMessage:
    def __init__(self, bonus: Bonus) -> None:
        self._bonus = bonus

    @property
    def photo(self) -> InputFile:
        return FSInputFile(PHOTO_PATH)

    @property
    def text(self) -> str:
        file_path = TEMPLATES_DIR / "Нет фишек.txt"
        if self._bonus.chips > 0:
            file_path = TEMPLATES_DIR / "Есть флаеры.txt"
        template = read_txt(file_path)
        return template.format(**self._bonus.model_dump())

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        return bonus_kb()
