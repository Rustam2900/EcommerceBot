all_languages = ['en', 'uz']

message_history = {}

default_languages = {
    "language_not_found": "Siz toʻgʻri tilni tanlamadingiz!\n"
                          "Вы не выбрали правильный язык!",
    "welcome_message": "Salom, botimizga xush kelibsiz!\n"
                       "Quyidagi tillardan birini tanlang!\n\n"
                       "Hello, welcome to our bot!\n"
                       "Choose one of the languages below!",

    "uz": {
        "status": "status",
        "address": "manzil",
        "order_list": "buyurtmalar",
        "price": "narxi",
        "order_number": "order number",
        "enter_number": "Faqat raqam kiriting!",
        "order_address": "Iltimos, manzilingizni :",
        "reminder_days": "Keyingi buyurtmani qachon eslatish kerak (kun)",
        "order_created": "Buyurtma yaratildi",
        "order_not_created": "Buyurtma yaratilmadi!",
        "order_not_found": "Buyurtma topilmadi!",
        "order": "Buyurtmalarim",
        "full_name": "To'liq ismingizni kiriting",
        "individual": "Jismoniy shaxs",
        "legal": "Yuridik shaxs",
        "select_user_type": "Foydalanuvchi turini tanlang",
        "registration": "Ro'yxatdan o'tish",
        "login": "Kirish",
        "logout": "↩️ Akkauntdan chiqish",
        'exit': "Siz akkauntingizdan chiqdingiz",
        "sign_password": "Parolni kiritng",
        "company_name": "Kampaniya nomini kiriting",
        "employee_name": "xodimi ism familiyasini kiriting",
        "employee_count": "Kampaniyada ishchilar sonini kiriting",
        "company_contact": "Kampaniya telefon raqamini kiriting",
        "working_days": "Kampaniyadagi ish kuni sonini kiriting (haftasiga)",
        "duration_days": "Qancha vaqt mobaynida yetkazib berib turishimizni hohlaysiz? (necha kun)",
        "successful_registration": "Muvaffaqiyatli ro'yxatdan o'tildi",
        "successful_login": "Muvaffaqiyatli kirish",
        "user_not_found": "Foydalanuvchi topilmadi",
        "contact": "Telefon raqamingizni kiriting",
        "share_contact": "Kantaktni bo'lishish",
        "password": "Akkountingiz uchun parol kiriting",
        "web_app": "📎 Veb ilova",
        "settings": "⚙️ Sozlamalar",
        "contact_us": "📲 Biz bilan bog'lanish",
        "my_orders": "📦 Mening buyurtmalarim",
        "create_order": "✅ Buyurtma berish",
        "cancel": "❌ Bekor qilish",
        "select_language": "Tilni tanlang!",
        "successful_changed": "Muvaffaqiyatli o'zgartirildi",
        "contact_us_message": "Bizning manzil:\n{}\n\n"
                              "Biz bilan bog'laning:\n{}\n{}\n\n"
                              "Murojaat vaqti:\n{}"

    },

    "en": {
        "status": "status",
        "address": "адрес",
        "order_list": "orderсписок заказов",
        "price": "цена",
        "order_number": "номер заказа",
        "enter_number": "Введите только число!",
        "order_address": "Пожалуйста, укажите ваш адрес:",
        "reminder_days": "Когда напомнить о следующем заказе (день)",
        "order_created": "Заказ создан",
        "order_not_created": "Заказ не создан!",
        "order_not_found": "Заказ не найден!",
        "order": "Мои заказы",
        "full_name": "Введите свое полное имя",
        "individual": "Физическое лицо",
        "legal": "Юридическое лицо",
        "select_user_type": "Выберите тип пользователя",
        "registration": "registration",
        "login": "login",
        "logout": "↩️ logout",
        "exit": "Вы вышли из своей учетной записи",
        "sign_password": "Введите пароль",
        "company_name": "Введите название кампании",
        "employee_name": "Enter the employee's first and last name",
        "employee_count": "Введите количество работников в кампании.",
        "company_contact": "Введите номер телефона кампании",
        "working_days": "Введите количество рабочих дней в кампании (в неделю)",
        "duration_days": "Как долго вы хотите, чтобы мы доставили? (сколько дней)",
        "successful_registration": "Успешная регистрация",
        "successful_login": "Успешный вход",
        "user_not_found": "Пользователь не найден",
        "contact": "Введите свой номер телефона",
        "share_contact": "Поделиться контактом",
        "password": "Введите пароль для вашей учетной записи",
        "web_app": "📎 Веб-приложение",
        "settings": "⚙️ Настройки",
        "contact_us": "📲 Связаться с нами",
        "my_orders": "📦 Мои заказы",
        "create_order": "✅ Сделать заказ",
        "cancel": "❌ Отменить",
        "select_language": "Выберите язык!",
        "successful_changed": "Успешно изменено",
        "contact_us_message": "Наш адрес:\n{}\n\n"
                              "Связаться с нами:\n{}\n{}\n\n"
                              "Время подачи заявки:\n{}"
    }
}

user_languages = {}
local_user = {}

introduction_template = {
    'en':
        """
    🔹 Telegram Channel:  <a href="https://t.me/IT_RustamDevPythonMy">Python</a> 

    
    What can the bot do?
    - Ecommerce and online shopping
    - Latest and high-quality products
    - Manage and check your billing
    - Stay updated on exclusive discounts and promotions
    - Help with questions and support 
    🌐 EcommerceBot – the best online bot!

    🏠 Stay at home and enjoy unique services with ease!

    🟢 Join now: <a href="https://t.me/IT_RustamDevPythonMy">Python</a>
    ✉️  Telegram channel: <a href="https://t.me/IT_RustamDevPythonMy">Python</a>

    
    """,

    "uz":

        """
    Telagram kanal <a href="https://t.me/IT_RustamDevPythonMy">Python</a> 

    

    Bot nimalarni qila oladi?
    - Ecommerce and onlayn magazin
    - So'nggi va sifatli  mahsulotlar
    - Hisob-kitoblarni tekshirish
    - Eksklyuziv chegirmalar va aksiyalar haqida xabardor bo'lish
    - Savollar va yordam
    🌐 EcommerceBot – eng yahshi onlayn bot! 

    🏠 Uyda qolib unikal xizmatlardan foydalaning!

    🟢 Hoziroq qo'shiling: <a href="https://t.me/IT_RustamDevPythonMy">Python</a>
    ✉️ Telegram kanal: <a href="https://t.me/IT_RustamDevPythonMy">Python</a>

    

    """
}

bot_description = """
Bu bot Nima qila qila oladi?

💦 Ushbu bot Chere sof ichimlik suvini uydan turib istalgan vaqtda buyurtma qilishingiz va xizmat turlaridan foydalanishingiz uchun yaratilgan 💦

- - - - - - - - - - - - - - - - - - - - - - - - - 

💦 Этот бот создан для того, чтобы вы могли заказывать чистую питьевую воду Chere в любое время из дома и пользоваться услугами 💦
"""

offer_text = {
    "ru":
        "Сотрудники: {}\n"
        "День непрерывности: {}\n"
        "Мы рекомендуем вашим работникам {} бутылок с водой по 20 л.\n",
    "uz":
        """
    Xodim: {}
    Davomiylik kuni: {}
    Xodimlaringizga {} x 20 litrli suv idishlarini tavsiya qilamiz.
        """
}

order_text = {
    "uz": "Buyurtma raqami {} \n Buyurtma holati {}",
    "ru": "Номер заказа {} \n Статус заказа {}"
}

def fix_phone(phone):
    if "+" not in phone:
        return f"+{phone}"
    return phone