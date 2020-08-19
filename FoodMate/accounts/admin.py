from django.contrib import admin
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
from .models import Alarm

admin.site.register(get_user_model())
admin.site.register(Alarm)
