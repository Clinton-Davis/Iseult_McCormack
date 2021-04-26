from django.urls import path
from . import views
from .webhooks import webhook

app_name = 'checkout'

urlpatterns = [
    path('payment/', views.checkout_payment, name='payment'),
    path('address/', views.checkout_address, name='address'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook')
]