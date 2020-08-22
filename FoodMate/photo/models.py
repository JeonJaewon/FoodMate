from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone

class Category(models.Model):
    food = models.CharField(max_length=50)

    def __str__(self):
        return self.food


FOOD_CHOICES = [
    ('fruit', '과일'),
    ('vegetable', '채소'),
    ('meat', '정육'),
    ('dairy', '계란/유제품'),
    ('fish', '수산/건어물'),
    ('main_food', '쌀/김치/반찬'),
    ('bakery', '베이커리'),
    ('dessert', '디저트/음료'),
    ('health_food', '가공/건강식품'),
    ('household', '생활용품'),
]

FlAG = [
    ('모집 중', '모집 중'),
    ('모집 완료', '모집 완료'),
]

class Photo(models.Model):
    # 유저
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')
    # 제목
    title = models.CharField(max_length=13, default = '')
    # 내용
    text = models.TextField(max_length=180, default = '')
    # 지역 --> 지도에서 가져오나요? 사용자가 입력하고, 지도는 위치 보여주기용인듯 합니다!
    area = models.TextField(max_length=15, default = '')
    # 카테고리
    category = models.CharField(max_length=50, choices=FOOD_CHOICES, default = '')
    # 개수
    count = models.IntegerField(default=0)
    # 금액
    money = models.IntegerField(default=0)
    # 작성 시간
    created = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated = models.DateTimeField(auto_now=True)
    # 계산한 시간
    time_now = ''

    # 위도, 경도
    lat = models.TextField(default='')
    lng = models.TextField(default='')

    # 찜
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_post', blank=True)
    # url
    url = models.URLField(default='')
    # 거래 유무
    deal = models.CharField(max_length=50, choices=FlAG, default='Y')

    def __str__(self):
        return "text : " + self.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self, id])

    def created_string(self):
        time = timezone.now() - self.updated

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = timezone.now().date() - self.updated.date()
            return str(time.days) + '일 전'
        else:
            return self.updated


# Photo에 삽입된 이미지
class InsertedImage(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="inserted_image")
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.photo.title

#댓글 모델
class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments', null=True)
    #현재 로그인한 유저
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="comments")
    #댓글 내용
    text = models.TextField(max_length=300, default="")
    # 댓글 작성 시, 자동으로 댓글 작성한 날짜 저장
    created = models.DateTimeField(auto_now_add=True)
    # 댓글 수정 시, 자동으로 댓글 수정한 날짜 저장
    updated = models.DateTimeField(auto_now=True)
    # 대댓글 기능 구현 위해 대댓글 작성할 특정 댓글 선택
    # parentComment = models.ForeignKey("self", related_name='reply', on_delete=models.CASCADE,null=True, blank=True, default="")

    def __str__(self):
        return f"{self.username}님의 댓글"

    def created_string(self):
        time = timezone.now() - self.updated

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = timezone.now().date() - self.updated.date()
            return str(time.days) + '일 전'
        else:
            return self.updated

class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="re_comment")
    text = models.TextField(max_length=300, default="")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def created_string(self):
        time = timezone.now() - self.updated

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = timezone.now().date() - self.updated.date()
            return str(time.days) + '일 전'
        else:
            return self.updated