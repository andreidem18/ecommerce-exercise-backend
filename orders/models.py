from django.db import models
from products.models import Product
from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.product
    