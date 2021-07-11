import datetime

from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from loader import dp, bot
import messages

@dp.message_handler(text_startswith='!reo',is_chat_admin=True)
async def mute_member(message: Message):
	await message.delete()
	if message.reply_to_message:
		try:
			args = message.text[4:].strip()
			hours = args[:-1]
			
			if args[-1]=='m':
				final_time = datetime.timedelta(minutes=int(hours))
				time_type = 'daqiqa'
			else:
				final_time = datetime.timedelta(hours=int(hours))
				time_type = 'soat'
			chat_id = message.chat.id
			user_id = message.reply_to_message.from_user.id
			name = message.reply_to_message.from_user.full_name
			await bot.restrict_chat_member(
				chat_id,
                user_id,
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                until_date=final_time
				)
			await message.answer(
				text=f"""<a href="tg://user?id={user_id}">{name}</a> kapitan tomonidan {hours} {time_type}ga tribunalga topshirildi..."""
				)
			
		except Exception as e:
			await message.answer("Nimadir sindi...")
	else:
		await message.answer(text=messages.noreply)



@dp.message_handler(text_startswith='!unreo', is_chat_admin=True)
async def unmute_member(message: Message):
	await message.delete( )
	if message.reply_to_message:
		try:
			chat_id = message.chat.id
			user_id = message.reply_to_message.from_user.id
			name = message.reply_to_message.from_user.full_name
			await bot.restrict_chat_member(
				chat_id,
                user_id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
				)
			await bot.send_message(chat_id,
				text=f"""<a href="tg://user?id={user_id}">{full_name}</a> tribunaldan ozod etildi..."""
				)
			
		except:
			await message.answer("Nimadir sindi...")
	else:
		await message.answer(text=messages.noreply)
















