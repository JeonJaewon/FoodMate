from django.urls import path
from .views import login, signup, agreement, profile, update
app_name = "accounts"

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('basic_info/', update, name='basic_info'),
    path('login/', login, name='login'),
    path('agreement/', agreement, name='agreement'),
    path('signup/', signup, name='signup')
]