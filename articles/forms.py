from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.forms import ClearableFileInput
from .models import Articles, Comment

class ArticlesForm(forms.Form):
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
            }
        )
    )
    class Meta:
        model = Articles
        fields = ('title','content','image',)

class CommentForm(forms.Form):
    content = forms.CharField(
        label_suffix='',label='',
        widget=forms.Textarea(
            attrs={
                'style':'height:150px;'
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)
