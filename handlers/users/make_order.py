from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from states.make_order import MakeOrder


from keyboards.default import choose_country
from keyboards.default import main_menu_others

from loader import dp, bot


@dp.message_handler(text='Беларусь', state=MakeOrder.WAITING_FOR_COUNTRY_DETAILS)
async def answer_country(message: types.Message, state: FSMContext):
    await message.answer('Напишите ваш телефон-имя-город для связи \n'
                         'в формате: +375 29 000 00 00-Сергей-Минск', reply_markup=ReplyKeyboardRemove())
    await MakeOrder.CONTACT_FORM__NAME.set()


@dp.message_handler(state=MakeOrder.WAITING_FOR_COUNTRY_DETAILS)
async def answer_country(message: types.Message, state: FSMContext):
    await message.answer('К сожалению мы еще не работаем в вашем регионе \n'
                         'Можем вам предложить: ', reply_markup=main_menu_others)
    await state.reset_state()


@dp.message_handler(text='Россия', state=MakeOrder.CHOOSE_COUNTRY)
async def answer_country(message: types.Message, state: FSMContext):
    await message.answer('К сожалению мы еще не работаем в вашем регионе \n'
                         'Можем вам предложить: ', reply_markup=main_menu_others)
    await state.reset_state()


@dp.message_handler(text='Украина', state=MakeOrder.CHOOSE_COUNTRY)
async def answer_country(message: types.Message, state: FSMContext):
    await message.answer('К сожалению мы еще не работаем в вашем регионе \n'
                         'Можем вам предложить: ', reply_markup=main_menu_others)
    await state.reset_state()


@dp.message_handler(text='Другая', state=MakeOrder.CHOOSE_COUNTRY)
async def answer_country(message: types.Message, state: FSMContext):
    await message.answer('Введите название страны: ')
    await MakeOrder.WAITING_FOR_COUNTRY_DETAILS.set()


@dp.message_handler(text='Казахстан', state=MakeOrder.CHOOSE_COUNTRY)
async def answer_country(message: types.Message, state: FSMContext):
    await message.answer('К сожалению мы еще не работаем в вашем регионе \n'
                         'Можем вам предложить: ', reply_markup=main_menu_others)
    await state.reset_state()


@dp.message_handler(text='Беларусь', state=MakeOrder.CHOOSE_COUNTRY)
async def answer_country(message: types.Message, state: FSMContext):
    await message.answer('Напишите ваш телефон-имя-город для связи \n'
                         'в формате: +375 29 000 00 00-Сергей-Минск ', reply_markup=ReplyKeyboardRemove())
    await MakeOrder.CONTACT_FORM__NAME.set()


@dp.message_handler(text='Заказать беседку')
async def get_offer(message: types.Message):
    with open('data/order_preview.jpg', 'rb') as photo:
        await message.answer_photo(photo=photo, caption='Беседка деревянная шестиугольная \n'
                             'Вмещает 10 человек \n'
                             'Площадь - 7м2, 2,8м в диаметре \n'
                             'В комплекте: Беседка, пол, стол, встроенные лавки. \n'
                             'Доставка + Монтаж \n'
                             'Стоимость: 1200$')
    await message.answer('В какой стране вы нахоитесь ?', reply_markup=choose_country)
    await MakeOrder.CHOOSE_COUNTRY.set()