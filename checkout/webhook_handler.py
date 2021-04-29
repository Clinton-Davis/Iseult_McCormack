from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime
from .models import Order, OrderLineItem
from shop.models import Product
from profiles.models import UserProfile
import json
import time


class StripeWH_Handler:

    def __init__(self, request):

        self.request = request


    def _send_shopping_confirmation_email(self, order):
        """Send a confirmation email"""

        customer_email = order.email

        subject = 'Iseult McCormack Creations Confirmation Email.'

        body = render_to_string(
            'checkout\emails\confirmation_email_body.txt',
            {'order': order,
             'lineitems': OrderLineItem,
             'contact_email': settings.DEFAULT_FROM_EMAIL,
             })
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False,
        )
        
    def handle_event(self, event):
        """Handles genric/unknow/unexpected events."""

        return HttpResponse(
            content=f'Unhandled Webhook revieved: {event["type"]}',
            status=200)


    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        grand_total = round(intent.charges.data[0].amount / 100, 2)
        print(intent)
       

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        profile = UserProfile.objects.get(user__username=username)
       
       
        
        # self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
        
    def handle_payment_intent_payment_failed(self, event):
        """ Handles payment failing events"""
        return HttpResponse(
            content=f'Webhook failed revieved: {event["type"]}',
            status=200
        )