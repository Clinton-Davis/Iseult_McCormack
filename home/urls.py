from django.urls import path
from home.views import ContactView, IndexView, TermsView, GalleryView


urlpatterns = [

    path('', IndexView, name='home'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('contact/',  ContactView.as_view(), name='contact')
]
