from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from ..keyboards import start_keyboard
from src.suchef_bot.core.entities import User
from src.suchef_bot.core.use_cases import Registration


registration_router = Router()


@registration_router.message(Command("start"))
async def start(message: Message, registration: FromDishka[Registration]) -> None:
    telegram_id: int = message.from_user.id
    username: str = message.from_user.username
    is_registered = await registration.login(telegram_id)
    if not is_registered:
        await message.answer(
            f"Здравствуйте, {username}\\! Вам нужно пройти регистрацию. Это займёт всего пару секунд",
            reply_markup=start_keyboard()
        )
    else:
        await message.answer("Вы уже зарегистрированы")


@registration_router.message(F.contact)
async def share_contact(message: Message, registration: FromDishka[Registration]) -> None:
    telegram_id: int = message.from_user.id
    username: str = message.from_user.username
    phone_number: str = message.contact.phone_number
    user = User(telegram_id=telegram_id, username=username, phone_number=phone_number)
    await registration.register(user)
    await message.answer(
        """Вы успешно зарегистрированы! Ваш промо-код за регистрацию: 1224
        Примените его нашем сайте при оформлении заказа на сумму от 700 руб."""
    )
