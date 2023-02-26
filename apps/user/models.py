from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices


# Create your models here.
class User(AbstractUser):
    phone = CharField(max_length=25)

    class Type(TextChoices):
        MERCHANT = 'merchant', 'Sotuvchi'
        CLIENT = 'client', 'Haridor'

    type = CharField(max_length=25, choices=Type.choices, default=Type.CLIENT)
