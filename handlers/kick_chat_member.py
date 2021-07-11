import datetime
import messages
from loader import dp, bot

from aiogram.dispatcher.filters import Text
from aiogram.types import Message

@dp.message_handler(Text(equals="!ban"), is_chat_admin=True)
async def ban_member(message: Message):
	await message.delete()
	if message.reply_to_message:
		chat_id = message.chat.id
		user_id = message.reply_to_message.from_user.id
		full_name = message.reply_to_message.from_user.full_name
		
		await bot.kick_chat_member(chat_id, user_id)
		await message.answer(
			text= f"""<a href="tg://user?id={user_id}">{full_name}</a> admin tomonidan guruhdan chetlatildi...""")

		
	else:
		await message.answer(text = messages.noreply)











