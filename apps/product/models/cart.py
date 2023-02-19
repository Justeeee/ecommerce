from django.db.models import Model, ForeignKey, CASCADE, SmallIntegerField


class Cart(Model):
    product = ForeignKey('product.Product', CASCADE)
    user = ForeignKey('user.User', CASCADE)
    quantity = SmallIntegerField(default=1)

    @property
    def total_price(self):
        return sum(self.user.cart_set.values_list('product__price', flat=True))

