import asyncio
import logging

from aiogram import Bot

from src.suchef_bot.ioc import container
from src.suchef_bot.bot.dispatcher import create_dispatcher
from src.suchef_bot.infrastructure.broker.app import create_faststream_app


async def start_bot() -> None:
    bot = await container.get(Bot)
    dp = create_dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def start_broker() -> None:
    faststream_app = await create_faststream_app()
    await faststream_app.broker.start()


async def main() -> None:
    await asyncio.gather(
        start_bot(),
        start_broker()
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
