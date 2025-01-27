from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command


from utils.commands import set_commands
from handlers.start import get_start
from state.register import RegisterState
from state.create import CreateState
from handlers.profile import view_profile
from handlers.register import start_register, register_name, register_phone
from filters.checkAdmin import checkAdmin
from handlers.admin.create import create_game, select_place, select_date, select_time, select_minplayer, select_maxplayer, select_price


load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')
ad = os.getenv('AD')

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


# функция приветствия
async def start_bot(bot: Bot):
    # await bot.send_message(admin_id, text='Бот каким-то чудом запустился:)')
    await bot.send_message(ad, text='Бот каким-то чудом запустился:)')

dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))

# Регистрируем хендлеры регистрации
dp.message.register(start_register, F.text == 'Зарегистрироваться на сайте')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)
# Регистрируем хендлеры с созданием игры
dp.message.register(create_game, Command(commands='create'), checkAdmin())
dp.callback_query.register(select_place, CreateState.place)
dp.callback_query.register(select_date, CreateState.date)
dp.callback_query.register(select_time, CreateState.time)
dp.message.register(select_minplayer, CreateState.minplayer)
dp.message.register(select_maxplayer, CreateState.maxplayer)
dp.message.register(select_price, CreateState.price)
# Регистрием хендлер профиля
dp.message.register(view_profile, F.text == 'Профиль')


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
