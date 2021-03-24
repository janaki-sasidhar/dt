from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    logged_in_firsttime = models.BooleanField('logged_in_firsttime',default=False)
    realm = models.CharField('realm',max_length=100,null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email



class Notes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
