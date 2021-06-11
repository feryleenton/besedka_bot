from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu_others = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('Получить чертежи беседки')],
    [KeyboardButton('Сотрудничество')]

], resize_keyboard=True)