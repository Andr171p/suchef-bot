import logging
import asyncio

from src.suchef_bot.ioc import container
from src.suchef_bot.core.entities import UserMessage, AssistantMessage
from src.suchef_bot.core.use_cases import ChatAssistant


async def main() -> None:
    chat_id = "1"
    chat_assistant = await container.get(ChatAssistant)
    while True:
        text = input("User: ")
        user_message = UserMessage(chat_id=chat_id, text=text)
        assistant_message = await chat_assistant.answer(user_message)
        print(f"AI: {assistant_message.text}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())