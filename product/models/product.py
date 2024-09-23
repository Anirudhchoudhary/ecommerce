from django.db import models


from common.models import Image
from product.models import Price


class Product(models.Model):
    is_active = models.BooleanField(default=True, help_text="Is product active.")
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=126)
    description = models.TextField()


    def __str__(self):
        return f"{self.name} | {self.id}"
