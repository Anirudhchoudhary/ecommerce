from django.db import models

from product.models import Product

class Rating(models.Model):
    number = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} | {self.id}"
