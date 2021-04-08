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
    """ Adds a specified product to cart, Checks for sizes and quantity of the sizes
    if sizes are the same it adds to quantity, addes to cart and redirecs to products page
    """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    size = None
    quantity = 1
    bag = request.session.get('bag', {})
    bag[item_id] = quantity
    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect(redirect_url)