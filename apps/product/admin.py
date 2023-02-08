from django.contrib import admin

from apps.product.models import Product, Category, Shop , SubCategory

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Shop)

