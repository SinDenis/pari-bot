from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from UserStates import UserStates
from aiogram.filters.state import StateFilter

from config import TOKEN
from keyboard_utils import keyboards
import services.in_memory_pari_service as ps

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


#Стартовый обработчик
@dp.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я пари-бот!", reply_markup=kb)
    await state.set_state(UserStates.BASE)


#Состояние BASE
@dp.message(F.text == "Мои пари", StateFilter(UserStates.BASE))
async def send_welcome(message: types.Message):
    kb = keyboards[UserStates.BASE]
    paris = ps.get_pari_by_user_id(message.from_user.id)
    if len(paris) == 0:
        answer_text = "У тебя нет пари("
    else:
        i = 1
        answer_text = "Твои пари:"
        for pari in paris:
            answer_text += "\n" + str(i) + ") " + pari
            i+=1
    await message.answer(answer_text, reply_markup=kb)


@dp.message(F.text == "Создать пари", StateFilter(UserStates.BASE))
async def send_welcome(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.CREATING_PARI]
    await message.answer("Введите название пари", reply_markup=kb)
    await state.set_state(UserStates.CREATING_PARI)


#Состояние CREATING_PARI
@dp.message(F.text == "Отмена", StateFilter(UserStates.CREATING_PARI))
async def cancel_creating_pari(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Отменяю создание пари", reply_markup=kb)
    await state.set_state(UserStates.BASE)


@dp.message(StateFilter(UserStates.CREATING_PARI))
async def create_new_pari(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    ps.add_pari_by_user_id(message.from_user.id, message.text)
    await message.answer("Пари \"" + message.text + "\" создано", reply_markup=kb)
    await state.set_state(UserStates.BASE)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
