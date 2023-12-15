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
    content = forms.CharField(
        label_suffix='',label='',
        widget=CKEditorWidget(
            attrs={
                'class':'form-control',
                'style':'width:100%; height:400px;',
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