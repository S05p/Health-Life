from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, UserChangeForm
from django.forms.widgets import ClearableFileInput

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label_suffix='',label='',
        error_messages={'required': '사용자 이름을 확인해주세요'},
        widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'성함을 입력해주세요'
            }
        )
    )
    nickname = forms.CharField(
        label_suffix='',label='',
        error_messages={'required': '닉네임을 확인해주세요'},
        widget = forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder': '닉네임을 입력해주세요'
            }
        )
    )
    profile_image = forms.ImageField(
        label_suffix='',label='',
        error_messages={'required': '이미지를 확인해주세요'},
        widget = ClearableFileInput(
            attrs= {
                'class':'form-control',
            }
        )
    )
    hobbies = forms.ChoiceField(
        label_suffix='',label='',
        error_messages={'required': '취미를 확인해주세요'},
    )
    email = forms.EmailField(
        label_suffix='',label='',
        error_messages={'required': '이메일을 확인해주세요'},
        widget = forms.EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder': '이메일을 입력해주세요'
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('username','nickname','profile_image','hobbies','email',)

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('password1','password2',)

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(
        label_suffix='', label='',
        error_messages={'required': '닉네임을 확인해주세요'},
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )
    profile_image = forms.ImageField(
        label_suffix='', label='',
        error_messages={'required': '이미지를 확인해주세요'},
        widget=ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    hobbies = forms.ChoiceField(
        label_suffix='', label='',
        error_messages={'required': '취미를 확인해주세요'},
        widget=forms.ChoiceField()
    )
    email = forms.EmailField(
        label_suffix='', label='',
        error_messages={'required': '이메일을 확인해주세요'},
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_image', 'hobbies', 'email',)