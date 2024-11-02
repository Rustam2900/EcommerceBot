import environ

from aiogram import Dispatcher, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.keyboards import get_languages, get_main_menu

from bot.utils import default_languages, user_languages, introduction_template, \
    local_user, fix_phone
from django.conf import settings
from aiogram.client.default import DefaultBotProperties
from asgiref.sync import sync_to_async
from bot.db import save_user_language, save_user_info_to_db

from bot.states import UserStates

dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


# @dp.message()
# async def get_image(msg: Message):
#     await msg.answer(msg.photo[-1].file_id)


@dp.message(CommandStart())
async def welcome(message: Message):
    user_id = message.from_user.id

    user = await CustomUser.objects.filter(telegram_id=user_id).afirst()

    if user and user.user_lang:
        main_menu_markup = await get_main_menu(user.user_lang)
        await message.answer(
            text=introduction_template[user.user_lang],
            reply_markup=main_menu_markup
        )
    else:
        msg = default_languages['welcome_message']
        await message.answer(msg, reply_markup=get_languages())


@dp.callback_query(lambda call: call.data.startswith("lang"))
async def get_query_languages(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user_lang = call.data.split("_")[1]

    await save_user_language(user_id, user_lang)

    await bot.answer_callback_query(call.id)
    await state.set_state(UserStates.name)

    await call.message.answer("Quyidagi kurslardan birini tanlang \n\n Выберите один из курсов ниже",
                              reply_markup=None)


@dp.callback_query(UserStates.name)
async def reg_user_contact(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user_lang = user_languages[user_id]
    await state.set_state(UserStates.contact)
    await call.message.answer(text=default_languages[user_lang]['employee_name'])


@dp.message(UserStates.contact)
async def company_contact(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_lang = user_languages[message.from_user.id]
    if message.text is None:
        phone = fix_phone(message.contact.phone_number)
        await state.update_data(company_contact=phone)
    else:
        phone = fix_phone(message.text)
        await state.update_data(company_contact=phone)
    state_data = await state.get_data()
    user_data = {
        "full_name": state_data['name'],
        "phone_number": company_contact,
        "username": message.from_user.username,
        "user_lang": user_lang,
        "telegram_id": user_id,
        "tg_username": f"https://t.me/{message.from_user.username}",
    }
    await save_user_info_to_db(user_data)
    await message.answer(text="aaa",
                         reply_markup=None)
    await state.clear()
