from django.contrib import admin

from .models import Blog, BlogComment, BlogView, Like


class BlogListAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured',)
    list_editable = ('featured',)


admin.site.register(Blog,  BlogListAdmin)

admin.site.register(BlogComment)
admin.site.register(BlogView)
admin.site.register(Like)
