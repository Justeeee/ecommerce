from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryModelViewSet, ProductModelViewSet, ShopModelViewSet, SubCategoryModelViewSet, \
    ShopProductsViewSet, CartView

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('category', CategoryModelViewSet, 'category')
router.register('subcategory', SubCategoryModelViewSet, 'subcategory')
router.register('shop', ShopModelViewSet, 'shop')
router.register('shop_products', ShopProductsViewSet, 'shop_products')
router.register('cart', CartView, 'cart')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('apps.user.urls')),
]
