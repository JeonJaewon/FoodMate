from django.contrib import admin
from .models import Photo, InsertedImage, Comment, ReComment

admin.site.register(Photo)
admin.site.register(InsertedImage)
admin.site.register(Comment)
admin.site.register(ReComment)