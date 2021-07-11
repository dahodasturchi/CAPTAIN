import datetime

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ChatType
from loader import dp, bot

import messages



@dp.message_handler(commands='help', chat_type=ChatType.SUPERGROUP or ChatType.GROUP)
async def for_help(message: Message):
	try:
		await bot.send_message(message.chat.id, text = messages.help_to, disable_web_page_preview=True)
	except Exception as e:
		print(e)

@dp.message_handler(commands='help', chat_type=ChatType.PRIVATE)
async def private_help(message: Message):
	await bot.send_message(message.chat.id, text = messages.about.replace("\t",""), disable_web_page_preview=True)



@dp.message_handler(commands='main',chat_type= ChatType.PRIVATE)
async def main_help(message: Message):
	await message.answer(messages.help.replace("\t",""))







