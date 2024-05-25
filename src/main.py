from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
   await bot.send_message(message.chat.id,"Привет! Я простой эхо-бот!")

@dp.message()
async def send_answer(message: types.Message):
   await bot.send_message(message.chat.id, message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())