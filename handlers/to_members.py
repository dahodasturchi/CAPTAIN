from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram import types
from loader import dp, bot



@dp.message_handler(text_startswith='!to',is_chat_admin=True)
async def to_member(message: Message):
	text_to = message.text[3:].strip()
	await message.delete()
	if text_to is not None:
		await bot.send_message(message.chat.id, text=text_to)
	
















