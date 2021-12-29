from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.serializer import OrderSerializer

@api_view(['GET'])
def get_orders(request):
    user = request.user
    serialized = OrderSerializer(user.orders, many=True)
    return Response(status=status.HTTP_200_OK, data=serialized.data)
