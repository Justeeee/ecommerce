from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.product.models.category import Category
from apps.product.models.product import Product
from apps.product.serializers import CategoryModelSerializer, ProductModelSerializer


# Create your views here.
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

