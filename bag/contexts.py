from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    bag_items = []
    bag_total = 0
    product_count = 0
    
    if bag_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = bag_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - bag_total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + bag_total 
    
    context = {
        'bag_items':bag_items,
        'bag_total':bag_total,
        'product_count':product_count,
        'delivery':delivery,
        'free_delivery_delta':free_delivery_delta,
        'free_delivery_threshold' : settings.FREE_DELIVERY_THRESHOLD,
        'tax_persentage': settings.TAX_RATE_PERCENTAGE,
        'grand_total':grand_total,
    }
    return context