from loader import dp, bot
from scrapper import paster, screen

from aiogram.types import Message





@dp.message_handler(commands="paste")
async def pasted(message: Message):
	if message.reply_to_message:
		code = message.reply_to_message.text
		result = paster(code)
		await message.reply(result)




@dp.message_handler(commands='screen')
async def creener(message:Message):
	args = message.get_args().strip()
	var = screen(args)
	if var:
		await message.reply_photo(open('screen.jpg','rb'))
	else:
		await message.answer('Uzr, qo‘limdan kelmadi...')

