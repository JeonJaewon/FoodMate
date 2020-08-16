from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='아이디(이메일)')
    nickname = models.CharField(max_length=8, verbose_name='닉네임')
    user_photo = models.ImageField(upload_to='user_photo/%Y/%m/%d', blank=True)
    living = models.CharField(max_length=200, verbose_name='동네', default='')
