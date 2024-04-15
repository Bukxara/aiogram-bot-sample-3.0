from aiogram import types
from aiogram.filters.command import CommandStart

from loader import dp


@dp.message(CommandStart())
async def bot_start(message: types.Message):
    print(message.from_user)
    await message.answer(f"Hello {message.from_user.full_name}!")