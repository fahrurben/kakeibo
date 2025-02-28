from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    birthday = models.DateField(_('birthday'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'birthday')

    def __str__(self):
        return self.email