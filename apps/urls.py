from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryModelViewSet, ProductModelViewSet, ShopModelViewSet, SubCategoryModelViewSet, \
    ShopProductsViewSet, LikedView, add_product_to_cart
from apps.user.views import ClientModelViewSet, MerchantModelViewSet, UserModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('shop', ShopModelViewSet, 'shop')
router.register('category', CategoryModelViewSet, 'category')
router.register('subcategory', SubCategoryModelViewSet, 'subcategory')
router.register('shop_products', ShopProductsViewSet, 'shop_products')
router.register('liked', LikedView, 'liked')
router.register('client', ClientModelViewSet, 'client')
router.register('merchant', MerchantModelViewSet, 'merchant')
router.register('user', UserModelViewSet, 'user')



urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('apps.user.urls')),
    path('add_product_to_cart', add_product_to_cart, name='add_product_to_cart'),
]
