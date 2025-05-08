from aiogram.types import Message

from src.suchef_bot.core import AIResponse
from src.presentation.bot.presenters.orders_presenter import OrdersPresenter


class ChatBotPresenter:
    @staticmethod
    async def present(message: Message, ai_response: AIResponse) -> None:
        if ai_response.action == "orders_status":
            await OrdersPresenter.present(message, ai_response.orders)
        else:
            await message.answer(ai_response.answer)
