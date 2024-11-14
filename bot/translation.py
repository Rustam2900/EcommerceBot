from modeltranslation.translator import TranslationOptions, register
from bot import models


@register(models.CustomUser)
class CustomUserTranslation(TranslationOptions):
    fields = ('full_name', 'username')


@register(models.Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(models.Product)
class ProductTranslation(TranslationOptions):
    fields = ('name', 'color', 'description')


@register(models.Order)
class ProductTranslation(TranslationOptions):
    fields = ('address',)


@register(models.CartItem)
class ProductTranslation(TranslationOptions):
    fields = ('color',)
