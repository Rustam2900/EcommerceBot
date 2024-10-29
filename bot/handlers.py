from aiogram import Dispatcher, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, LabeledPrice
import environ

from bot.keyboards import get_languages, get_main_menu

from bot.utils import default_languages, user_languages, introduction_template, \
    local_user
from django.conf import settings
from aiogram.client.default import DefaultBotProperties
from asgiref.sync import sync_to_async

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(".env")

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
