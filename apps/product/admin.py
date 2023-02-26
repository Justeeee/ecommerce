from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin

from apps.product.models import Product, Category, Shop , SubCategory
from apps.product.models.product import ProductImages

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Shop)



class ProductImagesTabularInline(TabularInline):
    model = ProductImages
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = ('slug',)
    inlines = (ProductImagesTabularInline,)
