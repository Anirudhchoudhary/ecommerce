from django.contrib import admin

# Register your models here.
from product.models import Product, Price, Rating


class ProductAdmin(admin.ModelAdmin):
    model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Rating)
admin.site.register(Price)