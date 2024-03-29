from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, UserChangeForm
from django.forms.widgets import ClearableFileInput
from .models import *


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label_suffix='',label='',
        error_messages={'required': '사용자 이름을 확인해주세요'},
        widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'성함'
            }
        )
    )
    nickname = forms.CharField(
        label_suffix='',label='',
        error_messages={'required': '닉네임을 확인해주세요'},
        widget = forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder': '닉네임'
            }
        )
    )
    profile_image = forms.ImageField(
        label_suffix='',label='',
        error_messages={'required': '이미지를 확인해주세요'},
        required=False,
        widget = ClearableFileInput(
            attrs= {
                'class':'form-control',
            }
        )
    )
    email = forms.EmailField(
        label_suffix='',label='',
        error_messages={'required': '이메일을 확인해주세요'},
        widget = forms.EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder': '이메일'
            }
        )
    )
    password1 = forms.CharField(
        label_suffix='',label='',
        error_messages={'required': '비밀번호를 확인해주세요'},
        widget= forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'비밀번호',
            }
        )
    )
    password2 = forms.CharField(
        label_suffix='', label='',
        error_messages={'required': '비밀번호 재확인을 확인해주세요'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 재확인',
            }
        )
    )
    hobby1 = forms.CharField(
        label_suffix='',label='',
        required=True,
        widget = forms.HiddenInput(
            attrs={
            }
        )
    )
    hobby2 = forms.CharField(
        label_suffix='', label='',
        required=False,
        widget=forms.HiddenInput(
            attrs={
            }
        )
    )
    hobby3 = forms.CharField(
        label_suffix='', label='',
        required=False,
        widget=forms.HiddenInput(
            attrs={
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('username','nickname','profile_image','email',)

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label_suffix='', label='',
        error_messages={'required': '이전 비밀번호를 확인해주세요'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이전 비밀번호',
            }
        )
    )
    new_password1 = forms.CharField(
        label_suffix='', label='',
        error_messages={'required': '새로운 비밀번호를 확인해주세요'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '새로운 비밀번호',
            }
        )
    )
    new_password2 = forms.CharField(
        label_suffix='', label='',
        error_messages={'required': '새로운 비밀번호 재확인을 확인해주세요'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '새로운 비밀번호 재확인',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('password1','password2',)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label_suffix='', label='',
        error_messages={'required': '이메일을 확인해주세요'},
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일'
            }
        )
    )
    password = forms.CharField(
        label_suffix='', label='',
        error_messages={'required': '비밀번호를 확인해주세요'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )
    class Meta:
        models = get_user_model()
        fields = ('username','password',)

class CustomUserChangeForm(UserChangeForm):
    Hobbiy_Choices = (
        ('big three exercises ', '3대운동'),
        ('cycling', '싸이클'),
        ('bodyWeight_training', '맨몸운동'),
        ('bodybilding', '보디빌딩'),
        ('jogging', '조깅'),
        ('running', '러닝'),
        ('swimming', '수영'),
        ('WeightTraining', '웨이트트레이닝'),
        ('Yoga', '요가'),
        ('Pilates', '필라테스'),
        ('climbing', '클라이밍'),
        ('tennis', '테니스'),
    )
    nickname = forms.CharField(
        label_suffix='', label='',
        error_messages={'required': '닉네임을 확인해주세요'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    profile_image = forms.ImageField(
        label_suffix='', label='',
        error_messages={'required': '이미지를 확인해주세요'},
        required=False,
        widget=ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    hobbies = forms.MultipleChoiceField(
        label_suffix='', label='',
        error_messages={'required': '취미를 확인해주세요'},
        choices=Hobbiy_Choices,
        required=False,
        widget=forms.CheckboxSelectMultiple(
        ),
    )
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_image', 'hobbies',)

    password = forms.CharField(label='', widget=forms.HiddenInput(), required=False)