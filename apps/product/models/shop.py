from django.db.models import CharField, SlugField, TextField
from django.utils.text import slugify

from apps.shared.models import BaseModel


class Shop(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, blank=True, null=True)
    info = TextField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Shop.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)
