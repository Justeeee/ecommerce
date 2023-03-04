from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet

from apps.product.models import Product, Shop, Cart
from apps.product.models.cart import Liked
# from apps.product.models.sales import ProductSales
from apps.user.models import User


class ProductFilter(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

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


class LikedFilter(FilterSet):
    class Meta:
        model = Liked
        fields = ['user', 'product']

#
# class SalesFilter(FilterSet):
#     class Meta:
#         model = ProductSales
#         fields = ['user', 'month', 'total_sold']
