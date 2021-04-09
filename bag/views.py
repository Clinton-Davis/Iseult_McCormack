from django.conf import settings
from django.shortcuts import redirect, reverse, HttpResponse, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from shop.models import Product

class BagView(TemplateView):
    template_name = 'bag/bag.html'

    def get_context_data(self, **kwargs):
        tax_rate = settings.TAX_RATE_PERCENTAGE
        context = super().get_context_data(**kwargs)
        context['tax_rate'] = tax_rate
        context['in_bag'] = True
        return context

def add_to_bag(request, item_id):
    """ Adds quantity 1 to the bag as each item 
    is unquie gets the session and adds bag to it
    """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    size = None
    quantity = 1
    bag = request.session.get('bag', {})
    bag[item_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)