import messages
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands='start', chat_type="private")
async def command_start(message: Message):
	await message.answer(
        text=f"Salom,\nMen guruhlarda kapitanlarga yordam berish uchun yaratilganman\n\n/help "
        )
	if message.get_args().strip()=='about':
		await message.answer(messages.about.replace('\t',''),disable_web_page_preview=True)
