import math

from django.db.models import Model, DateField, IntegerField, ForeignKey, CASCADE

from apps.product.models import Product
from apps.user.models import User


# class ProductSales(Model):
#     user = ForeignKey('user.User', CASCADE)
#     products = Product.objects.all()
#
#     def save(self, *args, **kwargs):
#         if self.id:
#             total = 0.00
#             products = self.products.all()
#             total = math.fsum(pro.price * pro.count for pro in products)
#             self.total = total
#         super(ProductSales, self).save(*args, **kwargs)