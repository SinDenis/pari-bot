from uuid import uuid4

from aiogram import Bot, Dispatcher, types
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
from UserStates import UserStates
from keyboard_helper import keyboards

import pari_service as ps

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я пари-бот", reply_markup=kb)
    await state.set_state(UserStates.BASE)


@dp.message(F.text.lower() == 'мои пари', StateFilter(UserStates.BASE))
async def get_paris(message: types.Message):
    paris = ps.get_pari(message.from_user.id)
    text = ''
    for pari in paris:
        text += '\n' + pari
    await message.answer(f'Твои пари: {text}')


@dp.message(F.text.lower() == 'создать пари', StateFilter(UserStates.BASE))
async def add_paris(message: types.Message):
    pari_name = str(uuid4())
    ps.add_pari(message.from_user.id, pari_name)
    await message.answer(f'Пари {pari_name} было успешно создано')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
