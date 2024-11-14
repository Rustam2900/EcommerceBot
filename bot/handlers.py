import re
from aiogram import Dispatcher, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, ContentType
from bot.keyboards import get_languages, get_main_menu

from bot.utils import default_languages, user_languages, introduction_template, \
    fix_phone
from django.conf import settings
from aiogram.client.default import DefaultBotProperties
from bot.db import (save_user_language, save_user_info_to_db, get_my_orders,
                    get_all_categories, get_user_language, fetch_products_by_category,
                    get_product_detail, add_to_cart, get_cart_items, create_order,
                    link_cart_items_to_order, update_order_location)

from bot.states import UserStates, OrderState, OrderAddress
from bot.models import CustomUser

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

phone_number_validator = re.compile(r'^\+90 \d{3} \d{3} \d{2} \d{2}$')


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
    user_languages[user_id] = user_lang

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

    text = default_languages.get(user_lang, {}).get('contact', 'Please enter your phone number')
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
        error_message = default_languages[user_lang].get("sorry", "Error: Registration failed!")
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
    user_lang = user_languages.get(user_id, 'en')

    my_orders = await get_my_orders(user_id)

    if not my_orders:
        await message.answer(
            text=default_languages[user_lang]['order_not_found'],
            reply_markup=get_main_menu(user_lang)
        )
        return

    msg = ""
    sorted_orders = sorted(my_orders, key=lambda order: order.created_at, reverse=True)

    for order in sorted_orders:
        msg += f"Order #{order.id}\n"
        msg += f"Status: {order.get_status_display()}\n"
        msg += f"Address: {order.address}\n"
        msg += f"Phone: {order.phone_number}\n"
        msg += f"Total Price: {order.total_price} USD\n"
        msg += f"Created At: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        msg += "----------------------------\n"

    await message.answer(text=f"{default_languages[user_lang]['order']}\n {msg}")


@dp.message(F.text.in_(["Categories", "Категории"]))
async def get_categories(message: Message):
    user_id = message.from_user.id
    user_lang = await get_user_language(user_id)
    print(f"User language: {user_lang}")
    categories = await get_all_categories()
    inline_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[])
    inline_buttons = []

    for category in categories:
        if user_lang == 'ru':
            category_name = category.name_ru
        else:
            category_name = category.name_en
        inline_buttons.append(InlineKeyboardButton(text=category_name, callback_data=f"category_{category.id}"))
    inline_kb.inline_keyboard = [inline_buttons[i:i + 2] for i in range(0, len(inline_buttons), 2)]
    await message.answer(
        text="Please select a category:",
        reply_markup=inline_kb
    )


@dp.callback_query(lambda call: call.data.startswith("category_"))
async def handle_products_by_category(call: CallbackQuery):
    user_id = call.from_user.id
    user_lang = await get_user_language(user_id)
    category_id = int(call.data.split("_")[1])

    products = await fetch_products_by_category(category_id)
    inline_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[])
    inline_buttons = []

    for product in products:
        product_name = product.name_ru if user_lang == 'ru' else product.name_en
        inline_buttons.append(InlineKeyboardButton(text=product_name, callback_data=f"product_{product.id}"))

    inline_kb.inline_keyboard = [inline_buttons[i:i + 2] for i in range(0, len(inline_buttons), 2)]
    await call.message.edit_text("Mahsulotlar:", reply_markup=inline_kb)


@dp.callback_query(lambda call: call.data.startswith("product_"))
async def handle_product_detail(call: CallbackQuery):
    user_id = call.from_user.id
    product_id = int(call.data.split("_")[1])
    user_lang = await get_user_language(user_id)

    product = await get_product_detail(product_id)

    product_name = product.name_ru if user_lang == 'ru' else product.name_en
    description = product.description or "Tavsif mavjud emas"
    message_text = (
        f"📦 Mahsulot: {product_name}\n\n"
        f"📄 Tavsif: {description}\n"
        f"💲 Narxi: {product.price} so'm\n"
        f"📏 O'lchami: {product.size or 'Mavjud emas'}\n"
        f"🎨 Rangi: {product.color or 'Mavjud emas'}\n"
        f"🚚 Yetkazib berish vaqti: {product.delivery_time or 'Mavjud emas'}"
    )

    inline_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])
    inline_buttons = []
    inline_buttons.append(InlineKeyboardButton(text="Buyurtma berish", callback_data=f"order_{product.id}"))
    inline_kb.inline_keyboard = [inline_buttons[i:i + 2] for i in range(0, len(inline_buttons), 2)]

    await call.message.edit_text(message_text, reply_markup=inline_kb)


