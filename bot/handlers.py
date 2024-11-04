import environ
import re
from aiogram import types
from aiogram import Dispatcher, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from bot.models import Order
from bot.keyboards import get_languages, get_main_menu,get_user_contacts

from bot.utils import default_languages, user_languages, introduction_template, \
    local_user, fix_phone, order_text
from django.conf import settings
from aiogram.client.default import DefaultBotProperties
from asgiref.sync import sync_to_async
from bot.db import save_user_language, save_user_info_to_db, get_my_orders

from bot.states import UserStates
from bot.models import CustomUser

dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

phone_number_validator = re.compile(r'^\+998 \d{2} \d{3} \d{2} \d{2}$')


# @dp.message()
# async def get_image(msg: Message):
#     await msg.answer(msg.photo[-1].file_id)


@dp.message(CommandStart())
async def welcome(message: Message):
    user_id = message.from_user.id
    user = await CustomUser.objects.filter(telegram_id=user_id).afirst()

    if user and user.user_lang:
        main_menu_markup = get_main_menu(user.user_lang)
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

    text = default_languages[user_lang]['full_name']
    await call.message.answer(text, reply_markup=None)


@dp.message(UserStates.name)
async def reg_user_contact(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_lang = user_languages.get(user_id, 'en')

    await state.update_data(name=message.text)
    await state.set_state(UserStates.contact)

    # text = default_languages[user_lang]['contact']
    # , reply_markup=get_user_contacts(user_lang)
    text = await message.answer(text=default_languages[user_lang]['contact'], reply_markup=get_user_contacts(user_lang))

    await message.answer(text)


@dp.message(UserStates.contact)
async def company_contact(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_lang = user_languages.get(user_id, 'en')

    if message.contact:
        phone = fix_phone(message.contact.phone_number)
    else:
        phone = fix_phone(message.text)

    if not phone_number_validator.match(phone):
        error_message = default_languages[user_lang].get(
            "enter_number", "Please enter a valid phone number format: +998 XX XXX XX XX"
        )
        await message.answer(error_message)
        return

    await state.update_data(company_contact=phone)

    state_data = await state.get_data()
    user_data = {
        "full_name": state_data.get('name'),
        "phone_number": phone,
        "username": message.from_user.username,
        "user_lang": user_lang,
        "telegram_id": user_id,
        "tg_username": f"https://t.me/{message.from_user.username}",
    }

    try:
        await save_user_info_to_db(user_data)
        success_message = default_languages[user_lang].get("successful_registration",
                                                           "Thank you, registration successful!")
        await message.answer(text=success_message, reply_markup=get_main_menu(user_lang))

    except Exception as e:
        error_message = default_languages[user_lang].get("order_not_created", "Error: Registration failed!")
        await message.answer(text=error_message)

    await state.clear()



@dp.message(F.text.in_(["📲 Contact us", "📲 Связаться с нами"]))
async def contact_us(message: Message):
    user_id = message.from_user.id
    user_lang = user_languages.get(user_id, 'en')


    contact_info = f"{default_languages[user_lang]['contact_us']}\n" \
                   f"Address: Your Address Here\n" \
                   f"Email: Contact Email Here\n" \
                   f"Phone: Your Phone Number Here\n" \
                   f"Working Hours: Your Working Hours Here"
    
    await message.answer(contact_info)

@dp.message(F.text.in_(["📦 My orders", "📦 Мои заказы"]))
async def get_orders(message: Message):
    user_id = message.from_user.id
    phone_number = message.from_user.id
    user_lang = user_languages.get(user_id, 'en')
    my_orders = await get_my_orders(phone_number)
    msg = ""
    if my_orders:
        for order in my_orders:
            msg += f"{order_text[user_lang].format(order.order_number, order.status)}\n"
            msg += "----------------------------\n"
        await message.answer(text=f"{default_languages[user_lang]['order']}\n {msg}")
    else:
        await message.answer(text=default_languages[user_lang]['order_not_found'],
                             reply_markup=get_main_menu(user_lang))

# @dp.message(F.text.in_(["📦 My orders", "📦 Мои заказы"]))
# async def get_orders(message: Message):
#     user_id = message.from_user.id
#     phone_number = message.from_user.id
#     phone_number = await phone_number(user_id)  # Correctly get phone number
#     user_lang = user_languages.get(user_id, 'en')

#     print(f"User ID: {user_id}, Phone Number: {phone_number}")  # Debugging line

#     my_orders = await get_my_orders(phone_number)
#     print(f"My Orders: {my_orders}")  # Debugging line

#     msg = ""
#     if my_orders:
#         for order in my_orders:
#             msg += f"{order_text[user_lang].format(order[1], order[2])}\n"  # Adjust indexing based on your order structure
#             msg += "----------------------------\n"
#         await message.answer(text=f"{default_languages[user_lang]['order']}\n{msg}")
#     else:
#         await message.answer(text=default_languages[user_lang]['order_not_found'],
#                              reply_markup=get_main_menu(user_lang))
