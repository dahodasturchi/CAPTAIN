from loader import dp, bot

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ChatType

@dp.message_handler(commands="add",chat_type = ChatType.SUPERGROUP or ChatType.GROUP, is_chat_admin = True)
async def promote_member(message: Message):
	if message.reply_to_message:
		try:
			await message.delete()
			chat_id = message.chat.id
			user_id = message.reply_to_message.from_user.id
			await bot.promote_chat_member(
				chat_id,
				user_id,
				can_change_info=True,
				can_delete_messages=True,
				can_pin_messages=True,
				can_restrict_members=True
				)
			await bot.send_message(message.chat.id,'Bizda yangi admin bor...')
		except:
			pass




