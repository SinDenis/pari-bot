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
import tg_user_sercice as us

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    user = message.from_user
    us.register_user(user.username, user.id)
    await message.answer("Привет! Я пари-бот", reply_markup=kb)
    await state.set_state(UserStates.BASE)


@dp.message(F.text.lower() == 'мои пари', StateFilter(UserStates.BASE))
async def get_paris(message: types.Message):
    paris = ps.get_pari(message.from_user.username)
    text = ''
    for pari in paris:
        text += '\n' + str(pari)
    await message.answer(
        'Твои пари: ' + text if text != '' else 'У тебя нет пари'
    )


@dp.message(F.text.lower() == 'создать пари', StateFilter(UserStates.BASE))
async def add_pari(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.CREATING_PARI]
    await state.set_state(UserStates.CREATING_PARI)
    await message.answer('Введите через , параметры: название пари, описание пари, принимающего пари', reply_markup=kb)


@dp.message(F.text.lower() == 'отмена', StateFilter(UserStates.CREATING_PARI))
async def do_cancel_pari(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await state.set_state(UserStates.BASE)
    await message.answer('Создание пари отменено', reply_markup=kb)


@dp.message(StateFilter(UserStates.CREATING_PARI))
async def do_create_pari(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    challenger = message.from_user.username
    pari_name, pari_description, pari_taker = map(lambda msg: msg.strip(), message.text.split(','))
    added_pari = ps.add_pari(
        challenger,
        pari_name,
        pari_description,
        pari_taker
    )
    taker_tg_chat_id = us.get_tg_user_chat_id(pari_taker)
    text_ending = ''
    if (taker_tg_chat_id != None):
        taker_msg_text = f'''
        Привет! {challenger} отправил тебе пари, ниже его описание:
        
        {str(added_pari)}
        '''
        await bot.send_message(chat_id=taker_tg_chat_id, text=taker_msg_text)
        text_ending = f'Сообщение успешно отправлено {pari_taker}'
    else:
        text_ending = f'''
        Сообщение для {pari_taker} отправлено не было,
        так как он никогда не взаимодействовал с ботом'''
    await state.set_state(UserStates.BASE)
    await message.answer(f'Пари {pari_name} было успешно создано' + '\n' + text_ending,
                         reply_markup=kb)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
