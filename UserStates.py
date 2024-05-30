from aiogram.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    BASE = State()
    CREATING_PARI = State()
