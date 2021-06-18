from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from home.views import IndexView
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('iseult-admin/', admin.site.urls),
    path('bag/', include('bag.urls', namespace='bag')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('img/favicon.ico'))),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    url(r'^.*/$', IndexView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
