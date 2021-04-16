from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
      heading = models.CharField(max_length=254)
      bio = RichTextField(blank=True, null=True)
    
      def __str__(self):
        return self.heading
        