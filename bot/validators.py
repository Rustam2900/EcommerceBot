import re
from django.core.exceptions import ValidationError


def phone_number_validator(value):
    regex = re.compile(r"^\+998[012345789][0-9]{8}$")
    if not regex.match(value):
        raise ValidationError("Enter a valid phone number in the format +998XXXXXXXXX.")

    if len(value) > 20:
        raise ValidationError("Phone number cannot be longer than 20 characters.")
