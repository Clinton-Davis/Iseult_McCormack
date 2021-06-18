from django.contrib import admin
from .models import (About, Scarfs,
                     Paintings, ImageGallery,
                     Home, PrivacyPolicy,
                     TermsConditions, Comment)

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Scarfs)
admin.site.register(Paintings)
admin.site.register(ImageGallery)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsConditions)
