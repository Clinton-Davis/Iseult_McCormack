from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product

def bag_contents(request):
    bag_items = []
    bag_total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    sesh_zone = request.session.get('sesh_zone', {}) or 0
    
 
    
    
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        bag_total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id' : item_id,
            'quantity': quantity,
            'product': product,
            'product_count':  product_count
        })
    raw_delivery = sesh_zone
    delivery = raw_delivery / 100
    bag_total = bag_total / 100
    
    if bag_total < settings.FREE_DELIVERY_THRESHOLD:
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - bag_total 
        delivery = delivery
        print("delivary for", delivery)

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
        'grand_total': grand_total,
    }
    return context