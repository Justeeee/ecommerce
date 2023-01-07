import django_filters
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.product.models.category import Category
from apps.product.models.product import Product
from apps.product.models.shop import Shop
from apps.product.serializers import CategoryModelSerializer, ProductModelSerializer, ShopModelSerializer
from product.filter import ProductFilter, ShopFilter


# Create your views here.
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
