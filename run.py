from aiogram import Dispatcher, Bot
import os
import dotenv
from handlers import router

dotenv.load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))

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