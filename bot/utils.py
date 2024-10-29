all_languages = ['en', 'uz']

message_history = {}

default_languages = {
    "language_not_found": "Siz toʻgʻri tilni tanlamadingiz!\n"
                          "Вы не выбрали правильный язык!",
    "welcome_message": "Salom, botimizga xush kelibsiz!\n"
                       "Quyidagi tillardan birini tanlang!\n\n"
                       "Здравствуйте, добро пожаловать в наш бот!\n"
                       "Выберите один из языков ниже!",

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
        "employee_name": "Kampaniya xodimi ism familiyasini kiriting",
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

    "ru": {
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
        "registration": "Зарегистрироваться",
        "login": "Войти",
        "logout": "↩️ Выйти из аккаунта",
        "exit": "Вы вышли из своей учетной записи",
        "sign_password": "Введите пароль",
        "company_name": "Введите название кампании",
        "employee_name": "Введите имя и фамилию сотрудника кампании.",
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
    'ru':
        """
    💧Chere Water Company представляет <a href="https://t.me/chere_water_bot">Chere Water</a> 💧

    Решите все вопросы, связанные с водой Chere! 🚰

    Что может сделать бот?
    - Заказ воды
    - Знать о последних тарифах на воду
    - Проверка расчетов
    - Будьте в курсе эксклюзивных скидок и акций
    - Вопросы и помощь
    🌐 ChereBot - легкий и быстрый сервис!

    🏠 Оставайтесь дома и пользуйтесь уникальными услугами!

    🟢 Присоединяйтесь прямо сейчас: <a href="https://t.me/chere_water_bot">Chere Water</a>
    ✉️  Телеграм канал: <a href="https://t.me/chere_water_bot">Chere Water</a>

    Chere - Чистая вода, Здоровая жизнь!
    """,

    "uz":

        """
    💧 Chere Suv Kompaniyasi <a href="https://t.me/chere_water_bot">Chere Water</a> ni taqdim etadi 💧

    Chere suvi bilan bog'liq barcha masalalaringizni hal qiling! 🚰

    Bot nimalarni qila oladi?
    - Suv buyurtma qilish
    - So'nggi suv tariflarini bilish
    - Hisob-kitoblarni tekshirish
    - Eksklyuziv chegirmalar va aksiyalar haqida xabardor bo'lish
    - Savollar va yordam
    🌐 ChereBot – oson va tezkor xizmat! 

    🏠 Uyda qolib unikal xizmatlardan foydalaning!

    🟢 Hoziroq qo'shiling: <a href="https://t.me/chere_water_bot">Chere Water</a>
    ✉️ Telegram kanal: <a href="https://t.me/chere_water_bot">Chere Water</a>

    Chere - Sof Suv, Sog‘lom Hayot!

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






