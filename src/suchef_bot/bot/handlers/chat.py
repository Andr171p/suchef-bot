from aiogram import F, Router
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from faststream.rabbit import RabbitBroker

from src.suchef_bot.core.entities import UserMessage
from src.suchef_bot.core.use_cases import ChatAssistant


chat_router = Router()


@chat_router.message(F.text)
async def answer(
        message: Message,
        chat_assistant: FromDishka[ChatAssistant],
        broker: FromDishka[RabbitBroker]
) -> None:
    await message.bot.send_chat_action(message.from_user.id, "typing")
    user_message = UserMessage(chat_id=str(message.from_user.id), text=message.text)
    assistant_message = await chat_assistant.answer(user_message)
    await message.answer(assistant_message.text)
    await broker.publish([user_message, assistant_message], "tasks")
