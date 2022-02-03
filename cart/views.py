from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from cart.serializer import CartSerializer
from orders.models import Order
from .models import Cart
from orders.serializer import OrderSerializer

@api_view(['POST'])
def buy_cart(request):
    user = request.user
    orders = list()
    for item in user.cart.all():
        order = Order.objects.create(product=item.product, user=user, quantity=item.quantity)
        orders.append(order)
    user.cart.all().delete()
    serialized = OrderSerializer(orders, many=True)
    return Response(status=status.HTTP_200_OK, data = serialized.data)

@api_view(['GET'])
def get_cart(request):
    user = request.user
    serialized = CartSerializer(user.cart, many=True)
    return Response(status=status.HTTP_200_OK, data=serialized.data)


class QuantitySerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('quantity',)

@swagger_auto_schema(methods=['put'], request_body=QuantitySerializer)
@api_view(['PUT'])
def change_quantity(request, item_id):
    item = Cart.objects.get(id=item_id)
    item.quantity = request.data['quantity']
    item.save()
    serialized = CartSerializer(item)
    return Response(status=status.HTTP_200_OK, data=serialized.data)


@api_view(['DELETE'])
def remove_item(request, id):
    Cart.objects.get(id=id).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def empty_cart(request):
    request.user.cart.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
