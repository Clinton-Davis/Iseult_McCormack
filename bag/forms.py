from django import forms
from django_countries.fields import CountryField

class LocationForm(forms.Form):
    location = CountryField().formfield()