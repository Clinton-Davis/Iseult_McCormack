from django.test import TestCase, Client
from django.urls import reverse


class TestBagViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.bag = reverse("bag:bag_view")

    def test_bag_template_view(self):
        response = self.client.get(self.bag)
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed(response, 'bag/bag.html')
