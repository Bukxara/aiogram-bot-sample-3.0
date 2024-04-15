from aiogram import types

from loader import dp


@dp.message()
async def echo_handler(message: types.Message):
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
