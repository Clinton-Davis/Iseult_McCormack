from django.urls import path
from home.views import (
    ContactView, IndexView, 
    TermsView, GalleryView, 
    About
)

urlpatterns = [

    path('', IndexView.as_view(), name='home'),
    path('about/', About, name='about'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('contact/',  ContactView.as_view(), name='contact')
]
