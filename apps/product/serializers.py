from rest_framework.serializers import ModelSerializer

from apps.product.models.category import Category, SubCategory
from apps.product.models.product import Product
from apps.product.models.shop import Shop


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class SubCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name',)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'subcategory', 'information', 'shop')


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'info')

class ProductOfShopSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name' 'info', 'shop')