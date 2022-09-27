from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, ContentType, ParseMode
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import config
from commands import start_command
from handlers import callback_query, handler


storage = MemoryStorage()

bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)



scheduler = AsyncIOScheduler()

async def f():
    print('21qewds')

def get_horoscope_everyday() -> None:
    scheduler.add_job(f, "interval", seconds=2)


async def on_startup(_):
    print('Бот запущен')
    #get_horoscope_everyday()

async def on_shutdown(_):
    print('Бот отключён', end=' ')



@dp.callback_query_handler(lambda call:True)
async def callback_query_handler(call):
    await callback_query(bot, call)
    
@dp.message_handler(Command('start'))
async def start_message_handler(message):
    await start_command(bot, message)

@dp.message_handler()
async def text_message_handler(message):
    await handler(bot, message)

@dp.channel_post_handler()
async def channel_handler(message):
    await handler(bot, message)

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)