from django.urls import path
from .views import login, signup, agreement
app_name = "accounts"

urlpatterns = [
    path('login/', login, name='login'),
    path('agreement/', agreement, name='agreement'),
    path('signup/', signup, name='signup')
]