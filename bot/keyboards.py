from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from bot.utils import default_languages


def get_languages(flag="lang"):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="uz ", callback_data=f"{flag}_uz"),
         InlineKeyboardButton(text='en ', callback_data=f"{flag}_en")], ])
    return keyboard


def get_main_menu(language):
    main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=default_languages[language]['web_app']),
         KeyboardButton(text=default_languages[language]['settings'])],

        [KeyboardButton(text=default_languages[language]['contact_us']),
         KeyboardButton(text=default_languages[language]['my_orders'])],
        [KeyboardButton(text=default_languages[language]['logout']), ]

    ], resize_keyboard=True)
    return main_menu_keyboard


def get_registration_and_login_keyboard(user_language):
    registration_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=default_languages[user_language]['registration'], callback_data='registration')],
        [InlineKeyboardButton(text=default_languages[user_language]['login'], callback_data='login')], ])

    return registration_keyboard if registration_keyboard else []


def get_registration_keyboard(user_lang):
    registration_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=default_languages[user_lang]['registration'], callback_data='registration')]])
    return registration_keyboard if registration_keyboard else []
