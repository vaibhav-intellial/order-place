from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
    models.Product.save
