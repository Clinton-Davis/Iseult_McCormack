from django.urls import path
from shop.views import ProductDetailView, All_Products

app_name = 'shop'

urlpatterns = [

    path('', All_Products.as_view(), name='shop'),
    path('<pk>/', ProductDetailView.as_view(), name='product_detail'),

]