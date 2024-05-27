from aiogram.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    BASE = State()
    CREATING_PARI = State()
    PARI_CONFIGURATION_BASE = State()
    READING_PARI_CONFIGURATION = State()
    CONFIGURING_PARI = State()
