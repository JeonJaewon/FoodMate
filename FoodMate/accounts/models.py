from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='아이디(이메일)')
    nickname = models.CharField(max_length=8, verbose_name='닉네임')