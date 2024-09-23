from django.db import models

class Price(models.Model):

    class Currency(models.IntegerChoices):
        RUPEES = 0

    min_price = models.IntegerField(help_text="Min price for product")
    max_price = models.IntegerField(help_text="Max price for product")
    currency = models.IntegerField(choices=Currency, default=Currency.RUPEES)
