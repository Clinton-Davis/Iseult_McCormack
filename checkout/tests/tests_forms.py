from django.test import TestCase

from checkout.forms import OrderForm
from django.contrib.auth.models import User
from checkout.models import Order
from profiles.models import UserProfile


class TestOrderForm(TestCase):

    def setUp(self):
        invalid_data = {
            'order_number': '',
            'user_profile': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
            'street_address1': '',
            'street_address2': '',
            'town_or_city': '',
            'postcode': '',
            'county': '',
            'country': ''
        }
        self.invalid_data = invalid_data

    def test_OrderForm_(self):
        form = OrderForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('phone_number', form.errors.keys())
        self.assertIn('street_address1', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('postcode', form.errors.keys())

    def test_order_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'first_name', 'last_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',))
