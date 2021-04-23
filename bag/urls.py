from django.urls import path
from . import views
# from bag.views import LocationFormView, BagView

app_name = 'bag'

urlpatterns = [

    path('', views.bag_view, name='bag_view'),
    # path('', BagView.as_view(), name='bag_view'),
    # path('location/', LocationFormView.as_view(), name='location'),
    path('location/', views.add_location, name='add_location'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    

]