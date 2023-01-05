import django_filters

from apps.product.models.product import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']