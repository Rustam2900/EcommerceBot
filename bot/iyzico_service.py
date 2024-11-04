import requests
from django.conf import settings


def create_iyzico_payment(amount, user_id):
    # API URL'si
    url = f"{settings.IYZIPAY_BASE_URL}/payment/iyzipos"

    headers = {
        "Authorization": f"Basic {settings.IYZIPAY_API_KEY}:{settings.IYZIPAY_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "locale": "tr",  # Til
        "price": str(amount),  # To'lov miqdori
        "paidPrice": str(amount),  # To'lov miqdori
        "currency": "TRY",  # Valyuta
        "paymentCard": {
            "cardHolderName": "Foydalanuvchi Ismi",  # Foydalanuvchi ismi
            "cardNumber": "5528790000000008",  # Kredit karta raqami (real bo'lmasligi kerak)
            "expireMonth": "12",  # Karta amal qilish muddati
            "expireYear": "2030",  # Karta amal qilish yili
            "cvc": "123",  # CVC
            "registerCard": "0"  # Karta ro'yxatdan o'tkazilishi
        },
        "buyer": {
            "id": str(user_id),  # Foydalanuvchi identifikatori
            "name": "Foydalanuvchi Ismi",  # Foydalanuvchi ismi
            "surname": "Foydalanuvchi Familiyasi",  # Foydalanuvchi familiyasi
            "gsmNumber": "+998901234567",  # Telefon raqami
            "email": "foydalanuvchi@example.com",  # Email
            "identityNumber": "12345678901",  # Shaxsiy raqam
            "lastLoginDate": "2024-11-04 12:00:00",  # Oxirgi kirish sanasi
            "registrationDate": "2024-01-01 10:00:00",  # Ro'yxatdan o'tgan sanasi
            "registrationAddress": "Manzil",  # Ro'yxatdan o'tgan manzil
            "ip": "85.34.78.112",  # IP manzil
            "city": "Toshkent",  # Shahar
            "country": "O'zbekiston",  # Mamlakat
            "zipCode": "100000"  # Pochta indeksi
        }
    }

    # So'rovni yuborish
    response = requests.post(url, json=data, headers=headers)
    return response.json()  # Javobni qaytarish
