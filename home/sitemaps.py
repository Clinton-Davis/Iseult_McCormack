from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):

    property = 0.5
    changefreq = "daily"

    def items(self):

        return [
            'home',
            'about',
            'gallery',
            'contact',
            'terms',
            'privacy',
            'shop:shop'
        ]

    def location(self, item):
        return reverse(item)
