from django.conf import settings
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from shop.models import Product
from profiles.models import UserProfile
import datetime
import shortuuid
import uuid




class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='Orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(
        blank_label="Country *", blank=False, null=False)
    postcode = models.CharField(
        max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.IntegerField(null=False, default=0)
    order_total = models.IntegerField(null=False, default=0)
    grand_total = models.IntegerField(null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')
    stripe_receipt = models.URLField(
        max_length=254, null=False, blank=True, default='')
    
    def get_grand_total(self):
        return "{:.2f}".format(self.grand_total / 100)
    
    def get_delivery_cost(self):
        return "{:.2f}".format(self.delivery_cost / 100)
    
    def get_order_total(self):
        return "{:.2f}".format(self.order_total / 100)
    

    def _generate_order_number(self):
        """
        Generate a order number using date of creation and short uuid code.
        """
        u = uuid.uuid4()
        s = shortuuid.encode(u)
        shortuuid.decode(s) == u
        short = s[:3]
        d = datetime.datetime.now()
        date_code = d.strftime("%Y%m%d")   
        return date_code + short.upper()
    
    def update_total(self):
       
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        self.delivery_cost = self.delivery_cost
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
    
    def save(self, *args, **kwargs):
       
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=True, blank=False, 
                                on_delete=models.SET_NULL)
    product_size = models.CharField(
        max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.IntegerField(null=False, blank=False, editable=False)
    
    def save(self, *args, **kwargs):
        
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'Item codes {self.product.code} on order {self.order.order_number}'
    
    
class Delivary(models.Model):
        name = models.CharField(max_length=150, null=False, blank=False)
        code = models.CharField(max_length=2, null=False, blank=False)
        zone = models.IntegerField(null=False, blank=False, default=0)
        packet_price = models.IntegerField(null=False, blank=False, default=0)
        parcel_price = models.IntegerField(null=False, blank=False, default=0)
        
        def __str__(self):
            return self.name