from django.db import models
from products.models import Product
from users.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='cart')
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.user
