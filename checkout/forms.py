from django import forms
from django.forms import HiddenInput
from profiles.models import UserProfile
from .models import Order


class PaymentForm(forms.Form):
    hidden = forms.HiddenInput()
        
