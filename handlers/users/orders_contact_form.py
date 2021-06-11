from aiogram import types

from aiogram.dispatcher import FSMContext
from states.make_order import MakeOrder


from keyboards.default import choose_country
from keyboards.default import main_menu

from data.config import ADMINS

from loader import dp, bot


@dp.message_handler(state=MakeOrder.CONTACT_FORM__CITY)
async def contact_form_city(message: types.Message, state: FSMContext):
    city = message.text
    state_data = await state.get_data()
    phone = state_data['phone']
    name = state_data['name']

    for admin in ADMINS:
        await bot.send_message(admin, '<b>Новвя заявка на покупку беседки !</b>\n'
                                      ''+name+'\n'+''+phone+'\n'+''+city+'')
    await message.answer('Спасибо, ваша заявка принята, с вами свяжуться в близжайшее время !', reply_markup=main_menu)
    await state.reset_state()


@dp.message_handler(state=MakeOrder.CONTACT_FORM__PHONE)
async def contact_from_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data(phone=phone)
    await message.answer('Введите свой город: ')
    await MakeOrder.CONTACT_FORM__CITY.set()


@dp.message_handler(state=MakeOrder.CONTACT_FORM__NAME)
async def contact_form_name(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        await bot.send_message(admin, '<b>Новвя заявка на покупку беседки !</b>\n'
                                      ''+message.text)
    await message.answer('Спасибо, ваша заявка принята! \n'
                         'Мы позвоним вам в рабочее время с 8:00 до 20:00', reply_markup=main_menu)
    await state.reset_state()