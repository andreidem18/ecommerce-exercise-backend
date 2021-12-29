from rest_framework.serializers import ModelSerializer

from products.serializer import ProductSerializer
from .models import Order

class OrderSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'product', 'quantity', 'purchase_date')