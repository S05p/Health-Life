from django import forms
from django.forms import ClearableFileInput
from .models import Articles, Comment

class ArticlesForm(forms.Form):
    content = forms.CharField(
        label_suffix='',label='',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
            }
        )
    )
    image = forms.ImageField(
        label_suffix='',label='',
        widget=ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Articles
        fields = ('content','image',)

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
