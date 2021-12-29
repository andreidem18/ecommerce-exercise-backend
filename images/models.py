from django.db import models
from products.models import Product

class Image(models.Model):
    url = models.URLField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='images')
    
    def __str__(self):
        return self.url
