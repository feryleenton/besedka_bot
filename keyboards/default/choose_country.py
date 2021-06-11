from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


choose_country = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('Россия')],
    [KeyboardButton('Беларусь')],
    [KeyboardButton('Украина')],
    [KeyboardButton('Казахстан')],
    [KeyboardButton('Другая')],

], resize_keyboard=True)