from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pay_keyword = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплатить', callback_data='PAY')]
])