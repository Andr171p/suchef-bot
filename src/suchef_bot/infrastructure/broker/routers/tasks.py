import logging

from typing import List

from faststream.rabbit import RabbitRouter
from dishka.integrations.base import FromDishka

from src.suchef_bot.core.entities import BaseMessage
from src.suchef_bot.core.interfaces import MessageRepository


logger = logging.getLogger(__name__)

tasks_router = RabbitRouter()


@tasks_router.subscriber("tasks")
async def save_messages(
        messages: List[BaseMessage],
        message_repository: FromDishka[MessageRepository]
) -> None:
    await message_repository.bulk_create(messages)
    logger.info("Messages saved successfully")
