from django.urls import path
from home.views import (
    ContactView, IndexView, 
    TermsView, GalleryView, 
    aboutview
)

urlpatterns = [

    path('', IndexView.as_view(), name='home'),
    path('about/', aboutview, name='about'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('contact/',  ContactView.as_view(), name='contact')
]
