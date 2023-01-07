from rest_framework.viewsets import ModelViewSet

from apps.product.models import Category, Product, Shop
from apps.product.serializers import CategoryModelSerializer, ProductModelSerializer, ShopModelSerializer
from apps.product.filter import ProductFilter, ShopFilter


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filterset_class = ProductFilter


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer
    filterset_class = ShopFilter
