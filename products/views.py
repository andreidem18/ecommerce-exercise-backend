from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from products.serializer import ProductSerializer
from .models import Product
from cart.models import Cart
from cart.serializer import CartSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products(request):
    data = dict()
    if request.query_params:
        for k, v in request.query_params.items():
            data[k] = v
    products = Product.objects.filter(**data)
    serialized = ProductSerializer(products, many=True)
    return Response(status=status.HTTP_200_OK, data = serialized.data)


@api_view(['GET'])
def product_detail(request, id):
    product = Product.objects.get(id=id)
    serialized = ProductSerializer(product)
    return Response(status=status.HTTP_200_OK, data = serialized.data)



class AddToCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('product', 'quantity')

@swagger_auto_schema(methods=['post'], request_body=AddToCartSerializer)
@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    product = Product.objects.get(id=request.data['product'])
    cart = Cart.objects.create(user=user, product=product, quantity=request.data['quantity'])
    serialized = CartSerializer(cart)
    return Response(status=status.HTTP_200_OK, data = serialized.data)
