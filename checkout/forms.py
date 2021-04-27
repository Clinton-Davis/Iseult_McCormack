from django import forms
from django.forms import HiddenInput
from profiles.models import UserProfile
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)



        
