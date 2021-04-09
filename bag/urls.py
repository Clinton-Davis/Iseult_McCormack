from django.urls import path
from . import views
from bag.views import BagView

app_name = 'bag'

urlpatterns = [

    path('', BagView.as_view(), name='bag_view'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),

]