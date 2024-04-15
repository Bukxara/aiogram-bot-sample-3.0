from aiogram import types
from aiogram.filters.command import BotCommand

from loader import dp


# @dp.message(BotCommand())
# async def bot_help(message: types.Message):
#     text = ("Commands: ",
#             "/start - Start the bot",
#             "/help - Help")
    
#     await message.answer("\n".join(text))