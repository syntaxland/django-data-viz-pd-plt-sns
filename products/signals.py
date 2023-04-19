from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Product

# @receiver(pre_save, sender=Product)
# def set_slug(sender, instance, **kwargs):
#     instance.slug = slugify(instance.name)

@receiver(pre_save, sender=Product)
def update_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
