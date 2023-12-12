from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.forms import ClearableFileInput
from .models import *

class ArticlesForm(forms.ModelForm):
    Category_Choices = [
        ('3대운동','3대운동'),
        ('린매스업', '린매스업'),
        ('유산소운동', '유산소운동'),
        ('보디빌딩', '보디빌딩'),
        ('자유', '자유'),
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
    image = forms.ImageField(
        label_suffix='',label='',
        required=False,
        widget=ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    content = forms.CharField(
        label_suffix='',label='',
        widget=CKEditorWidget(
            attrs={
                'class':'form-control',
                'style':'width:100%',
            }
        )
    )
    class Meta:
        model = Articles
        fields = ('title','content','image',)

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
