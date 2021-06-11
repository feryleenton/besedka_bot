from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.default import main_menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте!\n"
                         f"Выберете один из пунктов", reply_markup=main_menu)
