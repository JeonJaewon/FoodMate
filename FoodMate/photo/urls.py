from django.urls import path, include
from django.conf.urls.static import static
from .views import PhotoDelete, PhotoDetail, PhotoList
from django.conf import settings
from django.conf.urls import url

from . import views

app_name = "photo"
urlpatterns = [
    path("create/", views.create, name='create'),
    path("delete/<int:pk>/",PhotoDelete.as_view(), name='delete'),
    path("detail/<int:pk>/",PhotoDetail.as_view(), name='detail'),
    path("list/",PhotoList.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