@dp.callback_query(lambda call: call.data.startswith("order_"))
async def handle_order_start(call: CallbackQuery, state: FSMContext):
    product_id = int(call.data.split("_")[1])
    await call.message.answer("Mahsulot rangi kiriting:")

    await state.update_data(product_id=product_id)
    await state.set_state(OrderState.waiting_for_color)


@dp.message(OrderState.waiting_for_color)
async def process_color(message: Message, state: FSMContext):
    await state.update_data(color=message.text)
    await message.answer("Mahsulot o'lchamini kiriting:")
    await state.set_state(OrderState.waiting_for_size)


@dp.message(OrderState.waiting_for_size)
async def process_size(message: Message, state: FSMContext):
    await state.update_data(size=message.text)
    await message.answer("Mahsulot miqdorini kiriting:")
    await state.set_state(OrderState.waiting_for_quantity)


@dp.message(OrderState.waiting_for_quantity)
async def process_quantity(message: Message, state: FSMContext):
    data = await state.get_data()
    quantity = int(message.text)
    print("quantity: ", quantity)
    product_id = data['product_id']
    color = data['color']
    size = data['size']

    await add_to_cart(
        user_id=message.from_user.id,
        product_id=product_id,
        color=color,
        size=size,
        quantity=quantity
    )

    await message.answer("Mahsulot savatchaga qo'shildi!")
    await state.clear()


@dp.message(F.text.in_(["basket", "корзина"]))
async def show_cart(message: Message, state: FSMContext):
    user_id = message.from_user.id
    cart_items = await get_cart_items(user_id)

    if not cart_items:
        await message.answer("Savatchangiz bo'sh.")
        return

    message_text = "Sizning savatchangiz:\n\n"
    for item in cart_items:
        message_text += (
            f"📦 {item.product.name_ru} - {item.quantity} dona\n"
            f"🎨 Rang: {item.color}, 📏 O'lcham: {item.size}\n"
            f"💲 Narx: {item.amount} so'm\n\n"
        )

    inline_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])
    inline_buttons = []
    inline_buttons.append(InlineKeyboardButton(text="Buyurtma berish", callback_data=f"confirm_order"))
    inline_kb.inline_keyboard = [inline_buttons[i:i + 2] for i in range(0, len(inline_buttons), 2)]
    await message.answer(message_text, reply_markup=inline_kb)
    # await state.set_state(OrderAddress.location)


# @dp.callback_query(lambda call: call.data == "confirm_order")
# async def confirm_order(call: CallbackQuery, state: FSMContext):
#     user_id = call.from_user.id
#     order = await create_order(user_id)
#
#     await link_cart_items_to_order(user_id, order)
#     await call.message.answer("Buyurtmangiz qabul qilindi!")

def create_location_keyboard():
    location_button = KeyboardButton(text="Joylashuvni yuborish", request_location=True)
    location_keyboard = ReplyKeyboardMarkup(
        keyboard=[[location_button]],  # Keyboard layout formatini qo'shamiz
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return location_keyboard


@dp.callback_query(lambda c: c.data == "confirm_order")
async def request_location(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Buyurtmani tasdiqlash uchun joylashuvingizni yuboring.",
                                        reply_markup=create_location_keyboard())
    await state.set_state(OrderAddress.location)
    await callback_query.answer()


@dp.message(F.content_type == ContentType.LOCATION, OrderAddress.location)
async def save_location_and_create_order(message: Message, state: FSMContext):
    user_id = message.from_user.id
    latitude = message.location.latitude
    longitude = message.location.longitude

    order = await create_order(user_id)
    await link_cart_items_to_order(user_id, order)
    await update_order_location(order, latitude, longitude)

    await message.answer("Buyurtmangiz qabul qilindi va saqlandi.")
    await state.clear()
