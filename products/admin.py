from django.contrib import admin
from .models import Product, Category


# Setting Admin models for admin config
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CatergoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Registering models for the admin tool
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CatergoryAdmin)
