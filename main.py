import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import FSInputFile

from config import setting
from keyboard import keyboard_start

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    photo = FSInputFile("test.jpg")
    await message.answer_photo(photo=photo,
                               caption=f"Вот тут вот будет твой текст какой захочешь и можем картинку добавить из твоей коллекции",
                               reply_markup=keyboard_start())

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=setting.token_bot)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())