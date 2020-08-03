from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    ('Y', 'yes'),
    ('N', 'no'),
]


class Photo(models.Model):
    # 유저
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    # 제목
    title = models.CharField(max_length=50)
    # 내용
    text = models.TextField(blank=True)
    # 지역 --> 지도에서 가져오나요?

    # 카테고리
    category = models.CharField(max_length=50, choices=FOOD_CHOICES)
    # 개수
    count = models.IntegerField(default=0)
    # 금액
    money = models.IntegerField(default=0)
    # 작성 시간
    created = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated = models.DateTimeField(auto_now=True)
    # 위도, 경도
    # location = models.ForeignKey(, on_delete=models.CASCADE, related_name='user')
    # 찜
    like = models.ManyToManyField(User, related_name='like_post', blank=True)
    # 댓글 수
    comment = models.ManyToManyField(User, related_name='favorite_post', blank=True)
    # url
    #url = models.CharField(max_length=200)
    # 거래 유무
    deal = models.CharField(max_length=50, choices=FlAG)

    def __str__(self):
        return "text : " + self.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self, id])


class Image(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="images_photo")
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.photo.title

#댓글 모델
class Comment(models.Model):
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE, related_name='comments')
    #현재 로그인한 유저
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="comments")
    #댓글 내용
    text = models.TextField(default="")
    # 댓글 작성 시, 자동으로 댓글 작성한 날짜 저장
    created = models.DateTimeField(auto_now_add=True)
    # 댓글 수정 시, 자동으로 댓글 수정한 날짜 저장
    updated = models.DateTimeField(auto_now=True)
    # 대댓글 기능 구현 위해 대댓글 작성할 특정 댓글 선택
    parentComment = models.ForeignKey("self", on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"{self.username}님의 댓글"