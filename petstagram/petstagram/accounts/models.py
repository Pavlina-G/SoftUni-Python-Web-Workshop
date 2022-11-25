from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from petstagram.core.model_mixins import ChoicesEnumMixin
from petstagram.core.validators import validate_only_letters

'''
Naming the User model:
- Something generic - AppUser, ApplicationUser
- Prefix with application name - PetstagramUser
'''


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


# print(Gender.choices())
# print(Gender.max_len())

class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=Gender.max_len(),
        choices=Gender.choices(),
    )

    # is_verified = models.BooleanField(
    #     default=False,
    # )

    # Users log in with `email`
    # USERNAME_FIELD = 'email'
