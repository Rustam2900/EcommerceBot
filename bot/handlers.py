import json

from aiogram import Dispatcher, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, LabeledPrice
import environ
from django.contrib.auth.hashers import make_password
from pyexpat.errors import messages
from rest_framework_simplejwt.utils import aware_utcnow

import requests

from bot.db import create_user_db, get_company_contacts, get_my_orders, login_user, create_item_db, \
    create_order_from_cart, create_order_db
from bot.keyboards import get_languages, get_user_types, get_registration_keyboard, get_user_contacts, \
    get_main_menu, get_confirm_button, get_registration_and_login_keyboard, inline_create_order, location_user
from bot.states import LegalRegisterState, IndividualRegisterState, LoginStates, LegalAddressReminderState, \
    IndividualAddressReminderState
from bot.utils import default_languages, user_languages, introduction_template, calculate_total_water, \
    offer_text, order_text, local_user, fix_phone, message_history
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from aiogram.client.default import DefaultBotProperties
from asgiref.sync import sync_to_async
from order.models import Order
from users.models import CustomUser

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(".env")
# PROVIDER_TOKEN = env.str('PROVIDER_TOKEN')
dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))




@dp.message(CommandStart())
async def welcome(message: Message):
    user_lang = user_languages.get(message.from_user.id, None)
    user_phone = local_user.get(message.from_user.id, None)
    if user_phone and user_lang:
        await message.answer_photo(
            photo="AgACAgIAAxkBAANfZyC1l5KceiuaFyIoPsCljhipBdYAAmneMRuhEwhJd1YhKDb_CDoBAAMCAAN5AAM2BA",
            caption=introduction_template[user_lang], reply_markup=get_main_menu(user_lang))
    else:
        msg = default_languages['welcome_message']
        await message.answer(msg, reply_markup=get_languages())