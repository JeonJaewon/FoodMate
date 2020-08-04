from django import forms
from .models import Photo, Image, Comment


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title','text','category','count','money','url' ]
        template_name_suffix = '_create'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = '제목'


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='')

    class Meta:
        model = Image
        fields = ['image', ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = '댓글'



ImageFormSet = forms.inlineformset_factory(Photo, Image, form=ImageForm, extra=3)