from django.contrib import admin
from .models import Photo, InsertedImage, Comment, ReComment
from .forms import InsertedImageForm

admin.site.register(Photo)
# admin.site.register(InsertedImage)
admin.site.register(Comment)
admin.site.register(ReComment)

@admin.register(InsertedImage)
class CountryAmin(admin.ModelAdmin):
    form = InsertedImageForm

