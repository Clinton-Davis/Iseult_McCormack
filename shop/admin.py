from django.contrib import admin
from .models import Product, Category, productComment, ProductView


class ProductAdmin(admin.ModelAdmin):
    #? Can be add later if needed 'feat_item','sales_items'
    list_display = ('name', 'inventory', 'code', 'category','price','in_stock',)

    list_editable = ('in_stock', 'inventory','price',)

    list_filter = ('category', 'in_stock', 'inventory',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','name',)


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',)


# admin.site.register(ProductView, ProductViewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(productComment)
