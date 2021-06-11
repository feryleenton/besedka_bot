from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('Заказать беседку')],
    [KeyboardButton('Получить чертежи беседки')],
    [KeyboardButton('Сотрудничество')]

], resize_keyboard=True)