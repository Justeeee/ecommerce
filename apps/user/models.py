from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


# Create your models here.
class User(AbstractUser):
    phone = CharField(max_length=25)
