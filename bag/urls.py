from django.urls import path
from . import views
from bag.views import BagView

app_name = 'bag'

urlpatterns = [

    path('', BagView.as_view(), name='bag_view'),
    # path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    # path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    # path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),

]