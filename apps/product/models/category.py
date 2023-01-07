from uuid import uuid4

from django.db.models import CharField, SlugField, CASCADE, UUIDField
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True, )
    slug = SlugField(max_length=255, unique=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        i = Category.objects.filter(slug=self.slug).count()
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += f'{i}'

        super().save(force_insert, force_update, using, update_fields)
