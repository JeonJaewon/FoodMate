from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.base import View
from django.contrib.auth.models import User
from urllib.parse import urlparse
from .models import Photo,Image

from .forms import PhotoForm, ImageFormSet, ImageForm, CommentForm
from django.db import transaction
from django.shortcuts import render
from django.forms import modelformset_factory

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import  login_required

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

    def comment_create(request):
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.username_id = request.user.id

                with transaction.atomic():
                    comment.save()
                    return redirect('/')
        else:
            comment = CommentForm()
        return render(request, 'photo/photo_detail.html', {
                                        'form': form,
                                        })


class PhotoList(ListView):
    template_name_suffix = '_list'
    queryset = Photo.objects.all()

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(PhotoList, self).get_context_data(**kwargs)

        context['object'] = self.queryset
        return context