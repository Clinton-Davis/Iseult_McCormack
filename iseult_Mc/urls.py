from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from home.views import IndexView

urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('bag/', include('bag.urls', namespace='bag')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('img/favicon.ico'))),
    url(r'^.*/$', IndexView, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
