from rest_framework.serializers import ModelSerializer
from products.serializer import ProductSerializer
from .models import Cart

class CartSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ('id', 'product', 'quantity')