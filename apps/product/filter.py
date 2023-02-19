from django_filters.rest_framework import FilterSet

from apps.product.models import Product, Shop, Cart
from apps.product.serializers import ProductModelSerializer
from apps.user.models import User


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'subcategory', 'shop']


class ShopFilter(FilterSet):
    class Meta:
        model = Shop
        fields = ['name', ]


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'username']


class ShopProductsFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['shop_id', ]


class CartFilter(FilterSet):
    class Meta:
        model = Cart
        fields = ['user', 'product']
