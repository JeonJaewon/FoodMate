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
from .models import Photo, InsertedImage, Comment

from .forms import PhotoForm, ImageFormSet, InsertedImageForm, CommentForm
from django.db import transaction
from django.shortcuts import render
from django.forms import modelformset_factory

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import  login_required
from datetime import datetime

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
                                    'image_formset': image_formset,
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

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'
    context_object_name = "product"

    #~~시간 전
    # time = datetime.now()
    # model.time_now = str(time.month - model.updated.month)
    # if model.created.day == time.day:
    #     time_now = str(time.hour - model.created.hour) + "시간 전"
    # else:
    #     if model.updated.month == time.month:
    #         time_now = str(time.day - model.created.day) + "일 전"
    #     else:
    #         if model.updated.year == time.year:
    #             time_now = str(time.month - model.updated.month) + "개월 전"

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super().get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['image'] = InsertedImage.objects.all()
        context['comment'] =Comment.objects.all()

        return context

def comment_create(request):
    if request.method == 'POST':
        photo_form =PhotoForm(request.POST, request.FILES)
        comment_form = CommentForm(request.POST, request.FILES)

        if photo_form.is_valid() and comment_form.is_valid():
            photo = photo_form.save(commit=False)
            comment = comment_form.save(commit=False)
            comment.username_id = request.user.id

            with transaction.atomic():
                comment_form.instance = photo
                comment.save()
                return redirect('/')
        else:
            photo_form = PhotoForm()
            comment = CommentForm()
        return render(request, 'photo/photo_detail.html', {
                                        'comment_form':comment_form
                                        })

def photo_list(request): #카테고리, 지역에 따라 list가 다릅니다\
    articles = Photo.objects.all()
    map = {}

    # photo model을 key로 하고, image url을 value로 하는 맵 생성
    for i in range(1, articles.count()+1):
        tmp = articles.get(pk=i)
        obj = (InsertedImage.objects.get(photo=tmp))
        map[articles.get(pk=i)] = obj.image.url

    return render(request, "photo/photo_list.html", {"data": map})