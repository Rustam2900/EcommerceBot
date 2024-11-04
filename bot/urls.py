# payments/urls.py
from django.urls import path
from .views import CreatePaymentView, PaymentView

urlpatterns = [
    path('create/', CreatePaymentView.as_view(), name='create-payment'),
    path('process-payment/', PaymentView.as_view(), name='process_payment'),

]
