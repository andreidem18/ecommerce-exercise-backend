from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from orders.models import Order
from orders.serializer import OrderSerializer
from .models import User
from .serializer import UserSerializer, CreateUserSerializer
        

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return super().get_serializer_class()
    
    
    def get_permissions(self):
        if self.request.method == 'POST': permissions = (AllowAny, )
        else: permissions = (IsAuthenticated, )
        return [permission() for permission in permissions]
    
    
    def create(self, request):
        user = User.objects.create(
            email = request.data['email'], first_name = request.data['first_name'], last_name = request.data['last_name']
        )
        user.set_password(request.data['password'])
        serialized = CreateUserSerializer(user)
        return Response(status = status.HTTP_201_CREATED, data = serialized.data)
    
    
    @action(methods=['GET'], detail=False)
    def myself(self, request):
        user = request.user
        serialized = UserSerializer(user)
        return Response(status=status.HTTP_200_OK, data = serialized.data)
    
    @swagger_auto_schema(methods=['post'], request_body=None)
    @action(methods=['POST'], detail=False)
    def buy_cart(self, request):
        user = request.user
        orders = list()
        for item in user.cart.all():
            order = Order.objects.create(product=item.product, user=user, quantity=item.quantity)
            orders.append(order)
        user.cart.all().delete()
        serialized = OrderSerializer(orders, many=True)
        return Response(status=status.HTTP_200_OK, data = serialized.data)
    
