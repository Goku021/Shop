from django.contrib import admin
from .models import Product, Category


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'available', 'category']
    list_filter = ['price', 'created', 'category', 'available']
    list_editable = ['available', 'price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
