from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from bot.validators import phone_number_validator


class CustomUser(models.Model):
    full_name = models.CharField(_("full name"), blank=True, max_length=255)
    username = models.CharField(_("username"), blank=True, max_length=255, null=True)
    phone_number = models.CharField(_("phone number"), blank=True, unique=True, validators=[phone_number_validator],
                                    max_length=20)
    user_lang = models.CharField(_("user language"), blank=True, null=True, max_length=10)
    telegram_id = models.CharField(_("telegram id"), blank=True, null=True, max_length=255, unique=True)
    tg_username = models.CharField(_("telegram username"), blank=True, null=True, max_length=255, unique=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    