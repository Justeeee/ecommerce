import django_filters

from apps.product.models.product import Product
from apps.product.models.shop import Shop


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


class ShopFilter(django_filters.FilterSet):
    class Meta:
        model = Shop
        fields = ['name',]