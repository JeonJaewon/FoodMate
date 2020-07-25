from django.urls import path
from .views import popup
urlpatterns = [
    path('', popup)
]