from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re


async def start_register(message: Message, state: FSMContext):
    await message.answer('⭐️Давайте начнем регистрацию \n Для начала скажите как к Вам обращаться?')
    await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'😀 Приятно познакомиться {message.text} \n'
                         f'📞 Теперь укажите номер телефона, чтобы быть на связи \n'
                         f'Формат телефона: +7хххххххххх \n\n'
                         f'⚠️ Внимание! Я чувствителен к формату')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)


# Функция обработки ввода телефона
async def register_phone(message: Message, state: FSMContext):
    if (re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        msg = f'Приятно познакомиться {reg_name} \n\n Ваш номер: {reg_phone}'
        await message.answer(msg)
        await state.clear()
    else:
        await message.answer(f'Номер указан в неправильном формате')
