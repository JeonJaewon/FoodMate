from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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
        labels = {
            'email': '',
            'username': '',
            'nickname': ''
        }
        help_texts = {
            'username': ''
        }
