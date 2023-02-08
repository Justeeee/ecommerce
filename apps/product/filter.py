from django_filters.rest_framework import FilterSet

from apps.product.models import Product, Shop


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'subcategory', 'shop']


class ShopFilter(FilterSet):
    class Meta:
        model = Shop
        fields = ['name', ]

# TODO add user filter