
from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = RichTextField(blank=True, null=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    sales_items = models.BooleanField(default=False)
    feat_item = models.BooleanField(default=False)
    item_code = models.CharField(max_length=25, null=False,
                            blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'pk': self.pk})

    @property
    def productcomments(self):
        return self.productcomment_set.all()

    @property
    def productcomments_count(self):
        return self.productcomment_set.all().count

    # @property
    # def rating_ave(self):
    #     """Gets the average rating on product"""
    #     all_ratings = self.productcomment_set.all().aggregate(Avg('rating'))
    #     self.rating = all_ratings['rating__avg'] or 0
    #     self.save()
    #     return all_ratings['rating__avg']

    # @property
    # def view_count(self):
    #     return self.productview_set.all().count()
    
    
class productComment(models.Model):
    """To be able to comment on a Product"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class ProductView(models.Model):
    """Keeps track of views """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name