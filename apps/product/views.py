from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from apps.product.filter import ProductFilter, ShopFilter, ShopProductsFilter, CartFilter, LikedFilter
from apps.product.models import Category, Product, Shop, Cart
from apps.product.models.cart import Liked
from apps.product.models.category import SubCategory
from apps.product.serializers import CategoryModelSerializer, ProductModelSerializer, ShopModelSerializer, \
    SubCategoryModelSerializer, ShopProductsSerializer, CartModelSerializer, LikedModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filterset_class = ProductFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['price']


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer
    filterset_class = ShopFilter


class ShopProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ShopProductsSerializer
    filterset_class = ShopProductsFilter


class LikedView(ModelViewSet):
    queryset = Liked.objects.all()
    serializer_class = LikedModelSerializer
    filterset_class = LikedFilter


def add_product_to_cart(request):
    product_id = request.POST.get('product_id')
    customer_id = request.POST.get('customer_id')
    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(
        customer_id=customer_id,
        product_id=product_id
    )

    if created:
        cart.quantity += 1

        if cart.quantity > product.stock:
            return  # raise error

        cart.save()

        product.stock -= cart.quantity
        product.save()
    else:
        return  # raise error
