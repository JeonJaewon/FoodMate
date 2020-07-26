from django.urls import path
from .views import popup
from .views import index
urlpatterns = [
    path('', index),
    path('popup/', popup, name='popup'),
]