import os
import asyncio
import threading

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

load_dotenv()
#API_TOKEN = os.getenv("BOT_TOKEN")
#PORT = int(os.getenv("PORT", 8080))
BOT_TOKEN = "8571820554:AAFuvPpbdK4jewtTMvaWon4ScSn5r4A_fIE"
PORT = 10000

disp = Dispatcher()
app = FastAPI()

@disp.message(Command("start"))
async def startMethod(message: Message):
    await message.answer("Bot active")

@app.api_route("/", methods=["GET", "HEAD"])
async def check():
    return {"status":"bot is running"}

async def main():
    bot = Bot(token=BOT_TOKEN)
    await disp.start_polling(bot)


async def runner():
    asyncio.run(main())

@app.on_event("startup")
async def startup():
    bot  = Bot(token=BOT_TOKEN)
    asyncio.create_task(disp.start_polling(bot))
    
    
if __name__ == "__main__":
    threading.Thread(target=runner).start()
    uvicorn.run(app,host = "0.0.0.0", port=PORT)
