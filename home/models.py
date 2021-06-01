from django.db import models
from ckeditor.fields import RichTextField

class Home(models.Model):
      class Meta:
        verbose_name_plural = 'Home'
      heading = models.CharField(max_length=254)
      bio = RichTextField(blank=True, null=True)
    
      def __str__(self):
        return self.heading
      
      
class About(models.Model):
      heading = models.CharField(max_length=254)
      bio = RichTextField(blank=True, null=True)
    
      def __str__(self):
        return self.heading
      
      
class Scarfs(models.Model):
      class Meta:
        verbose_name_plural = 'Scarfs'
        
      heading = models.CharField(max_length=254)
      discription = RichTextField(blank=True, null=True)
    
      def __str__(self):
        return self.heading
      
      
class Paintings(models.Model):
      class Meta:
        verbose_name_plural = 'Paintings'
        
      heading = models.CharField(max_length=254)
      discription = RichTextField(blank=True, null=True)
    
      def __str__(self):
        return self.heading
      
class ImageGallery(models.Model):
      name = models.CharField(max_length=150)
      image = models.ImageField(upload_to='gallery/', blank=False)
      
      def __str__(self):
        return self.name
        