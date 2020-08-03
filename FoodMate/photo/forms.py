from django import forms
from .models import Photo, Image


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title','text','category','count','money', ]
        template_name_suffix = '_create'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = '제목'


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='')

    class Meta:
        model = Image
        fields = ['image', ]


ImageFormSet = forms.inlineformset_factory(Photo, Image, form=ImageForm, extra=3)