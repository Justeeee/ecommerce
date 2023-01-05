from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register('category', CategoryModelViewSet, 'category')
router.register('product', ProductModelViewSet, 'product')

urlpatterns = [
    path('', include(router.urls)),
]