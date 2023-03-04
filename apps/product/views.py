from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from apps.product.filter import ProductFilter, ShopFilter, ShopProductsFilter, LikedFilter, CartFilter
from apps.product.models import Category, Product, Shop, Cart
from apps.product.models.cart import Liked
from apps.product.models.category import SubCategory
# from apps.product.models.sales import ProductSales
from apps.product.serializers import CategoryModelSerializer, ProductModelSerializer, ShopModelSerializer, \
    SubCategoryModelSerializer, ShopProductsSerializer, LikedModelSerializer, CartModelSerializer


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


class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    filterset_class = CartFilter


# class SalesView(ModelViewSet):
#     queryset = ProductSales.objects.all()
#     serializer_class = SalesModelSerializer
