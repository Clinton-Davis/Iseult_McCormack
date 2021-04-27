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
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.ForeignKey("Delivary", on_delete=models.SET_NULL,
                                     null=True, blank=True)
    order_total = models.IntegerField( null=False, default=0)
    grand_total = models.IntegerField( null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

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
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.delivery_cost
        else:
            self.delivery_cost = 0
        print(self.delivery_cost)
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set
        the order number if it hasn't been set already.
        """
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
        """
        Override the original save method to set
        the order number if it hasn't been set already.
        """
        
        self.lineitem_total = self.product.price.get_price * self.quantity
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