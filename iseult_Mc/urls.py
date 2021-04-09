from django.conf import settings
from django.conf.urls.static import static
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
    path('shop/', include('shop.urls', namespace='shop')),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('img/favicon.ico'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
