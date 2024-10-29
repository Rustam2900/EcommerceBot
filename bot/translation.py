from modeltranslation.translator import TranslationOptions, register
from bot import models


@register(models.CustomUser)
class WhyUsTranslation(TranslationOptions):
    fields = ('full_name', 'username')
