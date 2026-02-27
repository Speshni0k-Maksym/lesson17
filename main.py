import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
    
disp = Dispatcher()

@disp.message(Command("start"))
async def startMethod(message: Message):
    await message.answer("Bot active")





async def main():
    bot = Bot(token=API_TOKEN)

    await disp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())