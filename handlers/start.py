from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Здравствуйте, рад видеть Вас😋 \n'
                           f'Бот поможет записаться на игру по футболу в г. Москва \n'
                           f'Также вы можете отслеживать свою статистику \n\n\n', reply_markup=register_keyboard)
