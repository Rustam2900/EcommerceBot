from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from bot.models import CustomUser, Category, Order, Product, CartItem


@admin.register(CustomUser)
class CustomUserAdmin(TranslationAdmin):
    list_display = ('id', 'username', 'phone_number')
    list_display_links = ('id', 'username', 'phone_number')
    search_fields = ('username', 'phone_number')



@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'category', 'price', 'size', 'color', 'delivery_time')
    list_filter = ('category', 'size', 'color')
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ('user', 'status', 'total_price', 'created_at','phone_number')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'address', 'phone_number')


@admin.register(CartItem)
class CartItemAdmin(TranslationAdmin):
    list_display = ('user', 'product', 'quantity', 'is_visible', 'created_at')
    list_filter = ('user', 'product', 'is_visible')
    search_fields = ('user__username', 'product__name')

