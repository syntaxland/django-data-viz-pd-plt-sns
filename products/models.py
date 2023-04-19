from django.db import models
from django.utils.text import slugify
# from django.db.models.signals import pre_save
# from django.dispatch import receiver

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text='in US dollars $')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.created.strftime('%a, %d/%m/%Y %H:%M:%S %Z')}"

    # Auto-generate slug
    def save(self, *args, **kwargs):
        if not self.id:
            # Generate slug for new instances only
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# # Define signal handler to update slug field
# def update_slug(sender, instance, **kwargs):
#     instance.slug = slugify(instance.name)
# # Connect pre_save signal to Product
# pre_save.connect(update_slug, sender=Product)

# @receiver(pre_save, sender=Product)
# def set_slug(sender, instance, **kwargs):
#     instance.slug = slugify(instance.name)
