from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product
from profiles.models import UserProfile
from checkout.models import Delivary

def bag_contents(request):
    bag_items = []
    bag_total = 0
    bag_categorys = []
    product_count = 0
    bag = request.session.get('bag', {})
    
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        bag_total += quantity * product.price
        product_count += quantity
        bag_categorys.append(product.category.name)
        bag_items.append({
            'item_id' : item_id,
            'quantity': quantity,
            'product': product,
            'product_count':  product_count
        })
    
    if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            if profile.country == "":
                code = Delivary.objects.get(code="00")
                code_packet_price = code.packet_price /100
                code_parcel_price = code.parcel_price /100
            else:
                default_country = profile.country
                code = Delivary.objects.get(code=default_country)
                code_packet_price = code.packet_price /100
                code_parcel_price = code.parcel_price /100

    else:
        code = Delivary.objects.get(code="00")
        code_packet_price = code.packet_price /100
        code_parcel_price = code.parcel_price /100
        
    bag_total = bag_total / 100
    
    if bag_total < settings.FREE_DELIVERY_THRESHOLD:
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - bag_total 
        if "painting" in bag_categorys :
            delivery = code_parcel_price
        else:
            delivery = code_packet_price
    else:
        delivery = 0
        free_delivery_delta = 0
        
    grand_total = delivery + bag_total 
    
    context = {
        'bag_items':bag_items,
        'bag_total':bag_total,
        'product_count':product_count,
        'selected_location': code.name,
        "code_packet_price": code_packet_price,
        "code_parcel_price": code_parcel_price,
        'free_delivery_delta':free_delivery_delta,
        'free_delivery_threshold' : settings.FREE_DELIVERY_THRESHOLD,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context