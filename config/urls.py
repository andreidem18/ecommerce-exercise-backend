"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from cart.views import buy_cart, empty_cart, get_cart, change_quantity, remove_item
from categories.views import get_categories
from orders.views import get_orders
from products.views import add_to_cart, products
from users.views import UserViewSet



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('categories/', get_categories),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('orders', get_orders),
    path('cart/empty_cart', empty_cart),
    path('cart/<id>/remove_item', remove_item),
    path('cart/<item_id>/change_quantity', change_quantity),
    path('cart/buy', buy_cart),
    path('cart/', get_cart),
    path('products/add_to_cart/',add_to_cart),
    path('products/', products),
    path('admin/', admin.site.urls),
] + router.urls
