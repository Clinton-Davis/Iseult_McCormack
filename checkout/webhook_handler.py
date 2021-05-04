from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime
from .models import Order, OrderLineItem, Delivary
from shop.models import Product
from profiles.models import UserProfile
import json
import time




class StripeWH_Handler:

    def __init__(self, request):

        self.request = request


    def _shopping_confirmation_email(self, order):
        """Send a confirmation email"""
        
        customer_email = order.email
        subject = 'Iseult McCormack Creations Confirmation Email.'
        body = render_to_string(
            'checkout\emails\shopping_email_body.txt',
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
    def _email_order(self, order):
        """Send a confirmation email"""
        order_email = settings.DEFAULT_FROM_EMAIL,
        subject = 'New Order From WebSite!'
        body = render_to_string(
            'checkout\emails\order_emails.txt',
            {'order': order,
             'lineitems': OrderLineItem,
             'contact_email': settings.DEFAULT_FROM_EMAIL,
             })
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [order_email],
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
        stripe_receipt = intent.charges.data[0].receipt_url
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        billing_details = intent.charges.data[0].billing_details
        
        order_exists = False
        attempt = 1
        while attempt <= 60:
            try:
                order = Order.objects.get(stripe_pid=pid)
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            order.stripe_receipt = stripe_receipt
            order.save()
            
            self._shopping_confirmation_email(order)
            self._email_order(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified in database',
                status=200)
        
    def handle_payment_intent_payment_failed(self, event):
        """ Handles payment failing events"""
        return HttpResponse(
            content=f'Webhook failed revieved: {event["type"]}',
            status=200
        )