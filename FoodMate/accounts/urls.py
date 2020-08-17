from django.urls import path
from .views import login, signup, agreement, profile, update, login_update,logout ,security, delete
app_name = "accounts"

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('basic_info/', update, name='basic_info'),
    path('login_info/', login_update, name='login_info'),
    path('security/', security, name='security'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('delete/', delete, name='delete'),
    path('agreement/', agreement, name='agreement'),
    path('signup/', signup, name='signup')
]