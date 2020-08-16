from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'input_box', 'placeholder': '비밀번호'})
        # widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'input_box', 'placeholder': '비밀번호 확인'})
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # 커스텀 유저 모델이 아닌 직접 정의한 유저 모델을 사용하므로 get_user_model()을 사용
        fields = ('email', 'password1', 'password2', 'username', 'nickname')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'input_box',
                    'placeholder': '아이디(이메일)'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'input_box',
                    'placeholder': '이름'
                }
            ),
            'nickname': forms.TextInput(
                attrs={
                    'class': 'input_box',
                    'placeholder': '닉네임'
                }
            )
        }

        # 입력 폼 위의 텍스트
        labels = {
            'email': '',
            'username': '',
            'nickname': ''
        }

        # 입력 폼 아래 도움말
        help_texts = {
            'username': ''
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']  # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input_box',
                    'placeholder': '아이디'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'input_box',
                    'placeholder': '비밀번호'
                }
            )
        }

        # 입력 폼 위의 텍스트
        labels = {
            'username': '',
            'password': ''
        }

        # 입력 폼 아래 도움말
        help_texts = {
            'username': ''
        }

class basic_info_form(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['user_photo', 'username','nickname', 'living']

        widgets = {
            'user_photo': forms.FileInput(
                attrs={
                    'class': 'photo_box',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'username_box',
                }
            ),
            'nickname': forms.TextInput(
                attrs={
                    'class': 'nickname_box',
                }
            ),
            'living': forms.TextInput(
                attrs={
                    'class': 'living_box',
                }
            ),
        }

        # 입력 폼 위의 텍스트
        labels = {
            'user_photo': '',
            'username': '',
            'nickname': '',
            'living': '',
        }

        # 입력 폼 아래 도움말
        help_texts = {
            'username': ''
        }