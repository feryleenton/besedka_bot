from aiogram import types

from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline import pay_keyword, paying_method_keyword

from loader import dp, bot


@dp.callback_query_handler(text='PAY')
async def get_payment_methods(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.delete()
    await call.message.answer('Выберете удобный способ оплаты: ', reply_markup=paying_method_keyword)


@dp.message_handler(text='Получить чертежи беседки')
async def buy_drawing(message: types.Message):
    await message.answer('Вы можете приобрести комплект простых \n'
                         'и понятных чертежей для самостоятельного \n'
                         'изготовления деревянной беседки.')
    await message.answer('К чертежам прилагается подетальная \nспецификация всех элементов. \nСправиться даже ребенок!')
    with open('data/drawing_preview.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption='Чертежи защищены авторским правом. \n'
                                                  'За использование в коммерческих целях \n'
                                                  'предусмотрено административное \n'
                                                  'преследование по закону. ')
    await message.answer('Купить файл с чертежами: BESEDKA.PDF \n'
                         '<b>К оплате: 3.490 РУБ</b>', reply_markup=pay_keyword)
