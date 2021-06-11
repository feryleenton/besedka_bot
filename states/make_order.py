from aiogram.dispatcher.filters.state import StatesGroup, State


class MakeOrder(StatesGroup):
    CHOOSE_COUNTRY = State()
    WAITING_FOR_COUNTRY_DETAILS = State()
    CONTACT_FORM__NAME = State()
    CONTACT_FORM__PHONE = State()
    CONTACT_FORM__CITY = State()