from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="orders", description="Узнать статус заказа"),
        BotCommand(command="flyers", description="Мои фишки"),
        BotCommand(command="promos", description="Акции")
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )
