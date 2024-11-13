import requests
from django.conf import settings


def create_iyzico_payment(amount, user_id):
    url = f"{settings.IYZIPAY_BASE_URL}/payment/iyzipos"

    headers = {
        "Authorization": f"Basic {settings.IYZIPAY_API_KEY}:{settings.IYZIPAY_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "locale": "tr",
        "price": str(amount),
        "paidPrice": str(amount),
        "currency": "TRY",
        "paymentCard": {
            "cardHolderName": "Foydalanuvchi Ismi",
            "cardNumber": "5528790000000008",
            "expireMonth": "12",
            "expireYear": "2030",
            "cvc": "123",
            "registerCard": "0"
        },
        "buyer": {
            "id": str(user_id),
            "name": "Foydalanuvchi Ismi",
            "surname": "Foydalanuvchi Familiyasi",
            "gsmNumber": "+998901234567",
            "email": "foydalanuvchi@example.com",
            "identityNumber": "12345678901",
            "lastLoginDate": "2024-11-04 12:00:00",
            "registrationDate": "2024-01-01 10:00:00",
            "registrationAddress": "Manzil",
            "ip": "85.34.78.112",
            "city": "Toshkent",
            "country": "O'zbekiston",
            "zipCode": "100000"
        }
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()
