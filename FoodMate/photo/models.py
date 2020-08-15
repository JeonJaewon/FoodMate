from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.conf import settings

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
    ('Y', '모집중'),
    ('N', '모집완료'),
]


class Photo(models.Model):
    # 유저
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')
    # 제목
    title = models.CharField(max_length=13, default = '')
    # 내용
    text = models.TextField(max_length=180, default = '')
    # 지역 --> 지도에서 가져오나요? 사용자가 입력하고, 지도는 위치 보여주기용인듯 합니다!
    area = models.TextField(max_length=180, default = '')
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

    # location = models.ForeignKey(, on_delete=models.CASCADE, related_name='user')
    # 찜
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_post', blank=True)
    # 댓글 수
    comment = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_post', blank=True)
    # url
    url = models.URLField(default = '')
    # 거래 유무
    deal = models.CharField(max_length=50, choices=FlAG, default='Y')

    def __str__(self):
        return "text : " + self.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self, id])

# Photo에 삽입된 이미지
class InsertedImage(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="inserted_image")
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.photo.title

#댓글 모델
class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    #현재 로그인한 유저
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="comments")
    #댓글 내용
    text = models.TextField(max_length=200, default="")
    # 댓글 작성 시, 자동으로 댓글 작성한 날짜 저장
    created = models.DateTimeField(auto_now_add=True)
    # 댓글 수정 시, 자동으로 댓글 수정한 날짜 저장
    updated = models.DateTimeField(auto_now=True)
    # 대댓글 기능 구현 위해 대댓글 작성할 특정 댓글 선택
    # parentComment = models.ForeignKey("self", on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"{self.username}님의 댓글"