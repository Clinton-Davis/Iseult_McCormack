from django.test import TestCase
from shop.models import Product
from shop.models import Category


class ProductModelTests(TestCase):

    fixtures = [
        "category.json",
        "product.json"
    ]

    def test_product_name(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, "Blue Pink Orange")
        
    def test_product_category(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.category, 1)

    def test_product_description(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.description, "Product test description")

    def test_product_has_sizes(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.has_sizes, False)

    def test_product_in_stock(self):
        product = Product.objects.get(id=1)
        self.assertNotEqual(product.in_stock, False)

    def test_product_display_items(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.sales_items, False)

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        self.assertEquals(product.get_absolute_url(), '/shop/1/')


