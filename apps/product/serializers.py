from rest_framework.serializers import ModelSerializer

from apps.product.models import Cart
from apps.product.models.cart import Liked
from apps.product.models.category import Category, SubCategory
from apps.product.models.product import Product
# from apps.product.models.sales import ProductSales
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
        fields = ('id', 'name', 'price', 'count', 'subcategory', 'information', 'shop', 'delivery_time')


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'info', 'photo')


class ShopProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartModelSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class LikedModelSerializer(ModelSerializer):
    class Meta:
        model = Liked
        fields = '__all__'

#
# class SalesModelSerializer(ModelSerializer):
#     class Meta:
#         model = ProductSales
#         fields = ['user', 'month', 'total_sold']
