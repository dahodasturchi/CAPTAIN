from loader import dp, bot

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ContentType



@dp.message_handler(Text(equals='!pin'), is_chat_admin=True)
async def pinning(message: Message):
	if message.reply_to_message:
		try:
			await message.delete()
			await bot.pin_chat_message(message.chat.id,message.reply_to_message.message_id)
			await bot.send_message(message.chat.id,f'{message.from_user.full_name} guruhda xabar qadadi!')
		except Exception as e:
			print(e)
			

@dp.message_handler(content_types=ContentType.PINNED_MESSAGE)
async def delete_pin(message: Message):
	await message.delete()





