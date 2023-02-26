from django.db import transaction
from django.shortcuts import get_object_or_404
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


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer
    filterset_class = ShopFilter


class ShopProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ShopProductsSerializer
    filterset_class = ShopProductsFilter


class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    filterset_class = CartFilter

    @transaction.atomic
    def confirm_order(request, order_id):
        order = get_object_or_404(Cart, id=id)
        for line_item in order.line_items.all():
            product = line_item.product
            quantity = line_item.quantity
            product.available_inventory -= quantity
            product.save()
        # other order confirmation logic


class LikedView(ModelViewSet):
    queryset = Liked.objects.all()
    serializer_class = LikedModelSerializer
    filterset_class = LikedFilter
