from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from urllib.parse import urlparse
from .models import Photo, InsertedImage

from .forms import PhotoForm, ImageFormSet, InsertedImageForm
from django.db import transaction
from django.shortcuts import render
from django.forms import modelformset_factory


def create(request):
    # ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=4)
    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if photo_form.is_valid() and image_formset.is_valid():
            photo = photo_form.save(commit=False)
            photo.author_id = request.user.id

            with transaction.atomic():
                photo.save()
                image_formset.instance = photo
                image_formset.save()
                return redirect('/')
    else:
        photo_form = PhotoForm()
        image_formset = ImageFormSet()
    return render(request, 'photo/photo_create.html', {
                                    'photo_form': photo_form,
                                    'image_formset':image_formset,
                                    })

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoDelete, self).dispatch(request, *args, **kwargs)

class PhotoDetail(DetailView): #추가 수정 필요
    model = Photo
    template_name_suffix = '_detail'



def photo_list(request): #카테고리, 지역에 따라 list가 다릅니다\
    articles = Photo.objects.all()
    map = {}

    # photo model을 key로 하고, image url을 value로 하는 맵 생성
    for i in range(1, articles.count()+1):
        tmp = articles.get(pk=i)
        obj = (InsertedImage.objects.get(photo=tmp))
        map[articles.get(pk=i)] = obj.image.url

    return render(request, "photo/photo_list.html", {"data": map})


