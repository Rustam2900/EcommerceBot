from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from bot.utils import default_languages


def get_languages(flag="lang"):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ru 🇷🇺", callback_data=f"{flag}_ru"),
         InlineKeyboardButton(text="en 🇺🇸", callback_data=f"{flag}_en")],
    ])
    return keyboard

# def get_user_contacts(user_language):
#     keyboard = ReplyKeyboardMarkup(keyboard=[
#         [KeyboardButton(text=default_languages[user_language]['share_contact'], request_contact=True)],
#     ], resize_keyboard=True)
#
#     return keyboard


def get_main_menu(language):
    main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=default_languages[language]['categories'],),
            KeyboardButton(text=default_languages[language]['contact_us']),
            KeyboardButton(text=default_languages[language]['my_orders'])
        ]
    ], resize_keyboard=True)
    return main_menu_keyboard
