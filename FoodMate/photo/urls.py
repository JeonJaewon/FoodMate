from django.urls import path, include
from django.conf.urls.static import static
from .views import PhotoDelete, PhotoDetail, photo_list, photo_search
from django.conf import settings

from . import views

app_name = "photo"
urlpatterns = [
    path('', photo_list, name='list'),
    path("create/", views.create, name='create'),
    path("delete/<int:pk>/",PhotoDelete.as_view(), name='delete'),
    path("detail/<int:pk>/",PhotoDetail.as_view(), name='detail'),
    path("search/", photo_search, name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
