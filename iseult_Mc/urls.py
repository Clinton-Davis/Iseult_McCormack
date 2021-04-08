from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from home.views import IndexView

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('bag/', include('bag.urls', namespace='bag')),
    path('shop/', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
