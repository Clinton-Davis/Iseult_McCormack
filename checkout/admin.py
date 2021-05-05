from django.contrib import admin
from .models import Order, OrderLineItem, Delivary


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    exclude = ('product_size', 'lineitem_total')
    # readonly_fields = ('lineitem_total',)



class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 
                       'order_total','grand_total','original_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'delivery_cost', 
              'order_total', 'grand_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'order_total', 
                    'delivery_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Delivary)