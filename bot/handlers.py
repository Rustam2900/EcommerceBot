import environ

from aiogram import Dispatcher, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, LabeledPrice

from django.contrib.auth.hashers import make_password

from bot.keyboards import get_languages, get_main_menu, get_registration_and_login_keyboard

from bot.utils import default_languages, user_languages, introduction_template, \
    local_user, fix_phone
from django.conf import settings
from aiogram.client.default import DefaultBotProperties
from asgiref.sync import sync_to_async

from bot.states import LoginStates, RegistrationStates

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(".env")

dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


# @dp.message()
# async def get_image(msg: Message):
#     await msg.answer(msg.photo[-1].file_id)


@dp.message(CommandStart())
async def welcome(message: Message):
    user_lang = user_languages.get(message.from_user.id, None)
    user_phone = local_user.get(message.from_user.id, None)
    if user_phone and user_lang:
        await message.answer_photo(
            photo="AgACAgIAAxkBAAIYtWcg00g6GdyujioWIHTgVyhUODX_AAIh6zEbReUJSWhHNoTxx5LMAQADAgADeAADNgQ",
            caption=introduction_template[user_lang], reply_markup=get_main_menu(user_lang))
    else:
        msg = default_languages['welcome_message']
        await message.answer(msg, reply_markup=get_languages())


@dp.callback_query(F.data.startswith("lang"))
async def get_query_languages(call: CallbackQuery):
    user_id = call.from_user.id
    user_lang = call.data.split("_")[1]
    user_languages[user_id] = user_lang
    user = local_user.get(user_id, None)
    if user is None:
        await call.message.answer_photo(
            photo="AgACAgIAAxkBAAIYtWcg00g6GdyujioWIHTgVyhUODX_AAIh6zEbReUJSWhHNoTxx5LMAQADAgADeAADNgQ",
            caption=introduction_template[user_lang], reply_markup=get_registration_and_login_keyboard(user_lang))
    else:
        await call.message.answer_photo(
            photo="AgACAgIAAxkBAAIYtWcg00g6GdyujioWIHTgVyhUODX_AAIh6zEbReUJSWhHNoTxx5LMAQADAgADeAADNgQ",
            caption=introduction_template[user_lang], reply_markup=get_main_menu(user_lang))


@dp.callback_query(F.data == "registration")
async def reg_user_contact(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user_lang = user_languages[user_id]
    await state.set_state(RegistrationStates.name)
    await call.message.answer(text=default_languages[user_lang]['contact'])


@dp.callback_query(RegistrationStates.name)
async def reg_user_contact(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user_lang = user_languages[user_id]
    await state.set_state(RegistrationStates.contact)
    await call.message.answer(text=default_languages[user_lang]['employee_name'])


@dp.message(RegistrationStates.contact)
async def company_contact(message: Message, state: FSMContext):
    user_lang = user_languages[message.from_user.id]
    if message.text is None:
        phone = fix_phone(message.contact.phone_number)
        await state.update_data(company_contact=phone)
    else:
        phone = fix_phone(message.text)
        await state.update_data(company_contact=phone)
    await message.answer(text=default_languages[user_lang]['password'])
    await state.set_state(LegalRegisterState.password)


@dp.message(RegistrationStates.password)
async def working_days(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_lang = user_languages[user_id]
    state_data = await state.get_data()
    employees_count = int(state_data['employee_count'])
    durations_days = int(state_data['duration_days'])
    total_water = calculate_total_water(state_data['working_days'], employees_count, durations_days)
    data = {
        "full_name": state_data['name'],
        "username": message.from_user.username,
        "password": make_password(message.text),
        "company_name": state_data['company_name'],
        "phone_number": state_data['company_contact'],
        "user_lang": user_lang,
        "telegram_id": user_id,
        "tg_username": f"https://t.me/{message.from_user.username}",
    }
    await create_user_db(data)
    local_user[user_id] = state_data['company_contact']

    await message.answer(offer_text[user_lang].format(employees_count, durations_days, total_water),
                         reply_markup=get_confirm_button(user_lang))
    await state.clear()


@dp.callback_query(F.data == "login")
async def user_sign_in(call: CallbackQuery, state: FSMContext):
    user_lang = user_languages[call.from_user.id]
    await state.set_state(LoginStates.password)
    await call.message.answer(text=default_languages[user_lang]['sign_password'])
