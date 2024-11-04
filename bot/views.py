# payments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from .iyzico_service import create_iyzico_payment
from django.http import JsonResponse
from django.views import View




def create_payment(user_id):
    cart_items = CartItem.objects.filter(user_id=user_id, is_visible=True)

    total_amount = sum(item.calculate_amount() for item in cart_items)

    if total_amount > 0:
        payment = Payment.objects.create(
            user_id=user_id,
            amount=total_amount,
            status="pending"
        )

        return payment
    else:
        raise ValueError("Cart is empty or invalid total amount.")


class CreatePaymentView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        try:
            payment = create_payment(user_id)
            return Response({"payment_id": payment.id}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        amount = request.POST.get('amount')

        try:
            iyzico_response = create_iyzico_payment(user_id, amount)
            return JsonResponse(iyzico_response)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Something went wrong'}, status=500)
