from django.conf import settings
from django_countries import countries
from django.shortcuts import redirect, reverse, HttpResponse, get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from shop.models import Product
from profiles.models import UserProfile
from .forms import LocationForm
from .countries import Europe, United_Kindom, Irlenad

#? If in the future size becomes a avaiable, Use the Blue Code(?)

def get_location_zones(request):
    print(request)
    if request in Irlenad:
            zone = 0
    elif request in United_Kindom:
            zone = 550
    elif request in Europe:
            zone = 600
    else:
            zone = 700
    # sesh_zone = request.session.get('sesh_zone', {})
    # request.session['sesh_zone'] = zone
    print("get_location_zones", zone)
    # location_name = dict(countries)[location_code]
    # print("get_location_zones", location_name)
    return zone

def bag_view(request):
    template = 'bag/bag.html'
    location_form = LocationForm()
    
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            location_form = LocationForm(initial={ 'country': profile.default_country})
           
            # print(location_form.default_country)
        except UserProfile.DoesNotExist:
            location_form = LocationForm()
    else: 
        location_form = LocationForm()
                
    context = {
        'form' : location_form,
        'in_bag':True,
    }
    return render(request,template,context )


def add_to_bag(request, item_id):
    """ Adds quantity 1 to the bag as each item 
    is unquie gets the session and adds bag to it
    """

    product = get_object_or_404(Product, pk=item_id)
    # redirect_url = request.POST.get('redirect_url')
    redirect_url = "bag:bag_view"
    size = None
    quantity = 1
 
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        messages.warning(request, f'You already have the {product.name} in your bag.\
            Every item is unique.')
        return redirect(redirect_url)
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
        
        request.session['bag'] = bag
        return redirect(redirect_url)
    

def add_location(request):
    redirect_url = "bag:bag_view"
    
    context = {
       
    }
    return redirect(redirect_url)
    

       

#? def add_to_bag(request, item_id):
    # product = get_object_or_404(Product, pk=item_id)
    # quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    # size = None
    # if 'product_size' in request.POST:
    #      size = request.POST['product_size']
    # bag = request.session.get('bag', {}) 
    # if size:
    #      if item_id in list(bag.keys()):
    #          if size in bag[item_id]['items_by_size'].keys():
    #              bag[item_id]['items_by_size'][size] += quantity
    #              messages.success(
    #                  request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
    #          else:
    #              bag[item_id]['items_by_size'][size] = quantity
    #              messages.success(
    #                  request, f'Added size {size.upper()} {product.name} to your bag')
    #      else:
    #          bag[item_id] = {'items_by_size': {size: quantity}}
    #          messages.success(
    #              request, f'Added size {size.upper()} {product.name} to your bag')
    # else:
    #      if item_id in list(bag.keys()):
    #          bag[item_id] += quantity
    #          messages.success(
    #              request, f'Updated {product.name} quantity to {bag[item_id]}')
    #      else:
    #          bag[item_id] = quantity
    #          messages.success(request, f'Added {product.name} to your bag')
    # request.session['bag'] = bag
    # return redirect(redirect_url)
    
#? def adjust_bag(request, item_id):
    # """Adjust the quantity of the specified product to the specified amount"""
    # product = get_object_or_404(Product, pk=item_id)
    # quantity = int(request.POST.get('quantity'))
    # size = None
    # if 'product_size' in request.POST:
    #       size = request.POST['product_size']
    # bag = request.session.get('bag', {})
    # if size:
    #       if quantity > 0:
    #           bag[item_id]['items_by_size'][size] = quantity
    #           messages.success(
    #               request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
    #       else:
    #           del bag[item_id]['items_by_size'][size]
    #           if not bag[item_id]['items_by_size']:
    #               bag.pop(item_id)
    #           messages.success(
    #               request, f'Removed size {size.upper()} {product.name} from your bag')
    # else:
    #       if quantity > 0:
    #           bag[item_id] = quantity
    #           messages.success(
    #               request, f'Updated {product.name} quantity to {bag[item_id]}')
    #       else:
    #           bag.pop(item_id)
    #           messages.success(request, f'Removed {product.name} from your bag')
    # request.session['bag'] = bag
    # return redirect(reverse('view_bag'))

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