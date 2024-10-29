from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from bot.models import CustomUser


@admin.register(CustomUser)
class WhyUsAdmin(TranslationAdmin):
    list_display = ('id', 'username', 'email', 'phone_number')
    list_display_links = ('id', 'username', 'email', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')
