all_languages = ['en', 'ru']

message_history = {}

default_languages = {
    "language_not_found": "Siz toʻgʻri tilni tanlamadingiz!\n"
                          "Вы не выбрали правильный язык!",
    "welcome_message": "Salom, botimizga xush kelibsiz!\n"
                       "Quyidagi tillardan birini tanlang!\n\n"
                       "Hello, welcome to our bot!\n"
                       "Choose one of the languages below!",

    "en": {
        "status": "Status",
        "address": "Address",
        "order_list": "Orders",
        "price": "Price",
        "order_number": "Order Number",
        "enter_number": "Please enter only numbers!",
        "order_address": "Please enter your address:",
        "reminder_days": "When should we remind you for the next order (days)?",
        "order_created": "Order created",
        "order_not_created": "Order was not created!",
        "order_not_found": "Order not found!",
        "order": "My Orders",
        "full_name": "Enter your full name",
        "individual": "Individual",
        "legal": "Legal Entity",
        "select_user_type": "Select user type",
        "registration": "Registration",
        "login": "Login",
        "logout": "↩️ Logout",
        "exit": "You have logged out of your account",
        "sign_password": "Enter password",
        "company_name": "Enter company name",
        "employee_name": "Enter employee's full name",
        "employee_count": "Enter the number of employees in the company",
        "company_contact": "Enter the company's phone number",
        "working_days": "Enter the number of working days per week",
        "duration_days": "How long would you like us to deliver? (days)",
        "successful_registration": "Successfully registered",
        "successful_login": "Login successful",
        "user_not_found": "User not found",
        "contact": "Enter your phone number",
        "share_contact": "Share contact",
        "password": "Enter a password for your account",
        "web_app": "📎 Web App",
        "settings": "⚙️ Settings",
        "contact_us": "📲 Contact Us",
        "my_orders": "📦 My Orders",
        "create_order": "✅ Place Order",
        "cancel": "❌ Cancel",
        "select_language": "Select language!",
        "successful_changed": "Successfully changed",
        "contact_us_message": "Our address:\n{}\n\n"
                              "Contact us:\n{}\n{}\n\n"
                              "Working hours:\n{}"
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

    "ru":

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
