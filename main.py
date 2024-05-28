from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StateFilter
from aiogram import F

import pari_service
from UserStates import UserStates
from keyboard_helper import keyboards

import pari_service as ps

from config import TOKEN
import storage.db.user_db_repository as user_storage
import storage.db.pari_db_repository as pari_storage

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    user_storage.save_user(message.from_user.username, message.chat.id)
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я пари-бот", reply_markup=kb)
    await state.set_state(UserStates.BASE)


@dp.message(F.text == "Мои пари", StateFilter(UserStates.BASE))
async def my_paris(message: types.Message):
    text = "Твои пари:"
    paris = pari_storage.get_pari_by_challenger(message.from_user.username)
    text = text + pari_service.get_paris(paris)
    await message.answer(text)


@dp.message(F.text == "Мои пари на выполнение", StateFilter(UserStates.BASE))
async def my_paris(message: types.Message):
    text = "Твои пари:"
    paris = pari_storage.get_pari_by_taker(message.from_user.username)
    text = text + pari_service.get_paris(paris)
    await message.answer(text)


@dp.message(F.text == "Создать пари", StateFilter(UserStates.BASE))
async def set_pari_name(message: types.Message, state: FSMContext):
    text = ps.set_pari_name()
    await message.answer(text)
    await state.set_state(UserStates.SETTING_PARI_TAKER)


@dp.message(StateFilter(UserStates.SETTING_PARI_TAKER))
async def set_pari_taker(message: types.Message, state: FSMContext):
    pari_storage.add_pari(message.text, message.from_user.username)
    text = ps.set_pari_taker()
    await message.answer(text)
    await state.set_state(UserStates.PARI_CREATED)


@dp.message(StateFilter(UserStates.PARI_CREATED))
async def pari_created(message: types.Message, state: FSMContext):
    pari = pari_storage.set_pari_taker(message.from_user.username, message.text)
    text = ps.add_pari(pari.taker_name, pari.name)
    taker_user = user_storage.get_user(pari.taker_name)
    if taker_user is not None:
        taker_message = "Пользователь " + pari.challenger_name + " заключил с вами пари: " + pari.name
        await bot.send_message(taker_user, taker_message)
    else:
        text += f", однако пользователь {pari.taker_name} не зарегестрирован в боте, так что ему не придет уведомление"
    await message.answer(text)
    await state.set_state(UserStates.BASE)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
