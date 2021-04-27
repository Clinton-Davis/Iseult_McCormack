from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from .forms import PaymentForm
from .models import Order, OrderLineItem, Delivary
from shop.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe
import json


def get_delivary_price(request):
    """
    Finds the user, and gets there saved country code.
    Finds the categorys in the session bag
    Returns the price
    """
    profile = UserProfile.objects.get(user=request.user)
    user_delivary_code = profile.country
    code = get_object_or_404(Delivary, code=user_delivary_code)
    bag = request.session.get('bag', {})
    for item_id, item_data in bag.items():
        product = Product.objects.get(id=item_id)
    if product.category.name == "paintings":
        delivery = code.parcel_price
    else:
        delivery = code.packet_price
    return delivery
    

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout_address(request):
    template = "checkout/addressform.html"
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('checkout:payment'))
        else:
            messages.error(
                request, 'Update failed, Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
   
    context = {
        "address_form": form
    }
    return render(request, template, context)        



def checkout_payment(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    payment_form = PaymentForm()
    profile = get_object_or_404(UserProfile, user=request.user)
    delivary = get_delivary_price(request)
    
    
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        payment_form = PaymentForm()
        
        
        if payment_form.is_valid():
            pid = request.POST.get('client_secret').split('_secret')[0]
            order = payment_form.save(commit=False)
            order.stripe_pid = pid
            order.delivery_cost = delivary
            print("insideform_valid", delivary)
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout:checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('shop:shop'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )


    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout_payment.html'
    context = {
       
        'profile': profile,
        'payment_form': payment_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'on_checkout_page': True
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    
    bag = request.session.get('bag', {})
    for item_id, item_data in bag.items():
         product = Product.objects.get(id=item_id)
         qty = item_data
         inventory = product.inventory - qty
         if inventory == 0:
             product.in_stock = False
         product.save()
         
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile   
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(
                profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

   
    
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)