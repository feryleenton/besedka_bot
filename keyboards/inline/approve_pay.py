from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

approve_pay_keyword = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплатил', callback_data='APPROVED')]
])