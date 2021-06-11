from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

paying_method_keyword = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='На карту', callback_data='CARD'),
     InlineKeyboardButton(text='Qiwi', callback_data='QIWI')]
])