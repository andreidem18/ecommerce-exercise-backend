from rest_framework.serializers import ModelSerializer
from cart.serializer import CartSerializer
from orders.serializer import OrderSerializer
from .models import User

class UserSerializer(ModelSerializer):
    cart = CartSerializer(read_only=True, many=True)
    orders = OrderSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'cart', 'orders')
        
class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
