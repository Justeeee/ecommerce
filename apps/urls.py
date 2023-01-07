from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryModelViewSet, ProductModelViewSet, ShopModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('category', CategoryModelViewSet, 'category')
router.register('shop', ShopModelViewSet, 'shop')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('apps.user.urls')),
]
