from django.contrib import admin
from .models import Product, Category, productComment, ProductView


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_stock', 'sales_items',
                    'price', 'category', 'feat_item',
                     )

    list_editable = ('in_stock', 'sales_items',
                     'price', 'category', 'feat_item',)

    list_filter = ('category', 'in_stock', 'feat_item',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','name',)


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',)


admin.site.register(ProductView, ProductViewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(productComment)
