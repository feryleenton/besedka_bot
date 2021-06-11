from aiogram import types

from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline import pay_keyword, paying_method_keyword, approve_pay_keyword

from loader import dp, bot


@dp.callback_query_handler(text='APPROVED')
async def get_payment_methods(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=10)
    await call.message.answer('Спасибо за оплату! \nФайл с чертежами: BESEDKA.PDF \n'
                              'Будет отправлен на вашу почту сразу \n'
                              'после поступления платежа. \n'
                              'Если у вас что-то не получилось напишите \n'
                              'нам в поддержку в WhatsApp:<code> +7 925 825 15 65</code>')


@dp.callback_query_handler(text='CARD')
async def get_payment_methods(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.delete()
    await call.message.answer('Оплатите 3.490 РУБ на карту: \n'
                              '<code>5536 9137 8676 6184</code> \n'
                              'В комментариях к платежу обязательно напишите фразу: \n'
                              '“Чертежи беседки” \n'
                              'и напишите адрес вашей электронной почты, \n'
                              'на которую нужно отправить чертежи. \n'
                              'Если у вас что-то не получилось напишите \n'
                              'нам в поддержку в WhatsApp:<code> +7 925 825 15 65</code>', reply_markup=approve_pay_keyword)