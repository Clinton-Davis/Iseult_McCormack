# from django.test import TestCase
# from shop.views import All_Products
# from shop.models import Product

# class TestShopView(TestCase):
    
#     fixtures = [
#         'category.json',
#         'product.json'
#     ]
    
#     def test_shop_list_view(self):
#         response = self.client.get(reversed('shop:shop'))
#         print(response)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertTemplateUsed(response, template_name='shop/shop.html')
#         # self.assertTrue('product' in response.context)
        
#     def test_shop_detail_view(self):
#         product = Product.objects.get(id=1)
#         response = self.client.get(reversed('shop:product_detail'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name='shop/product_detial.html')
#         self.assertTrue('product' in response.context)
    
    
        
        
        