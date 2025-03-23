from aiogram import F, Router
from aiogram.filters  import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветствую, я бот-валютчик, могу дать современный курс валюты")

@router.message(Command("help"))
async def help_bot(message: Message):
    await message.answer(
        "команда popular_course выводит курс топ 10 самых популярных валют в мире"
        "используйте команду course_output если хотите узнать курс конкретной валюты"
                         )