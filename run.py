from aiogram import Dispatcher, Bot
from config import TOKEN
from handlers import router

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

async def main():
    await dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Произошла ошибка")

#CoinGecko API pycoingecko