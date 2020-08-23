from django import forms
from .models import Photo, InsertedImage, Comment, ReComment
from .widgets import PreviewFileWidget

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'count', 'money', 'category', 'text', 'area', 'lat', 'lng']
        template_name_suffix = '_create'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'title_box',
                    'placeholder': '제목을 입력하세요.(13자)',
                    'id': 'title'
                }
            ),
            'count': forms.NumberInput(
                attrs={
                    'class': 'count_box',
                    'placeholder': '0'
                }
            ),
            'money': forms.NumberInput(
                attrs={
                    'class': 'money_box',
                    'placeholder': '0'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'category_box',
                    'placeholder': '선택해주세요'
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'text_box',
                    'placeholder': '제품에 대한 상세설명을 입력해주세요 180자*',
                    'rows': 10
                }
            ),
            'area': forms.TextInput(
                attrs={
                    'class': 'area_box',
                    'placeholder': '상세 위치를 기입해주세요'
                }
            ),
            'lat': forms.TextInput(
                attrs={
                    'id': 'lat',
                }
            ),
            'lng': forms.TextInput(
                attrs={
                    'id': 'lng',
                }
            ),
        }
        labels = {
            'title': '',
            'count': '',
            'money': '',
            'category': '',
            'text': '',
            'area': '',
            'url': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [("", "선택해주세요"), ] + list(self.fields["category"].choices)[0:]


class InsertedImageForm(forms.ModelForm):
    class Meta:
        model = InsertedImage
        fields = ['image', ]
        widgets = {
            'image': PreviewFileWidget,
        }
        labels = {
            'image': '',
        }
        # widgets = {
        #     'image': forms.FileInput(
        #         attrs={
        #             'class': 'input_box',
        #         }
        #     )
        # }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'class': 'text_box',
                    'placeholder': '댓글을 입력하세요'
                }
            )
        }
        labels = {
            'text': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['text'].label = '댓글'

class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ['text', ]
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'class': 're_text_box',
                    'placeholder': '답글을 입력하세요'
                }
            )
        }
        labels = {
            'text': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['text'].label = '댓글'

ImageFormSet = forms.inlineformset_factory(Photo, InsertedImage, form=InsertedImageForm, extra=4)


# class SearchForm(forms.ModelForm):
#     word = forms.CharField()
