from rest_framework.viewsets import ModelViewSet

from apps.product.filter import ProductFilter, ShopFilter, ShopProductsFilter, CartFilter
from apps.product.models import Category, Product, Shop, Cart
from apps.product.models.category import SubCategory
from apps.product.serializers import CategoryModelSerializer, ProductModelSerializer, ShopModelSerializer, \
    SubCategoryModelSerializer, ShopProductsSerializer, CartModelSerializer


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

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(user=self.request.user).first
