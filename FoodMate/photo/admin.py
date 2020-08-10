from django.contrib import admin
from .models import Photo, InsertedImage, Comment

admin.site.register(Photo)
admin.site.register(InsertedImage)
admin.site.register(Comment)