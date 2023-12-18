from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.forms import ClearableFileInput
from .models import *

class ArticlesForm(forms.ModelForm):
    Category_Choices = [
        (str('3대운동'),str('3대운동')),
        (str('린매스업'), str('린매스업')),
        (str('유산소운동'), str('유산소운동')),
        (str('보디빌딩'), str('보디빌딩')),
        (str('자유'), str('자유')),
        (str('식단'),str('식단')),
    ]
    category = forms.CharField(
        label_suffix='', label='',
        widget=forms.Select(
            choices=Category_Choices,

            attrs={
                'class': 'form-control',
            }
        )
    )
    title = forms.CharField(
        label_suffix='',label='',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Articles
        fields = ('category','title','content',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label_suffix='',label='',
        widget=forms.Textarea(
            attrs={
                'style':'height:30px;weight:100%;',
                'class':'form-control'
            }
        )
    )
    parent_comment_id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput
    )
    class Meta:
        model = Comment
        fields = ('content',)

class ReportForm(forms.ModelForm):
    title = forms.CharField(
        label_suffix='', label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    reason = forms.CharField(
        label_suffix='',label='',
        widget= forms.Textarea(
            attrs={
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Report
        fields = ('title','reason',)