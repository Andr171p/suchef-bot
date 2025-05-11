from aiogram.types import FSInputFile, InlineKeyboardMarkup

from src.suchef_bot.core.entities import Order, Bonus, Promo

from .keyboards import (
    payment_keyboard,
    confirmed_payment_keyboard,
    bonus_keyboard,
    promo_keyboard
)

from src.suchef_bot.utils import read_txt
from src.suchef_bot.constants import (
    STATUS_IMAGES_DIR,
    STATUS_TEMPLATES_DIR,
    BONUSES_IMAGES_DIR,
    BONUSES_TEMPLATES_DIR
)


class OrderMessage:
    def __init__(self, order: Order) -> None:
        self.order = order

    @property
    def image(self) -> FSInputFile:
        image_file = STATUS_IMAGES_DIR / f"{self.order.status}.png"
        return FSInputFile(image_file)

    @property
    def text(self) -> str:
        if self.order.status == "Принят оператором":
            template_file = (
                    STATUS_TEMPLATES_DIR
                    / f"{self.order.status}"
                    / f"{self.order.delivery_method}.txt"
            )
        else:
            template_file = STATUS_TEMPLATES_DIR / f"{self.order.status}.txt"
        template = read_txt(template_file)
        return template.format(**self.order.model_dump())

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        if self.order.pay_status == "CONFIRMED":
            return confirmed_payment_keyboard(self.order.pay_link)
        return payment_keyboard(self.order.pay_link)


class BonusMessage:
    def __init__(self, bonus: Bonus) -> None:
        self.bonus = bonus

    @property
    def image(self) -> FSInputFile:
        image_file = BONUSES_IMAGES_DIR / "flyers.png"
        return FSInputFile(image_file)

    @property
    def text(self) -> str:
        if self.bonus.chips > 0:
            template_file = BONUSES_TEMPLATES_DIR / "Есть флаеры.txt"
        else:
            template_file = BONUSES_TEMPLATES_DIR / "Нет фишек.txt"
        template = read_txt(template_file)
        return template.format(**self.bonus.model_dump())

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        return bonus_keyboard()


class PromoMessage:
    def __init__(self, promo: Promo) -> None:
        self.promo = promo

    @property
    def image(self) -> str:
        return self.promo.url

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        return promo_keyboard(self.promo.title)
