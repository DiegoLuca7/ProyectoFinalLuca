from django.contrib import admin

from appcoder.models import Products, ImageProducts

from appcoder.models import Category

from orders.models import Order


class ImageProductAdmin(admin.TabularInline):
    model = ImageProducts


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "talle", "price", "stock")
    list_filter = ("stock", "price")
    list_per_page = 3
    inlines = [
        ImageProductAdmin
    ]
    

admin.site.register(Category)

admin.site.register(Order)
