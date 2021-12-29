from rest_framework.serializers import ModelSerializer
from .models import Product
from images.models import Image

class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'url')

class ProductSerializer(ModelSerializer):
    images = ImagesSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'images')