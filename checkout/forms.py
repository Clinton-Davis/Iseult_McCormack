from django import forms
from django.forms import HiddenInput
from profiles.models import UserProfile
from .models import Order


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ("delivery_cost",'order_number','user_profile','date',
                   'delivery_cost','order_total','grand_total',
                   'original_bag','stripe_pid',
                   )
        
        
