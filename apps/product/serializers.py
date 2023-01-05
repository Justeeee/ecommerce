from rest_framework.serializers import ModelSerializer

from apps.product.models.category import Category
from apps.product.models.product import Product
from apps.product.models.shop import Shop


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'category','information')

class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','name', 'info')
