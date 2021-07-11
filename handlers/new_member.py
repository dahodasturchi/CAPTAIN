from aiogram.types import Message
from aiogram import types
from loader import dp, bot
import messages

from time import gmtime, strftime



@dp.message_handler(content_types = types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(message: Message):
	user = message.new_chat_members[0]
	moment = strftime("%H:%M", gmtime())
	top = moment.index(':')
	now_time =f'{int(moment[:top])+5}:{moment[top+1:]}'
	await bot.send_message(message.chat.id,text=f"""
		Xush kelibsiz!!! <a href="tg://user?id={user.id}">{user.full_name}</a> [{now_time}]
		""")
	try:
		await message.delete()
	except:
		await bot.send_message(message.chat.id,'Adminlar kimdur meni admin qilib qo‘ysin, iltimos...')






@dp.message_handler(content_types = types.ContentTypes.LEFT_CHAT_MEMBER)
async def new_member(message: Message):
	await message.delete()
