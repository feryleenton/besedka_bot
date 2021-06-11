from aiogram.dispatcher.filters.state import StatesGroup, State


class RequestPartnership(StatesGroup):
    WAITING_FOR_OFFER = State()
    WAITING_FOR_EMAIL = State()