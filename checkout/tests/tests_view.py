from django.test import TestCase, Client
from django.urls import reverse


class TestCheckoutViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout = reverse("checkout:checkout_payment")

    def test_checkout_payment_view(self):
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('checkout/checkout_payment.html')

    def setUp(self):
        self.client = Client()
        self.checkout = reverse("checkout:address")

    def test_checkout_address_view(self):
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('checkout/checkout_address.html')
