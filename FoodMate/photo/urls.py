from django.urls import path, include
from django.conf.urls.static import static
from .views import PhotoDetail, photo_list, photo_search, PhotoLike, my_activity, comment_photo, written_photo, pagination_ajax
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
    path("delete/<int:pk>/", views.delete, name='delete'),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name='detail'),
    path("detail/<int:pk>/edit", views.edit, name='edit'),
    path("search/", photo_search, name='search'),
    path("pagination_ajax/", views.pagination_ajax, name='pagination_ajax'),
    path("category_ajax/", views.category_ajax, name='category_ajax'),
    path("delete_comment/<int:recomment_id>/<int:photo_id>", views.delete_comment, name='delete_comment'),
    path('create_recomment/<int:comment_id>/<int:photo_id>', views.create_recomment, name="create_recomment"),
    path('deal/<int:photo_id>',views.deal, name='deal'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)