from django.db import models
from django.contrib.auth.models import AbstractUser
from photo.models import Comment
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='아이디(이메일)')
    nickname = models.CharField(max_length=8, verbose_name='닉네임')
    user_photo = models.ImageField(upload_to='user_photo/%Y/%m/%d', blank=True)
    living = models.CharField(max_length=200, verbose_name='동네', default='')


class Alarm(models.Model):
    # 알람을 받을 유저
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="alarms")
    # 알람의 실질적 내용 (댓글)
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)
