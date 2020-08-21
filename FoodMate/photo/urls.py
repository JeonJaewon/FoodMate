from django.urls import path, include
from django.conf.urls.static import static

from .views import PhotoDetail, photo_list, photo_search, PhotoLike, my_activity, comment_photo, written_photo,call_ajax
from django.conf import settings

from . import views

app_name = "photo"
urlpatterns = [
    path('', photo_list, name='list'),
    path("my_activity/", views.my_activity, name='my_activity'),
    path("written_photo/", views.written_photo, name='written_photo'),
    path("like_photo/", views.like_photo, name='like_photo'),
    path("comment_photo/", views.comment_photo, name='comment_photo'),
    path("like/<int:photo_id>/", PhotoLike.as_view(), name='like'),
    path("create/", views.create, name='create'),
    path("delete/<int:pk>/",views.delete, name='delete'),
    path("detail/<int:pk>/",PhotoDetail.as_view(), name='detail'),
    path("edit/<int:pk>/",views.edit, name='edit'),
    path("search/", photo_search, name='search'),
    path("call_ajax/", call_ajax, name='call_ajax'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)