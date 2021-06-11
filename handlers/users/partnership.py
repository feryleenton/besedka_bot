from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from states import RequestPartnership
from keyboards.default import main_menu
from data.config import ADMINS


@dp.message_handler(state=RequestPartnership.WAITING_FOR_EMAIL)
async def complete_offer(message: types.Message, state: FSMContext):
    contact_email = message.text
    state_data = await state.get_data()
    partnership_offer = state_data['offer']

    for admin in ADMINS:
        await bot.send_message(admin, '<b>Поступило новое предложение о сотрудничестве !</b>\n'
                                '' + partnership_offer + '\n' + 'Контактные данные: ' + contact_email)

    await message.answer('Спасибо за обращение!\n'
                         'Ожидайте звонка', reply_markup=main_menu)
    await state.reset_state()


@dp.message_handler(state=RequestPartnership.WAITING_FOR_OFFER)
async def get_contacts(message: types.Message, state: FSMContext):
    await state.update_data(offer=message.text)
    await message.answer('Напишите ваш телефон и имя в формате: \n'
                         '+7 925 555 55 55 - Алексей')
    await RequestPartnership.WAITING_FOR_EMAIL.set()


@dp.message_handler(text='Сотрудничество')
async def get_offer(message: types.Message):
    await message.answer('Коротко изложите ваше предложение ')
    await RequestPartnership.WAITING_FOR_OFFER.set()